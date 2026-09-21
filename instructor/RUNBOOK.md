# Day-of runbook

**Route selection:** this is the coding-route runbook. For zero programmers or an unknown/mixed cohort, follow [NO_CODE_DELIVERY.md](NO_CODE_DELIVERY.md) instead. It replaces these notebook activities and has its own Day 5 presentation timing.

The compressed version. Print it, hold it, work from it. The full explanations live in each day's `TEACHING_GUIDE.md`; this is what you need while standing up.

## Every morning, before participants arrive (30 minutes)

- [ ] Laptop on power, projector connected, screen readable **from the back row** — walk to the back and check.
- [ ] Jupyter running, today's `worked.ipynb` open, **kernel restarted and all cells run**. Do this every day, not once.
- [ ] Today's `worked_RESULTS.md` open in a second tab. This is your fallback if anything fails live.
- [ ] Notifications off, screen-sharing settings checked, font size increased in the editor.
- [ ] Timer visible to the room.
- [ ] Handbooks and task cards on the tables.
- [ ] Two minutes with the interpreter: today's new terms, and the first demonstration.

## The cycle you repeat all day

1. **State the question** (1 min) — one practical question, no code on screen.
2. **Explain the idea** (4 min) — then **stop and let the interpreter work**. Do not type during interpretation.
3. **Demonstrate one small thing** (5 min) — then pause again. Leave the code on screen.
4. **Pairs do it** (10–15 min) — walk the room; do not stay at the front.
5. **Compare and interpret** (5 min) — ask one pair, not all ten.

If interpretation is running long, **cut an extension task**. Never cut a break, and never cut the core lab.

## Three sentences to have ready

- When you do not know: *"I want to verify that rather than give you an inaccurate answer. I'll record it and come back to you."* Then actually write it down, and actually come back.
- When a demo fails: *"Let's look at the saved output and the reasoning, and isolate the environment problem separately."* Switch to `worked_RESULTS.md`.
- Before moving on: *"Can someone explain that result in their own words?"* Silence is not understanding.

---

## Day 1 — Exploratory data analysis

**Files:** `day-01-eda/` — `TEACHING_GUIDE.md`, `TASK_CARDS.md`, `student.ipynb`, `worked.ipynb`, `ANSWER_KEY.md`

| Time | Do this | Watch for |
|---|---|---|
| 0–20 | Welcome, course frame, pair roles, entry diagnostic | Set the pair roles properly now — it shapes all five days |
| 20–50 | EDA concepts, Python for tables | Keep code lines short and on screen during interpretation |
| 50–90 | **Lab A** — data audit | Every pair must reach 122 / 2 / 3 / 2 / 1 |
| 90–105 | Compare audits, discuss which issues need a business rule | |
| 105–120 | **Break** — say the return time aloud | |
| 120–150 | Mean vs median, dispersion, outliers. **Then: chart choice and chart repair** | The three bad charts are in the handbook |
| 150–195 | **Lab B** — cleaning and summary | Expect 119 valid, 116 priced, EUR 10,210 |
| 195–210 | **Break** | |
| 210–260 | **Teach the briefing format** (10 min), then **Lab C** — management briefing, capstone chosen | The briefing format is used every day after this — invest the ten minutes |
| 260–285 | Five groups, one finding each | |
| 285–300 | Exit questions, recap | Collect the capstone problems |

**Numbers to have memorised:** 122 raw rows · 2 duplicates · 3 missing prices · 2 missing channels · 1 invalid quantity · 119 valid · 116 priced · EUR 10,210 · Store 6,310 / Online 3,700 / Unknown 200.

**The two points that must land:** missing is not zero; the 80-unit order stays and the −2 order goes, and the reason is the business rule, not the number.

**If you are running late:** drop the chart-repair exercise to 10 minutes. Do not drop the briefing format.

---

## Day 2 — Machine learning

**Files:** `day-02-machine-learning/` — plus `instructor/first_model.ipynb` for anyone lost

| Time | Do this | Watch for |
|---|---|---|
| 0–20 | Recap EDA; identify inputs and target in the route example | "What do we know at dispatch time?" |
| 20–50 | Split, baseline, regression | Explain the split **before** the algorithm |
| 50–90 | **Lab A** — regression and MAE | 8.43 model vs 24.34 baseline |
| 90–105 | Compare explanations; leakage discussion | |
| 105–120 | **Break** | |
| 120–150 | Classification, confusion matrix, validation. **Then: explainability** | |
| 150–195 | **Lab B** — classifier and error counts | 9 missed delays, 2 false alarms |
| 195–210 | **Break** | |
| 210–260 | **Lab C** — clustering/PCA walkthrough, then tree depths. Capstone check-in | Keep the PCA part guided, not independent |
| 260–285 | Five groups report | |
| 285–300 | Exit questions | |

**Numbers:** 400 routes, 300/100 split · baseline MAE 24.34 · model MAE 8.43 · 9 missed delays · 2 false alarms · delayed means above 85 minutes (a teaching threshold, say so).

**The two points that must land:** a score without a baseline means nothing; the imputer lives inside the pipeline, and why.

**If you are running late:** the clustering/PCA section becomes a 10-minute demonstration you drive. Do not cut the confusion matrix.

---

## Day 3 — Time series and NLP

**Files:** `day-03-time-series-nlp/`

| Time | Do this | Watch for |
|---|---|---|
| 0–20 | Recap test-set protection; sort example dates | |
| 20–50 | Trend, weekly seasonality, chronological holdout | Draw the boundary on screen |
| 50–90 | **Lab A** — baselines, decomposition, ARIMA | ARIMA loses. That is the lesson |
| 90–105 | Why the complex model lost. **Then: rolling-origin backtesting** | |
| 105–120 | **Break** | |
| 120–150 | Text representation and classification | |
| 150–195 | **Lab B** — classify messages, inspect ambiguity | |
| 195–210 | **Break** | |
| 210–260 | **The text-and-time bridge** (10 min), then **Lab C** — training-only validation, text failure cases. Capstone check-in | |
| 260–285 | Five groups report | |
| 285–300 | Exit questions | |

**Numbers:** 210 daily observations · 28-day holdout · weekly baseline MAE 5.53 · ARIMA(1,1,1) MAE 22.11 · 16 training / 8 test messages.

**The two points that must land:** never train on the future; 100% on eight English messages is not evidence — say the sentence out loud yourself before a participant says it to a manager.

**If you are running late:** cut the text-and-time bridge to three spoken sentences. Do not cut the baseline comparison.

---

## Day 4 — Bayesian and generative

**Files:** `day-04-bayesian-generative/`

| Time | Do this | Watch for |
|---|---|---|
| 0–20 | Probability refresher: rate versus count | |
| 20–50 | Prior, likelihood, posterior on the defect example | |
| 50–90 | **Lab A** — update the defect probability, compare priors. **Then: posterior to decision** | The decision step is what makes this day land for non-technical attendees |
| 90–105 | Credible intervals and their assumptions | |
| 105–120 | **Break** | |
| 120–150 | MCMC: propose, compare, accept or stay | |
| 150–195 | **Lab B** — traces, chain means, autocorrelation | |
| 195–210 | **Break** | |
| 210–260 | **Lab C** — future-batch simulation, synthetic durations. **Then: synthetic data governance.** Capstone check-in | |
| 260–285 | Five groups report | |
| 285–300 | Exit questions | |

**Numbers:** prior Beta(2,18), mean 0.10 · 8 defective of 100 · posterior Beta(10,110), mean ≈0.0833 · 4 chains · 2,000 warm-up draws.

**The two points that must land:** a credible interval is a statement under a model and a prior, not a guarantee; parameter uncertainty and outcome variability are different questions.

**If you are running late:** the synthetic-durations critique can be a discussion instead of a lab. Do not cut the posterior-to-decision step.

---

## Day 5 — Big data, advanced models, close

**Files:** `day-05-big-data/` — including `spark_worked.ipynb` and `OFFLINE_ACTIVITY.md`

**Check Spark starts on your laptop before participants arrive.** If it does not, do not troubleshoot live — run `OFFLINE_ACTIVITY.md` and say plainly that we are using the prepared alternative.

| Time | Do this | Watch for |
|---|---|---|
| 0–20 | Recap evaluation; when one machine stops being enough | |
| 20–50 | Partitions, Hadoop/MapReduce, Spark; SQL demo | Keep HDFS / YARN / MapReduce / Spark distinct |
| 50–90 | **Lab A** — Spark aggregation and SQL agreement | Have the offline activity ready for any pair that cannot start Spark |
| 90–105 | Actions, shuffles, data movement | |
| 105–120 | **Break** | |
| 120–150 | Feature assembly and the MLlib pipeline | |
| 150–195 | **Lab B** — evaluation against a baseline | |
| 195–210 | **Break** | |
| 210–260 | Neural/GAN briefing (10 min), **production readiness** (10 min), **capstone presentations** (30 min) | Three minutes per group, hard limit — use the timer |
| 260–285 | **Final practical** (20 min) | |
| 285–300 | **Course evaluation, exit self-assessment, recap, next steps** | Hand out the post-course pack; collect both forms |

**The two points that must land:** local Spark proves the code runs, not that it scales; production readiness is monitoring, ownership and a retraining trigger, not working code.

**Do not run out of time for the close.** If Day 5 is slipping, shorten the GAN briefing. The evaluation form and the exit self-assessment are contractual deliverables and evidence for the organiser — protect those 15 minutes.

---

## When things go wrong

| Situation | Do this |
|---|---|
| A pair's environment will not run | Give them the executed notebook and `worked_RESULTS.md`; they interpret while support fixes it. They lose no learning. |
| Your demo throws an error | Do not debug live for more than 60 seconds. Switch to the saved results, continue, fix at the break. |
| Interpretation is taking much longer than planned | Cut extensions, then cut the third lab to a demonstration. Never the break. |
| The cohort is far more advanced than expected | Move to the extension tasks, raise the depth of questions — and tell the organiser the same day, in writing. |
| The cohort has no Python at all | Switch to NO_CODE_DELIVERY.md and its paper workbook; no code modification is required. Explain the outcome distinction to the organiser. |
| A question you cannot answer | Use the sentence. Write it in the parking list. Answer it the next morning. |
| A participant dominates discussion | Move to "each group agrees one finding" — the format already does this work for you. |
| You are 20 minutes behind at the break | Recalculate from the fixed points: breaks and the 285-minute close do not move. Everything else does. |

## Parking list

Keep a visible list of unanswered questions. Answer them the next morning in the first five minutes. Unanswered questions destroy credibility far faster than saying "I'll check".

| Day | Question | Asked by | Answered |
|---|---|---|---|
| | | | |
