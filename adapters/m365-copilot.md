# Set up Reprocess as a Microsoft 365 Copilot agent

About 5 minutes, with no install and no admin rights, **if your organization allows users to create agents**. If you don't see "Create agent", ask your M365 admin, or use the fallback at the bottom.

Menu names change between Copilot releases. If a label below doesn't match, look for the closest equivalent.

## Steps
1. Open Microsoft 365 Copilot (the Copilot app, m365copilot.com, or Copilot in Teams).
2. Choose **Create agent** (sometimes under *Agents* or *Explore agents*), then the **Configure** tab.
3. Fill in:
   - **Name:** `Reprocess: AI-native workflow redesign`
   - **Description:** `Redesigns an existing workflow or SOP: what to automate, where AI helps, where humans stay in control, and how to build it with open-source tools.`
   - **Instructions:** paste the full contents of [`prompt/reprocess.md`](../prompt/reprocess.md). It is kept under the 8,000-character limit.
4. **Knowledge:** upload these files:
   - [`knowledge/tool-catalog.md`](../knowledge/tool-catalog.md)
   - [`knowledge/question-bank.md`](../knowledge/question-bank.md)
   - [`knowledge/report-template.html`](../knowledge/report-template.html). If .html uploads are blocked, rename it to `report-template.txt`.
5. **Capabilities:** turn on **Code interpreter**, so the agent can try to create the report file for download.
6. **Starter prompts** (optional):
   - `Here's my SOP, redesign it` (then attach the SOP)
   - `I don't have an SOP, interview me`
   - `Analyze one sub-process of a large workflow`
7. **Create**, then share it with colleagues if your tenant allows.

## Data and policy
- Copilot inside your company tenant is usually covered by your organization's data protection terms. Still follow your company's AI-use policy and remove sensitive data you don't need.
- The agent can't see your systems. It only knows what you tell it or upload.

## Known Copilot limitations (to test and report)
- Long answers may be cut off. The prompt tells the agent to split the HTML report into parts. If it stops mid-way, reply `continue`.
- Whether Code interpreter produces a downloadable `.html` file can vary. If it doesn't, copy the HTML code block into Notepad and save it as `reprocess-report.html`.
- Diagrams load from jsDelivr. Some corporate networks block it; the report then shows diagram code, which you can paste into mermaid.live.

## Fallback: no agent builder
Open Copilot chat, attach `dist/reprocess-full.md`, and type:
`Follow the instructions in the attached file. Start now.`
