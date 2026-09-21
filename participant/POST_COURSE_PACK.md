# After the course — what to do next

Hand this out on Day 5, and email it again a week later.

---

## The first thing

Within three days, open one notebook from the course on your own machine and run it end to end. Not to learn anything new — to confirm your setup still works. The single most common reason a course produces no change is that people never open the material again, and the barrier is almost always a broken environment rather than lost motivation.

## Your 30-day plan

**Week 1 — reproduce.** Run all five days' worked notebooks on your own machine. Change one number in each and predict what will happen before you run it. This takes about three hours in total and it is the highest-value thing on this page.

**Week 2 — substitute.** Take one of your own datasets — a spreadsheet is fine — and run the Day 1 audit on it: rows, duplicates, missing values, invalid values. Write the five-line briefing about what you found. Show it to one colleague.

**Week 3 — model something small.** Pick a question from your own work that Day 2 covers. Build the baseline first. Then build one model. Compare them. If the model does not beat the baseline, that is a real and reportable result.

**Week 4 — present.** Take your capstone one-pager, update it with what you learned in weeks 1–3, and put it in front of the person who would have to approve the work.

## The checklist to bring to every meeting

Keep this where you will see it. It is most of what the course was for.

- What is the baseline?
- How was the data split, and why that way?
- How many examples are in the test set?
- How many times has that test set been looked at?
- Which type of error costs more, and does the metric reflect that?
- Who is missing from this data?
- What would this not tell us, even if it worked perfectly?

## What to learn next

Choose one, not all five. Depth in one is worth more than a pass over all of them.

| If your work is mostly... | Go deeper into | Start with |
|---|---|---|
| Forecasting and planning | Seasonal models and proper backtesting | statsmodels SARIMAX documentation; then implement rolling-origin evaluation |
| Prediction and classification | Pipelines, calibration, explainability | scikit-learn user guide, sections on pipelines and inspection |
| Text | Embeddings and modern text models | Start with what a vector representation is, before any model |
| Decisions under uncertainty | Bayesian modelling with a probabilistic programming library | Re-derive the Day 4 defect example, then move to a library |
| Data volume | SQL first, Spark second | SQL is more useful more often than Spark is |

## Documentation worth bookmarking

- [pandas getting-started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)
- [scikit-learn common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) — the most useful page in the whole library
- [scikit-learn cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html)
- [statsmodels time-series analysis](https://www.statsmodels.org/stable/tsa.html)
- [PySpark getting started](https://spark.apache.org/docs/latest/api/python/getting_started/index.html)

## Three habits worth more than any library

1. **Build the baseline before the model.** Every time. It takes two minutes and it tells you whether the next two days are worth spending.
2. **Write the limitation before someone asks.** Stating a weakness yourself makes your other claims more believable, not less.
3. **Restart the kernel and run everything.** If it does not reproduce from a clean state, it is not a result yet.

## Your materials

Everything from the course is yours to keep and reuse: all five days of notebooks, the worked solutions, the recorded outputs, the answer keys, and this handbook. The synthetic datasets carry no restriction.

## One last thing

The most valuable thing in this course was not a method. It was the habit of asking what a result does *not* establish. That question will make you more useful than any particular technique, and it works in every meeting you will ever sit in.
