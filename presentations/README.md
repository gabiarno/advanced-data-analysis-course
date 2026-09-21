# Course presentations

Two routes to a deck exist, and they are complementary rather than alternatives. The Canva designs are the intended delivery decks; the generated PowerPoint files cover the days Canva does not yet reach and serve as the offline fallback.

## Canva presentations

The following Canva presentations have been created. Open the links to view or edit them with the appropriate Canva permissions. These are links to Canva designs, not PDF or PowerPoint files stored in this repository.

| Day | Topic | Canva presentation | Pages reported by Canva | Slides in the plan | Source plan |
|---|---|---|---:|---:|---|
| 1 | Exploratory Data Analysis | [Open in Canva](https://www.canva.com/d/xZogMoxHxWhMG64) | 19 | 18 | [Slide plan](day-01-slide-plan.md) |
| 2 | Machine Learning | [Open in Canva](https://www.canva.com/d/F9PQkTpmGRxh2Sj) | 19 | 19 | [Slide plan](day-02-slide-plan.md) |
| 3 | Time Series and Text Analysis | [Open in Canva](https://www.canva.com/d/mTnHPSeTfx0jRaa) | 20 | 17 | [Slide plan](day-03-slide-plan.md) |
| 4 | Bayesian Analysis and Generative Models | Not found in the connected Canva account yet | — | 17 | [Slide plan](day-04-slide-plan.md) |
| 5 | Big Data and Advanced Models | [Open in Canva](https://www.canva.com/d/y6Y8Az0W4hvWegT) | 21 | 20 | [Slide plan](day-05-slide-plan.md) |

The "slides in the plan" column is counted directly from the `## Slide N:` headings in each plan by `scripts/build_slide_decks.py`. **Days 1, 3 and 5 do not match**, so Canva has either added or dropped slides. Reconcile each before teaching — a missing slide is a missing figure.

## Generated PowerPoint decks

```bash
python -m pip install -r requirements-build.txt
python scripts/build_slide_decks.py
```

This writes five editable 16:9 decks to `dist/slides/`, one per day, built directly from the plans. Every recorded figure and every speaker note is carried across verbatim, and each chart, table or diagram is marked with a `[ VISUAL TO ADD ]` placeholder describing what belongs there.

They are plain by design and are not intended to replace the Canva decks. They are useful for three specific things:

1. **Day 4**, which has no Canva design yet.
2. **An offline fallback.** The Canva decks need an account and a connection; a venue in Genoa may supply neither. A `.pptx` on the laptop always opens.
3. **A reference for the review pass.** Because they are generated from the plans, their slide count and their figures are correct by construction — compare the Canva decks against them.

## Status and review

The cover text confirms the day/topic for the four linked Canva designs. Full slide-by-slide factual and visual review remains pending. Generated page counts differ from some source plans, so check coverage before teaching.

Known issues from the cover check:
- Day 2 contains the template text "BORCELLE".
- Day 5 contains a printed "01 of 23" counter although Canva reports 21 pages.
- Days 1, 3 and 5 have page counts that do not match their plans (see the table above).

Use the source plans to check numerical results, synthetic-data labels, notebook paths, speaker notes, readability and template leftovers. No Canva PDF/PPTX exports have been added to the repository. Day 4 requires its generated design link or completion of its Canva generation step.

Ask the organiser whether LPC requires its own template and branding before investing further in either route.

## Design identifiers

These identifiers allow the connected Canva tools to locate designs if an editor link changes.

| Day | Canva design ID |
|---|---|
| 1 | DAHV2s0Vp8A |
| 2 | DAHV2vDOrHw |
| 3 | DAHV2uwXVg0 |
| 5 | DAHV2szfymg |
