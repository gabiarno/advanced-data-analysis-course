# Participant-facing material

**Start with [NO_CODE_WORKBOOK.md](NO_CODE_WORKBOOK.md)** for five days of practical work without programming. The handbook provides supporting concepts and optional coding labs.

Everything in this folder is written for participants, not for the instructor. It is plain English, free of internal planning notes, and safe to hand over or print exactly as it is.

## What is here

| File | What it is | When it is used |
|---|---|---|
| [NO_CODE_WORKBOOK.md](NO_CODE_WORKBOOK.md) | Core paper activities, supplied evidence and individual final assessment | Every day; included first in the generated handbook |
| [HANDBOOK.md](HANDBOOK.md) | The printed workbook: five days of content, labs and blank result tables to fill in | Handed out on Day 1 |
| [CHEATSHEET_METHODS.md](CHEATSHEET_METHODS.md) | Method selection, metrics, splits and the seven ways a result goes wrong | Bound into the handbook; used all week and after |
| [CHEATSHEET_PYTHON.md](CHEATSHEET_PYTHON.md) | Python and pandas reference with the course's actual code patterns | Bound into the handbook |
| [EUROPEAN_PRACTICE.md](EUROPEAN_PRACTICE.md) | How Europe governs public-sector analysis: which rules apply, the principles that constrain design, two European failures | Bound into the handbook; taught across all five days |
| [GLOSSARY_EN_AR.md](GLOSSARY_EN_AR.md) | English–Arabic glossary, **draft for interpreter validation** | Interpreter briefing, then bound into the handbook |
| [CAPSTONE.md](CAPSTONE.md) | The week-long project brief and its five supplied scenarios | Introduced Day 1, presented Day 5 |
| [PRE_COURSE_PACK.md](PRE_COURSE_PACK.md) | Welcome letter, setup instructions, what to bring | Send as soon as possible before Day 1 |
| [POST_COURSE_PACK.md](POST_COURSE_PACK.md) | 30-day plan, what to learn next, the meeting checklist | Day 5, and emailed again a week later |
| [FEEDBACK_FORM.md](FEEDBACK_FORM.md) | Course evaluation | Day 5 close |
| [EXIT_SELF_ASSESSMENT.md](EXIT_SELF_ASSESSMENT.md) | Confidence check, compared against the entry diagnostic | Day 5, before the recap |
| [CERTIFICATE_TEMPLATE.md](CERTIFICATE_TEMPLATE.md) | Certificate wording, if the organiser does not supply one | After the course |

## Producing the handbook

The handbook, the two reference cards, the glossary and the capstone brief are assembled into one document:

```bash
python scripts/build_participant_handbook.py
```

This writes `dist/participant-handbook.html` — a single self-contained file with no external dependencies.

**To print:** open it in a browser and print to PDF or to paper. The print stylesheet adds page breaks between days, keeps the tables together, and drops the navigation. Print double-sided, A4. Check the print preview after building; the no-code workbook adds pages.

**To distribute online:** send the same HTML file. It works offline, on a phone, with no server and no internet connection. It is one file, so it can be emailed or put on a USB drive.

Print 20 copies plus five spares. Ask the organiser who is printing — venue printing is cheaper than carrying 25 bound documents through an airport, but it must be arranged in advance.

## Before you hand anything out

1. Have the interpreter review `GLOSSARY_EN_AR.md` and apply their corrections. The Arabic column is a draft.
2. Confirm dates, the instructor's name and the organiser's name where the templates show `‹placeholders›`.
3. Check with the organiser whether LPC requires its own branding on participant material.
