# Security policy

Reprocess is a prompt pack: markdown instructions, knowledge files and an HTML report template. It runs inside whichever AI assistant you use, so most security questions are about **what it tells people to build** and **what the report file does when opened**.

## Please report
- Advice that would lead users to an unsafe design: e.g. letting AI move money, change bank details, or act on emails without a human gate; recommending internet-exposed self-hosting; missing a major legal or security trigger.
- Prompt-injection weaknesses: SOP or document content that can make the assistant ignore its rules, add links, or recommend a specific tool.
- Report-template issues: script injection, external requests beyond the pinned Mermaid library, or bypasses of the Content-Security-Policy.
- Tool-catalog errors: wrong licenses, typosquatted or abandoned projects, missing security warnings.

## How to report
Use GitHub's **private vulnerability reporting** (Security tab → *Report a vulnerability*) on this repository. For non-sensitive issues, a normal GitHub issue is fine. Please include the platform (Copilot, ChatGPT, Claude, Gemini), the input that caused it (with personal data removed) and the output.

## What's in scope for the report file
The template loads one script: Mermaid, pinned to an exact version from cdn.jsdelivr.net with a Subresource Integrity hash. A Content-Security-Policy blocks all other scripts, inline event handlers, external images, forms and frames. Diagram text is rendered in the browser and is not sent anywhere. Opening the file does contact jsDelivr, which sees your IP address and browser details.

## Never put in issues or pull requests
Credentials, internal URLs, customer data, or unredacted SOPs.
