#!/usr/bin/env python3
"""Check a Reprocess HTML report against the template's safety rules.

Usage: python3 -I scripts/check-report.py report.html [more.html ...]
Exits 1 if any report breaks a rule. Uses only the standard library.
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parent.parent / "knowledge" / "report-template.html"
ALLOWED = {"html", "head", "meta", "title", "style", "body", "h1", "h2", "h3", "p", "ul", "ol", "li",
           "table", "tr", "th", "td", "thead", "tbody", "b", "i", "span", "div", "br", "pre", "script"}
ALLOWED_ATTRS = {"class", "lang", "charset", "name", "content", "http-equiv", "src", "colspan", "rowspan"}
BAD_DIAGRAM_LINE = re.compile(r"^\s*(%%|(click|style|linkStyle)\b)", re.I)
BAD_LABEL_CHARS = re.compile(r"[<>&'`;%|]")


def template_parts():
    t = TEMPLATE.read_text(encoding="utf-8")
    csp = re.search(r'<meta http-equiv="Content-Security-Policy"[^>]*>', t).group(0)
    script = re.search(r'<script src="[^"]+"></script>', t).group(0)
    return csp, script


class Checker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.problems, self.metas, self.scripts, self.styles = [], 0, 0, 0

    def handle_starttag(self, tag, attrs):
        if tag not in ALLOWED:
            self.problems.append(f"disallowed tag <{tag}>")
        for name, _ in attrs:
            if name not in ALLOWED_ATTRS:
                self.problems.append(f"disallowed attribute {name!r} on <{tag}>")
        if tag == "meta":
            self.metas += 1
            a = dict(attrs)
            equiv = (a.get("http-equiv") or "").lower()
            if equiv and equiv != "content-security-policy":
                self.problems.append(f"disallowed <meta http-equiv={equiv!r}> (e.g. refresh redirects)")
            if a.get("name") not in (None, "viewport"):
                self.problems.append(f"unexpected <meta name={a.get('name')!r}>")
        if tag == "script":
            self.scripts += 1
        if tag == "style":
            self.styles += 1


def check(path):
    text = Path(path).read_text(encoding="utf-8")
    csp, script = template_parts()
    c = Checker()
    c.feed(text)
    problems = list(c.problems)
    if csp not in text:
        problems.append("Content-Security-Policy meta tag missing or changed")
    if text.count("<script") != 1 or script not in text:
        problems.append("pinned Mermaid script missing or changed, or extra scripts present")
    if c.metas > 3:
        problems.append(f"{c.metas} meta tags (template has 3)")
    if c.styles != 1:
        problems.append(f"{c.styles} style blocks (template has 1)")
    if "{{" in text:
        problems.append("unfilled {{PLACEHOLDER}}")
    if "Not legal, tax, financial or security advice" not in text:
        problems.append("disclaimer missing")
    for block in re.findall(r'<pre class="mermaid">(.*?)</pre>', text, re.S):
        for line in block.splitlines():
            if BAD_DIAGRAM_LINE.match(line):
                problems.append(f"forbidden diagram line: {line.strip()[:60]}")
            for label in re.findall(r'"([^"]*)"', line):
                if BAD_LABEL_CHARS.search(label):
                    problems.append(f"special character in diagram label: {label[:60]}")
    size = len(text.encode("utf-8"))
    if size > 60_000:
        problems.append(f"report is {size // 1000} KB (aim under 30 KB)")
    elif size > 30_000:
        print(f"  note: {path} is {size // 1000} KB (aim under 30 KB)")
    return problems


def main(paths):
    failed = False
    for p in paths:
        problems = check(p)
        status = "OK" if not problems else "FAIL"
        print(f"{status} {p}")
        for msg in problems:
            print(f"  - {msg}")
        failed |= bool(problems)
    return 1 if failed else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1:]))
