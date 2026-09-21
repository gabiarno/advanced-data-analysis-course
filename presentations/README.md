# Course presentations

Five English slide plans, each following the practical course material, preserving the recorded synthetic results and carrying speaker notes and pair activities. They are the source for the generated decks in `dist/slides/`.

| Day | Slide plan | Generated deck | Review status |
|---|---|---|---|
| 1 | [EDA](day-01-slide-plan.md) | `dist/slides/day-01.pptx` | Visual placeholders to replace; figures to verify |
| 2 | [Machine learning](day-02-slide-plan.md) | `dist/slides/day-02.pptx` | Visual placeholders to replace; figures to verify |
| 3 | [Time series and text](day-03-slide-plan.md) | `dist/slides/day-03.pptx` | Visual placeholders to replace; figures to verify |
| 4 | [Bayesian and generative models](day-04-slide-plan.md) | `dist/slides/day-04.pptx` | Visual placeholders to replace; figures to verify |
| 5 | [Big data and advanced models](day-05-slide-plan.md) | `dist/slides/day-05.pptx` | Visual placeholders to replace; figures to verify |

These files are slide specifications. Two routes turn them into decks:

- **Generated PowerPoint.** `python scripts/build_slide_decks.py` writes five editable 16:9 decks to `dist/slides/`, carrying every figure and every speaker note across and marking each chart or diagram with a `[ VISUAL TO ADD ]` placeholder. This is the fastest route to a working deck.
- **Canva.** Build from these plans by hand, as originally intended, if the organiser requires LPC branding.

Either way the decks are not finished until a review pass has replaced every visual placeholder and checked the slides against the plans for exact figures, notebook filenames, readability and notes. See `dist/README.md`.
