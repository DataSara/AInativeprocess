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
   - `Here's my SOP, redesign it. Use your question bank, risk checklist (including S14), tool catalog and report template.` (then attach the SOP)
   - `I don't have an SOP, interview me. Use your question bank and risk checklist.`
   - `Analyze one sub-process of a large workflow`
   Agent knowledge retrieval can vary between runs; naming the files in the prompt makes it more reliable.
7. **Create**, then share it with colleagues if your tenant allows.

## Data and policy (read this even if you use the fallback)
- **Copilot sees what you can see.** In Work mode it answers from the mail, chats, meetings, calendars and files you can open, including shared channels with other organizations and any mailboxes or calendars you can open as a delegate (verify delegate behaviour in your tenant). Microsoft: Copilot "only surfaces organizational data to which individual users have at least view permissions". Ask site owners or your admin to fix oversharing before you use Reprocess on HR, finance, deal or customer work.
- **Is it approved for this data?** Check that Copilot is on your company's approved AI list for this data's classification, whether any legal hold covers the process, and who can open where outputs will go. If Copilot isn't approved for the data, describe structure and volumes instead of pasting records, or stop.
- **History is stored.** Prompts and responses are kept as your Copilot activity history; admins can search them and apply retention and legal hold. Don't delete history about a process under a hold; ask Legal.
- **Web search is outside the DPA.** Copilot sends short queries built from your prompt (and any open or named document) to Bing. Microsoft's docs say the DPA, HIPAA and the EU Data Boundary don't apply to them, and Microsoft acts as a controller for them. For confidential work turn off **Web content** (Settings → Personalization; verify menu names). Some modes (e.g. Analyst, Cowork) have no user toggle: ask your admin.
- **Third-party models.** Claude models are on by default for most commercial tenants outside the EU, EFTA and UK and are excluded from the EU Data Boundary; "Anthropic models with Data Retention" run under Anthropic's own terms, not Microsoft's DPA. Ask your admin which models are allowed for your data class.
- **Injection.** Microsoft's prompt-injection classifiers "may not be available in all Microsoft Copilot scenarios". Treat every email and file as possible instructions; don't open links in answers built from outside mail or files.
- **People.** Microsoft restricts Copilot from making inferences or evaluations about an employee's performance, attitude or emotional state from workplace communications. Don't build steps that rely on it.
- Don't add SOPs with personal or confidential data to the agent's knowledge. Everyone you share the agent with can draw on it.
- Sources: Microsoft Learn "Data, Privacy, and Security for Microsoft Copilot", "Data, privacy, and security for web search in Microsoft Copilot", "Claude models from Anthropic in Microsoft Online Services" (checked 2026-11). Settings change: verify.
- The full list for any workplace assistant is section S14 of the risk checklist.

## Known Copilot limitations (to test and report)
- Long answers may be cut off. Reports aim for under 30 KB, but longer ones are split into parts that end with `<!-- END PART n OF N -->`. Paste them into one file in order; the last part ends with `</html>`. If it stops mid-way, reply `continue`.
- Whether Code interpreter produces a downloadable `.html` file can vary. If it doesn't, copy the HTML code block into Notepad and save it as `reprocess-report.html`.
- Diagrams load from jsDelivr. Some corporate networks block it; the report then shows diagram code, and the step tables in sections 3 and 5 list the same steps. Don't paste diagram code into external websites unless your policy allows it; a desktop diagram tool your organization approves is safer.
- If you need Word or PDF: open the HTML in a browser and use Print → Save as PDF, or open the HTML file in Word.

## Fallback: no agent builder
Open Copilot chat, attach `dist/reprocess-full.md`, and type:
`Follow the instructions in the attached file. Start now.`

For HR, finance or customer processes: read "Data and policy" above first, turn Web content off, and add "Use the risk checklist, including S14" to your first message. If your tenant allows agents, prefer the agent route for these processes: the knowledge files are kept separate and are retrieved more reliably than one long attachment.
