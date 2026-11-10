# Reprocess tool assessment kit

Reprocess never names commercial products. When a ready-made tool fits better than building, it names the **type** of tool (e.g. "booking app with deposits and reminders", "field-service app with quoting and invoicing", "practice-management system that signs a BAA", "validated eQMS", "AP invoice-capture service") and gives the user this kit to compare real products themselves. Tailor it: include the sections that matter for this process, add process-specific must-haves, and drop the rest.

The same kit works for open-source tools and for new features or add-ons of tools the user already has.

## 1. Must-haves for this process (fill in from the analysis)
List the 3–8 capabilities the redesigned process needs from the tool, e.g. "sends a reminder 24 h before the appointment", "three-way match against purchase orders", "approval with a login, not a link". A tool that misses a must-have is out, however good the rest is.
- For tools that staff, candidates or customers use, add: accessible to disabled users (WCAG 2.2 AA as the usual benchmark, verify).

## 1b. How to find 2–3 candidates (Reprocess won't name them)
- Search for the tool type plus your sector and size, e.g. "booking app for small salons with deposits".
- Ask your trade association, professional body, accountant or peers what they use, and what they'd avoid.
- Check the app marketplace or integrations page of the tools you already use: listed apps already connect to them.
- Read independent reviews from businesses of your size; ignore "best of" lists that are adverts.
- Shortlist only tools that clearly cover your must-haves on their public pricing or feature pages.
- Inside a company: start with IT's software catalogue and procurement; the security, privacy and AI review route decides; peers in other teams may already use an approved tool.

## 2. Score card (use for 2–3 shortlisted tools)
| Criterion | Weight (1–3) | Tool 1 | Tool 2 | Tool 3 |
|---|---|---|---|---|
| Covers every must-have | gate: yes/no | | | |
| Signs the agreement you need (DPA; BAA for US health data; client consent where required) | gate: yes/no | | | |
| Works with the tools you already use (import/export, integrations) | | | | |
| Total monthly cost at your volume, incl. add-ons, per-user fees, card or SMS fees | | | | |
| Setup effort (hours) and who will do it | | | | |
| Ease of use for the people who'll use it daily | | | | |
| Data and privacy terms (section 3) | | | | |
| Security (section 4) | | | | |
| Compliance features you need (section 5) | | | | |
| AI features: what they do, can they be turned off, does your data train them | | | | |
| Getting your data out (section 6) | | | | |
| Vendor or project health (section 7) | | | | |
Score each 1–5, multiply by the weight, and add up. Treat it as a structured way to compare, not a verdict.

## 3. Data and privacy questions to ask the vendor
- Where is my data stored (country/region)? Who at the vendor can see it?
- Will you sign a data processing agreement (DPA)? For US health data: a Business Associate Agreement (BAA)?
- Is my data, or my customers' data, used to train AI models? Can I opt out in writing?
- How long is data kept after I cancel? Can I delete it myself?
- Which subcontractors (sub-processors) handle my data?
- Is there a business plan with different terms from the consumer plan?
- Does the vendor use my data for its own purposes (analytics, product improvement, advertising)?
- Which AI providers (sub-processors) process my data, where, and how long do they keep it?
- How quickly will you notify me of a data breach, and how?
- Is data encrypted in transit and at rest? Can you share an independent security report or certification?

## 4. Security questions
- Login: is multi-factor authentication available, and can I require it for all users? Single sign-on (for organizations)?
- Roles: can I limit what each person sees and does?
- Audit log: does it record who changed what, and can admins edit or delete the log?
- Approvals: does an approval need a login, or can anyone with a link approve?
- Integrations: what access does each connection ask for (read-only vs full)? Can I revoke it?
- Can the vendor's AI features act on my emails, documents or accounts by themselves? Can I limit them to drafts that a person approves?
- Has the vendor published security information (independent audit report, security page, vulnerability disclosure)?
- What happens when a staff member leaves: can I remove their access in one place?

## 5. Compliance features (only those that apply; see the risk checklist)
- Finance and audit: approval workflows with thresholds, segregation of duties, unchangeable records, export of evidence for auditors. For SOX-relevant systems ask for the vendor's SOC 1 Type II report (and SOC 2 for security), the complementary user-entity controls you must run, how configuration changes are logged, and whether you can restrict who changes workflows and approval rules.
- Health: BAA, minimum-necessary access, audit trail.
- Regulated quality records (e.g. medical devices, pharma): electronic signatures and audit trails that meet your rules; the vendor's validation support package.
- Marketing messages: consent capture, opt-out handling, quiet hours.
- Card payments: card data handled by the payment provider, never stored by you.
- Records: retention settings that match your legal retention periods.

## 6. Getting out (lock-in)
- Can I export all my data (including history and attachments) in a standard format (CSV, PDF, JSON)? Try it during the trial.
- Is there a contract minimum or notice period? Are prices fixed for a period?
- If the vendor shuts down or is bought, what happens to my data?

## 7. Vendor or project health
- How long has it existed? Is it actively updated (recent releases, security fixes)?
- Open source: licence type (permissive, copyleft or source-available), number of active maintainers, last release date.
- Support: hours, channels, response times on your plan.
- Reviews from businesses of your size and sector, from sources you trust (not the vendor's own site).

## 8. Trial plan (before you commit)
1. Run 5–10 realistic but **made-up** cases through the free trial, including one awkward exception. Don't put real customer, patient or staff data into a trial until the agreement in section 3 is signed.
2. Have the person who will use it daily do the trial, not just the buyer.
3. Test the export (section 6) and the remove-a-user process (section 4).
4. Check the real monthly bill at your volume against your budget.
5. Write down what the tool will **not** do, and who does that step instead.

## 9. Red flags
- Claims of "fully autonomous", "100% accurate" or "no human needed" for anything involving money, people, safety or customers.
- No way to export your data, or no written answer on AI training use.
- Approvals that work by link alone for money or regulated decisions.
- Pressure to sign before the trial ends, or prices only "on request" for a small business.
- Asks for passwords to other systems instead of a proper integration.
- No written answer on where data is stored or who processes it.
- No way to turn off AI features, or AI that sends or acts without approval by default.
- Won't sign a DPA (or a BAA for health data) on the plan you can afford.

*This kit helps you structure your own assessment. It is not an endorsement or a legal review; check contracts with a qualified adviser where the stakes are high.*
