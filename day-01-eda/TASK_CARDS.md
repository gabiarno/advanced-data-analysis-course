# Day 1 task cards

Work in pairs. One person operates the notebook; the other checks and explains. Swap roles every 10–15 minutes. Use student.ipynb; worked.ipynb is available if you are blocked.

## A — Can we trust the raw table? (40 minutes)

Goal: find data-quality issues before making changes.

1. Open student.ipynb and run Setup.
2. Count rows with `len(raw)`.
3. Count exact duplicates with `raw.duplicated().sum()`.
4. Count missing fields with `raw.isna().sum()`.
5. Inspect non-positive quantities with `raw.loc[raw['units'] <= 0]`.
6. Read the data dictionary and explain which records need review.

Expected: 122 raw rows; 2 duplicate records; 3 missing prices; 2 missing channels; 1 non-positive quantity.

Check question: Why is an 80-unit order different from a negative quantity in this exercise?

## B — Make a transparent summary (45 minutes)

Goal: create an auditable descriptive summary.

1. Remove exact duplicate records.
2. Save the invalid quantity record separately, then exclude it from valid orders.
3. Label missing channels Unknown. Leave missing prices missing.
4. Calculate `revenue = units * unit_price`.
5. Compare channel counts and recorded revenue using the worked example if needed.
6. Draw one chart with a title and axis labels.

Expected: 119 valid orders; 116 with known revenue; recorded revenue EUR 10,210. This is not a total for orders with missing prices.

Check question: Why must the report mention three unknown prices?

## C — Explain a result to a manager (50 minutes)

Goal: turn a calculation into a qualified finding.

1. Identify the channel with the larger recorded revenue.
2. Compare the number of orders and average order revenue.
3. Inspect the large bulk order. Keep it in the main result.
4. Write three sentences: finding, limitation, next step.
5. Join another pair and agree one finding for a brief group report.

Expected: Store has EUR 6,310 recorded revenue versus Online EUR 3,700; Unknown accounts for EUR 200. This does not prove Store is inherently better or explain causality.

Extension: compare summaries with and without the bulk order, clearly labelling both. Explain why removing a valid order changes the question.
