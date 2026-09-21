"""Assemble the participant-facing Markdown into one self-contained HTML file.

The output at dist/participant-handbook.html has no external dependencies: it is
a single file that opens offline on any device, and prints cleanly to A4 through
a browser's print-to-PDF. Run it after editing anything in participant/.

    python scripts/build_participant_handbook.py

The Markdown subset supported here is exactly what the participant documents use:
headings, paragraphs, tables, ordered/unordered/task lists, fenced code,
blockquotes, horizontal rules, and inline bold/italic/code/links.
"""

from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "participant"
OUTPUT = ROOT / "dist" / "participant-handbook.html"

# Order matters: this is the order the printed handbook is bound in.
SECTIONS = [
    "HANDBOOK.md",
    "CAPSTONE.md",
    "CHEATSHEET_METHODS.md",
    "CHEATSHEET_PYTHON.md",
    "GLOSSARY_EN_AR.md",
]

INLINE_CODE = re.compile(r"`([^`]+)`")
BOLD = re.compile(r"\*\*([^*]+)\*\*")
ITALIC = re.compile(r"(?<!\*)\*([^*\n]+)\*(?!\*)")
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def inline(text: str) -> str:
    """Escape a line, then apply inline Markdown. Code spans are protected."""
    spans: list[str] = []

    def stash(match: re.Match[str]) -> str:
        spans.append(html.escape(match.group(1), quote=False))
        return f"\x00{len(spans) - 1}\x00"

    text = INLINE_CODE.sub(stash, text)
    text = html.escape(text, quote=False)
    text = LINK.sub(r'<a href="\2">\1</a>', text)
    text = BOLD.sub(r"<strong>\1</strong>", text)
    text = ITALIC.sub(r"<em>\1</em>", text)
    for index, code in enumerate(spans):
        text = text.replace(f"\x00{index}\x00", f"<code>{code}</code>")
    return text


def split_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_divider(line: str) -> bool:
    return bool(re.fullmatch(r"\|[\s:|-]+\|", line.strip()))


def render(markdown: str, slug: str) -> tuple[str, list[tuple[int, str, str]]]:
    """Return rendered HTML plus (level, anchor, title) entries for the contents."""
    out: list[str] = []
    toc: list[tuple[int, str, str]] = []
    lines = markdown.splitlines()
    index = 0
    seen: dict[str, int] = {}

    def anchor(title: str) -> str:
        base = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-") or "section"
        base = f"{slug}-{base}"
        seen[base] = seen.get(base, 0) + 1
        return base if seen[base] == 1 else f"{base}-{seen[base]}"

    while index < len(lines):
        line = lines[index]
        stripped = line.strip()

        if not stripped:
            index += 1
            continue

        if stripped.startswith("```"):
            index += 1
            body: list[str] = []
            while index < len(lines) and not lines[index].strip().startswith("```"):
                body.append(html.escape(lines[index], quote=False))
                index += 1
            index += 1
            out.append("<pre><code>" + "\n".join(body) + "</code></pre>")
            continue

        if re.fullmatch(r"-{3,}", stripped):
            out.append('<hr class="section-break">')
            index += 1
            continue

        heading = re.match(r"(#{1,4})\s+(.*)", stripped)
        if heading:
            level = len(heading.group(1))
            title = heading.group(2).strip()
            ident = anchor(title)
            if level <= 2:
                toc.append((level, ident, title))
            out.append(f'<h{level} id="{ident}">{inline(title)}</h{level}>')
            index += 1
            continue

        if stripped.startswith("|"):
            header = split_row(stripped)
            if index + 1 < len(lines) and is_divider(lines[index + 1]):
                index += 2
                rows: list[list[str]] = []
                while index < len(lines) and lines[index].strip().startswith("|"):
                    rows.append(split_row(lines[index]))
                    index += 1
                head = "".join(f"<th>{inline(c)}</th>" for c in header)
                body_html = ""
                for row in rows:
                    row = (row + [""] * len(header))[: len(header)]
                    body_html += "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>"
                out.append(f"<table><thead><tr>{head}</tr></thead><tbody>{body_html}</tbody></table>")
                continue

        if stripped.startswith("> "):
            quote: list[str] = []
            while index < len(lines) and lines[index].strip().startswith(">"):
                quote.append(lines[index].strip().lstrip(">").strip())
                index += 1
            paragraphs = "\n".join(quote).split("\n\n")
            inner = "".join(f"<p>{inline(p.strip())}</p>" for p in paragraphs if p.strip())
            out.append(f"<blockquote>{inner}</blockquote>")
            continue

        if re.match(r"- \[[ xX]\]\s", stripped):
            items: list[str] = []
            while index < len(lines) and re.match(r"- \[[ xX]\]\s", lines[index].strip()):
                text = lines[index].strip()[5:].strip()
                items.append(f'<li class="task">{inline(text)}</li>')
                index += 1
            out.append('<ul class="tasklist">' + "".join(items) + "</ul>")
            continue

        if re.match(r"[-*]\s+", stripped):
            items = []
            while index < len(lines) and re.match(r"[-*]\s+", lines[index].strip()):
                items.append(f"<li>{inline(lines[index].strip()[2:].strip())}</li>")
                index += 1
            out.append("<ul>" + "".join(items) + "</ul>")
            continue

        if re.match(r"\d+\.\s+", stripped):
            items = []
            while index < len(lines) and re.match(r"\d+\.\s+", lines[index].strip()):
                text = re.sub(r"^\d+\.\s+", "", lines[index].strip())
                items.append(f"<li>{inline(text)}</li>")
                index += 1
            out.append("<ol>" + "".join(items) + "</ol>")
            continue

        paragraph: list[str] = []
        while index < len(lines) and lines[index].strip():
            nxt = lines[index].strip()
            if nxt.startswith(("#", "|", "> ", "```")) or re.match(r"([-*]|\d+\.)\s+", nxt):
                break
            paragraph.append(nxt)
            index += 1
        if paragraph:
            out.append(f"<p>{inline(' '.join(paragraph))}</p>")
        else:
            index += 1

    return "\n".join(out), toc


STYLE = """
:root {
  --page: #ffffff; --ink: #14213d; --muted: #5a6478; --rule: #d8dde8;
  --accent: #0f766e; --accent-soft: #e6f2f1; --code-bg: #f5f7fa;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --page: #12151c; --ink: #e8ecf4; --muted: #9aa5bb; --rule: #2b3444;
    --accent: #5eead4; --accent-soft: #16302f; --code-bg: #1a1f2a;
  }
}
:root[data-theme="dark"] {
  --page: #12151c; --ink: #e8ecf4; --muted: #9aa5bb; --rule: #2b3444;
  --accent: #5eead4; --accent-soft: #16302f; --code-bg: #1a1f2a;
}
* { box-sizing: border-box; }
body {
  margin: 0; background: var(--page); color: var(--ink);
  font: 16px/1.62 Georgia, "Times New Roman", serif;
  -webkit-text-size-adjust: 100%;
}
.sheet { max-width: 44rem; margin: 0 auto; padding: 3rem 16px 6rem; }
h1, h2, h3, h4 { font-family: "Helvetica Neue", Arial, sans-serif; line-height: 1.25; color: var(--ink); }
h1 { font-size: 2rem; margin: 3.5rem 0 1.25rem; padding-bottom: .5rem; border-bottom: 3px solid var(--accent); }
h2 { font-size: 1.35rem; margin: 2.5rem 0 .75rem; }
h3 { font-size: 1.08rem; margin: 1.75rem 0 .5rem; }
h4 { font-size: .95rem; margin: 1.25rem 0 .4rem; text-transform: uppercase; letter-spacing: .05em; color: var(--muted); }
p { margin: 0 0 .9rem; }
ul, ol { margin: 0 0 1rem; padding-left: 1.4rem; }
li { margin-bottom: .35rem; }
ul.tasklist { list-style: none; padding-left: .2rem; }
li.task::before { content: "\\2610"; margin-right: .6rem; color: var(--accent); }
a { color: var(--accent); }
code {
  font: .88em/1.5 "SF Mono", Menlo, Consolas, monospace;
  background: var(--code-bg); padding: .1em .35em; border-radius: 3px;
}
pre {
  background: var(--code-bg); border-left: 3px solid var(--accent);
  padding: .9rem 1rem; overflow-x: auto; border-radius: 4px; margin: 0 0 1.1rem;
}
pre code { background: none; padding: 0; font-size: .85rem; }
blockquote {
  margin: 0 0 1.1rem; padding: .85rem 1.1rem;
  background: var(--accent-soft); border-left: 4px solid var(--accent); border-radius: 0 4px 4px 0;
}
blockquote p:last-child { margin-bottom: 0; }
table {
  width: 100%; border-collapse: collapse; margin: 0 0 1.2rem;
  font-family: "Helvetica Neue", Arial, sans-serif; font-size: .86rem;
}
th, td { border: 1px solid var(--rule); padding: .45rem .6rem; text-align: left; vertical-align: top; }
th { background: var(--accent-soft); font-weight: 600; }
hr.section-break { border: 0; border-top: 1px solid var(--rule); margin: 2.5rem 0; }
.cover { text-align: center; padding: 4rem 0 3rem; border-bottom: 3px solid var(--accent); }
.cover h1 { border: 0; font-size: 2.5rem; margin: 0 0 .4rem; }
.cover .sub { font-size: 1.15rem; color: var(--muted); font-family: "Helvetica Neue", Arial, sans-serif; }
.cover .meta { margin-top: 2rem; font-size: .9rem; color: var(--muted); font-family: "Helvetica Neue", Arial, sans-serif; }
.contents { margin: 2.5rem 0; font-family: "Helvetica Neue", Arial, sans-serif; font-size: .92rem; }
.contents ol { list-style: none; padding: 0; }
.contents .lvl2 { padding-left: 1.4rem; font-size: .86rem; color: var(--muted); }
.contents a { text-decoration: none; }
.contents a:hover { text-decoration: underline; }
.note { font-size: .85rem; color: var(--muted); font-family: "Helvetica Neue", Arial, sans-serif; }

@media print {
  :root {
    --page: #fff; --ink: #14213d; --muted: #555; --rule: #bbb;
    --accent: #0f766e; --accent-soft: #eef4f3; --code-bg: #f4f4f4;
  }
  @page { size: A4; margin: 18mm 16mm; }
  body { font-size: 10.5pt; }
  .sheet { max-width: none; padding: 0; }
  .contents { page-break-after: always; }
  h1 { page-break-before: always; page-break-after: avoid; }
  .cover h1 { page-break-before: auto; }
  h2, h3, h4 { page-break-after: avoid; }
  table, pre, blockquote { page-break-inside: avoid; }
  tr { page-break-inside: avoid; }
  a { color: inherit; text-decoration: none; }
  .screen-only { display: none; }
}
"""


def main() -> None:
    body: list[str] = []
    contents: list[tuple[int, str, str]] = []

    for name in SECTIONS:
        path = SOURCE / name
        if not path.exists():
            raise SystemExit(f"missing source file: {path}")
        slug = path.stem.lower().replace("_", "-")
        rendered, toc = render(path.read_text(encoding="utf-8"), slug)
        body.append(f'<section id="{slug}">{rendered}</section>')
        contents.extend(toc)

    toc_html = "".join(
        f'<li class="lvl{level}"><a href="#{ident}">{html.escape(title)}</a></li>'
        for level, ident, title in contents
        if level <= 2
    )

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Participant Handbook</title>
<style>{STYLE}</style>
</head>
<body>
<div class="sheet">
  <header class="cover">
    <h1>Advanced Data Analysis Techniques</h1>
    <div class="sub">Participant handbook</div>
    <div class="meta">
      Five days &middot; Genoa &middot; English delivery with Arabic interpretation<br>
      <span class="screen-only">Print this page to PDF, or read it on any device offline.</span>
    </div>
  </header>
  <nav class="contents">
    <h2>Contents</h2>
    <ol>{toc_html}</ol>
  </nav>
  {"".join(body)}
</div>
</body>
</html>
"""
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(page, encoding="utf-8")
    size_kb = OUTPUT.stat().st_size / 1024
    print(f"wrote {OUTPUT.relative_to(ROOT)} ({size_kb:.0f} KB, {len(contents)} headings)")


if __name__ == "__main__":
    main()
