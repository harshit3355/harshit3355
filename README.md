<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,50:1e3a8a,100:7c3aed&height=230&section=header&text=Harshit%20Nagila&fontSize=62&fontColor=ffffff&fontAlignY=36&desc=DevOps%20%C2%B7%20Cloud%20%C2%B7%20SRE%20%C2%B7%20DevSecOps&descSize=20&descAlignY=58&animation=fadeIn" alt="Harshit Nagila: DevOps, Cloud, SRE, DevSecOps" width="100%" />

<a href="#-pick-your-path"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3200&pause=900&color=70A5FD&center=true&vCenter=true&width=720&height=50&lines=3+years+running+cloud+infrastructure+in+production;Azure+OpenAI+%2B+AWS+Bedrock+on+regulated+data;18+open-source+research+prototypes%2C+each+benchmarked;30%2B+pull+requests+merged+upstream;Terraform+%C2%B7+Kubernetes+%C2%B7+GitHub+Actions+%C2%B7+OIDC" alt="Typing intro: 3 years running cloud infrastructure in production; Azure OpenAI and AWS Bedrock on regulated data; 18 open-source research prototypes; 30+ pull requests merged upstream" /></a>

[![Portfolio](https://img.shields.io/badge/Portfolio-0b1f3a?style=for-the-badge&logo=netlify&logoColor=white)](https://harshit-portfolio-3355.netlify.app)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/harshit555)
[![Medium](https://img.shields.io/badge/Medium-000000?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@harshitnagila555)
[![Email](https://img.shields.io/badge/Email-1f2937?style=for-the-badge&logo=gmail&logoColor=white)](mailto:harshitnagila3355@gmail.com)

<img src="https://komarev.com/ghpvc/?username=harshit3355&label=Profile%20views&color=7c3aed&style=flat-square" alt="Profile views" />

</div>

## 👋 About me

I'm a DevOps engineer with **3 years** in cloud infrastructure. In my current role I'm the sole DevOps
engineer on **ciATHENA**, an agentic AI analytics platform for life-sciences clients. I took it from its
first environment to launch:

- **29 container apps × 3 environments** on Azure Container Apps, **85+ Terraform resources** per environment
- **10k+ requests a day** from **250+ users**
- Approval-gated releases on GitHub Actions and Azure DevOps, with revision-based **auto-rollback**
- GitHub OIDC instead of static cloud keys, Entra SSO, ISO 27001 evidence and SOC 2 preparation
- **Azure OpenAI and AWS Bedrock in production**, on regulated life-sciences data

Outside work I build open-source prototypes for problems I run into on cloud and AI platforms, write about
them on Medium, and contribute fixes upstream.

---

## 🧭 Pick your path

<details>
<summary><b>👔 Hiring? The 30-second version</b></summary>
<br/>

- **3 years** in DevOps and cloud. Sole DevOps engineer on a production agentic AI platform, from first environment to launch.
- **Azure + AWS in production**: Container Apps, ECS Fargate, Terraform, GitHub Actions / Azure DevOps, OIDC, Entra SSO.
- **AI infrastructure on regulated data**: Azure OpenAI and AWS Bedrock, ISO 27001 evidence, SOC 2 preparation.
- **Certified**: AWS CloudOps Engineer – Associate, HashiCorp Terraform Associate (004).
- **Proof beyond the day job**: two installable Kubernetes tools in Go (an Argo Rollouts canary plugin and a Vertical Pod Autoscaler memory recommender), 18 benchmarked open-source prototypes, 20+ PRs merged upstream, 10 technical articles.

📬 [harshitnagila3355@gmail.com](mailto:harshitnagila3355@gmail.com) · [LinkedIn](https://linkedin.com/in/harshit555)

</details>

<details>
<summary><b>🛠️ Engineer? Start with these three repos</b></summary>
<br/>

1. [**policy-synapse**](https://github.com/harshit3355/policy-synapse): one policy, four enforcement points, and a differential tester that catches where they disagree.
2. [**hephaestus-ledger**](https://github.com/harshit3355/hephaestus-ledger): signing the image is not enough. This proves every live AI deployment part came from the approved release.
3. [**chaos-witness**](https://github.com/harshit3355/chaos-witness): chaos tests aimed at the guarantees you promised, scored by how many of them a campaign actually checked.

Each repo has its architecture diagram, the benchmark and the limits in its README.

</details>

<details>
<summary><b>📖 Prefer reading? Start with these articles</b></summary>
<br/>

- [Your Image Is Signed. Is Your AI Deployment?](https://medium.com/@harshitnagila555/your-image-is-signed-is-your-ai-deployment-01c2dbaa572a)
- [When Terraform and the Cloud Disagree, Which One Is Right?](https://medium.com/@harshitnagila555/when-terraform-and-the-cloud-disagree-which-one-is-right-3324a1553c4d)
- [Your Chaos Test Passed. Which Guarantee Did It Actually Check?](https://medium.com/@harshitnagila555/your-chaos-test-passed-which-guarantee-did-it-actually-check-b34b55fc8353)

</details>

---

## 🧰 Tools you can install

| Project | What it does |
| --- | --- |
| [**rollouts-plugin-metric-sequential**](https://github.com/harshit3355/rollouts-plugin-metric-sequential) | Argo Rollouts metric plugin in Go. Aborts a canary when Prometheus error counts show a real regression, using a sequential test that stays valid however often Argo checks it. **Worst false rollback 1.7%, against 30.6% for a z-test checked every interval; a 2x regression is caught in about 7 intervals.** A kind end-to-end test in CI runs it inside the real Argo Rollouts controller. [v0.1.0](https://github.com/harshit3355/rollouts-plugin-metric-sequential/releases/tag/v0.1.0) ships with SHA-256 sums and SLSA build provenance. |
| [**vpa-recommender-oom-budget**](https://github.com/harshit3355/vpa-recommender-oom-budget) | Alternative Vertical Pod Autoscaler recommender in Go. You set an OOM-kill budget and it sizes each container's memory to meet it, with one margin calibrated on the whole fleet's history. On a held-out sample of Google's public Borg trace (3,179 tasks), **asked for 0.01 OOM kills per container-day, got 0.0101; asked 0.003, got 0.0030.** It does not save memory: at the same OOM rate it needs within 2 to 4% of what VPA's and KRR's defaults need. A kind end-to-end test in CI runs it with the real VPA 1.8.1 updater and admission controller. [v0.1.0](https://github.com/harshit3355/vpa-recommender-oom-budget/releases/tag/v0.1.0) ships binaries, a container image, SHA-256 sums and SLSA build provenance. |

---

## 🔬 Open-source research prototypes

18 projects. Each one takes a single failure mode, builds a working prototype, and measures it against a
baseline on a synthetic or simulated benchmark. Every README states the method, the numbers and the limits.

<p align="center">
  <a href="https://github.com/harshit3355/policy-synapse"><img src="https://raw.githubusercontent.com/harshit3355/harshit3355/output/pin-policy-synapse.svg" alt="policy-synapse" width="49%" /></a>
  <a href="https://github.com/harshit3355/hephaestus-ledger"><img src="https://raw.githubusercontent.com/harshit3355/harshit3355/output/pin-hephaestus-ledger.svg" alt="hephaestus-ledger" width="49%" /></a>
  <a href="https://github.com/harshit3355/aegis-nexus"><img src="https://raw.githubusercontent.com/harshit3355/harshit3355/output/pin-aegis-nexus.svg" alt="aegis-nexus" width="49%" /></a>
  <a href="https://github.com/harshit3355/chaos-witness"><img src="https://raw.githubusercontent.com/harshit3355/harshit3355/output/pin-chaos-witness.svg" alt="chaos-witness" width="49%" /></a>
</p>

**Security, supply chain and compliance**

| Project | What it does |
| --- | --- |
| [**policy-synapse**](https://github.com/harshit3355/policy-synapse) | Tests one policy across CI, Kubernetes admission, Terraform plan and runtime Rego. **Caught 100% of 708 injected bugs; hand-written policies caught 56.9%.** |
| [**hephaestus-ledger**](https://github.com/harshit3355/hephaestus-ledger) | Checks that every live AI deployment part (image, SBOM, Terraform state, model config, policy, identity) came from the approved release. **19/19 breaks caught; image signatures alone caught 1/19.** |
| [**aegis-nexus**](https://github.com/harshit3355/aegis-nexus) | Narrows credentials at every hop when AI agents delegate to each other across clouds. **Leakage after compromise: 242,782 → 7 weight-hours.** |
| [**janus-gate**](https://github.com/harshit3355/janus-gate) | Finds which GitHub Actions identities a cloud OIDC trust policy really accepts (AWS, Entra ID, GCP) and fails CI on the extras. |
| [**chronos-keys**](https://github.com/harshit3355/chronos-keys) | Plans secret rotation in a safe order across caches, restarts and scheduled jobs. |
| [**argus-evidence**](https://github.com/harshit3355/argus-evidence) | Builds ISO 27001 / SOC 2 control evidence continuously from cloud config and logs, in a hash-chained bundle. |
| [**ariadne-thread**](https://github.com/harshit3355/ariadne-thread) | Traces sensitive fields through OpenTelemetry Collector pipelines to the backend that stores them. |
| [**penelope-loom**](https://github.com/harshit3355/penelope-loom) | Gates AI-agent tool calls by side effect, and undoes them when a plan fails. |
| [**cassandra-upgrade**](https://github.com/harshit3355/cassandra-upgrade) | Scores dependency updates by whether your code reaches the changed functions and your tests cover them. |

**Reliability and SRE**

| Project | What it does |
| --- | --- |
| [**chaos-witness**](https://github.com/harshit3355/chaos-witness) | Chaos testing aimed at explicit guarantees, not random faults. **Found 7/7 planted weaknesses; a manual checklist found 4/7.** |
| [**faultweaver**](https://github.com/harshit3355/faultweaver) | Lets an automated fix run only when independent telemetry backs the root cause. **Unsafe actions: 29 → 11 across 240 incidents.** |
| [**burn-sentry**](https://github.com/harshit3355/burn-sentry) | SLO burn-rate alerts that stay trustworthy on low-traffic services. |
| [**orpheus-rollback**](https://github.com/harshit3355/orpheus-rollback) | Decides if a release can really be rolled back across code, schema, config and feature flags. |
| [**canary-tribunal**](https://github.com/harshit3355/canary-tribunal) | Statistically valid promote / rollback calls for LLM features scored by noisy LLM judges. |

**Platform, IaC and cost**

| Project | What it does |
| --- | --- |
| [**terracog**](https://github.com/harshit3355/terracog) | Terraform drift triage: revert, codify, quarantine or escalate. **Regret 0.59, against 2.75 for always-revert.** |
| [**titan-fleet**](https://github.com/harshit3355/titan-fleet) | One controller for LLM API routing and GPU autoscaling under SLO budgets. **Beat the baseline in 23 of 25 scenarios.** |
| [**midas-lens**](https://github.com/harshit3355/midas-lens) | Explains AI cost spikes by the deploy, prompt or config change that caused them. |
| [**carbon-oracle**](https://github.com/harshit3355/carbon-oracle) | Carbon-aware scheduling of AI jobs across regions, with a bound on missed deadlines. |

Also: [gh-oidc-trust-fixtures](https://github.com/harshit3355/gh-oidc-trust-fixtures) (labelled Terraform fixtures for OIDC trust-policy scanners) ·
[llm-gateway-quota-overshoot](https://github.com/harshit3355/llm-gateway-quota-overshoot) (reproducible harness for a LiteLLM budget-overshoot bug)

---

## 🗺️ Architecture diagrams

Every project ships its architecture as a diagram. Click one to open it, then drag to pan and scroll to zoom.

<details>
<summary><b>rollouts-plugin-metric-sequential</b>: anytime-valid canary analysis inside Argo Rollouts</summary>

```mermaid
flowchart LR
  P[Prometheus] -->|bad and total events,<br/>canary and baseline,<br/>since last measurement| R[Plugin Run]
  S[Previous measurement metadata:<br/>test state + window end] --> R
  R --> T[Sequential test<br/>mixture likelihood ratio<br/>H0: canary rate <= 1.1 x baseline]
  T -->|e-value >= 1/alpha| F[Failed: Rollout aborts]
  T -->|otherwise| OK[Successful: Rollout continues]
  T --> S2[New measurement metadata:<br/>state, e-value, window counts]
```

</details>

<details>
<summary><b>vpa-recommender-oom-budget</b>: VPA memory sized for an OOM-kill budget</summary>

```mermaid
flowchart LR
  P["Prometheus<br/>cAdvisor working set"] -->|"hourly peaks, 14 days"| R["oom-budget recommender"]
  K["Pods<br/>lastState OOMKilled"] -->|"OOM kills"| C[("ConfigMap<br/>OOM history")]
  C --> R
  R --> Q["One fleet-wide margin q<br/>from pooled surprises:<br/>P(next-hour peak over limit) = budget / 24"]
  Q --> V["VPA status.recommendation<br/>memory = 14-day peak x (1 + q)"]
  V --> U["VPA updater and admission controller<br/>resize the pods"]
```

</details>

<details>
<summary><b>aws-ecs-platform-blueprint</b>: Terraform + ECS Fargate platform on AWS</summary>

```mermaid
flowchart TB
    user([Client])

    subgraph aws["AWS Region - ap-south-1"]
        subgraph vpc["VPC 10.20.0.0/16"]
            subgraph public["Public subnets - 2 AZs"]
                alb["Application Load Balancer<br/>access logs to S3"]
                nat["NAT Gateway"]
            end
            subgraph private["Private subnets - 2 AZs"]
                task1["ECS Fargate task<br/>ARM64 - non-root"]
                task2["ECS Fargate task"]
            end
            subgraph dbsub["Database subnets - 2 AZs, no internet route"]
                rds[("RDS PostgreSQL 18.6<br/>encrypted - PITR")]
            end
        end

        ecr[["ECR<br/>immutable tags"]]
        secrets[["Secrets Manager<br/>RDS-managed password"]]
        cw[["CloudWatch<br/>logs - metrics - alarms - dashboard"]]
        sns[["SNS to email / Slack"]]
    end

    user -->|"80 / 443"| alb
    alb -->|"8000"| task1
    alb -->|"8000"| task2
    task1 -->|"5432 TLS"| rds
    task2 -->|"5432 TLS"| rds
    task1 -.->|egress| nat
    ecr -.->|image pull| task1
    secrets -.->|"DB_USER / DB_PASSWORD"| task1
    task1 -.->|"JSON logs + metrics"| cw
    alb -.-> cw
    rds -.-> cw
    cw --> sns
```

</details>

<details>
<summary><b>policy-synapse</b>: one policy intent, tested across four enforcement points</summary>

```mermaid
flowchart LR
  I[intents.json<br/>governance intent IR] --> C[compiler]
  C --> CI[CI Rego<br/>K8s manifest]
  C --> AD[Gatekeeper<br/>AdmissionReview]
  C --> TF[Terraform plan Rego<br/>plan JSON]
  C --> RT[runtime Rego<br/>deploy request]
  H[hand-written policies] -.-> D
  I --> S[PSF boundary suite]
  CI & AD & TF & RT --> D[differential engine<br/>OPA]
  S --> D
  D --> R[fingerprints, GCS,<br/>minimal counterexamples]
```

</details>

<details>
<summary><b>hephaestus-ledger</b>: release provenance for AI deployments</summary>

```mermaid
flowchart LR
  AR[Release root<br/>approver-signed:<br/>env, sequence, run, commit] --> RUN[CI run<br/>OIDC identity + commit]
  RUN -->|SLSA provenance| I[Image digest]
  RUN -->|CycloneDX claim| S[SBOM]
  RUN -->|plan claim| TF[Terraform plan]
  RUN -->|model claim| M[Model manifest + config hash]
  RUN -->|policy claim| PB[Policy bundle + version]
  TF -. pins digest .-> I
  TF -. declares .-> WI[Workload identity + roles]
  TF -. declares endpoint .-> M
  TF -. must equal .-> ST[Applied state]
  L[Live assembly<br/>from runtime observer] --> V{Reachable from<br/>the active root?}
  AR --> V
  V -->|every component| OK[exit 0, RGS 0]
  V -->|gaps| GAP[per-component reasons, RGS, exit 1]
```

</details>

<details>
<summary><b>aegis-nexus</b>: attenuating delegation chains for AI agents</summary>

```mermaid
flowchart LR
  U[user consent] --> G[delegation gateway<br/>policy decision]
  I1[aws.sim issuer] --> WP[WIT planner]
  I2[azure.sim issuer] --> WR[WIT researcher]
  I3[gcp.sim issuer] --> WC[WIT coder / linter]
  WP --> G
  G -->|hop 0: user entitlement, 1 h| P[planner]
  P -->|hop 1: task caps, 10 min| R[researcher]
  P -->|hop 1: task caps, 15 min| C[coder]
  C -->|hop 2: narrower, 5 min| L[linter]
  WR -.bound.-> R
  WC -.bound.-> C
  R & C & L -->|chain + PoP| T{tool verifier<br/>offline}
  T -->|allow + audit path| X[search / docs / repo / mail / model / storage]
  T -->|deny| D[reason]
```

</details>

<details>
<summary><b>janus-gate</b>: who a CI-to-cloud OIDC trust policy really lets in</summary>

```mermaid
flowchart LR
  TP[Trust configuration<br/>AWS trust policy / Entra FIC / GCP provider + bindings] --> E[Evaluator<br/>per-cloud condition semantics]
  TP --> W
  I[Declared intent<br/>repos, refs, environments, PRs] --> W[Witness claim space<br/>intent + policy constants +<br/>look-alikes + wildcard members]
  CS[GitHub Actions claim model<br/>sub format, precedence, immutable IDs] --> W
  W --> E
  E --> S[Accepted tokens]
  I --> D{Diff}
  S --> D
  D --> X[Excess identity classes<br/>+ witness subject + TES]
  D --> G[Gated findings<br/>depend on GitHub environment rules]
  D --> U[Locked-out intent]
  X --> C[CI gate: exit 1]
```

</details>

<details>
<summary><b>chronos-keys</b>: dependency-aware secret rotation</summary>

```mermaid
flowchart LR
  INV[Declared consumer inventory<br/>refresh kind, TTL, delay bound,<br/>restart time, job schedule] --> G[Rotation Dependency Graph]
  ST[Store bounds<br/>add propagation] --> G
  G --> P[Staged planner<br/>add, promote, restart, wait, revoke]
  P --> PLAN[Ordered plan + safe-by times]
  PLAN --> GATE[Human approval / runbook]
  P --> SIM[Rotation simulator<br/>versions, caches, restarts, jobs]
  LOG[Access log<br/>usage guard, optional] -.-> P
  FLEET[Synthetic fleets<br/>incl. shadow + stale consumers] --> SIM
  SIM --> M[RBE + time-to-revoke<br/>failure taxonomy]
```

</details>

<details>
<summary><b>argus-evidence</b>: continuous ISO 27001 / SOC 2 evidence</summary>

```mermaid
flowchart LR
  CFG[Config history<br/>changes, snapshots,<br/>recorder heartbeats] --> TL[Control Operation Timeline<br/>hourly: verified / violated / unknown]
  LOG[Activity log<br/>API calls, sign-ins,<br/>hourly delivery digests] --> TL
  TIX[Ticket export] --> TL
  CTL[Control specs<br/>Python properties] --> TL
  TL --> ESS[Evidence Sufficiency Score]
  TL --> GAP[Gap report]
  TL --> BUN[Hash-chained bundle<br/>events + intervals]
  BUN --> VER[verify: chain + recompute<br/>+ optional anchored head]
  VER --> AUD[Auditor review]
```

</details>

<details>
<summary><b>ariadne-thread</b>: sensitive-data lineage through telemetry pipelines</summary>

```mermaid
flowchart LR
  SRC[Source declarations<br/>fields + labels per service] --> G[Collector graph<br/>receivers, pipelines,<br/>processors, connectors, exporters]
  CFG[Collector config<br/>JSON-encoded] --> G
  G --> TEP[TEP analyser<br/>label propagation on<br/>symbolic field templates]
  TEP --> P[Exposure paths<br/>source, label, form,<br/>backend, region, retention, field]
  CAN[Canary values<br/>3 formats per label] --> EMU[Pipeline emulator<br/>concrete values]
  G --> EMU
  EMU --> ST[Backend storage]
  ST --> GT[Ground truth<br/>canary search: raw and SHA-1]
  GT --> CMP{compare}
  P --> CMP
```

</details>

<details>
<summary><b>penelope-loom</b>: compensation-gated tool execution for AI agents</summary>

```mermaid
flowchart LR
  AG[Scripted agent plan<br/>+ one injected fault] --> GATE{Effect gate}
  REG[Tool registry<br/>effect class + compensation contract] --> GATE
  GATE -->|read / reversible| EXE[Execute with<br/>idempotency key]
  GATE -->|compensable + contract| EXE
  GATE -->|compensable, no contract| BLK[Block]
  GATE -->|irreversible| ESC[Escrow in ledger]
  EXE --> LED[(Effect ledger)]
  ESC --> LED
  LED --> OK{Plan commits?}
  OK -->|yes| APP[Human approves each<br/>held effect, then release]
  OK -->|no / crash| UNW[Discard escrow,<br/>unwind in reverse,<br/>guarded compensations]
  UNW --> HUM[Escalate what<br/>could not be undone]
```

</details>

<details>
<summary><b>cassandra-upgrade</b>: break risk for dependency updates</summary>

```mermaid
flowchart LR
  OLD[library vN<br/>parsed, never imported] --> DIFF[API diff<br/>removed, signature, default,<br/>body, transitive, changelog flag]
  NEW[library vN+1<br/>parsed, never imported] --> DIFF
  APP[client source] --> CG[call graph from the entry point<br/>+ argument shape of each call]
  TEST[client tests on vN<br/>line tracer] --> COV[covered call sites]
  DIFF --> R[reachable changed call sites<br/>+ call-site binding check]
  CG --> R
  R --> S[Break Risk Score<br/>noisy-OR over evidence]
  COV --> S
  CI[client tests on vN+1] --> D{red build, or<br/>score >= 0.5?}
  S --> D
  D -->|yes| B[block, with the call sites that explain why]
  D -->|no| M[merge]
  GT[ground truth: run the client workload<br/>on vN and on vN+1] -. evaluation only .-> E[benchmark]
```

</details>

<details>
<summary><b>chaos-witness</b>: chaos campaigns aimed at explicit obligations</summary>

```mermaid
flowchart LR
  C[contract.json<br/>10 obligations] --> G[campaign generator<br/>failure class -> proxy faults]
  G --> P1[LLM proxy] & P2[tool proxy] & P3[identity proxy] & P4[store proxy]
  W[client workload<br/>3 runs, 2 tenants] --> O[orchestrator under test]
  O --> P1 & P2 & P3 & P4
  P1 & P2 & P3 & P4 --> M[mock LLM / tool / IdP / store]
  P1 & P2 & P3 & P4 -. request log .-> V[obligation checks]
  M -. ledger, store, issued tokens .-> V
  W -. status, latency .-> V
  V --> A[verdicts, counterexamples, ACC]
```

</details>

<details>
<summary><b>faultweaver</b>: evidence-bounded remediation</summary>

```mermaid
flowchart LR
  S[Simulator: 17 services + 1 third-party API<br/>fault injection, blind spots,<br/>shared and faulty exporters] --> O[Observed telemetry<br/>metrics, logs, traces, change events]
  O --> G[Hypothesis generator<br/>graph-constrained, deterministic]
  G --> W[Diagnostic Witness Graph<br/>cause + propagation path + witnesses]
  W --> C{DWC >= tau?}
  C -->|no| P[Falsifying probe<br/>read-only, budget 3]
  P --> O
  C -->|yes| A[Remediation proposal]
  C -->|no probe left| E[Escalate to human]
```

</details>

<details>
<summary><b>burn-sentry</b>: uncertainty-aware SLO burn-rate alerting</summary>

```mermaid
flowchart LR
  REQ[Request outcomes<br/>per minute] --> W[Workbook long windows 1 h / 6 h<br/>+ traffic-aware short window]
  W --> POST[Beta-Binomial posterior<br/>per window]
  POST --> D{P burn > k x budget<br/>>= c ?}
  D -->|yes, short window agrees| PAGE[Page]
  D -->|no, but P >= 0.2<br/>and posterior wide| PROBE[Synthetic probe session<br/>6 req/min for 10 min]
  PROBE --> REQ
  D -->|no| OK[No action]
```

</details>

<details>
<summary><b>orpheus-rollback</b>: release reversibility analysis</summary>

```mermaid
flowchart LR
  REL[Release manifest<br/>changes + declared inverses<br/>+ declared code reads/writes] --> C[Change classifier<br/>reversibility type]
  C --> G[Release Reversibility Graph<br/>nodes: changes, old/new code<br/>edges: couplings]
  G --> V{Verdict}
  V -->|safe / safe with steps| PLAN[Ordered rollback plan]
  V -->|unsafe| REF[Refuse: roll forward<br/>or escalate]
  PLAN --> SIM[SQLite simulator<br/>traffic after every step]
  ORA[Oracle: execute every<br/>plan from the catalogue] --> GT[Ground truth]
  SIM --> EV[Errors / data-loss evidence]
  GT --> EV
```

</details>

<details>
<summary><b>canary-tribunal</b>: anytime-valid canary decisions for LLM features</summary>

```mermaid
flowchart LR
  T[Paired traffic:<br/>each sampled request<br/>replayed on both versions] --> B[Baseline outputs]
  T --> C[Canary outputs]
  B --> J[LLM judge scores<br/>simulated: noise, position bias,<br/>verbosity bias]
  C --> J
  H[Human-labelled<br/>calibration set] --> N[Judge-bias interval<br/>E judge diff - human diff]
  J --> CS[Anytime-valid confidence<br/>sequence on the paired difference]
  N --> Q[Quality interval:<br/>CS shifted and widened]
  CS --> Q
  GR[Latency / cost / refusal<br/>confidence sequences] --> D{Deterministic rule}
  Q --> D
  D --> P[Promote / rollback / continue]
```

</details>

<details>
<summary><b>terracog</b>: intent-aware Terraform drift triage</summary>

```mermaid
flowchart LR
  TF[terraform show -json<br/>resource_drift] --> G[Intent Delta Graph]
  EV[CloudTrail records<br/>principal, session, ticket] --> G
  IT[ITSM export<br/>incident / change status] --> G
  W[world.json<br/>service graph, SLO burn,<br/>policies, directory] --> G
  G --> I[intent + confidence]
  G --> R[REVERT end state:<br/>policy on IaC value,<br/>capacity or traffic lost]
  G --> C[CODIFY end state:<br/>policy on live value,<br/>capacity cut kept]
  I --> S[expected harm<br/>per action]
  R --> S
  C --> S
  S --> O[REVERT / CODIFY /<br/>QUARANTINE / HUMAN_REVIEW<br/>+ Markdown evidence]
```

</details>

<details>
<summary><b>titan-fleet</b>: LLM API routing + GPU autoscaling under SLO budgets</summary>

```mermaid
flowchart LR
  R[requests<br/>interactive / batch / background] --> P[slow planner<br/>Holt forecast, one cold start ahead]
  R --> Q[fast router<br/>marginal $ + budget-priced P miss]
  B[error-budget tracker<br/>per class] --> Q
  P -->|replicas| S[self-hosted pool<br/>queue, cold start, $/GPU-h]
  H[health: 5xx / 429 cooldowns,<br/>metered quota, queue depth] --> Q
  Q --> A[apiA-east / apiA-west<br/>Azure-OpenAI-like]
  Q --> BB[apiB-east<br/>Bedrock-like]
  Q --> S
  Q --> M[Prometheus-style counters]
```

</details>

<details>
<summary><b>midas-lens</b>: change-attributed cost anomalies for AI workloads</summary>

```mermaid
flowchart LR
  USE[Usage logs<br/>requests, tokens<br/>per route x tenant x model] --> SER[Factor series<br/>volume, mix,<br/>tokens in/out, price]
  PRICE[Price table] --> SER
  SER --> CP[CUSUM change points<br/>per factor x scope]
  CP --> MAT[Materiality check<br/>LMDI cost contribution]
  EVT[Change log<br/>deploy, prompt, config,<br/>routing, tenant, price] --> ATT[Alignment<br/>scope + type + time]
  MAT --> ATT
  ATT --> REP[Ranked causes<br/>USD/h each, or UNLOGGED]
```

</details>

<details>
<summary><b>carbon-oracle</b>: risk-bounded carbon-aware job scheduling</summary>

```mermaid
flowchart LR
  J[synthetic AI jobs<br/>class, runtime, deadline,<br/>residency zone] --> F[feasible windows<br/>allowed regions x start slots]
  C[GB regional carbon<br/>forecast] --> O[RGW optimizer<br/>min carbon + cost]
  H[history of queue-wait and<br/>runtime errors] --> B[chance constraint<br/>P miss <= eps]
  F --> O
  B --> O
  O --> P[placement: region, submit time]
  P --> S[simulator: realised carbon,<br/>queue wait, runtime]
  S --> R[Green Regret vs<br/>hindsight oracle]
```

</details>

---

## 🤝 Upstream open-source contributions

**30+ pull requests merged** into other people's projects.
[See every merged PR →](https://github.com/search?q=author%3Aharshit3355+is%3Apr+is%3Amerged+-user%3Aharshit3355&type=pullrequests)

| Project | Contribution |
| --- | --- |
| [daniel-b92/bruno-vs-code-extension](https://github.com/daniel-b92/bruno-vs-code-extension/pull/413) | Recursive, configurable sequence normalization in the collection explorer |
| [PreethamNoelP/checkride](https://github.com/PreethamNoelP/checkride/pull/22) | Document every detected sink, checked against the source |
| [RakTikoo/ci-command-truth](https://github.com/RakTikoo/ci-command-truth/pull/6) | Test fixtures for Python tooling commands in CI |
| [dlealvilla/local-ai-stack](https://github.com/dlealvilla/local-ai-stack/pull/43) | Document the runtime override environment variables |
| [kamranzafar/flipjack](https://github.com/kamranzafar/flipjack/pull/27) | Runnable Spring Boot example app, built and tested in CI |
| [gdt050579/AppCUI-rs](https://github.com/gdt050579/AppCUI-rs/pull/296) | Window guide with real terminal screenshots and an example app |
| [GoDiao/dreamcoder](https://github.com/GoDiao/dreamcoder/pull/260) | Provider-preset tutorial in English and Chinese |
| [kathennn/stream-clip-maker](https://github.com/kathennn/stream-clip-maker/pull/6) | Side-effect-free preview mode and numbered moment selection |
| [scylladb/python-driver](https://github.com/scylladb/python-driver/pull/1273) | Set the Python 3 language level for the Cython build |
| [Consolonia/Consolonia](https://github.com/Consolonia/Consolonia/pull/735) | CI: NativeAOT smoke test |
| [Kareadita/Kavita](https://github.com/Kareadita/Kavita/pull/4972) | Fix seams between images in the webtoon reader |
| [traceopt-ai/traceml](https://github.com/traceopt-ai/traceml/pull/650) | Hide the empty step-memory card on CPU-only runs |
| [Soneso/stellar-agent-wallet](https://github.com/Soneso/stellar-agent-wallet/pull/308) | Silence intentional ShellCheck warnings on macro metavariables |
| [Stellar-Developer-Observatory](https://github.com/The-Big-Danny/Stellar-Developer-Observatory/pull/43) | CI: dependency and license audit |
| [flisk-sh/citable](https://github.com/flisk-sh/citable/pull/46) | Return 404 for static-file paths |
| [repo-engineering-skills](https://github.com/basitalisandhu/repo-engineering-skills/pull/10) | Verify environment defaults in docs ([+1 follow-up](https://github.com/basitalisandhu/repo-engineering-skills/pull/13)) |
| [hettiger/clg](https://github.com/hettiger/clg/pull/24) | Configurable release timezone |
| [adjective-rob/snap](https://github.com/adjective-rob/snap/pull/5) | Windows setup script |

---

## 🏗️ Infrastructure reference builds

| Project | What it is |
| --- | --- |
| [**aws-ecs-platform-blueprint**](https://github.com/harshit3355/aws-ecs-platform-blueprint) | Terraform + ECS Fargate on AWS: 3-tier VPC, RDS PostgreSQL, gated GitHub Actions delivery, Prometheus/Grafana and CloudWatch |
| [**aws-ecs-terraform**](https://github.com/harshit3355/aws-ecs-terraform) | `Internet → ALB → ECS Fargate → RDS`, plus local Postgres with migrations, seed data and self-verifying backup/restore |
| [**ansible-linux-lab**](https://github.com/harshit3355/ansible-linux-lab) | Ansible done properly: inventory as code, idempotent roles, validated handlers, staged rollouts, health checks |
| [**wisecow-kubernetes-tls**](https://github.com/harshit3355/wisecow-kubernetes-tls) | A legacy Bash service containerised and run on Kubernetes behind NGINX Ingress with cert-manager TLS |
| [**flask-counter-ecr-pipeline**](https://github.com/harshit3355/flask-counter-ecr-pipeline) | Source to resource-capped container: Docker, SonarQube, GitHub Actions to Amazon ECR |
| [**strapi-ephemeral-ec2-environments**](https://github.com/harshit3355/strapi-ephemeral-ec2-environments) | Disposable environments on EC2: Terraform plus on-demand deploy and destroy workflows |
| [**azure-vm-health-check**](https://github.com/harshit3355/azure-vm-health-check) | Bash sweep of VMs across Azure subscriptions, CPU/memory/disk as CSV with threshold alerts |
| [**selfhosting-reference-library**](https://github.com/harshit3355/selfhosting-reference-library) | Compose stacks, Ansible playbooks and reverse-proxy configs for ~90 self-hosted services |

---

## ✍️ Writing

I write up each project on [Medium](https://medium.com/@harshitnagila555): the problem, what I built, the numbers and the limits.

- [Your Chaos Test Passed. Which Guarantee Did It Actually Check?](https://medium.com/@harshitnagila555/your-chaos-test-passed-which-guarantee-did-it-actually-check-b34b55fc8353)
- [The Linter Should Not Hold the Keys to the Kingdom](https://medium.com/@harshitnagila555/the-linter-should-not-hold-the-keys-to-the-kingdom-6a7d0e97580d)
- [Right Service, Wrong Fix](https://medium.com/@harshitnagila555/right-service-wrong-fix-adc57294a60e)
- [When Terraform and the Cloud Disagree, Which One Is Right?](https://medium.com/@harshitnagila555/when-terraform-and-the-cloud-disagree-which-one-is-right-3324a1553c4d)
- [Your LLM Gateway and Your GPU Autoscaler Don't Share a Budget](https://medium.com/@harshitnagila555/your-llm-gateway-and-your-gpu-autoscaler-dont-share-a-budget-31f0278bc1aa)
- [Your Image Is Signed. Is Your AI Deployment?](https://medium.com/@harshitnagila555/your-image-is-signed-is-your-ai-deployment-01c2dbaa572a)
- [One Rule, Four Policies: Testing Policy-as-Code Across Enforcement Surfaces](https://medium.com/@harshitnagila555/one-rule-four-policies-testing-policy-as-code-across-enforcement-surfaces-38fa87a24ced)
- [AI Agents Are Writing Your Infrastructure Code. Is Anyone Governing It?](https://medium.com/@harshitnagila555/ai-agents-are-writing-your-infrastructure-code-is-anyone-governing-it-2a2db17750f7)
- [Forty Minutes Was Enough](https://medium.com/@harshitnagila555/forty-minutes-was-enough-19709bc59072)
- [Deploy Without Fear](https://medium.com/@harshitnagila555/deploy-without-fear-5992ac7dbca6)

---

## 🧰 Tech

<p>
  <img src="https://skillicons.dev/icons?i=azure,aws,gcp,terraform,docker,kubernetes,ansible,githubactions,jenkins,grafana,prometheus,python,bash,linux,postgres,redis&theme=dark&perline=8" alt="Azure, AWS, GCP, Terraform, Docker, Kubernetes, Ansible, GitHub Actions, Jenkins, Grafana, Prometheus, Python, Bash, Linux, PostgreSQL, Redis" />
</p>

**Cloud**: Azure (Container Apps, App Service, Front Door, APIM, Key Vault, Logic Apps, Azure OpenAI, Cosmos DB) · AWS (ECS Fargate, EKS, ECR, Lambda, EventBridge, S3, RDS, CloudFront, Bedrock) · GCP

**Infrastructure as code and containers**: Terraform (modular, multi-environment) · Ansible · Docker · Kubernetes · Helm · NGINX Ingress · cert-manager

**CI/CD and GitOps**: GitHub Actions · Azure DevOps · GitLab CI · Jenkins · Argo CD · GitHub OIDC

**DevSecOps**: Trivy · SonarQube · Gitleaks · Bandit · Safety · Snyk · OPA / Rego · Checkov

**Observability**: Prometheus · Grafana · Log Analytics · CloudWatch · CloudTrail · Datadog · ELK

**Languages**: Python · Bash · SQL · JavaScript

---

## 🎖️ Certifications

![AWS CloudOps Engineer – Associate](https://img.shields.io/badge/AWS-CloudOps_Engineer_Associate-FF9900?style=flat-square&logo=amazonwebservices&logoColor=white)
![HashiCorp Terraform Associate 004](https://img.shields.io/badge/HashiCorp-Terraform_Associate_004-844FBA?style=flat-square&logo=terraform&logoColor=white)
![AWS Cloud Practitioner](https://img.shields.io/badge/AWS-Cloud_Practitioner-FF9900?style=flat-square&logo=amazonwebservices&logoColor=white)
![Azure Fundamentals AZ-900](https://img.shields.io/badge/Microsoft-Azure_Fundamentals_AZ--900-0078D4?style=flat-square&logo=microsoftazure&logoColor=white)
![OCI Foundations](https://img.shields.io/badge/Oracle-OCI_Foundations-F80000?style=flat-square&logo=oracle&logoColor=white)
![Google Cybersecurity](https://img.shields.io/badge/Google-Cybersecurity_Professional-4285F4?style=flat-square&logo=google&logoColor=white)
![IBM DevOps](https://img.shields.io/badge/IBM-DevOps_for_Enterprise_Agility-052FAD?style=flat-square&logo=ibm&logoColor=white)

---

## 📊 GitHub activity

<div align="center">
  <img src="https://www.gitskins.com/api/premium-card?username=harshit3355&theme=midnight" alt="GitSkins profile card" width="80%" />
  <br/><br/>
  <img src="https://raw.githubusercontent.com/harshit3355/harshit3355/output/stats.svg" alt="GitHub stats" width="49%" />
  <img src="https://raw.githubusercontent.com/harshit3355/harshit3355/output/top-langs.svg" alt="Top languages" width="49%" />
  <br/><br/>
  <img src="https://streak-stats.demolab.com/?user=harshit3355&background=0F172A&ring=7C3AED&fire=70A5FD&currStreakNum=FFFFFF&sideNums=FFFFFF&currStreakLabel=70A5FD&sideLabels=A5B4FC&dates=94A3B8&stroke=1E3A8A&hide_border=true&border_radius=12" alt="Contribution streak" width="70%" />
  <br/><br/>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/harshit3355/harshit3355/output/github-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/harshit3355/harshit3355/output/github-snake.svg" />
    <img src="https://raw.githubusercontent.com/harshit3355/harshit3355/output/github-snake-dark.svg" alt="A snake eating my GitHub contribution graph, regenerated daily" width="100%" />
  </picture>
</div>

---

<div align="center">

<sub>MCA, Manipal University Jaipur (CGPA 9.01) · BCA, Chandigarh University · Employee of the Quarter, Q1 2025<br/>
Former GDSC Cloud Lead: taught cloud to 500+ students through hands-on workshops</sub>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:7c3aed,50:1e3a8a,100:0f172a&height=120&section=footer" alt="" width="100%" />

<sub>Widgets: [GitSkins](https://www.gitskins.com) (Midnight) · [capsule-render](https://github.com/kyechan99/capsule-render) · [readme-typing-svg](https://github.com/DenverCoder1/readme-typing-svg) · [github-readme-stats](https://github.com/stats-organization/github-readme-stats-action) · [streak-stats](https://github.com/DenverCoder1/github-readme-streak-stats) · [Platane/snk](https://github.com/Platane/snk)</sub>

</div>
