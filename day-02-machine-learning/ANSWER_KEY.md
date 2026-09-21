# Instructor answer key

## Worked answers

Regression: 24.34 baseline MAE versus 8.43 model MAE on the synthetic holdout. The reduction is about 15.91 minutes in average absolute error. This does not establish performance on actual routes.

Classification: logistic regression has the highest mean validation F1 in this run. Matrix [[55,2],[9,34]] gives 9 missed delays and 2 false alerts. Delayed-class recall is 34/43≈0.791; precision is 34/36≈0.944. Accuracy is 0.89 versus a 0.57 majority-class baseline. The selected model was fixed before final testing.

Clusters contain 109, 93 and 98 rows. One PCA component retains about 53.1% of standardised variance; it discards about 46.9%. Cluster labels are arbitrary identifiers and may permute across implementations.

The depth experiment is exploratory validation on training data. It must not be used to revise the reported final-test claim without a new untouched evaluation. See solutions.ipynb for runnable code.

## Exit check and key

1. What makes actual arrival time a bad feature before dispatch? It is unavailable and leaks the outcome.
2. What does the bottom-left confusion-matrix cell represent? Actual delayed, predicted not delayed: a false negative.
3. Why impute inside the pipeline? Each training fold learns its own imputation without its validation fold.
4. Does k=3 prove three natural groups? No.
5. Is explained variance predictive accuracy? No.

## Marking guide

10 points: correct workflow 2; calculations 2; interpretation 2; limitation 2; clear explanation 2. Use this for formative feedback, not certification. Numerical reference values are recorded in worked_RESULTS.md; Spark has spark_worked_RESULTS.md.
