# Reprocess

**Redesign your existing workflow to be AI-native, honestly.** Works in the AI assistant you already use (Microsoft 365 Copilot, ChatGPT, Claude, Gemini). Nothing to install.

Give it your SOP, or answer a few questions. Reprocess will:

1. Map your current process step by step, and check it with you.
2. Put each step in one category: **automate without AI** · **AI drafts, a human approves** · **AI acts within guardrails** · **keep it human** · **eliminate**.
3. Place **human gates** where accountability, risk or irreversibility require them, and say what evidence would justify loosening them.
4. Recommend **how to build it** with open-source tools: one recommended option plus 1–2 alternatives, including a low-AI option when that's the sensible answer.
5. List **limitations**: what it couldn't assess, how the AI steps can fail, and what extra information would sharpen the advice.
6. Produce a **downloadable HTML report** with current- and future-state diagrams.

It works for a one-person process (freelancer bookkeeping) up to a multi-site process (retail supply chain). Large processes are split into sub-processes and analyzed one at a time.

## What it won't do
- Promise AI can do everything. It recommends plain rules and integrations wherever they're enough.
- Invent savings. Estimates come only from your own time and volume figures, with the arithmetic shown.
- Replace your accountant, lawyer, compliance team or IT security review.

## Use it in 60 seconds
| Where | How |
|---|---|
| **Any AI chat** | Download [`dist/reprocess-full.md`](dist/reprocess-full.md), attach it, and type: *"Follow the instructions in the attached file. Start now."* |
| **Microsoft 365 Copilot agent** | See [adapters/m365-copilot.md](adapters/m365-copilot.md) |
| **ChatGPT Custom GPT** | Instructions: paste [`prompt/reprocess.md`](prompt/reprocess.md). Knowledge: upload the files in [`knowledge/`](knowledge/). Enable Code Interpreter. |
| **Claude Project** | Project instructions: paste `prompt/reprocess.md`. Project knowledge: upload `knowledge/`. |
| **Claude Skill** | Zip `dist/claude-skill/` and upload it under Settings → Capabilities → Skills. |
| **Gemini Gem** | Instructions: paste `prompt/reprocess.md`. Knowledge: upload `knowledge/`. |

**Privacy:** remove personal data, customer data and secrets before sharing an SOP, and follow your organization's AI policy.

## Example
[`examples/solo-bookkeeping/`](examples/solo-bookkeeping/) contains a freelance consultant's monthly bookkeeping SOP and the report Reprocess should produce from it. In that example, 6 of 10 future steps need no AI, and the no-server, no-AI option is a real contender.

## Repo layout
```
prompt/reprocess.md          core instructions (under 8,000 chars for Copilot / Custom GPT limits)
knowledge/                   question bank, open-source tool catalog, HTML report template
examples/                    sample SOPs and expected reports
adapters/                    platform setup guides
scripts/build.sh             builds dist/ and checks the character limit
dist/                        generated files: do not edit by hand
```

## Contributing
- Edit `prompt/` or `knowledge/`, then run `scripts/build.sh`.
- Tool catalog changes must include the license and a source link. Licenses change, so re-verify them before each release.
- New examples are welcome, especially corporate processes (accounts payable, sales reporting, onboarding, supply chain).

## License
[MIT](LICENSE). Use, copy, modify and share it freely; keep the copyright notice.
