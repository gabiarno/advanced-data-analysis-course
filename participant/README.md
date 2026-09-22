# Your course materials

Start with [the illustrated handbook](../dist/participant-handbook.pdf). It follows the five-day workshop, explains the ideas in ordinary English and leaves space for your own notes.

| Material | How to use it |
|---|---|
| [Handbook PDF](../dist/participant-handbook.pdf) | Print or read the 28-page visual classroom edition |
| [HANDBOOK.md](HANDBOOK.md) | Read the same core content in the repository |
| [Technical reference](HANDBOOK_TECHNICAL_REFERENCE.md) | Look up the earlier, more detailed explanations |
| [Method card](CHEATSHEET_METHODS.md) | Check questions, methods, metrics and pitfalls |
| [Python card](CHEATSHEET_PYTHON.md) | Find syntax patterns used in the notebooks |
| [Capstone](CAPSTONE.md) | Develop your one-page proposal through the week |
| [Pre-course pack](PRE_COURSE_PACK.md) | Prepare the laptop and bring a generalised problem |
| [Post-course pack](POST_COURSE_PACK.md) | Plan what to try after the workshop |
| [European practice](EUROPEAN_PRACTICE.md) | See how European public bodies govern this work, and two cases where it failed |
| [English–Arabic glossary](GLOSSARY_EN_AR.md) | Draft terminology for interpreter validation |
| [Paper fallback](NO_CODE_WORKBOOK.md) | Continue the analysis if a laptop is unavailable |

The daily folders contain the Python practicals. Run the prepared examples, make the requested changes and explain the result to your partner.

## Build the editions

```bash
python -m pip install -r requirements-handbook.txt
python scripts/build_visual_handbook.py
python scripts/build_participant_handbook.py
```

The visual builder reads participant/handbook_content.json and regenerates the Markdown, PDF and diagrams. The HTML builder produces the handbook with reference appendices and embedded chart images. Keep the separate tutor script and answer keys out of participant packs.

For printing, use A4 and check the preview. Print 20 copies plus five spares. Have the interpreter validate the glossary before distributing it as an approved translation.
