# Reprocess tool catalog (open-source first)

Status: DRAFT, last reviewed 2026-11. Licenses reflect the maintainer's best knowledge and **must be re-verified before each release**. Projects change licenses, owners and security posture; always tell the user to check the current license, version and security advisories.

**Security rule for every self-hosted tool:** keep it off the public internet (VPN for remote access), turn on authentication and MFA, change default passwords, patch at least monthly, and subscribe to the project's GitHub Security Advisories. Several tools below have had critical remote-code-execution bugs, some listed in the CISA Known Exploited Vulnerabilities catalog. That's a reason to patch fast and keep them internal, not necessarily to avoid them. See the "Safe default deployment" notes at the end.

Columns: **Tool** · **Use it for** · **License** · **Skill** (N = no-code UI, L = low-code, C = code) · **Self-host effort** (S/M/L) · **Notes**

"OSI" = an OSI-approved open-source license. "Source-available" = the code is public but use is restricted. Say so when you recommend one.

## Orchestration and integration (moving data between systems, schedules, triggers)
| Tool | Use it for | License | Skill | Self-host | Notes |
|---|---|---|---|---|---|
| n8n | Visual workflows, 400+ integrations, AI nodes, approval steps ("send and wait for response") | Sustainable Use License (source-available, not OSI) | N/L | S | Free to self-host for your own internal business use. Hosting it for clients or inside a paid product may need a commercial license (verify). SSO, external secrets and log streaming are paid features (verify). Has had critical RCEs in 2025–26 (e.g. CVE-2025-68613, in CISA KEV): patch promptly. Most popular choice for business users. |
| Activepieces | Visual workflows, Zapier-like | MIT (community edition) | N | S | Some enterprise features are paid. Fewer integrations than n8n. |
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
| Tesseract | OCR engine | Apache-2.0 | C | S | Weak on poor photos and handwriting. |
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
| Invoice Ninja | Invoicing, quotes, payment reminders, client portal | Elastic License 2.0 for v5 (source-available, not OSI; verify) | N | M | Free to self-host for your own business; a hosted plan exists. |

## Process modeling (documenting the as-is / to-be)
| Tool | Use it for | License | Notes |
|---|---|---|---|
| Mermaid | Diagrams as text (used in Reprocess reports) | MIT | Renders on GitHub, many wikis, mermaid.live. |
| draw.io (diagrams.net) | Drag-and-drop process diagrams | Apache-2.0 | Desktop app or browser. |

## Selection notes for the AI
- Corporate users often can't self-host without IT approval. Say what approval they'll need and offer the least-infrastructure option.
- Prefer one orchestration tool and add others only for clear gaps.
- Local models (Ollama) keep data in-house but are less accurate than large hosted models. Say this trade-off plainly.
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
