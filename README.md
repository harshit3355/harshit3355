# Harshit Nagila

**DevOps & Cloud Infrastructure Engineer** — DevSecOps · Azure · AWS · Terraform

I build secure, production-grade cloud infrastructure. For the past two years I have owned the Terraform,
DevSecOps and observability foundations behind **ciATHENA**, an agentic AI analytics platform serving
life-sciences clients — three isolated Azure environments on Container Apps plus an independent AWS
production stack on ECS Fargate.

Most of my day-to-day work lives in private repositories. What is here are the reference builds:
complete, documented infrastructure I use to work out a pattern before it goes anywhere near production.

📍 Gurugram, India · 🔗 [Portfolio](https://harshit-portfolio-3355.netlify.app) · [LinkedIn](https://linkedin.com/in/harshit555) · ✉️ harshitnagila3355@gmail.com

---

## What I work on

- **Multi-cloud infrastructure as code** — reusable Terraform modules provisioning 85+ resources per
  environment with isolated state, making a new client environment reproducible instead of hand-built.
- **DevSecOps pipelines** — GitHub Actions gating every pull request on Gitleaks, Bandit and Flake8 SAST,
  Safety CVE checks, SonarQube quality gates and Trivy image scans at zero-critical thresholds.
- **Supply chain hardening** — GitHub OIDC role assumption replacing static cloud keys, per-environment
  scoped secrets, BuildKit-injected secrets that never persist in image layers, SHA-pinned actions.
- **Observability** — centralised across Azure Managed Grafana, Log Analytics, CloudWatch and CloudTrail.

---

## Selected work

| Project | What it is |
| --- | --- |
| [**aws-ecs-platform-blueprint**](https://github.com/harshit3355/aws-ecs-platform-blueprint) | Terraform + ECS Fargate platform: 3-tier VPC, RDS PostgreSQL, gated GitHub Actions delivery pipeline, Prometheus/Grafana and CloudWatch observability |
| [**aws-ecs-terraform**](https://github.com/harshit3355/aws-ecs-terraform) | `Internet → ALB → ECS Fargate → RDS` stack, plus a local Postgres environment with migrations, seed data, an indexed reporting query, and backup/restore scripts that verify their own work |
| [**ansible-linux-lab**](https://github.com/harshit3355/ansible-linux-lab) | Disciplined Ansible: inventory as code, reusable role defaults, idempotent tasks, validated handlers, staged rollouts, post-deployment health checks |
| [**wisecow-kubernetes-tls**](https://github.com/harshit3355/wisecow-kubernetes-tls) | Containerising a non-cloud-native Bash service and running it properly on Kubernetes behind NGINX Ingress with cert-manager TLS |
| [**flask-counter-ecr-pipeline**](https://github.com/harshit3355/flask-counter-ecr-pipeline) | The full path from source to a resource-capped, registry-hosted container — Docker, SonarQube, GitHub Actions to Amazon ECR |
| [**selfhosting-reference-library**](https://github.com/harshit3355/selfhosting-reference-library) | Deployable Compose stacks, Ansible playbooks and reverse-proxy configs for ~90 self-hosted services |

---

## Tech

**Cloud** — Azure (Container Apps, Front Door, VNets, Private Endpoints, Azure OpenAI, Cosmos DB) · AWS (ECS Fargate, ECR, EC2, VPC, CloudFront, PrivateLink, DynamoDB, Aurora, Bedrock)

**Infrastructure as Code** — Terraform (modular, multi-environment) · Ansible · SaltStack · Docker · EKS

**CI/CD & GitOps** — GitHub Actions · GitLab CI · Jenkins · CircleCI · Argo CD · GitHub OIDC

**DevSecOps** — SonarQube · Trivy · Gitleaks · Bandit · Flake8 · Safety · Snyk

**Security & Compliance** — Azure HIPAA Policy Pack · AWS Conformance Packs · WAF · Zero Trust networking

**Observability** — Prometheus · Grafana · Datadog · Splunk · ELK · Azure Managed Grafana · Log Analytics · CloudWatch · CloudTrail

**Data** — Snowflake · PostgreSQL · Cosmos DB · Redis · Azure SQL

**Languages** — Python · Bash · JavaScript · SQL

---

## Certifications

HashiCorp Terraform Associate (004) · Microsoft Azure Fundamentals (AZ-900) · AWS Certified Cloud Practitioner · Google Cloud Cybersecurity Professional · Oracle Cloud Infrastructure Foundations · IBM DevOps for Enterprise Agility

---

<sub>MCA, Manipal University Jaipur · Former GDSC Cloud Lead — taught cloud technologies to 500+ students through hands-on workshops.</sub>
