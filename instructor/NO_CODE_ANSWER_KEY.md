# No-code workbook — facilitator answers

Keep separate from participant copies. Alternative recommendations earn credit when evidence, assumptions and limitations are explicit. Every case is synthetic; do not infer real business performance.

## Day 1

A: 8 raw rows; remove one duplicate and one invalid sale; 6 valid orders; 5 priced. Keep the confirmed bulk order. Unknown channel stays visible. Missing price does not become zero.

B: Store 2 valid/2 priced, EUR 420, mean 210; Online 3 valid/2 priced, EUR 110, mean 55; Unknown 1/1, EUR 30, mean 30. Total known revenue EUR 560. Excluding the bulk order for sensitivity only gives Store EUR 20, Online EUR 110, Unknown EUR 30: the ranking changes. The sensitivity result does not justify deleting a valid record. Total valid revenue is unknown because one price is missing.

C: Sample finding: “Store contributes EUR 420 of EUR 560 known revenue, dominated by one valid EUR 400 order.” The data describe recorded sales, not the effect of reallocating a budget. Recover missing price, inspect a longer representative period and design an appropriate intervention evaluation. This eight-row case differs from the original 122-row notebook; do not mix their totals.

## Day 2

A: baseline absolute errors 20,0,20,40; MAE 20 minutes. Model errors 5,5,10,10; MAE 7.5. Four examples are insufficient for generalisation. Distance and scheduled stops can be available at dispatch; actual arrival and later complaints leak future information.

B: TN 55, FP 2, FN 9, TP 34. Accuracy 89%; recall 34/43=79.1%; precision 34/36=94.4%. Model error cost 9×100+2×20=940; always-on-time baseline 43×100=4,300. If missed delays cost 1, model costs 49 and baseline 43, reversing preference under the supplied simplified costs. These are error-cost comparisons, not a measured business ROI. Do not tune thresholds on this final test.

C: regression, classification, clustering, PCA respectively. Clusters require stability, meaning and an actionable use; PCA maximises retained variance, not business relevance. Feature importance describes model dependence, not causal intervention effects.

Exit: yes; aggregate accuracy may conceal costly missed cases or subgroup failures.

## Day 3

A: last-value errors 0,20,20,0,20,20: MAE 13.33; weekly errors all 5: MAE 5. Weekly pattern helps the simple method here. Across multiple origins fit preprocessing and models on past data only; evaluate each on the next window. Keep the last window unused until choices are fixed. This worksheet specifies an evaluation design; it does not claim the original notebook already executes rolling backtests.

B: M 1 Billing; M 2 Delivery; M 3 multiple issues/human review; M 4 likely Delivery with sarcasm, allow review; M 5 Human review; M 6 multiple issues/human review. Accept reasoned alternative routing if policy is explicit. Eight correct easy English examples only describe those eight cases. They do not validate Arabic, dialect, mixed-language, real-world or rare-case performance.

C: totals 6,8,8; delivery shares 50%,62.5%,50%. Wednesday final counts cannot enter a Wednesday morning forecast. Tuesday counts can only if available before that forecast is issued. Changes in classifier labels may create artificial category trends even when total demand is stable.

## Day 4

A: escalate under the 20% policy because 23.75%>20%; do not escalate under 30%. Neither rule is a universal recommendation. Mean and exceedance probability answer different questions. The posterior assumes the specified prior, representative independent Bernoulli sampling and a sufficiently stable underlying rate.

B: close means are reassuring but insufficient. Ask for traces and mixing diagnostics, autocorrelation and effective sample sizes; compare against the available exact solution. Different stuck chains cannot be repaired by averaging. Do not claim diagnostics were calculated merely because this worksheet asks for them.

C: rate interval describes uncertainty about a parameter under the model; future-count interval includes both that uncertainty and future sampling variability. Generated data may reproduce sensitive or unrepresentative source patterns; provenance, disclosure review and fitness-for-use checks are needed. No legal-compliance conclusion is established here.

Exit:23.75% is the probability the underlying rate exceeds 10%, not an expected defect count. Expected future count is about 8.33 under this model (simulation about 8.32).

## Day 5

A: A 10 orders/EUR 420/mean 42; B 4/EUR 240/mean 60; total 14/EUR 660. A partition means 50 and 40; unweighted average 45 is wrong because partition sizes differ. Use total sum/total count. Distributed choice depends on measured memory, runtime, growth, resilience needs and available support, not a tool name.

B: GAN spread 0.287 is far below target 0.6 even though means are close. Inspect distribution/tails and failure modes. Accuracy 0.847 versus 0.827 needs uncertainty, representative testing and cost comparisons. An example pilot condition: review the latest 100 labelled predictions weekly; pause automated routing if missed-delay rate exceeds the pre-agreed limit, with the named operations owner reverting to manual triage. That limit must be justified for the actual use case; no classroom number is an industry standard.

## Final practical rubric · 10 points

1. Classification (1), operational decision and available feature (1).
2. Past-to-future held-out evaluation with no leakage (1), explicit baseline (1), request confusion matrix and error costs or equivalent informative evidence (1).
3. Accuracy does not establish value beyond baseline (1); synthetic is no privacy guarantee (1); local execution is no scale proof (1).
4. Specific next step with owner (1), measurable stop condition and action (1).

Use scores for formative feedback, not certification of production competency. Accept written responses in Arabic when the interpreter can review them; assess reasoning rather than English fluency. Each participant completes an individual answer even if the capstone is shared. A useful next-step recommendation is a limited, monitored pilot after representative validation, not immediate automatic deployment.
