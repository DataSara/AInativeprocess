# Reprocess

**Redesign your existing workflow to be AI-native, honestly.** Works in the AI assistant you already use (Microsoft 365 Copilot, ChatGPT, Claude, Gemini). Nothing to install.

Give it your SOP, or answer a few questions. Reprocess will:

1. Map your current process step by step, and check it with you.
2. Put each step in one category: **automate without AI** · **AI drafts, a human approves** · **AI acts within guardrails** · **keep it human** · **eliminate**.
3. Place **human gates** where accountability, risk or irreversibility require them (money, master data, prices, decisions about people, regulated sign-offs), and say what evidence would justify loosening them.
4. **Flag risk, compliance and security issues to check**: e.g. GDPR automated decisions, EU AI Act high-risk uses, SOX segregation of duties, HIPAA, PCI, pricing law, prompt injection, payment fraud, self-hosting exposure. It flags them for your experts to check; it never declares a design compliant.
5. Recommend **how to build it** with open-source tools: one recommended option plus 1–2 alternatives, including a low-AI option when that's the sensible answer.
6. List **limitations**: what it couldn't assess, how the AI steps can fail, and what extra information would sharpen the advice.
7. Produce a **downloadable HTML report** with current- and future-state diagrams.

It works for a one-person process (freelancer bookkeeping) up to a multi-site process (retail supply chain). Large processes are split into sub-processes and analyzed one at a time.

## What it won't do
- Promise AI can do everything. It recommends plain rules and integrations wherever they're enough.
- Invent savings. Estimates come only from your own time and volume figures, with the arithmetic shown.
- Replace your accountant, lawyer, compliance team or IT security review. It points out what they should look at.
- Let AI move money, change bank details, set customer prices or make decisions about people without a human approver.

## Use it in 60 seconds
| Where | How |
|---|---|
| **Any AI chat** | Download [`dist/reprocess-full.md`](dist/reprocess-full.md), attach it, and type: *"Follow the instructions in the attached file. Start now."* |
| **Microsoft 365 Copilot agent** | See [adapters/m365-copilot.md](adapters/m365-copilot.md) |
| **ChatGPT Custom GPT** | Instructions: paste [`prompt/reprocess.md`](prompt/reprocess.md). Knowledge: upload all four files in [`knowledge/`](knowledge/). Enable Code Interpreter. |
| **Claude Project** | Project instructions: paste `prompt/reprocess.md`. Project knowledge: upload `knowledge/`. |
| **Claude Skill** | Zip `dist/claude-skill/` and upload it under Settings → Capabilities → Skills. |
| **Gemini Gem** | Instructions: paste `prompt/reprocess.md`. Knowledge: upload `knowledge/`. |

**Privacy:** remove personal data, customer data and secrets before sharing an SOP, and follow your organization's AI policy. Use a business AI plan for confidential processes, and never paste health records, card numbers or passwords.

## Example
[`examples/solo-bookkeeping/`](examples/solo-bookkeeping/) contains a freelance consultant's monthly bookkeeping SOP and the report Reprocess should produce from it. In that example, 6 of 10 future steps need no AI, and the no-server, no-AI option is a real contender.

## Repo layout
```
prompt/reprocess.md          core instructions (under 8,000 chars for Copilot / Custom GPT limits)
knowledge/                   question bank, open-source tool catalog, risk and security checklist, HTML report template
examples/                    sample SOPs and expected reports
adapters/                    platform setup guides
scripts/build.sh             builds dist/ and checks the character limit
dist/                        generated files: do not edit by hand
```

## Contributing
- Edit `prompt/` or `knowledge/`, then run `scripts/build.sh`.
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
