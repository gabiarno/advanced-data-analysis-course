# Reference 1 — Choosing and evaluating a method

The card to keep on your desk. Read across: the question you have, the method that fits, how you evaluate it, and the mistake that most often invalidates it.

## Match the question to the method

| Your question | Method | Output | Evaluate with | Baseline to beat | The usual mistake |
|---|---|---|---|---|---|
| How much / how many? | Regression | A number | MAE or RMSE on held-out data | Predict the training mean | Reporting the metric without the baseline |
| Which category? | Classification | A label, or a probability | Precision, recall, confusion matrix | Predict the most common class | Using accuracy when classes are imbalanced |
| Which of these are similar? | Clustering | Group assignments | Stability, and fitness for the intended use | A sensible manual segmentation | Treating the clusters as discovered truth |
| Too many columns to work with | PCA / dimensionality reduction | Fewer derived columns | Variance retained | Keeping the original columns | Reading retained variance as accuracy |
| What happens next, in time? | Time-series forecast | Future values, with an interval | MAE on a *chronological* holdout, ideally rolling | Repeat last value; repeat last season | Random train/test split |
| What is this text about? | Text classification | A label | Precision and recall on held-out documents | Most common class | Fitting the vocabulary before splitting |
| How likely is it, given what I knew? | Bayesian inference | A posterior distribution | Posterior predictive checks | The prior alone | Reading a credible interval as a guarantee |
| I need data I cannot share | Generative / synthetic data | Artificial records | Compare distributions, not just means | The real data's summary statistics | Assuming synthetic implies anonymous |
| It does not fit in memory | Distributed processing (Spark) | The same answer, at scale | Correctness against a small-sample check | Doing it in pandas | Believing a local run proves scalability |

## Which metric, and why

| Metric | Says | Use it when | Careful |
|---|---|---|---|
| MAE | Average size of the error, in the target's units | Errors cost roughly in proportion to their size | Averages hide the worst cases |
| RMSE | Like MAE but punishes large errors more | One big error is much worse than several small | Not in the target's units in an intuitive way |
| Accuracy | Fraction of predictions that were right | Classes are balanced and errors cost the same | Useless at 95% when 95% of cases are one class |
| Precision | Of the cases we flagged, how many were real | False alarms are expensive | Says nothing about what you missed |
| Recall | Of the real cases, how many we caught | Missing a case is expensive | Trivially 100% if you flag everything |
| F1 | A balance of precision and recall | You need one number and costs are symmetric | Hides an asymmetric cost structure |
| Variance retained (PCA) | How much variation the kept components represent | Deciding how many components | Not a measure of predictive performance |

## The evaluation split, chosen by how the data arose

| If your data is... | Split by | Because |
|---|---|---|
| Independent cases, no order | Random | Nothing links the rows |
| Ordered in time | Time — hold out the *latest* period | You will never have future data at prediction time |
| Repeated per customer, patient, site | Group — all of one entity on one side | Otherwise the model recognises the entity, not the pattern |
| Strongly imbalanced classes | Stratified random | To keep rare cases in both halves |
| Text | Random by document, vocabulary fitted on the training side only | Vocabulary built on everything leaks |

## Seven ways a good result turns out to be wrong

1. **Leakage.** A feature encodes the answer, or preprocessing saw the held-out data. *Test:* would this value genuinely be available at the moment of prediction?
2. **Contaminated test set.** You tuned, looked at the test score, tuned again. *Test:* how many times have you looked at that number?
3. **Wrong split.** Random split on ordered or grouped data. *Test:* how did these rows arise?
4. **No baseline.** An impressive-sounding score that a trivial rule matches. *Test:* what does "always guess the mean" score?
5. **Unrepresentative data.** The evaluation set does not resemble deployment. *Test:* who and what is missing from this data?
6. **Too few examples.** 100% on eight cases. *Test:* how many held-out cases, really?
7. **Metric does not match the cost.** Optimising accuracy when a missed case costs 50 times a false alarm. *Test:* what does each type of error cost?

## Sentences worth memorising

- "What is the baseline?"
- "How was the data split, and why that way?"
- "How many examples are in the test set?"
- "How many times has that test set been looked at?"
- "What would this *not* tell us, even if it worked perfectly?"
- "Who is missing from this data?"

## Words to avoid, and what to say instead

| Instead of | Say |
|---|---|
| This proves | This is consistent with |
| X causes Y | X and Y are associated; the data cannot separate cause here |
| The model is 94% accurate | The model caught 41 of 46 delays and raised 8 false alarms on held-out data |
| The optimal model | The best of the four candidates we compared on validation data |
| The data shows | This sample shows, with these caveats |
