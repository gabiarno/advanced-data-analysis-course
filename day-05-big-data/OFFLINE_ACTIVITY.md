# Day 5 fallback — no Spark runtime

This is an interpretation and algorithm exercise, not a replacement claim that Spark ran successfully. Use it only when installation/startup was not completed before class.

## Partition exercise (15 minutes)

Give one pair records A10, B20, A5 and another pair C7, B3, C8. Each pair calculates a subtotal by key. Join the pairs and combine matching keys. Expected global totals A15, B23, C15. Ask what information had to move between groups and whether two independent subtotals were enough to answer the global question.

## Read the saved Spark output (15 minutes)

Open spark_worked_RESULTS.md. Identify the source row count and the regional aggregation. Explain why collecting two rows is safe here and why collecting the whole source would not scale indefinitely.

## SQL-on-paper task (10 minutes)

Write a query selecting region, COUNT(*), SUM(amount), and AVG(amount) grouped by region. Expected mean amounts are 50 and 51. Compare the query with the DataFrame expression in spark_worked.ipynb.

## Model interpretation (45-minute Lab B fallback)

Use the saved Spark model results. In pairs: identify features/label (10 min), explain train/test split (10 min), compare model and baseline MAE (10 min), identify two limits of transferring this result to production (10 min), explain the recommendation to another pair (5 min).

## Honest reporting

Say “We analysed a previously executed Spark example and practised its logic” if using this fallback. Do not say the participants trained a live Spark model.
