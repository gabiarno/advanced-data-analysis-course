# Practical analytics workbook — no programming required

Five days · English with Arabic interpretation · paper, pen and optional calculator.

Work in five teams of four. Rotate decision owner, evidence checker, critical reviewer and spokesperson each activity. Everyone writes an individual exit answer. All data below are synthetic. Small hand-calculation cases are separately authored teaching examples, not extracts from the larger notebooks. Recorded notebook results are labelled explicitly.

Use the handbook's five-line briefing: finding, evidence, limitation, next step, what would change my mind. Use the existing CAPSTONE.md throughout the week. No installation, account, Python knowledge or internet is required.

## Day 1 — Can we trust the report?

### A · Audit the data · 40 minutes

Spend 10 minutes reading, 15 agreeing rules, 10 auditing and 5 recording disagreements.

This separately authored order table records sales, not returns. Repeated order IDs are accidental duplicates. Confirmed bulk orders are valid. Missing prices cannot be recovered during this exercise.

| Order | Channel | Units | EUR per unit | Note |
|---|---|---|---|---|
| 01 | Store | 2 | 10 | |
| 02 | Online | 3 | 20 | |
| 02 | Online | 3 | 20 | Repeated record |
| 03 | Store | -1 | 10 | Invalid sale quantity |
| 04 | Online | 4 | Missing | |
| 05 | Store | 80 | 5 | Confirmed bulk order |
| 06 | Missing | 2 | 15 | |
| 07 | Online | 1 | 50 | |

Choose keep, exclude or investigate for each row. Record raw count, duplicates removed, invalid rows removed, valid orders and priced orders. Explain why the bulk order and the negative order receive different treatment. Retain unknown channel as a category.

Your audit and rules: ________________________________________

### B · Calculate and challenge · 45 minutes

Spend 15 minutes calculating, 15 drawing and 15 challenging another team's chart.

Revenue = units × price. Exclude unpriced orders from revenue calculations, but retain them in the audit. Calculate known revenue by channel and mean known revenue per priced order. Sketch a bar chart with a zero baseline, units and a title that says what was excluded. Compare totals before and after excluding the valid bulk order as a sensitivity check, not as a cleaning decision. Would your ranking change?

| Channel | Valid orders | Priced orders | Known revenue EUR | Mean per priced order EUR |
|---|---|---|---|---|
| Store | | | | |
| Online | | | | |
| Unknown | | | | |

Repair these claims: “Missing revenue is zero”; “Store causes larger sales”; “Delete the bulk order because it changes the answer.”

### C · Advise a manager · 50 minutes

Spend 15 minutes drafting a five-line briefing, 15 exchanging peer feedback and 20 choosing your capstone decision, owner and missing data. The manager asks: “Should I move the online budget to stores?” Your answer must distinguish a descriptive finding from a causal claim. List evidence needed before moving the budget.

Exit: What does the known revenue total leave out? __________________

## Day 2 — Is a model worth using?

### A · Forecast delivery duration · 40 minutes

Spend 10 minutes reading, 15 calculating and 15 discussing the evaluation design. This is a separate four-route teaching case; predictions are supplied.

| Route | Actual minutes | Baseline prediction | Model prediction |
|---|---|---|---|
| A | 40 | 60 | 45 |
| B | 60 | 60 | 55 |
| C | 80 | 60 | 70 |
| D | 100 | 60 | 90 |

Absolute error ignores the sign. MAE is the sum of absolute errors divided by the number of routes. Calculate both MAEs. Which is better on these four routes? Why is that not enough to deploy?

At morning dispatch, choose usable features: planned distance, scheduled stops, actual arrival time, complaints received after delivery. Explain each exclusion. Propose a future-period test if the system will predict future deliveries.

### B · Put a cost on errors · 45 minutes

Spend 10 minutes labelling cells, 15 calculating and 20 deciding. These counts are recorded results from the course's synthetic classifier, on 100 held-out routes.

| Actual status | Predicted on time | Predicted delayed |
|---|---|---|
| On time | 55 | 2 |
| Delayed | 9 | 34 |

A missed delay costs 100 teaching cost units; a false alarm costs 20. Correct predictions cost zero. These are hypothetical error costs, not measured intervention benefits or deployment costs.

Calculate accuracy, delayed-route recall, delayed-prediction precision and total error cost. Compare with predicting every route on time. Now suppose a missed delay costs only 1 unit: does the preferred option change? Why should a threshold be selected using validation data and costs before the final test?

Decision and assumptions: ________________________________________

### C · Select a method and challenge a vendor · 50 minutes

Spend 15 minutes matching methods, 15 reviewing a vendor claim and 20 updating your capstone.

Match: predict minutes; flag likely delay; group similar customers without labels; compress many correlated measurements for a two-axis display. Choose regression, classification, clustering or PCA. Explain why a cluster is not automatically a useful business segment and why a two-axis plot can lose information.

A vendor says: “Our model uses distance heavily, so reducing distance will cause the predicted savings.” Explain the missing causal evidence. Ask for baseline performance, a held-out evaluation and subgroup errors. Add target, decision-time features and error costs to the capstone.

Exit: Can a higher-accuracy model be worse for the business? Explain. __________

## Day 3 — Predict the future and interpret messages

### A · Compare forecasts · 40 minutes

Spend 10 minutes calculating, 15 discussing validation and 15 designing a split. Separate six-day teaching case:

| Day | Actual volume | Last-value forecast | Weekly forecast |
|---|---|---|---|
| 1 | 100 | 100 | 95 |
| 2 | 120 | 100 | 115 |
| 3 | 80 | 100 | 85 |
| 4 | 100 | 100 | 105 |
| 5 | 120 | 100 | 115 |
| 6 | 80 | 100 | 85 |

Compute MAE. Recorded results from the larger course notebook are: last-value MAE 22.38, weekly 5.53, ARIMA 22.11 on a final 28-day holdout. Why might a simpler method win? Repeatedly choosing models after seeing that final window contaminates it.

Sketch rolling evaluation: train days 1–28, validate 29–35; train 1–35, validate 36–42; train 1–42, validate 43–49. Reserve days 50–56 for one final test. At each origin, use only data available then. Explain why random shuffling can leak the future.

### B · Route messages with uncertainty · 45 minutes

Spend 15 minutes labelling, 15 comparing disagreements and 15 designing a review policy. Separate authored cases; choose Billing, Delivery or Human review. More than one issue may be present.

| ID | Message |
|---|---|
| M1 | My invoice was charged twice. |
| M2 | The parcel arrived two days late. |
| M3 | It arrived late and I was charged twice. |
| M4 | Great, another perfect delivery — still waiting! |
| M5 | Please call me about yesterday. |
| M6 | Where is the refund for my missing parcel? |

Do not invent a model confidence score. Record an agreed label, ambiguity and human escalation rule. The original notebook correctly classified eight easy authored English test examples. Explain why this does not establish performance on Arabic, mixed-language messages, dialects or real complaints. Describe a representative, locally reviewed evaluation set without collecting personal data in class.

### C · Connect text to time · 50 minutes

Spend 15 minutes aggregating, 15 checking availability and 20 updating your capstone. These are separate simulated category counts. Counts include all messages available at the daily cutoff, not later corrections.

| Day | Billing | Delivery | Uncertain |
|---|---|---|---|
| Monday | 2 | 3 | 1 |
| Tuesday | 1 | 5 | 2 |
| Wednesday | 3 | 4 | 1 |

Calculate total messages by day and delivery share by day. Can Wednesday's final counts enter a forecast issued Wednesday morning? Can Tuesday's counts? State the availability assumption. What would happen if the classifier began labelling more messages “uncertain”? Add a time-respecting split and text-review policy to the capstone if applicable.

Exit: What does eight out of eight tell us, and what does it not tell us? _______

## Day 4 — Decide under uncertainty

### A · Translate probability into action · 40 minutes

Spend 10 minutes reading, 15 deciding and 15 checking sensitivity. Recorded Bayesian example: prior Beta(2,18), observe 8 defective items among 100, posterior Beta(10,110). Supplied summaries: posterior mean 8.33%; 95% credible interval about 4.1%–13.9%; probability the underlying defect rate exceeds 10% is about 23.75%. No integration is required.

For this fictional exercise, the organisation's policy is: escalate for additional inspection if that probability exceeds 20%. Apply the rule. What happens if the agreed threshold was 30% instead? Explain why a posterior mean below 10% does not settle the decision. State assumptions about sampling and stability. This policy is a teaching scenario, not a legal or industry requirement.

### B · Challenge a simulation · 45 minutes

Spend 15 minutes inspecting evidence, 15 explaining it and 15 designing checks. Recorded four-chain MCMC means range approximately 0.0831–0.0842, close to the exact posterior mean 0.0833. Does agreement of means prove convergence? What else would you ask to see: traces, autocorrelation, effective sample sizes, sensitivity to starting points?

Compare with a separately authored failed run: chain means 0.03, 0.08, 0.14, 0.20. Explain why averaging those chains does not repair poor exploration. When an exact solution exists, explain why it is a useful check on the sampler.

### C · Future outcomes and synthetic data · 50 minutes

Spend 15 minutes interpreting, 15 reviewing a sharing proposal and 20 updating the capstone. Recorded simulation: in the next 100 items, mean defects approximately 8.32 and central 95% predictive interval approximately 2–17. Distinguish this count interval from the credible interval for the underlying rate.

A supplier proposes to share generated service records because “synthetic means anonymous and realistic.” Draft questions about the source data, rare-record copying, unusual cases, distribution checks and intended use. No real records are exchanged in this exercise. Add an uncertainty statement, action threshold and who approves the action to the capstone.

Exit: Does 23.75% probability mean 23.75 defective items in the next batch? ______

## Day 5 — Scale, deployment and the final recommendation

### A · Combine distributed results · 40 minutes

Spend 15 minutes calculating, 10 cross-checking and 15 choosing infrastructure. Separate partition exercise:

| Partition | Channel | Orders | Revenue EUR |
|---|---|---|---|
| 1 | A | 2 | 100 |
| 1 | B | 1 | 90 |
| 2 | A | 8 | 320 |
| 2 | B | 3 | 150 |

Combine counts and sums for each channel, then calculate the global mean. Compare A's correct mean with the unweighted average of the two partition means. Explain the error. A 5 MB daily file fits on a laptop; a workload processing terabytes with a strict deadline might require distributed infrastructure. What measurements, costs and operational support would you request before choosing?

### B · Approve a pilot, not just a score · 45 minutes

Spend 10 minutes reading, 20 drafting a pilot and 15 peer reviewing. Recorded synthetic results: Spark regression MAE 2.248 versus baseline 20.227; local neural classifier accuracy 0.847 versus linear 0.827. The latter is a different task, so do not compare its accuracy to regression MAE. A toy GAN targeting mean 2.0 and standard deviation 0.6 generated approximately 2.10 and 0.287. What does the GAN miss?

Specify: decision owner; baseline; representative future test; acceptable error costs; subgroup checks; human override; monitoring frequency; pause/rollback trigger; rollback owner. Each trigger needs a measurable condition and an action. Explain why a local Spark demo does not prove production scalability and why a small accuracy improvement alone does not justify a neural network.

### C · Capstone presentation · 50 minutes

Use 15 minutes to finish one group briefing using the existing six CAPSTONE.md headings. Then five groups each have seven minutes: three minutes speaking, three for interpretation and one for feedback. Each person retains their own written page, even when the group presents a shared scenario.

### Individual final practical · 20 minutes

Use 5 minutes for translated instructions and 15 for individual written answers. No coding, no group answer. A service team wants to predict tomorrow's delayed visits using past records. A vendor claims 96% accuracy; a baseline predicting no delays scores 95%.

1. Name the method, decision and one feature available at scheduling time.
2. Specify a split and baseline. What additional evidence would you request?
3. Correct: “96% proves the model is useful”; “synthetic guarantees privacy”; “running Spark locally proves scale.”
4. Recommend one next step, an owner and a measurable stop condition.

Your answers: ____________________________________________________
