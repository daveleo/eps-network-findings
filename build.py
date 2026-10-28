"""Builds the public GitHub Pages site from the page sources in src/.

The sources are the same HTML fragments that are published as claude.ai artifacts (title,
style and content, without <html>/<head>/<body>). This wraps each into a standalone page,
replaces the private artifact links with links between the public pages, and writes the
pages plus index.html next to this script.

Usage: python build.py
"""
import re
from pathlib import Path

HERE = Path(__file__).parent
PAGES = ["review.html", "supply-sag.html", "why-v3-3.html", "comparison.html", "why-v3-2.html", "executive-summary.html", "findings.html", "report.html"]
PAGES_DA = ["supply-sag-da.html", "hvorfor-v3-3.html", "comparison-da.html"]
LINKS = {
    "https://claude.ai/artifact/J9VgdUUEVsGfzwXQDGdx4w": "executive-summary.html",
    "https://claude.ai/artifact/5QSELy6vCJndKRkRy8Edn6": "findings.html",
    "https://claude.ai/artifact/Yc1rw3SGEY3BKTsdVw8w69": "report.html",
}
# The report mentions an older, internal summary page; it isn't part of this site.
DROP = [(r" \(summary page; published at https://claude\.ai/artifact/[A-Za-z0-9]+\)", " (an earlier, internal summary page)")]
NAV_OPEN = ('<nav style="max-width:1040px;margin:0 auto;padding:14px 20px 0;font:13px/1.4 \'IBM Plex Mono\',Consolas,monospace;'
            'display:flex;flex-wrap:wrap;gap:6px 18px">')
NAV = (NAV_OPEN + '<a href="index.html">All documents</a>'
       '<a href="review.html">Evidence review</a>'
       '<a href="supply-sag.html">Supply sag (bench study)</a>'
       '<a href="why-v3-3.html">Why v3.3</a><a href="comparison.html">All versions compared</a>'
       '<a href="executive-summary.html">Executive summary</a><a href="findings.html">Findings at a glance</a>'
       '<a href="report.html">Full report</a><a href="supply-sag-da.html" lang="da">På dansk</a></nav>')
NAV_DA = (NAV_OPEN + '<a href="review.html" lang="en">Evidence review (engelsk)</a>'
          '<a href="supply-sag-da.html">Spændingsdyk (bænkforsøg)</a>'
          '<a href="hvorfor-v3-3.html">Hvorfor v3.3 (kort)</a>'
          '<a href="comparison-da.html">Alle versioner sammenlignet</a>'
          '<a href="index.html">Alle dokumenter (engelsk)</a></nav>')


def wrap(fragment, lang="en", nav=NAV):
    for url, local in LINKS.items():
        fragment = fragment.replace(url, local)
    for pattern, repl in DROP:
        fragment = re.sub(pattern, repl, fragment)
    head_end = fragment.index("</style>") + len("</style>")
    head, body = fragment[:head_end], fragment[head_end:]
    return ('<!doctype html>\n<html lang="' + lang + '">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            + head + '\n<style>body{margin:0}nav a{color:var(--accent)}</style>\n</head>\n<body>\n'
            + nav + body + '\n</body>\n</html>\n')


def main():
    for name in PAGES + PAGES_DA:
        da = name in PAGES_DA
        out = wrap((HERE / "src" / name).read_text(encoding="utf-8"), "da" if da else "en", NAV_DA if da else NAV)
        assert "claude.ai/artifact" not in out, f"private link left in {name}"
        (HERE / name).write_text(out, encoding="utf-8")
        print("wrote", name, len(out), "bytes")
    (HERE / "index.html").write_text(wrap((HERE / "src" / "index.html").read_text(encoding="utf-8")), encoding="utf-8")
    print("wrote index.html")


if __name__ == "__main__":
    main()
