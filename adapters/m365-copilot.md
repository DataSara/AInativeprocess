# Set up Reprocess as a Microsoft 365 Copilot agent

About 5 minutes, with no install and no admin rights, **if your organization allows users to create agents**. Many regulated tenants disable agent creation: if you don't see "Create agent", **use the fallback at the bottom**, which works in plain Copilot chat.

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
   - [`knowledge/risk-checklist.md`](../knowledge/risk-checklist.md)
   - [`knowledge/tool-assessment-kit.md`](../knowledge/tool-assessment-kit.md)
5. **Capabilities:** turn on **Code interpreter**, so the agent can try to create the report file for download.
6. **Starter prompts** (optional):
   - `Here's my SOP, redesign it. Use your question bank, risk checklist, tool catalog and report template.` (then attach the SOP)
   - `I don't have an SOP, interview me. Use your question bank and risk checklist.`
   - `Analyze one sub-process of a large workflow`
   Agent knowledge retrieval can vary between runs; naming the files in the prompt makes it more reliable.
7. **Create**, then share it with colleagues if your tenant allows.

## Data and policy
- Copilot inside your company tenant is usually covered by your organization's data protection terms. Still follow your company's AI-use policy and remove sensitive data you don't need.
- The agent can't see your systems. It only knows what you tell it or upload.
- Turn off web search for this agent unless your policy allows it; web grounding can send query content outside your tenant under different terms (verify current Microsoft docs).
- Don't add SOPs with personal or confidential data to the agent's knowledge. Everyone you share the agent with can draw on it.

## Known Copilot limitations (to test and report)
- Long answers may be cut off. Reports aim for under 30 KB, but longer ones are split into parts that end with `<!-- END PART n OF N -->`. Paste them into one file in order; the last part ends with `</html>`. If it stops mid-way, reply `continue`.
- Whether Code interpreter produces a downloadable `.html` file can vary. If it doesn't, copy the HTML code block into Notepad and save it as `reprocess-report.html`.
- Diagrams load from jsDelivr. Some corporate networks block it; the report then shows diagram code, and the step tables in sections 3 and 5 list the same steps. Don't paste diagram code into external websites unless your policy allows it; a desktop diagram tool your organization approves is safer.
- If you need Word or PDF: open the HTML in a browser and use Print → Save as PDF, or open the HTML file in Word.

## Fallback: no agent builder
Open Copilot chat, attach `dist/reprocess-full.md`, and type:
`Follow the instructions in the attached file. Start now.`
