# Instructor answer key

## Worked answers

Training dates: 2026-01-01 to 2026-07-01. Final test: 2026-07-02 to 2026-07-29. Last-value MAE≈22.38, weekly-repeat≈5.53, fixed ARIMA≈22.11. The nonseasonal ARIMA illustration misses important weekly structure; complexity alone is not an advantage. The test is one artificial window, not proof of a generally superior method.

All eight deliberately easy held-out messages are correctly classified in the recorded run. This is weak evidence because the sample is tiny and authored with shared vocabulary. The ambiguous message receives a delivery label, but no gold label or calibrated confidence is supplied.

For the development split, use only the 182 training observations: 168 for fitting/reference and 14 for validation. See solutions.ipynb. Appropriate Arabic development requires representative labelled Arabic examples, suitable text processing, and language-aware evaluation including ambiguity and domain variation.

## Exit check and key

1. Why avoid a random temporal split? It can let future information enter training.
2. Does a trailing mean fully decompose a series? No.
3. Must ARIMA beat a baseline? No.
4. When should TF-IDF learn vocabulary/statistics? From training text only.
5. Does perfect accuracy on eight English examples validate Arabic use? No.

## Marking guide

10 points: correct workflow 2; calculations 2; interpretation 2; limitation 2; clear explanation 2. Use this for formative feedback, not certification. Numerical reference values are recorded in worked_RESULTS.md; Spark has spark_worked_RESULTS.md.
