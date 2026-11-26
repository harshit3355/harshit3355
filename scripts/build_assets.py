"""Build the SVG images used by README.md.

Run from anywhere:  python scripts/build_assets.py
Writes assets/*.svg. Needs network once, to embed GitHub avatars in the
"merged upstream into" strip (SVGs shown through <img> cannot load remote
images). Standard library only. Edit the data below when a number changes.
"""
import base64
import textwrap
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"

# ponytail: system font stacks, not embedded fonts. Rendering varies a little by OS;
# embed a subset webfont here if pixel-identical type ever matters.
SANS = "'Segoe UI', Inter, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
MONO = "'JetBrains Mono', 'Cascadia Code', 'SF Mono', Menlo, Consolas, monospace"

BG, CARD, LINE = "#0b1120", "#0f172a", "#22304f"
TEXT, SOFT, MUTED, DIM = "#e2e8f0", "#cbd5e1", "#94a3b8", "#64748b"
BLUE, VIOLET, PURPLE, GREEN, AMBER, RED = "#70a5fd", "#a78bfa", "#7c3aed", "#34d399", "#fbbf24", "#f87171"

ANIMATED = ".up,.grow,.type,.blink,.cursor,.node,.pulse"
BASE_CSS = f"""
text{{font-family:{SANS}}} .mono{{font-family:{MONO}}}
.up{{opacity:0;animation:up .7s ease-out forwards}}
@keyframes up{{from{{opacity:0;transform:translateY(14px)}}to{{opacity:1;transform:translateY(0)}}}}
.grow{{transform-box:fill-box;transform-origin:left center;transform:scaleX(0);animation:grow 1.1s cubic-bezier(.2,.8,.2,1) forwards}}
@keyframes grow{{to{{transform:scaleX(1)}}}}
.blink{{animation:blink 1.6s ease-in-out infinite}}
@keyframes blink{{50%{{opacity:.25}}}}
@media (prefers-reduced-motion:reduce){{{ANIMATED}{{animation:none!important;opacity:1!important;transform:none!important;clip-path:none!important}}}}
"""


def q(s):
    return escape(str(s), {'"': "&quot;"})


def width_of(s, size, mono=False):
    return len(s) * size * (0.6 if mono else 0.55)


def svg(w, h, body, title, css="", defs=""):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
        f'role="img" aria-label="{q(title)}"><title>{q(title)}</title>'
        f"<style>{BASE_CSS}{css}</style><defs>{defs}</defs>{''.join(body)}</svg>"
    )


def text(x, y, s, size, fill, weight=400, cls="", anchor="start", extra=""):
    c = f' class="{cls}"' if cls else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" font-weight="{weight}" '
            f'text-anchor="{anchor}"{c} {extra}>{q(s)}</text>')


def delay(sec):
    return f'style="animation-delay:{sec:.2f}s"'


def chip(x, y, label, color, size=13, h=30, spacing=0):
    w = width_of(label, size) + 26 + len(label) * spacing
    return (f'<rect x="{x:.1f}" y="{y}" width="{w:.0f}" height="{h}" rx="{h / 2}" fill="{color}" fill-opacity=".12" '
            f'stroke="{color}" stroke-opacity=".45"/>'
            + text(x + 13, y + h / 2 + size * 0.36, label, size, color, 600,
                   extra=f'letter-spacing="{spacing}"')), w


def chips(x, y, labels, color, size=13):
    out = []
    for label in labels:
        part, w = chip(x, y, label, color, size)
        out.append(part)
        x += w + 10
    return "".join(out)


def gradient(gid, a, b):
    return (f'<linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="0">'
            f'<stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient>')


def card_bg(w, h, rx=22):
    return f'<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="{rx}" fill="url(#cardbg)" stroke="{LINE}"/>'


CARD_GRADIENT = ('<linearGradient id="cardbg" x1="0" y1="0" x2="1" y2="1">'
                 f'<stop offset="0" stop-color="{CARD}"/><stop offset="1" stop-color="#131c3a"/></linearGradient>')


# --------------------------------------------------------------------------- hero
def hero():
    W, H = 1200, 460
    defs = f"""
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BG}"/>
<stop offset=".55" stop-color="#111a3a"/><stop offset="1" stop-color="#1e1b4b"/></linearGradient>
<radialGradient id="g1"><stop offset="0" stop-color="{PURPLE}" stop-opacity=".38"/><stop offset="1" stop-color="{PURPLE}" stop-opacity="0"/></radialGradient>
<radialGradient id="g2"><stop offset="0" stop-color="#2563eb" stop-opacity=".32"/><stop offset="1" stop-color="#2563eb" stop-opacity="0"/></radialGradient>
<linearGradient id="name" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#c4b5fd"/></linearGradient>
<linearGradient id="trail" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{BLUE}" stop-opacity="0"/><stop offset="1" stop-color="{BLUE}"/></linearGradient>
<pattern id="dots" width="26" height="26" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.1" fill="#273352"/></pattern>
<clipPath id="frame"><rect width="{W}" height="{H}" rx="24"/></clipPath>
<clipPath id="term"><rect x="650" y="50" width="486" height="312" rx="14"/></clipPath>"""
    css = f"""
.type{{clip-path:inset(0 100% 0 0);animation:type .7s steps(26,end) forwards}}
@keyframes type{{to{{clip-path:inset(0 0 0 0)}}}}
.cursor{{opacity:0;animation:cur 1s step-end 4.4s infinite}}
@keyframes cur{{0%,49%{{opacity:1}}50%,100%{{opacity:0}}}}
.node{{animation:lit 4.5s linear infinite}}
@keyframes lit{{0%,22%,100%{{stroke:#3b4f80;fill:{BG}}}4%,14%{{stroke:{BLUE};fill:#1e3a8a}}}}
.pulse{{animation:travel 4.5s linear infinite}}
@keyframes travel{{from{{transform:translateX(0)}}to{{transform:translateX(1008px)}}}}"""
    b = [
        f'<g clip-path="url(#frame)"><rect width="{W}" height="{H}" fill="url(#bg)"/>'
        f'<rect width="{W}" height="{H}" fill="url(#dots)" opacity=".55"/>'
        f'<circle cx="170" cy="30" r="380" fill="url(#g1)"/><circle cx="1090" cy="480" r="360" fill="url(#g2)"/></g>',
        f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="24" fill="none" stroke="#2a3a63"/>',
    ]
    # left column
    label = "Production · Azure + AWS · AI platforms"
    cw = width_of(label, 14) + 48
    b.append(f'<g class="up"><rect x="64" y="58" width="{cw:.0f}" height="34" rx="17" fill="#111c38" stroke="#2a3a63"/>'
             f'<circle class="blink" cx="84" cy="75" r="5" fill="{GREEN}"/>'
             + text(98, 80, label, 14, SOFT, 600) + "</g>")
    b.append(text(64, 166, "Harshit Nagila", 64, "url(#name)", 800, "up", extra=f'letter-spacing="-1.5" {delay(.1)}'))
    b.append(text(64, 208, "DevOps · Cloud · SRE · DevSecOps", 20, BLUE, 600, "up mono", extra=delay(.2)))
    b.append(text(64, 252, "I run production AI infrastructure on Azure and AWS,", 18, SOFT, 400, "up", extra=delay(.3)))
    b.append(text(64, 279, "and build Kubernetes tooling in the open.", 18, SOFT, 400, "up", extra=delay(.35)))
    b.append(f'<g class="up" {delay(.45)}>'
             + chips(64, 308, ["3 yrs in production", "OpenAI + Bedrock", "Terraform · K8s"], VIOLET, 14) + "</g>")

    # terminal
    x, y, w, h = 650, 50, 486, 312
    b.append(f'<g class="up" {delay(.15)}><g clip-path="url(#term)">'
             f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#080d1c" fill-opacity=".92"/>'
             f'<rect x="{x}" y="{y}" width="{w}" height="36" fill="#121b33"/></g>'
             f'<rect x="{x + .5}" y="{y + .5}" width="{w - 1}" height="{h - 1}" rx="14" fill="none" stroke="#2a3a63"/>'
             + "".join(f'<circle cx="{x + 22 + i * 20}" cy="{y + 18}" r="6" fill="{c}"/>'
                       for i, c in enumerate((RED, AMBER, GREEN)))
             + text(x + w / 2, y + 23, "harshit@prod: ~", 13, DIM, 400, "mono", "middle") + "</g>")
    lines = [
        ("cmd", "whoami", .6),
        ("out", "harshit · devops / sre · 3 yrs in production", 1.35),
        ("cmd", "terraform plan", 1.75),
        ("out", "No changes. 85+ resources match the config.", 2.5),
        ("cmd", "kubectl argo rollouts status checkout", 2.9),
        ("ok", "✔ Healthy · canary promoted", 3.95),
    ]
    ly = y + 72
    for kind, s, t0 in lines:
        if kind == "cmd":
            b.append(f'<text x="{x + 22}" y="{ly}" font-size="15" class="mono type" {delay(t0)}>'
                     f'<tspan fill="{GREEN}">$ </tspan><tspan fill="{TEXT}">{q(s)}</tspan></text>')
        else:
            b.append(text(x + 22, ly, s, 15, GREEN if kind == "ok" else MUTED, 400, "mono up", extra=delay(t0)))
        ly += 30
    b.append(f'<text x="{x + 22}" y="{ly}" font-size="15" class="mono up" fill="{GREEN}" {delay(4.3)}>$</text>'
             f'<rect class="cursor" x="{x + 40}" y="{ly - 14}" width="9" height="18" fill="{BLUE}"/>')

    # pipeline
    py, x0, x1 = 410, 96, 1104
    b.append(f'<line x1="{x0}" y1="{py}" x2="{x1}" y2="{py}" stroke="#2a3a63" stroke-width="2"/>')
    b.append(f'<g class="pulse"><rect x="{x0 - 70}" y="{py - 1.5}" width="70" height="3" rx="1.5" fill="url(#trail)"/>'
             f'<circle cx="{x0}" cy="{py}" r="5" fill="#c7d2fe"/></g>')
    for i, stage in enumerate(("commit", "build", "scan", "deploy", "observe")):
        nx = x0 + i * (x1 - x0) / 4
        b.append(f'<circle class="node" cx="{nx}" cy="{py}" r="8" fill="{BG}" stroke="#3b4f80" stroke-width="2" '
                 f'style="animation-delay:{i * 1.125:.3f}s"/>')
        b.append(text(nx, py + 32, stage, 13, MUTED, 400, "mono", "middle"))
    return svg(W, H, b, "Harshit Nagila: DevOps, Cloud, SRE, DevSecOps. Runs production AI infrastructure on "
                        "Azure and AWS and builds Kubernetes tooling in the open.", css, defs)


# ------------------------------------------------------------------ at a glance
TILES = [
    ("3 yrs", "DevOps in production", "Sole DevOps engineer, Azure + AWS", (BLUE, VIOLET)),
    ("29 × 3", "container apps × environments", "85+ Terraform resources per env", (VIOLET, "#f0abfc")),
    ("10k+", "requests a day", "from 250+ users, with auto-rollback", ("#22d3ee", BLUE)),
    ("2", "Kubernetes tools in Go", "released with SLSA build provenance", (GREEN, "#22d3ee")),
    ("18", "benchmarked prototypes", "method, numbers and limits in each", (AMBER, "#fb923c")),
    ("50+", "pull requests merged upstream", "Prefect, Docker, reviewdog, ScyllaDB", ("#f0abfc", VIOLET)),
]


def glance():
    W, H, tw, th, gap = 1200, 384, 384, 180, 24
    defs = "".join(gradient(f"t{i}", a, b) for i, (*_, (a, b)) in enumerate(TILES))
    b = []
    for i, (value, label, sub, _) in enumerate(TILES):
        x, y = (i % 3) * (tw + gap), (i // 3) * (th + gap)
        b.append(f'<g class="up" {delay(i * .08)}>'
                 f'<rect x="{x + .5}" y="{y + .5}" width="{tw - 1}" height="{th - 1}" rx="20" fill="{CARD}" stroke="{LINE}"/>'
                 f'<rect x="{x + 28}" y="{y + 26}" width="44" height="4" rx="2" fill="url(#t{i})"/>'
                 + text(x + 28, y + 94, value, 54, f"url(#t{i})", 800, extra='letter-spacing="-1"')
                 + text(x + 28, y + 130, label, 19, TEXT, 600)
                 + text(x + 28, y + 156, sub, 15, MUTED) + "</g>")
    return svg(W, H, b, "At a glance: " + "; ".join(f"{v} {l}" for v, l, *_ in TILES), defs=defs)


# -------------------------------------------------------------- feature cards
def bars(x, y, width, rows, top, step, size=15):
    """rows: (label, value, display, color). Bars grow from 0 when the image loads."""
    out = []
    for i, (label, value, shown, color) in enumerate(rows):
        ry = y + i * step
        out.append(text(x, ry, label, size, SOFT))
        out.append(text(x + width, ry, shown, size, color, 700, anchor="end"))
        out.append(f'<rect x="{x}" y="{ry + 12}" width="{width}" height="12" rx="6" fill="#18223f"/>')
        bw = max(8, width * value / top)
        out.append(f'<rect class="grow" x="{x}" y="{ry + 12}" width="{bw:.1f}" height="12" rx="6" fill="{color}" '
                   f'{delay(.35 + i * .15)}/>')
    return "".join(out)


def tool_card(kicker, name, desc, tags, chart_title, rows, top, step, note, note_color):
    W, H = 1200, 340
    b = [card_bg(W, H)]
    part, _ = chip(48, 40, kicker, VIOLET, 12, 28, 1.2)
    b.append(part)
    b.append(text(48, 112, name, 26, TEXT, 700, "mono"))
    for i, line in enumerate(textwrap.wrap(desc, 50)[:3]):
        b.append(text(48, 156 + i * 28, line, 18, SOFT))
    b.append(chips(48, 266, tags, BLUE, 13))
    b.append(text(652, 66, chart_title.upper(), 13, MUTED, 600, extra='letter-spacing="1"'))
    b.append(bars(652, 108, 500, rows, top, step))
    b.append(text(652, 300, note, 14, note_color))
    return svg(W, H, b, f"{name}: {desc} {note}", defs=CARD_GRADIENT)


TOOLS = {
    "tool-rollouts": dict(
        kicker="ARGO ROLLOUTS PLUGIN · GO · v0.1.0", name="rollouts-plugin-metric-sequential",
        desc="Aborts a canary when Prometheus error counts show a real regression, with a sequential "
             "test that stays valid however often Argo checks it.",
        tags=["kind e2e with Argo Rollouts v1.10.2", "SHA-256 + SLSA provenance"],
        chart_title="Worst false-rollback rate · lower is better",
        rows=[("This plugin", 1.7, "1.7%", GREEN), ("z-test checked every interval", 30.6, "30.6%", AMBER),
              ("2× threshold rule", 99.2, "99.2%", RED)],
        top=100, step=62, note="A 2× error regression is caught in about 7 intervals.", note_color=BLUE),
    "tool-vpa": dict(
        kicker="VERTICAL POD AUTOSCALER RECOMMENDER · GO · v0.1.0", name="vpa-recommender-oom-budget",
        desc="Set an OOM-kill budget; it sizes each container's memory to meet it, with one margin "
             "calibrated on the whole fleet's history.",
        tags=["Borg trace · 3,179 tasks", "kind e2e with VPA 1.8.1", "SLSA provenance"],
        chart_title="OOM kills per container-day · asked vs got",
        rows=[("Budget 0.01 · asked", .0100, "0.0100", DIM), ("Budget 0.01 · got", .0101, "0.0101", VIOLET),
              ("Budget 0.003 · asked", .0030, "0.0030", DIM), ("Budget 0.003 · got", .0030, "0.0030", VIOLET)],
        top=.012, step=46, note="No memory savings claimed: within 2–4% of VPA and KRR defaults.", note_color=MUTED),
}

PROJECTS = {
    "policy-synapse": ("SECURITY · POLICY AS CODE", VIOLET,
                       "One policy intent compiled to CI, admission, Terraform-plan and runtime Rego, "
                       "tested where they disagree.",
                       "Injected policy bugs caught · 708 mutants",
                       [("Boundary suite", 100, "708/708", VIOLET), ("Example tests", 56.9, "403/708", DIM)], 100),
    "hephaestus-ledger": ("SUPPLY CHAIN · PROVENANCE", BLUE,
                          "Proves every live AI deployment part, from image to model config, descends from "
                          "the approved release.",
                          "Constructed provenance breaks flagged · 19",
                          [("Provenance graph", 19, "19/19", BLUE), ("Image signature only", 1, "1/19", DIM)], 19),
    "aegis-nexus": ("AGENT IDENTITY · ZERO TRUST", "#f0abfc",
                    "Holder-bound delegation chains that narrow credentials at every hop between AI agents "
                    "across clouds.",
                    "Leakage after compromise · weight-hours · lower is better",
                    [("Attenuating chains", 7.06, "7", "#f0abfc"),
                     ("Token exchange, no attenuation", 242782, "242,782", DIM)], 242782),
    "chaos-witness": ("RELIABILITY · CHAOS", GREEN,
                      "Chaos campaigns aimed at the guarantees an AI platform promises, scored by how many "
                      "a run checked.",
                      "Planted weaknesses found · 7 in total",
                      [("Obligation-targeted", 7, "7/7", GREEN), ("Manual chaos checklist", 4, "4/7", DIM)], 7),
    "faultweaver": ("AIOPS · SAFE REMEDIATION", AMBER,
                    "An automated fix runs only when independent telemetry backs the root cause; otherwise "
                    "it probes or escalates.",
                    "Unsafe automated actions · 240 incidents · lower is better",
                    [("Evidence gate + probes", 11, "11", AMBER), ("Same agent, no gate", 29, "29", DIM)], 29),
    "terracog": ("IaC · TERRAFORM DRIFT", "#22d3ee",
                 "Terraform drift triage: revert, codify, quarantine or escalate, chosen by counterfactual "
                 "harm.",
                 "Decision regret · lower is better",
                 [("TerraCog", .59, "0.59", "#22d3ee"), ("Always revert", 2.75, "2.75", DIM)], 2.75),
}


def project_card(name, kicker, color, desc, caption, rows, top):
    W, H = 600, 300
    b = [card_bg(W, H, 20)]
    part, _ = chip(32, 28, kicker, color, 11, 26, 1.2)
    b.append(part)
    b.append(text(32, 96, name, 24, TEXT, 700, "mono"))
    for i, line in enumerate(textwrap.wrap(desc, 58)[:2]):
        b.append(text(32, 130 + i * 24, line, 16, SOFT))
    b.append(text(32, 196, caption.upper(), 12, MUTED, 600, extra='letter-spacing=".8"'))
    b.append(bars(32, 224, 536, rows, top, 40, 14))
    return svg(W, H, b, f"{name}: {desc} {caption}: " + ", ".join(f"{l} {s}" for l, _, s, _ in rows),
               defs=CARD_GRADIENT)


# ------------------------------------------------------------ merged upstream
MERGED = [("PrefectHQ", "prefect"), ("docker-library", "official-images"), ("docker-mailserver", "docker-mailserver"),
          ("reviewdog", "reviewdog"), ("komodorio", "helm-dashboard"), ("kubecolor", "kubecolor"),
          ("cdklabs", "cdk-from-cfn"), ("scylladb", "python-driver"), ("oliver006", "redis_exporter"),
          ("version-fox", "vfox"), ("yonahd", "kor"), ("itzg", "minecraft-server"), ("Kareadita", "Kavita"),
          ("Consolonia", "Consolonia")]


def avatar(owner):
    req = urllib.request.Request(f"https://github.com/{owner}.png?size=96", headers={"User-Agent": "readme-assets"})
    data = urllib.request.urlopen(req, timeout=30).read()
    mime = "image/png" if data[:4] == b"\x89PNG" else "image/jpeg"
    return f"data:{mime};base64,{base64.b64encode(data).decode()}"


def merged():
    W, H, per = 1200, 352, 7
    cw = (W - 96) / per
    b = [card_bg(W, H), text(48, 58, "Merged upstream into", 24, TEXT, 700),
         text(W - 48, 58, "50+ pull requests", 20, BLUE, 700, anchor="end")]
    defs = [CARD_GRADIENT]
    for i, (owner, label) in enumerate(MERGED):
        cx, cy = 48 + cw * (i % per + .5), 136 + (i // per) * 126
        defs.append(f'<clipPath id="a{i}"><circle cx="{cx:.1f}" cy="{cy}" r="36"/></clipPath>')
        b.append(f'<g class="up" {delay(i * .05)}>'
                 f'<circle cx="{cx:.1f}" cy="{cy}" r="40" fill="#ffffff" stroke="#2a3a63" stroke-width="2"/>'
                 f'<image href="{avatar(owner)}" x="{cx - 36:.1f}" y="{cy - 36}" width="72" height="72" '
                 f'clip-path="url(#a{i})"/>' + text(cx, cy + 62, label, 14, SOFT, 600, anchor="middle") + "</g>")
    return svg(W, H, b, "Merged upstream into: " + ", ".join(label for _, label in MERGED), defs="".join(defs))


# --------------------------------------------------------------- certificates
CERTS = [("AWS", "CloudOps Engineer – Associate", "#ff9900"), ("HASHICORP", "Terraform Associate (004)", VIOLET),
         ("AWS", "Cloud Practitioner", "#ff9900"), ("MICROSOFT", "Azure Fundamentals (AZ-900)", "#4ea1ff"),
         ("ORACLE", "OCI Foundations", "#ff6b5f"), ("GOOGLE", "Cybersecurity Professional", "#6ea8ff"),
         ("IBM", "DevOps for Enterprise Agility", "#78a9ff")]


def certs():
    W, tw, th, gap = 1200, 288, 104, 16
    H = th * 2 + gap
    b = []
    for i, (issuer, name, color) in enumerate(CERTS):
        row, col = divmod(i, 4)
        x0 = 0 if row == 0 else (W - (3 * tw + 2 * gap)) / 2
        x, y = x0 + col * (tw + gap), row * (th + gap)
        b.append(f'<g class="up" {delay(i * .06)}>'
                 f'<rect x="{x + .5}" y="{y + .5}" width="{tw - 1}" height="{th - 1}" rx="16" fill="{CARD}" stroke="{LINE}"/>'
                 f'<rect x="{x + 20}" y="{y + 22}" width="28" height="4" rx="2" fill="{color}"/>'
                 + text(x + 20, y + 50, issuer, 12, color, 700, extra='letter-spacing="1.4"')
                 + text(x + 20, y + 80, name, 15, TEXT, 600) + "</g>")
    return svg(W, H, b, "Certifications: " + "; ".join(f"{i} {n}" for i, n, _ in CERTS))


# ---------------------------------------------------------------------- footer
def footer():
    W, H = 1200, 170
    defs = (f'<linearGradient id="fw" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{PURPLE}"/>'
            f'<stop offset=".5" stop-color="#1e3a8a"/><stop offset="1" stop-color="{BG}"/></linearGradient>'
            f'<clipPath id="ff"><rect width="{W}" height="{H}" rx="24"/></clipPath>')
    b = [f'<g clip-path="url(#ff)">'
         f'<path d="M0 104 C200 64 400 144 600 104 S1000 64 1200 104 V170 H0Z" fill="url(#fw)" opacity=".9"/>'
         f'<path d="M0 128 C250 98 450 168 700 128 S1050 98 1200 134 V170 H0Z" fill="{PURPLE}" opacity=".35"/></g>',
         f'<text x="{W / 2}" y="56" font-size="16" text-anchor="middle" class="mono up">'
         f'<tspan fill="{GREEN}">harshit@prod:~$ </tspan><tspan fill="{TEXT}">exit </tspan>'
         f'<tspan fill="{DIM}"># thanks for stopping by</tspan></text>']
    return svg(W, H, b, "Thanks for stopping by", defs=defs)


def main():
    OUT.mkdir(exist_ok=True)
    files = {"hero": hero(), "glance": glance(), "merged": merged(), "certs": certs(), "footer": footer()}
    files.update({k: tool_card(**v) for k, v in TOOLS.items()})
    files.update({f"proj-{k}": project_card(k, *v) for k, v in PROJECTS.items()})
    for stem, content in files.items():
        root = ET.fromstring(content)  # self-check: every file must be well-formed SVG
        assert root.tag.endswith("svg") and root.get("viewBox"), stem
        (OUT / f"{stem}.svg").write_text(content, encoding="utf-8")
        print(f"assets/{stem}.svg  {len(content.encode()) // 1024} KB")


if __name__ == "__main__":
    main()
