"""Hostile-input tests for scripts/check-report.py.

Each case mutates the known-good example report and asserts the checker's verdict.
Run: python3 -I -m unittest discover -s tests
"""
import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("check_report", ROOT / "scripts" / "check-report.py")
check_report = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check_report)

GOOD = (ROOT / "examples" / "solo-bookkeeping" / "report.html").read_text(encoding="utf-8")
CSP = check_report.template_parts()[0]
SCRIPT = check_report.template_parts()[1]
BODY_END = "</body>"
FIRST_P = "<h2>1. Executive summary</h2>"
FIRST_DIAGRAM_LINE = "flowchart LR\n"


def run(html):
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html)
    try:
        return check_report.check(f.name)
    finally:
        Path(f.name).unlink()


def inject_body(html):
    return GOOD.replace(FIRST_P, html + FIRST_P, 1)


def inject_diagram(line):
    return GOOD.replace(FIRST_DIAGRAM_LINE, FIRST_DIAGRAM_LINE + line + "\n", 1)


class Passes(unittest.TestCase):
    def test_example_is_clean(self):
        self.assertEqual(run(GOOD), [])

    def test_part_markers_allowed(self):
        self.assertEqual(run(GOOD.replace(BODY_END, "<!-- END PART 2 OF 2 -->\n" + BODY_END)), [])

    def test_escaped_markup_in_text_allowed(self):
        self.assertEqual(run(inject_body("<p>Step: &lt;script&gt;alert(1)&lt;/script&gt;</p>")), [])


class Fails(unittest.TestCase):
    cases = {
        "uppercase script": inject_body("<SCRIPT>alert(1)</SCRIPT>"),
        "script split by comment": inject_body("<scr<!-- x -->ipt>alert(1)</script>"),
        "meta refresh": inject_body('<meta http-equiv="refresh" content="0;url=https://example.invalid">'),
        "meta refresh uppercase": inject_body('<META HTTP-EQUIV="Refresh" CONTENT="0;url=x">'),
        "base tag": inject_body('<base href="https://example.invalid/">'),
        "link tag": inject_body('<link rel="stylesheet" href="https://example.invalid/x.css">'),
        "anchor": inject_body('<a href="https://example.invalid">click</a>'),
        "svg": inject_body("<svg><circle r=5></circle></svg>"),
        "img onerror": inject_body("<img src=x onerror=alert(1)>"),
        "event handler on allowed tag": inject_body('<p onclick="alert(1)">x</p>'),
        "style attribute": inject_body('<p style="background:url(x)">x</p>'),
        "iframe": inject_body('<iframe src="https://example.invalid"></iframe>'),
        "form": inject_body('<form action="https://example.invalid"><button>x</button></form>'),
        "javascript url text": inject_body("<p>javascript:alert(1)</p>"),
        "duplicate CSP": inject_body(CSP),
        "CSP only inside comment": GOOD.replace(CSP, "<!-- " + CSP + " -->", 1),
        "CSP weakened": GOOD.replace("default-src 'none'", "default-src *", 1),
        "script only inside comment": GOOD.replace(SCRIPT, "<!-- " + SCRIPT + " -->", 1),
        "second external script": GOOD.replace(BODY_END, '<script src="https://example.invalid/x.js"></script>' + BODY_END),
        "mermaid version changed": GOOD.replace("mermaid@11.17.2/dist", "mermaid@11/dist", 1),
        "style block changed": GOOD.replace("max-width:980px", "max-width:9999px", 1),
        "footer removed": GOOD.replace("Not legal, tax, financial or security advice, and not a compliance determination.</b> This", "</b> This", 1),
        "template comment left": inject_body("<!-- Columns: # | Step -->"),
        "unclosed comment": GOOD.replace(BODY_END, "<!-- hidden " + BODY_END),
        "placeholder left": inject_body("<p>{{SUMMARY_BULLETS}}</p>"),
        "diagram click": inject_diagram('  click c1 href "https://example.invalid"'),
        "diagram init directive": inject_diagram('  %%{init: {"securityLevel": "loose"}}%%'),
        "diagram style line": inject_diagram("  style c1 fill:#f00"),
        "diagram entity in label": inject_diagram('  x1["Approve &quot;PO&quot; &gt; 5k"]'),
        "diagram url in label": inject_diagram('  x1["see https colon example"] --> x2["www.example.invalid"]'),
        "diagram hash in label": inject_diagram('  x1["Step #1; then"]'),
        "oversized": GOOD.replace(BODY_END, "<p>" + "x" * 50_000 + "</p>" + BODY_END),
    }

    def test_hostile_inputs_fail(self):
        for name, html in self.cases.items():
            with self.subTest(name):
                self.assertNotEqual(run(html), [], f"checker passed hostile case: {name}")


if __name__ == "__main__":
    unittest.main()
