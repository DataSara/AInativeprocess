# Reprocess

**Redesign your existing workflow to be AI-native, honestly.** Works in the AI assistant you already use (Microsoft 365 Copilot, ChatGPT, Claude, Gemini). Nothing to install.

Give it your SOP, or answer a few questions. Reprocess will:

1. Map your current process step by step, and check it with you.
2. Put each step in one category: **automate without AI** · **AI drafts, a human approves** · **AI acts within guardrails** · **keep it human** · **eliminate**.
   Forecasts, estimates and scores get their own mode, **model** (statistical or machine learning, not an LLM), with a baseline to beat and accuracy and bias monitoring.
   Then it **rethinks the flow**, not just the steps: model-first estimates that people can challenge, exception-based review, one versioned source of truth, fewer hand-offs, and a learning loop that checks predictions against outcomes.
3. Place **human gates** where accountability, risk or irreversibility require them (money, master data, prices, decisions about people, regulated sign-offs), and say what evidence would justify loosening them.
4. **Flag risk, compliance and security issues to check**: e.g. GDPR automated decisions, EU AI Act high-risk uses, hiring and background-check rules, inside information, SOX segregation of duties, HIPAA, PCI, pricing law, prompt injection, payment fraud, what a workplace assistant can see and store, self-hosting exposure. It flags them for your experts to check; it never declares a design compliant.
5. Recommend **how to get it done**, matched to your technical comfort: one recommended option plus 1–2 alternatives, always including a low- or no-AI option.
   - *Just want to use apps:* what you already have, then types of ready-made tools, with step-by-step safe-use instructions. Reprocess **never names commercial products**: it gives you a **tool assessment kit** (must-haves, score card, privacy, security and lock-in questions, trial plan, red flags) so you can judge vendors yourself.
   - *Want to build:* a responsibility disclaimer first, then open-source tools with licenses, access design, and the security, compliance and legal steps to go with them.
6. List **limitations**: what it couldn't assess, how the AI steps can fail, and what extra information would sharpen the advice.
7. Produce a **downloadable HTML report** with current- and future-state diagrams.

It works for a one-person process (freelancer bookkeeping) up to a multi-site process (retail supply chain). Large processes are split into sub-processes and analyzed one at a time.

## What it won't do
- Promise AI can do everything. It recommends plain rules and integrations wherever they're enough.
- Invent savings. Baselines come from your own time and volume figures. Any future time or reduction it proposes is marked [ASSUMPTION] for you to adjust, with the arithmetic shown, and expressed as capacity, not headcount.
- Replace your accountant, lawyer, compliance team or IT security review. It points out what they should look at.
- Let AI move money, change bank details, set customer prices or make decisions about people without a human approver.

## Use it in 60 seconds
| Where | How |
|---|---|
| **Any AI chat** | Download [`dist/reprocess-full.md`](dist/reprocess-full.md), attach it, and type: *"Follow the instructions in the attached file. Start now."* |
| **Microsoft 365 Copilot agent** | See [adapters/m365-copilot.md](adapters/m365-copilot.md) |
| **ChatGPT Custom GPT** | Instructions: paste [`prompt/reprocess.md`](prompt/reprocess.md). Knowledge: upload all six files in [`knowledge/`](knowledge/). Enable Code Interpreter. |
| **Claude Project** | Project instructions: paste `prompt/reprocess.md`. Project knowledge: upload `knowledge/`. |
| **Claude Skill** | Zip `dist/claude-skill/` and upload it under Settings → Capabilities → Skills. |
| **Gemini Gem** | Instructions: paste `prompt/reprocess.md`. Knowledge: upload `knowledge/`. |

**Privacy:** remove personal data, customer data and secrets you don't need, and follow your organization's AI policy. If the process itself runs on confidential data (HR, finance, customer work), first check that your assistant is approved for that data's classification, and describe structure and volumes instead of pasting real records. Workplace assistants can also see files and mail you have access to: see the data notes in [adapters/m365-copilot.md](adapters/m365-copilot.md). Use a business AI plan for confidential processes, and never paste health records, card numbers or passwords.

## Example
[`examples/solo-bookkeeping/`](examples/solo-bookkeeping/) contains a freelance consultant's monthly bookkeeping SOP and the report Reprocess should produce from it. In that example, 6 of 10 future steps need no AI, and the no-server, no-AI option is a real contender.

## Repo layout
```
prompt/reprocess.md          core instructions (under 8,000 chars for Copilot / Custom GPT limits)
knowledge/                   question bank, redesign patterns, open-source tool catalog, risk and security checklist, tool assessment kit, HTML report template
examples/                    sample SOPs and expected reports
adapters/                    platform setup guides
scripts/build.sh             builds dist/ and checks the character limit
scripts/check-report.py      checks a generated report against the template's safety rules
dist/                        generated files: do not edit by hand
```

## Contributing
- Edit `prompt/` or `knowledge/`, then run `scripts/build.sh`.
- Never add commercial product names to the prompt, knowledge files or examples (except as tools a user in an example already has). Describe tool types instead.
- Tool catalog changes must include the license and a link to the project's canonical repository. Licenses, ownership and security posture change, so re-verify them (and check recent security advisories) before each release.
- Risk checklist changes must cite the law or standard by name and article. Mark anything in flux as *(verify)*.
- `dist/` is generated. Pull requests that change `dist/` without the matching source change will be rejected; CI rebuilds and compares it.
- Never put credentials, internal URLs or confidential examples in prompt, knowledge or example files.
- `prompt/reprocess.md` must stay under 8,000 characters. Put bulky guidance in `knowledge/`.
- New examples are welcome, especially corporate processes (accounts payable, sales reporting, onboarding, supply chain).

## Disclaimer
Reprocess produces AI-generated drafts for discussion. They are **not legal, tax, financial or security advice**, and they make no compliance determination. Outputs can be wrong or incomplete. Review them with the people who run the process and with qualified professionals before acting; you are responsible for decisions made using them. Tools named are examples, not endorsements. Product names are trademarks of their owners; this project is not affiliated with or endorsed by them.

## Security
To report a prompt behaviour that produces harmful or unsafe advice, or a vulnerability in the report template, see [SECURITY.md](SECURITY.md).

## License
[MIT](LICENSE). Use, copy, modify and share it freely; keep the copyright notice.
