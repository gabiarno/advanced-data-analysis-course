# Generated deliverables

Everything here is produced by the scripts in `scripts/`. Do not edit these files directly — edit the source and rebuild, or your change will be overwritten.

| File | Built from | Command |
|---|---|---|
| `participant-handbook.html` | `participant/HANDBOOK.md`, `CAPSTONE.md`, both cheat sheets and the glossary | `python scripts/build_participant_handbook.py` |
| `slides/day-0N.pptx` | `presentations/day-0N-slide-plan.md` | `python scripts/build_slide_decks.py` |

## The handbook

`participant-handbook.html` is a single self-contained file. It needs no server, no internet and no software beyond a browser.

**To print:** open it and print to PDF or to paper. A4, double-sided, roughly 40 pages. The print stylesheet starts each day on a new page and keeps tables from splitting.

**To distribute online:** send the same file. It works offline, on a phone, and can be emailed or copied to a USB drive.

## The slide decks

Five editable 16:9 PowerPoint decks, one per day, with the speaker notes from each plan carried into the notes pane.

**They are not finished.** Every deck contains `[ VISUAL TO ADD ]` placeholders marking where a chart, table or diagram belongs, with the plan's description of what it should show. Before delivery:

1. Replace every placeholder with the real chart, table or diagram. The Day 2–5 figures already exist in each day's `figures/` folder.
2. Check every number against the slide plan and the day's `worked_RESULTS.md`. **The figures must not change.**
3. Confirm readability from the back of the room — titles about 36pt, body at least 24pt.
4. Ask the organiser whether LPC requires its own template, cover slide and branding. If so, import these slides into it rather than restyling them by hand.

The alternative route is to build the decks in Canva from the plans in `presentations/`, as originally intended. These generated files are a working starting point that preserves every figure and every speaker note; they are not a substitute for the review pass.
