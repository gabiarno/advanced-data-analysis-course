# Day 1 — Exploratory data analysis

## Learning outcomes

Learners will inspect a table, recognise missing and duplicate records, compare mean and median, describe dispersion, interpret three charts, flag unusual observations, and communicate a qualified finding.

Prerequisites: basic Python variables, lists, functions and comparisons. Required files: the student/worked notebooks and `datasets/retail_orders.csv`.

## Five-hour timetable — 20 participants with Arabic interpretation

Use 10 pairs; combine into five groups of four for reporting. Explanations and feedback include consecutive interpretation time. All written material remains in English; review task-card accessibility with the interpreter beforehand.

| Minutes | Activity | Visible completion check |
|---|---|---|
| 0–20 | Welcome, short diagnostic, pair setup | Each pair opens the student notebook and identifies a row. |
| 20–50 | Inspect a table; show missing and duplicate records | Each pair can identify one data-quality issue. |
| 50–90 | Pair lab A: load and audit | 122 rows, 2 exact duplicates, 3 missing prices. |
| 90–105 | Compare audit findings with interpretation | Distinguish an invalid quantity from a valid bulk order. |
| 105–120 | Break | |
| 120–150 | Demonstrate cleaning, summaries and labelled charts in short steps | Learners explain why unknown price is not zero. |
| 150–195 | Pair lab B: clean, summarise and plot | 119 valid orders; 116 priced orders; one labelled chart. |
| 195–210 | Break | |
| 210–260 | Pair challenge: compare channels and review unusual orders | Three-sentence briefing and one limitation. |
| 260–285 | Five groups report one result each, with interpretation | One finding, one limitation, one next step per group. |
| 285–300 | Exit questions and bridge to prediction | Explain why correlation is not causation. |

For the mean/median mini-demo, use [10, 12, 13, 15, 100] during the second demonstration cycle. For the final challenge, show the IQR flagging code as a guided optional step if learners are still consolidating summaries; the concept of reviewing rather than automatically deleting unusual orders remains core.

This schedule includes two 15-minute breaks and 135 minutes of protected pair practice. If five contact hours are required, add 30 minutes of supported practice and schedule breaks separately. See [interpreter and classroom guidance](../instructor/CLASSROOM_AND_INTERPRETER.md).

## Explanations and prompts

### What is EDA?

Say: “Before answering a business question, we need to understand how these data were collected, what each row represents, and what may be wrong or missing.”

Here each row is one synthetic retail order. A repeated customer is not necessarily a duplicate order. We remove exact duplicate records in this exercise because they are documented export errors.

Ask: “What could happen if we count one order twice?” Expected: inflated totals and potentially biased group comparisons.

### Python and pandas

Explain `df['units']` as a column, `df[df['units'] > 0]` as row filtering, and `groupby` as split–summarise–combine. Show a scalar comparison before a column comparison. Do not assume SQL knowledge.

### Centre and dispersion

For [10, 12, 13, 15, 100], the mean is 30 and the median is 13. The mean responds strongly to the large value. Neither is universally better: choose based on the question. Standard deviation describes spread around the mean; the interquartile range describes the middle half of the distribution. `pandas.Series.std()` uses the sample convention by default.

Ask: “Would the median tell us total revenue?” Expected: no; use a sum for the total.

### Missing values

Unknown is not zero. For this descriptive exercise, missing channels become Unknown, missing prices remain missing, and revenue totals explicitly cover priced orders only. Median filling can distort a business total, so it is not used here. Modelling-time imputation must be fitted on training data only.

### Invalid versus unusual

The exercise's business rule says orders must have positive units; returns are stored separately. The negative-unit record is invalid under that rule. A large positive bulk order is unusual but valid. An IQR fence is a review heuristic, not proof of an error or fraud. In another system negative units might legitimately represent returns.

### Charts

A histogram shows a distribution; a bar chart compares grouped values; a scatter plot shows paired numeric values. Always label axes and units. A channel with higher total revenue may simply have more orders: compare count and mean as well.

### Correlation

Correlation describes association, not cause. Revenue is mechanically calculated from units and price, so a units–revenue relationship is partly built into the definition. Marketing attribution would require additional evidence and a suitable design.

## Student exercise instructions

Use `student.ipynb`. Ask learners to predict the result before each code cell. During independent work, they may reuse earlier code but must explain their choices.

Basic completion: audit issues, apply rules, plot revenue and write a briefing.

Extension: compare total revenue, mean order revenue and median order revenue by channel. Explain why rankings can differ. Recalculate a descriptive summary excluding the bulk order as a sensitivity analysis; show both results and do not silently delete the order.

## Exit questions and answers

1. Why not replace every missing value with zero? It introduces an unsupported value and can bias results.
2. Is every IQR-flagged observation wrong? No; investigate its meaning and provenance.
3. Can correlation establish an advertising effect? No; confounding and other explanations remain.
4. Why report the number of missing prices beside revenue? The revenue total does not cover all valid orders.
5. What is the difference between cleaning for this report and preprocessing a predictive model? A predictive workflow must prevent information from held-out observations influencing learned preprocessing.

## Common learner questions

“Should we always remove duplicates?” No. Confirm what identifies an observation and whether repetition is meaningful.

“Why are the results synthetic?” We can practise safely with known issues and reproduce the lesson. These results are not evidence about an actual retailer.

“Which chart is best?” Start with the question and data types. There is no universally best chart.

“Why not predict revenue from units and price?” If both are already known and revenue is their product, arithmetic is preferable to a model. Day 2 uses a different synthetic prediction problem.
