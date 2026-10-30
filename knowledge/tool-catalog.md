# Reprocess tool catalog (open-source first)

Status: DRAFT. Licenses reflect the maintainer's best knowledge as of mid-2026 and **must be re-verified before each release**. Projects change licenses; always tell the user to check the current license and version.

Columns: **Tool** · **Use it for** · **License** · **Skill** (N = no-code UI, L = low-code, C = code) · **Self-host effort** (S/M/L) · **Notes**

"OSI" = an OSI-approved open-source license. "Source-available" = the code is public but use is restricted. Say so when you recommend one.

## Orchestration and integration (moving data between systems, schedules, triggers)
| Tool | Use it for | License | Skill | Self-host | Notes |
|---|---|---|---|---|---|
| n8n | Visual workflows, 400+ integrations, AI nodes, approval steps ("send and wait for response") | Sustainable Use License (source-available) | N/L | S | Free to self-host for internal business use; not OSI. Most popular choice for business users. |
| Activepieces | Visual workflows, Zapier-like | MIT (community edition) | N | S | Some enterprise features are paid. Fewer integrations than n8n. |
| Node-RED | Event/IoT-style flows, device and API wiring | Apache-2.0 | L | S | Strong for factory/IoT/sensor data. |
| Windmill | Scripts plus flows plus internal UIs | AGPL-3.0 (core) | L/C | M | Good when a team writes Python/TypeScript. |
| Kestra | Declarative (YAML) data and process orchestration | Apache-2.0 | L/C | M | Good for scheduled data pipelines. |
| Prefect | Python workflow orchestration | Apache-2.0 | C | M | For data/engineering teams. |
| Apache Airflow | Scheduled batch data pipelines | Apache-2.0 | C | L | Heavy; enterprise data teams. |
| Temporal | Long-running, durable business processes with retries | MIT | C | L | For engineering teams building critical multi-day workflows. |

## AI models and runtimes
| Tool | Use it for | License | Skill | Self-host | Notes |
|---|---|---|---|---|---|
| Ollama | Run open-weight LLMs locally or on a server | MIT | L | S | Quality depends on model size and hardware. Small models are weaker at complex extraction. |
| vLLM | High-throughput model serving | Apache-2.0 | C | L | Needs GPUs; for large volume. |
| LocalAI | OpenAI-compatible local API | MIT | L | M | Drop-in for tools expecting an OpenAI-style API. |
| Open-weight models (Llama, Mistral, Qwen, Gemma, etc.) | The models themselves | Varies, each has its own license | — | — | Check each model's license for commercial use. Not all are OSI. |

## AI app and agent builders
| Tool | Use it for | License | Skill | Self-host | Notes |
|---|---|---|---|---|---|
| Dify | Visual LLM apps, RAG chatbots, AI workflows | Apache-2.0 with extra conditions | N/L | M | Extra conditions limit multi-tenant SaaS use and logo removal. Verify. |
| Flowise | Visual LLM chains and agents | Apache-2.0 | N/L | S | |
| Langflow | Visual LLM flows | MIT | N/L | S | |
| AnythingLLM | Chat with your documents (RAG), desktop or server | MIT | N | S | Easiest "ask our SOPs/policies" setup. |
| LangGraph | Code-first agent workflows with human-in-the-loop checkpoints | MIT | C | M | |
| CrewAI | Code-first multi-agent workflows | MIT | C | M | |
| Haystack | Code-first RAG and search pipelines | Apache-2.0 | C | M | |

## Documents, OCR and extraction
| Tool | Use it for | License | Skill | Self-host | Notes |
|---|---|---|---|---|---|
| Paperless-ngx | Scan, OCR, tag and archive documents (receipts, invoices, letters) | GPL-3.0 | N | S | Has built-in auto-matching for tags and correspondents. Community AI add-ons exist; verify maturity. |
| Tesseract | OCR engine | Apache-2.0 | C | S | Weak on poor photos and handwriting. |
| docTR | Deep-learning OCR | Apache-2.0 | C | M | Better on varied layouts than Tesseract. |
| Docling | Convert PDFs/Office files to structured text/tables for LLMs | MIT | C | S | |
| Unstructured | Parse many document types for LLM pipelines | Apache-2.0 | C | M | |

## Human review, forms and internal tools (where human gates live)
| Tool | Use it for | License | Skill | Self-host | Notes |
|---|---|---|---|---|---|
| n8n forms / wait nodes | Simple approve/reject steps by email, chat or form | see above | N | S | Enough for many gates. |
| Appsmith | Internal review queues and admin UIs | Apache-2.0 | L | M | |
| Budibase | Internal apps and approval forms | GPL-3.0 (core) | N/L | M | |
| ToolJet | Internal tools | AGPL-3.0 | L | M | |
| Baserow | Airtable-like database with forms | MIT (core) | N | S | Good shared "work queue" table. |
| Label Studio | Reviewing and correcting AI labels/extractions at volume | Apache-2.0 | L | M | Useful when tracking AI accuracy. |

## Reporting and monitoring
| Tool | Use it for | License | Skill | Self-host | Notes |
|---|---|---|---|---|---|
| Metabase | Dashboards for business users | AGPL-3.0 | N | S | |
| Apache Superset | Enterprise BI dashboards | Apache-2.0 | L | M | |
| Grafana | Operational/time-series dashboards and alerts | AGPL-3.0 | L | M | |
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
- Corporate users often can't self-host without IT approval. Say what approval they'll need and offer the least-infrastructure option.
- Prefer one orchestration tool and add others only for clear gaps.
- Local models (Ollama) keep data in-house but are less accurate than large hosted models. Say this trade-off plainly.
- Self-hosting means owning updates, backups, security patches and uptime. Include a maintenance estimate.
