# Reprocess tool catalog (open-source first)

Status: DRAFT, last reviewed 2026-11. Licenses reflect the maintainer's best knowledge and **must be re-verified before each release**. Projects change licenses, owners and security posture; always tell the user to check the current license, version and security advisories.

**Security rule for every self-hosted tool:** keep it off the public internet (VPN for remote access), turn on authentication and MFA, change default passwords, patch at least monthly, and subscribe to the project's GitHub Security Advisories. Several tools below have had critical remote-code-execution bugs, some listed in the CISA Known Exploited Vulnerabilities catalog. That's a reason to patch fast and keep them internal, not necessarily to avoid them. See the "Safe default deployment" notes at the end.

Columns: **Tool** · **Use it for** · **License** · **Skill** (N = no-code UI, L = low-code, C = code) · **Self-host effort** (S/M/L) · **Notes**

"OSI" = an OSI-approved open-source license. "Source-available" = the code is public but use is restricted. Say so when you recommend one.

## Start here: what the user already has
Before any new tool, check the built-in features of what the user already has: their booking app, accounting software, online marketplace, point-of-sale, office suite (rules, forms, templates, reminders, built-in automation), and in organizations the ERP, warehouse, planning and CRM systems (configuration, unused licensed modules, workflow and approval engines). Ask the system owner to verify. These need no new system and often deliver most of the saving. Name these tools only when the user has named them. Paid add-ons or higher tiers of tools they already use are fair options; label them commercial, price "verify".

**Naming rule:** never name commercial products, except tools the user says they already use. Describe the tool type (e.g. "booking app with deposits", "field-service app", "AP invoice-capture service", "validated eQMS", "carrier identity-verification service") and attach the tool assessment kit. Open-source tools below may be named on the build path.

**Technical comfort decides the options:**
- *Apps only*: tools they already have, then ready-made tool types, with step-by-step how-to and safe-use rules. A general-purpose AI assistant on a business plan (not a consumer plan for sensitive data) is often the right "AI" for drafting and summarizing; explain how to use it safely (no personal or confidential data unless the plan's terms allow it, check every output). Nothing from the self-hosted sections below.
- *Configure*: settings, rules and built-in automation in tools they have, plus low-code open-source tools if they can get them approved or hosted. Employees: see "Inside a company" below.
- *Build*: open-source tools below, with the build disclaimer, access design, security, compliance and legal steps. Self-hosting only if they can run, patch and back up a server; in organizations, label it an "IT project" and name the approval path.
- Spreadsheets: LibreOffice Calc (MPL-2.0; verify), or the spreadsheet they already use.
- Forms: the office suite's form tool if already licensed; LimeSurvey (GPL-2.0+) or Formbricks (AGPL-3.0 core, some paid modules) if self-hosting.
- For solo and micro businesses with no IT person, the recommended option should need **no server**. Self-hosted rows below are alternatives unless the user says they can run, patch and back up a server.
- Don't recommend Skill C tools to users who said no-code or low-code.

## Inside a company: configure what you already have
For employees, "configure" usually means asking a system owner, not installing anything.
- Ask each system owner (HR system, applicant tracking, ERP, CRM, ticketing, reconciliation tool) what the licensed version already does; expect queue time and change control.
- The company's own low-code workflow tool (name it only if the user does) runs under admin data-loss-prevention rules: check allowed connectors and whether flows touching personal or financial data must be registered.
- Flows run under a service account or shared connection with a named co-owner, never one person's login.
- Built-in AI features of existing systems are new AI steps: check what they read, write and send, whether they act without a human, and their data terms (assessment kit).
- Agents built in the office suite share their knowledge with everyone they're shared with.
- Self-hosting open-source tools is an IT project with a security review: offer it only as an alternative, and only if the user's IT team builds and runs software.

## Orchestration and integration (moving data between systems, schedules, triggers)
| Tool | Use it for | License | Skill | Self-host | Notes |
|---|---|---|---|---|---|
| n8n | Visual workflows, 400+ integrations, AI nodes, approval steps ("send and wait for response") | Sustainable Use License (source-available, not OSI) | N/L | S | Free to self-host for your own internal business use. Hosting it for clients or inside a paid product may need a commercial license (verify). SSO, external secrets and log streaming are paid features (verify). Has had critical RCEs in 2025–26 (e.g. CVE-2025-68613, in CISA KEV): patch promptly. Most popular choice for business users. |
| Activepieces | Visual workflows, similar to commercial no-code automation services | MIT (community edition) | N | S | Some enterprise features are paid. Fewer integrations than n8n. |
| Node-RED | Event/IoT-style flows, device and API wiring | Apache-2.0 | L | S | Strong for factory/IoT/sensor data. The editor has no login by default: set `adminAuth` and `credentialSecret`. |
| Windmill | Scripts plus flows plus internal UIs | AGPL-3.0 (core) | L/C | M | Good when a team writes Python/TypeScript. AGPL: offering it to outside users over a network triggers source-sharing duties. |
| Kestra | Declarative (YAML) data and process orchestration | Apache-2.0 | L/C | M | Good for scheduled data pipelines. |
| Prefect | Python workflow orchestration | Apache-2.0 | C | M | For data/engineering teams. |
| Apache Airflow | Scheduled batch data pipelines | Apache-2.0 | C | L | Heavy; enterprise data teams. |
| Temporal | Long-running, durable business processes with retries | MIT | C | L | For engineering teams building critical multi-day workflows. |

## AI models and runtimes
| Tool | Use it for | License | Skill | Self-host | Notes |
|---|---|---|---|---|---|
| Ollama | Run open-weight LLMs locally or on a server | MIT | L | S | Quality depends on model size and hardware. Small models are weaker at complex extraction. **No built-in authentication:** keep it on localhost (`OLLAMA_HOST`) or behind an authenticating proxy. |
| vLLM | High-throughput model serving | Apache-2.0 | C | L | Needs GPUs; for large volume. |
| LocalAI | OpenAI-compatible local API | MIT | L | M | Drop-in for tools expecting an OpenAI-style API. |
| Open-weight models (Llama, Mistral, Qwen, Gemma, etc.) | The models themselves | Varies, each has its own license | — | — | Check each model's license for commercial use. Most are not OSI. Llama: community license with a user cap and acceptable-use policy. Gemma: terms with prohibited-use policy. Mistral and Qwen: varies by model (some Apache-2.0). |
| Hosted model APIs (any provider) | Larger, more accurate models without hardware | Commercial service | L | none | Not open source. Before sending business or personal data, check the data processing agreement, data region, retention, and whether inputs are used for training. Business plans differ from consumer plans. For health data you need a BAA. Set spend caps. |

## AI app and agent builders
| Tool | Use it for | License | Skill | Self-host | Notes |
|---|---|---|---|---|---|
| Dify | Visual LLM apps, RAG chatbots, AI workflows | Apache-2.0 with extra conditions (not OSI) | N/L | M | Extra conditions limit multi-tenant SaaS use and logo removal. Verify. |
| Flowise | Visual LLM chains and agents | Apache-2.0 | N/L | S | Has had auth-bypass and RCE CVEs: internal only, auth on, update promptly. Acquired in 2025 (verify current ownership and roadmap). |
| Langflow | Visual LLM flows | MIT | N/L | S | Several CVEs in CISA KEV since 2025, incl. unauthenticated RCE (CVE-2025-3248): internal only, auth on, update promptly. |
| AnythingLLM | Chat with your documents (RAG), desktop or server | MIT | N | S | Easiest "ask our SOPs/policies" setup. Index only curated, access-controlled documents; check that user permissions carry through. |
| LangGraph | Code-first agent workflows with human-in-the-loop checkpoints | MIT | C | M | |
| CrewAI | Code-first multi-agent workflows | MIT | C | M | |
| Haystack | Code-first RAG and search pipelines | Apache-2.0 | C | M | |

## Documents, OCR and extraction
| Tool | Use it for | License | Skill | Self-host | Notes |
|---|---|---|---|---|---|
| Paperless-ngx | Scan, OCR, tag and archive documents (receipts, invoices, letters) | GPL-3.0 | N | S | Has built-in auto-matching for tags and correspondents. Community AI add-ons exist; verify maturity and review them as code with access to all your documents. Turn on MFA; use an app password for the mail inbox. |
| Tesseract | OCR engine | Apache-2.0 | C | S | Command-line/developer tool, not for no-code users. Weak on poor photos and handwriting. |
| docTR | Deep-learning OCR | Apache-2.0 | C | M | Better on varied layouts than Tesseract. |
| Docling | Convert PDFs/Office files to structured text/tables for LLMs | MIT | C | S | |
| Unstructured | Parse many document types for LLM pipelines | Apache-2.0 | C | M | |

## Human review, forms and internal tools (where human gates live)
| Tool | Use it for | License | Skill | Self-host | Notes |
|---|---|---|---|---|---|
| n8n forms / wait nodes | Simple approve/reject steps by email, chat or form | see above | N | S | Enough for many low-risk gates. Approval links may work for anyone who holds them (verify): for money or regulated gates, require a login and log the approver. Set timeouts to hold, never auto-approve. |
| Appsmith | Internal review queues and admin UIs | Apache-2.0 | L | M | Check default-config security advisories (verify); keep internal. |
| Budibase | Internal apps and approval forms | GPL-3.0 (core) | N/L | M | |
| ToolJet | Internal tools | AGPL-3.0 | L | M | |
| Baserow | Airtable-like database with forms | MIT (core) | N | S | Good shared "work queue" table. |
| Label Studio | Reviewing and correcting AI labels/extractions at volume | Apache-2.0 | L | M | Useful when tracking AI accuracy. |

## Small-business operations (booking, CRM, invoicing, marketing, time, files)
Licences checked against each project's GitHub repository on 2026-11-10; re-verify before relying on them.
| Tool | Use it for | License | Skill | Self-host | Notes |
|---|---|---|---|---|---|
| Easy!Appointments | Online booking and appointment reminders | GPL-3.0 | N | M | Needs a web server. Most solo owners are better served by the booking feature of an app they already use. |
| Cal.com | Scheduling links and booking | MIT per current repo (repository moved in 2026; verify) | N | M | Hosted plans exist (commercial). |
| EspoCRM | CRM: leads, contacts, follow-up tasks | AGPL-3.0 | N/L | M | |
| Twenty | Modern CRM | AGPL-3.0 with some commercial-licensed files | N/L | M | |
| Mautic | Email marketing automation | GPL-3.0 | L | M | Consent and unsubscribe handling are your responsibility (see risk checklist §8). |
| listmonk | Newsletters and mailing lists | AGPL-3.0 | L | S | Needs an email-sending service (SMTP provider). |
| Invoice Ninja | Invoicing, quotes, payment reminders, client portal | Elastic License 2.0 (source-available, not OSI) | N | M | Free to self-host for your own business; hosted plan exists. |
| Akaunting | Small-business accounting and invoicing | Business Source License (source-available, not OSI) | N | M | Check the licence's use grant. |
| Kimai | Time tracking and timesheets | AGPL-3.0 | N | S | Staff hours feed pay; check working-time and pay rules. |
| Nextcloud | File sharing, client upload folders, calendar | AGPL-3.0 | N | M | Use expiring, password-protected upload links for client documents. |
| Vaultwarden / Bitwarden | Shared password manager (door codes, logins) | Vaultwarden: AGPL-3.0 (unofficial server). Bitwarden server: AGPL-3.0 plus Bitwarden License for some features | N | S | Hosted Bitwarden plans are commercial and need no server. Remove access the day someone leaves. |
| OmegaT | Translation memory (CAT tool) | GPL-3.0 (verify) | N | none (desktop) | |

**SMS and phone:** sending business texts always needs a commercial carrier or SMS gateway, and in the US usually 10DLC registration. There's no realistic open-source way around it. Consent and opt-out rules apply (risk checklist §8).

## Analytics, forecasting and optimization (numbers come from these, never from LLM text)
| Tool | Use it for | License | Skill | Self-host | Notes |
|---|---|---|---|---|---|
| pandas | Data cleaning and analysis in Python | BSD-3-Clause | C | none | |
| statsmodels | Statistical models, time-series forecasting | BSD-3-Clause | C | none | |
| scikit-learn | Machine-learning models (classification, regression, anomaly detection) | BSD-3-Clause | C | none | |
| Nixtla StatsForecast | Fast statistical forecasting at scale | Apache-2.0 | C | none | Back-test against the current method and a naive forecast before use. |
| Google OR-Tools | Optimization (routing, scheduling, load building) | Apache-2.0 | C | none | Open-source library despite the corporate maintainer. |
Any model that feeds decisions without per-item review: define the baseline it must beat, back-test, monitor accuracy and bias, and name an owner. In regulated or audited processes it may need validation.

## Reporting and monitoring
| Tool | Use it for | License | Skill | Self-host | Notes |
|---|---|---|---|---|---|
| Metabase | Dashboards for business users | AGPL-3.0 | N | S | Had a pre-auth RCE (CVE-2023-38646); other Metabase CVEs are in CISA KEV. Keep updated and internal. |
| Apache Superset | Enterprise BI dashboards | Apache-2.0 | L | M | |
| Grafana | Operational/time-series dashboards and alerts | AGPL-3.0 | L | M | Relicensed from Apache-2.0 in 2021. Keep updated (past CVEs in CISA KEV, e.g. CVE-2021-43798). |
| Langfuse | Trace, evaluate and monitor LLM calls (accuracy, cost) | MIT (core) | L | M | Use for B/C steps to measure correction rates. |
| Great Expectations | Data-quality checks | Apache-2.0 | C | M | Catch bad input before AI sees it. |

## Business systems (when the real gap is "no system of record")
| Tool | Use it for | License | Skill | Self-host | Notes |
|---|---|---|---|---|---|
| Odoo Community | ERP: sales, purchasing, inventory, accounting | LGPL-3.0 | N/L | M | Many modules are Enterprise-only (paid). Verify which you need. |
| ERPNext | ERP: accounting, inventory, HR, manufacturing | GPL-3.0 | N/L | M | Fully open source. |
| Firefly III | Personal/small-business finance tracking with rules engine | AGPL-3.0 | N | S | Not a full accounting/invoicing system. |
| GnuCash | Desktop double-entry bookkeeping; CSV import learns your categories | GPL-2.0+ | N | none (desktop) | No server needed. |

## Process modeling (documenting the as-is / to-be)
| Tool | Use it for | License | Notes |
|---|---|---|---|
| Mermaid | Diagrams as text (used in Reprocess reports) | MIT | Renders on GitHub, many wikis, mermaid.live. |
| draw.io (diagrams.net) | Drag-and-drop process diagrams | Apache-2.0 | Desktop app or browser. |

## Selection notes for the AI
- Corporate users often can't self-host without IT approval. Say what approval they'll need and offer the least-infrastructure option. If no open-source option is realistic under their IT constraints, say so in one line instead of padding.
- Corporate IT and security reviews check: SSO/SAML, audit logs, role-based access, data residency, and for regulated use e-signatures and validation support. Many open-source tools keep SSO and audit logs in paid editions: say "verify which edition includes it".
- An interactive AI chat assistant is not the same as an AI model an automation can call unattended. A step that needs AI inside a flow needs an API or a local model, with its own data terms.
- Prefer one orchestration tool and add others only for clear gaps.
- Local models (Ollama) keep data in-house but are less accurate than large hosted models. Say this trade-off plainly. It is also a legal question, not just accuracy: health, tax, children's or NDA-covered data may go to a hosted AI or SaaS only under the right agreement (BAA, DPA, client consent). Never suggest consumer AI plans for it (risk checklist §3–4).
- If the data is regulated, prefer the option with the fewest new systems holding it.
- Self-hosting means owning updates, backups, security patches and uptime. Include a maintenance estimate. If the user can't commit to monthly patching, recommend a desktop or managed option instead.
- For any AI step that reads emails, documents or web pages, follow the risk checklist's security section (prompt injection, least privilege, no send/pay/write tools without a gate).

## Safe default deployment (one line per tool)
- **n8n:** set `N8N_ENCRYPTION_KEY` and back it up separately; disable community packages in production (`N8N_COMMUNITY_PACKAGES_ENABLED=false`, verify); give each credential minimal scopes (e.g. read-only mail); keep it off the internet; require login on approval forms; patch promptly.
- **Ollama:** bind to localhost; it has no authentication. If other machines need it, put it behind a reverse proxy with authentication.
- **Langflow / Flowise / Dify:** internal network only, authentication on, update promptly. All have had serious CVEs.
- **Metabase / Grafana / Appsmith:** SSO or MFA, internal only, keep updated.
- **Paperless-ngx:** MFA; use a mail app password with the least access; encrypted backups.
- **Node-RED:** set `adminAuth` and `credentialSecret` before connecting anything real.
- **Any tool:** one service account per workflow, no admin API users, secrets in the tool's credential store or a secret manager, never in code or prompts.

Don't keep CVE lists here (they go stale). Point users to each project's GitHub Security Advisories page and to CISA KEV.
