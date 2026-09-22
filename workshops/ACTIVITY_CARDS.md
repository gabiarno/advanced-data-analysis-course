# Workshop cards | Varied formats, serious analytical work

The variety is deliberate: private prediction, pair investigation, role-play, exchanged cases, peer review and incident simulation. Participation is assessed through evidence and reasoning, not speaking confidence or speed. No compulsory performance games, elimination or public ranking.

## Daily rhythm

| Minutes | Format |
|---|---|
| 0–15 | Short retrieval challenge: write, compare, discuss |
| 15–30 | One worked example, with interpretation |
| 30–80 | Workshop A: 50 minutes |
| 80–100 | Exchange work and review another pair's reasoning |
| 100–115 | Break |
| 115–130 | One short demonstration, with interpretation |
| 130–180 | Workshop B: 50 minutes |
| 180–195 | Compare two approaches and resolve one misconception |
| 195–210 | Break |
| 210–270 | Workshop C: 60 minutes |
| 270–290 | Report and challenge; on Day 5, individual final practical |
| 290–300 | Individual exit and close; on Day 5, feedback and next steps |

Total 300 minutes including 30 minutes of breaks. Protected workshop/review blocks total 180 minutes: 50+20+50+60. Warm-up, discussion, reporting and exit work add participation. All timings include interpretation; do not add translation afterwards.

## Reusable facilitation pattern

For a 50-minute workshop: 5 minutes to explain and interpret the brief; 5 for individual prediction; 20 to investigate in pairs; 10 to exchange interpretations; 10 to record a result and discuss. For a 60-minute workshop use the specific split stated in the card, or add 10 minutes for capstone transfer. Do not extend the day.

At minutes 80–100: exchange one output with another pair; spend 5 minutes reading,8 checking its evidence,5 discussing feedback and 2 writing a revision. The tutor listens for misconceptions rather than marking everything publicly.

Use different low-pressure warm-ups: Day 1 a two-question experience interview; Day 2 three claims to correct; Day 3 arrange dates/features on the correct side of a forecast cutoff; Day 4 predict how an update changes a probability; Day 5 name a failure and the person who should respond. Participants write privately first and can contribute through their partner or interpreter. No prior coding-speed ranking.

For reporting on Days 1–4, five groups have four minutes each including interpretation: one finding and one limitation. Rotate the reporter; do not require a polished presentation every day. The final Day 5 presentation has its own seven-minute allocation.

## Three-question retrieval check (Day 2 opening)

Ask participants to mark each statement as defensible or in need of correction, then explain to a partner: (1) A missing price can safely become zero. (2) A valid unusual order should stay in the main analysis and can be explored in a labelled sensitivity check. (3) A larger channel total proves that moving customers to that channel increases spending.

Facilitator answers: (1) false unless a documented rule establishes zero; (2) defensible; (3) not established by a descriptive comparison. Collect explanations, not just votes. If you want to select discussion prompts randomly, use numbered cards; random choice is a facilitation aid, not a learning objective.

## Workshop cards

### 1A | Data-quality clinic | 50 minutes

**Format:** Pairs investigate, then exchange one disputed cleaning decision.

**Say:** “Open day-01-eda/student.ipynb. Audit first; document what each issue means before editing. Ask your partner to challenge one rule.”

**Hand in:** A five-line audit with row counts, actions and reasons.

**Facilitator check:** 122 raw; 2 duplicates; 1 invalid quantity; 119 valid; 116 priced. Keep the confirmed bulk order.

**Ask:** “Which rule would change if this were a returns table?”

**Support:** use the worked cell or saved output, then explain it. **Stretch:** change one assumption and predict its effect before running.

### 1B | Chart makeover | 50 minutes

**Format:** Pairs become an analyst and a busy service manager; switch halfway.

**Say:** “Make a channel chart from the cleaned data. Your partner has one minute to explain it without help. Revise whatever they misunderstood. Then compare the main result with the labelled bulk-order sensitivity.”

**Hand in:** Before/after chart and a caption explaining one improvement.

**Facilitator check:** Known revenue EUR 10,210; missing prices excluded. A total is not a causal channel comparison.

**Ask:** “Can the chart be correct but still encourage the wrong decision?”

**Support:** use the worked cell or saved output, then explain it. **Stretch:** change one assumption and predict its effect before running.

### 1C | The ranking reversal | 60 minutes

**Format:** Predict privately, calculate in pairs, then compare reasoning in fours.

**Say:** “Use Day 1 of workshops/experiments.ipynb. Guess the faster team overall and within each case type before running. Try common case mixes of 20%,50% and 80% complex work. Then write the briefing and choose your capstone decision.”

**Hand in:** A comparison under observed and common mixes; a decision and its owner.

**Facilitator check:** Pooled means A 12/B 23.3; at 50/50 A 20/B 16.5. B is faster within both types. Different workload mixes reverse the pooled ranking.

**Ask:** “What would you request before comparing two offices?”

**Support:** use the worked cell or saved output, then explain it. **Stretch:** change one assumption and predict its effect before running.

### 2A | Predict, run, explain | 50 minutes

**Format:** Both partners write a prediction before the operator runs the model.

**Say:** “Open Day 2 student notebook. Predict whether regression will beat the training-mean baseline. Run the example. Explain the difference and identify one feature that would arrive too late for dispatch.”

**Hand in:** Prediction, observed result and a two-sentence explanation.

**Facilitator check:** Saved MAE 24.34 vs 8.43 minutes. The synthetic evaluation does not establish real-service performance.

**Ask:** “What would make the improvement operationally irrelevant?”

**Support:** use the worked cell or saved output, then explain it. **Stretch:** change one assumption and predict its effect before running.

### 2B | The cost negotiation | 50 minutes

**Format:** One partner owns the service decision; the other owns the model. Swap the cost assumptions, not the final-test threshold.

**Say:** “Use the classification results. Negotiate which error matters more. Compare missed-delay cost 100/false-alarm 20 with missed-delay 1/false-alarm 20. Prepare a recommendation on the supplied fixed predictions.”

**Hand in:** Cost comparison and explicit assumptions agreed by both roles.

**Facilitator check:** Model 940 vs baseline 4,300; under changed costs 49 vs 43. These are illustrative error costs, not measured benefits.

**Ask:** “Which costs or consequences did this simple calculation omit?”

**Support:** use the worked cell or saved output, then explain it. **Stretch:** change one assumption and predict its effect before running.

### 2C | Model review panel | 60 minutes

**Format:** Two pairs exchange roles as proposing team and reviewers.

**Say:** “Use Day 2 of workshops/experiments.ipynb. Compare thresholds on validation data at missed-event costs 10,50,100. Fix the policy and threshold before opening the final cell. Another pair challenges the split, baseline and cost choice. Keep the original clustering/PCA walkthrough to ten minutes.”

**Hand in:** A threshold decision record, one final evaluation and one unresolved limitation.

**Facilitator check:** Choose using validation only. Test results describe the fixed procedure. Do not select another threshold from final-test performance.

**Ask:** “What evidence would make the review panel approve a limited pilot?”

**Support:** use the worked cell or saved output, then explain it. **Stretch:** change one assumption and predict its effect before running.

### 3A | Forecast comparison desk | 50 minutes

**Format:** Pairs propose a forecast; another pair checks the evidence behind the choice.

**Say:** “Run the predeclared Day 3 forecasts. Explain why the weekly rule wins in the saved example. Use training-only validation for any changes. No points for a better final-test score obtained by repeated tuning.”

**Hand in:** Comparison with baseline, cutoff date and limitation.

**Facilitator check:** Saved weekly MAE 5.53; last 22.38; fixed ARIMA 22.11. Complexity does not guarantee improvement.

**Ask:** “Would the same method necessarily win during a policy change?”

**Support:** use the worked cell or saved output, then explain it. **Stretch:** change one assumption and predict its effect before running.

### 3B | Write a case that challenges the classifier | 50 minutes

**Format:** Pairs exchange two authored messages; the other pair must explain the labels and uncertainty.

**Say:** “Run the Day 3 text pipeline. Write one multi-topic message and one ambiguous message. Exchange them before running predictions. Compare human judgement with the model and agree an escalation rule.”

**Hand in:** Two test cases, observed predictions and a human-review rule.

**Facilitator check:** Delivery/billing is not sentiment. Eight easy English cases do not establish broader language performance.

**Ask:** “Is the problem the algorithm, the categories or missing context?”

**Support:** use the worked cell or saved output, then explain it. **Stretch:** change one assumption and predict its effect before running.

### 3C | Backtesting relay | 60 minutes

**Format:** One partner checks the time boundaries; the other checks the error table. Swap at the second origin.

**Say:** “Use Day 3 of workshops/experiments.ipynb. Run four development origins; inspect each window before the average. Fix the method before final evaluation. Then discuss message counts available at a forecast cutoff and update the capstone split.”

**Hand in:** Origin-by-origin results, method choice and one final score.

**Facilitator check:** Each training history stops at its origin. Final 14 days remain separate until selection is complete.

**Ask:** “Which window would you investigate even if the average looked good?”

**Support:** use the worked cell or saved output, then explain it. **Stretch:** change one assumption and predict its effect before running.

### 4A | Estimate, reveal, update | 50 minutes

**Format:** Everyone writes an initial estimate; pairs explain how evidence changes it.

**Say:** “Open Day 4 student notebook. Predict whether the posterior mean will be exactly 8%. Run the update, change the prior, then increase the sample. Discuss interval width as well as the mean.”

**Hand in:** Before/after belief statement with modelling assumptions.

**Facilitator check:** Original 10/120=8.33%; uniform prior 9/102=8.82%; larger sample 18/220=8.18%.

**Ask:** “When would collecting more of the same data fail to help?”

**Support:** use the worked cell or saved output, then explain it. **Stretch:** change one assumption and predict its effect before running.

### 4B | Sampler detective | 50 minutes

**Format:** Pairs inspect evidence; another pair plays the sceptical reviewer.

**Say:** “Compare the MCMC traces and exact posterior. Investigate a very small proposal scale if time permits. List two reassuring signs and one check missing from the demonstration.”

**Hand in:** Evidence-based verdict on the approximation, with limits.

**Facilitator check:** Similar means alone do not prove convergence. High acceptance can accompany poor movement.

**Ask:** “What would you check before simply adding more iterations?”

**Support:** use the worked cell or saved output, then explain it. **Stretch:** change one assumption and predict its effect before running.

### 4C | The decision hearing | 60 minutes

**Format:** A group of four rotates analyst, decision owner, reviewer and reporter.

**Say:** “Use Day 4 of workshops/experiments.ipynb. Compare priors and 20%/30% policy triggers. Explain a changed decision without pretending one policy is mathematically mandatory. Spend fifteen minutes on the original predictive/generative results and finish the capstone uncertainty statement.”

**Hand in:** Probability, policy and action written as three separate statements.

**Facilitator check:** Probability of rate>10% is distinct from the policy probability trigger. Generated data do not establish privacy or real-world validity.

**Ask:** “Who should justify and approve the action threshold?”

**Support:** use the worked cell or saved output, then explain it. **Stretch:** change one assumption and predict its effect before running.

### 5A | Human partitions, then Python | 50 minutes

**Format:** Each pair receives a partition summary; two pairs combine results before checking in code.

**Say:** “First calculate the common A-channel mean from 2 orders/EUR 100 and 8 orders/EUR 320. Then use the original Spark SQL/DataFrame example or saved fallback. Explain what moves between workers and what collect does.”

**Hand in:** Correct combined mean, reconciled query output and a memory explanation.

**Facilitator check:** Combined mean 42, not 45. The full Spark example is separate: A 5,000/EUR 250,000; B 5,000/EUR 255,000.

**Ask:** “What would break if one partition were much larger than the others?”

**Support:** use the worked cell or saved output, then explain it. **Stretch:** change one assumption and predict its effect before running.

### 5B | An incident in the pilot | 50 minutes

**Format:** One pair operates the pilot; another is the review team.

**Say:** “Use Day 5 of workshops/experiments.ipynb. With the stated 12-minute limit, find the two-week trigger and decide who acts. Then inspect the original MLlib/neural/GAN results; explain why their headline metrics are insufficient.”

**Hand in:** Incident note: evidence, uncertainty, action, owner and return-to-service condition.

**Facilitator check:** The stated monitoring rule first triggers at week 7. It does not identify a cause. GAN spread 0.287 vs target 0.6 reveals a problem despite similar means.

**Ask:** “What changes if true outcomes arrive two weeks late?”

**Support:** use the worked cell or saved output, then explain it. **Stretch:** change one assumption and predict its effect before running.

### 5C | A proposal you can challenge | 60 minutes

**Format:** Five groups present; every participant retains an individual written page.

**Say:** “Use 20 minutes to complete the capstone,35 for five interpreted presentations, and 5 to write one useful peer suggestion. Present the decision, baseline, evaluation, limitation and next action.”

**Hand in:** A one-page proposal with owner and measurable stop condition.

**Facilitator check:** Seven minutes per group: 3 speaking,3 interpretation,1 feedback. Assess evidence and clarity, not salesmanship.

**Ask:** “What is the smallest useful next step you could take in two weeks?”

**Support:** use the worked cell or saved output, then explain it. **Stretch:** change one assumption and predict its effect before running.
