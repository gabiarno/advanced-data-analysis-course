# Advanced Data Analysis Techniques — programme

Five days, in person, Genoa. English delivery with Arabic interpretation. 20 participants.

## Who this is for

Confirmed cohort: personnel of the Ministry of Interior of Saudi Arabia. They work with Python and are not beginners. They are not IT professionals — they are domain and decision-making staff who analyse data as part of their work. They have asked specifically to learn how this work is done in Europe.

The programme is built on that profile:

- **Pitched at working analyst level.** No Python syntax teaching, no guided first model, no line-by-line walkthroughs. Participants read and modify working code from the first hour. Time is spent on method choice, evaluation design and judgement, which is where domain specialists gain most.
- **Framed in public administration throughout.** Service-centre demand, inspection scheduling, emergency call volume, records quality, road safety. Not retail, not logistics, not customer support.
- **European practice woven through every day.** Roughly 150 minutes across the week, attached to analytical activities rather than delivered as a compliance lecture. This is content the cohort asked for and it is the distinguishing feature of the programme.
- **Built on resource allocation, not scoring people.** Every exercise concerns places, processes, documents and resources. European practice draws a hard line there, and the course teaches that line explicitly, using European case law and Europe's own failures.

A no-code route covers any participant who turns out not to code, and any session where laptops fail. It is a fallback, not the default.

## How the course runs

**Practitioner level.** Each day is 300 minutes: about 90 minutes of explanation and demonstration, 135 minutes of protected hands-on work, 45 minutes of interpretation and reporting, and two 15-minute breaks.

**Everything is evaluated.** No method is presented without a baseline to beat, a stated evaluation strategy and an explicit limitation. Participants leave able to challenge a result, not only produce one. This is the same discipline European regulation requires, which is why the two fit together without friction.

**Pairs with two roles.** Ten pairs. One drives the keyboard; the other checks the result and writes the briefing. Roles swap every 10–15 minutes.

**Reproducible and offline.** Everything runs on a laptop with no internet, no cloud account and no GPU once installed. Every worked example has been executed and its output recorded, so a failed laptop never stops a lesson.

**Synthetic data, honestly labelled.** Practice datasets are generated from published rules. No confidential or personal data is involved, results are reproducible, and participants keep everything without restriction. They are also taught precisely what synthetic results can and cannot support.

## What participants take away

- A printed handbook with the full content, their own recorded results, and four reference cards: method selection, Python, the English–Arabic glossary, and European practice.
- A completed capstone on a problem from their own work, including its governance case.
- Runnable notebooks for every method, working on their own machine.
- A 30-day follow-up plan.

## Learning outcomes

By the end of the course, participants can:

1. Audit a dataset for quality problems and document defensible cleaning decisions.
2. Choose an appropriate method for a stated administrative question and justify the choice.
3. Evaluate a model honestly, against a baseline, using a split that respects how the data arose.
4. Recognise and prevent leakage, overfitting, contaminated test sets and unrepresentative evaluation.
5. Build and interpret forecasts, text classifiers, Bayesian updates and distributed queries.
6. Distinguish allocating resources from scoring people, and explain why European practice treats them differently.
7. Apply purpose limitation, minimisation, necessity and proportionality to the design of an analytics project.
8. Present a quantitative finding to a non-technical decision-maker with its evidence, its limitation and a next step.
9. State what a result does not establish — reliably and without prompting.

Outcomes 6, 7 and 9 are what distinguish this programme. All three are assessed daily.

## Day 1 — Data quality, description and communicating findings

*Understand the data before modelling it, explain what you found, and know why the purpose comes first.*

**Scenario.** A service-centre request log: counter and online channels, documents processed, fees collected. A directorate wants to report channel performance before deciding on counter opening hours.

| Session | Content |
|---|---|
| Opening | Course frame, pair roles, entry diagnostic |
| **European** | Purpose before data. The resource-versus-people distinction, written on the board for the week. What an ordinary compliant project looks like, and why its first three steps remove more risk than the rest combined |
| Concept | Data quality as an obligation, not housekeeping. What a row represents |
| **Lab A (40 min)** | Audit the request log: rows, duplicates, missing values, invalid counts |
| Concept | Central tendency, dispersion, correlation. Outliers that are errors against outliers that are real |
| **Lab B (45 min)** | Apply documented cleaning rules, compute fees collected, build one publication-quality chart |
| Concept | Chart choice and chart repair. The one-page briefing format, used every day from here |
| **Lab C (50 min)** | Management briefing on channel performance. Capstone problem chosen |
| Close | Group reporting, exit check |

**Key discipline:** missing is not zero, an outlier is not automatically an error, association is not cause — and purpose limitation means data collected for one purpose is not automatically available for another.

## Day 2 — Prediction, evaluation and what an error costs

*Predict something, prove it is worth trusting, and know who pays when it is wrong.*

**Scenario.** Scheduled inspection rounds. Which will overrun their slot, so the day can be rebalanced before citizens' appointments are cancelled?

| Session | Content |
|---|---|
| Concept | Supervised and unsupervised tasks. What information exists at decision time |
| Concept | The split before the algorithm; train, validate, test, and why the order matters |
| **Lab A (40 min)** | Regression on round duration, evaluated against a baseline |
| Concept | Classification, confusion matrices, precision and recall, the cost of each error type |
| **Lab B (45 min)** | Classify overrunning rounds; count missed overruns and false alarms; state the operational consequence |
| **European** | The Dutch childcare benefits scandal. Error cost to the citizen rather than the department. Protected attributes and their proxies. Feedback loops in enforcement. Distinguishing fact from assessment in administrative records |
| Concept | Trees, forests, cross-validation, tuning. Explainability: what the model used, and how |
| **Lab C (50 min)** | Clustering and dimensionality reduction; tree-depth comparison on training folds only |
| Close | Group reporting, exit check |

**Key discipline:** a model that beats no baseline has not been shown to work; a test set inspected repeatedly is no longer a test set; and the cost of a false positive is the cost to the person it lands on.

## Day 3 — Time series, text, and the high-risk boundary

*Data with an order, data without a table, and the line European law draws through both.*

**Scenario.** Daily emergency call volume for a control room, for shift planning. Separately, routing written incident reports to the responsible operational unit.

| Session | Content |
|---|---|
| Concept | Time-series challenges; why time order changes evaluation |
| Concept | Trend, seasonality, periodicity, decomposition |
| **Lab A (40 min)** | Naive and seasonal-naive baselines; decomposition and ARIMA on a chronological holdout |
| Concept | Rolling-origin backtesting — evaluating a forecast the way it will be used |
| **European** | AI Act Annex III covers dispatch prioritisation for emergency services. This exercise, deployed for real, would be high-risk. The obligations that follow, and the difference between forecasting how many calls arrive and prioritising which caller is answered |
| Concept | Turning text into features; the classification pipeline; where embeddings and language models fit |
| **Lab B (45 min)** | Route incident reports; inspect what the model gets wrong and why |
| **European** | Purpose limitation applied to free text. Narrative fields record assessments as though they were facts |
| **Lab C (50 min)** | Validate a forecast on training data only; document a text failure case |
| Close | Group reporting, exit check |

**Key discipline:** never train on the future; a perfect score on eight examples is not evidence; and forecasting demand is planning, while prioritising individuals is a different legal object.

## Day 4 — Uncertainty, decisions and verifiability

*Reasoning when you do not know, turning that into a decision, and being able to prove it.*

**Scenario.** A quarterly quality audit of processed records against a service standard. Eight errors in a sample of one hundred — a real deterioration, or normal variation?

| Session | Content |
|---|---|
| Concept | Prior, likelihood, posterior. Probability distributions |
| **Lab A (40 min)** | Update the error rate exactly; compare the effect of different priors |
| Concept | From posterior to decision: the probability the rate exceeds the service standard, and the action it triggers |
| Concept | Credible intervals; parameter uncertainty against outcome variability |
| **Lab B (45 min)** | MCMC — run four chains, inspect traces and autocorrelation against the exact answer |
| **European** | SyRI, stopped by a Dutch court in 2020. Verifiability as a legal requirement, not only a technical virtue. Necessity and proportionality as tests that come before accuracy. Limits on solely automated adverse decisions |
| Concept | Generative models and synthetic data; governance, and why synthetic does not mean anonymous |
| **Lab C (50 min)** | Simulate the next audit batch; generate and critique synthetic processing times |
| Close | Group reporting, exit check |

**Key discipline:** a credible interval describes a model's belief under stated assumptions, not a guarantee; and if nobody outside your team can verify a claim, it cannot be shown to be proportionate.

## Day 5 — Scale, production and the capstone

*What changes when data outgrows one machine, and what it takes to deploy any of this responsibly.*

**Scenario.** Service transaction records held per regional office, no longer comfortable on one machine.

| Session | Content |
|---|---|
| Concept | When one machine stops being enough; partitioned aggregation; the Hadoop ecosystem and where Spark sits |
| **Lab A (40 min)** | Spark DataFrame and SQL aggregation across regional partitions; confirm they agree |
| Concept | Spark MLlib pipelines. Why splitting regional data by record id is the wrong split |
| **Lab B (45 min)** | Fit and evaluate an MLlib model against a baseline |
| Concept | Deep learning applied at scale; GANs — generator and discriminator |
| **European** | Impact assessments as project design tools, not paperwork. Procurement as the control point: the vendor supplies the evidence, and the buyer must know what to demand. Independent supervision. Production readiness in European terms — monitoring, logging, a stop condition, a named owner, an appeal route |
| **Capstone (50 min)** | Complete and present the briefing, including its three governance questions |
| Close | Final practical, course evaluation, exit self-assessment, recap |

**Key discipline:** running locally proves the code works, not that the system scales; and a model nobody monitors is a model quietly failing.

## The European thread

Roughly 150 minutes across the week, attached to analytical activities rather than taught separately. It covers which instrument applies to what — the general regulation, the separate law-enforcement regime, the AI Act's risk tiers, and the Council of Europe treaty that is open to non-EU states; the principles that constrain project design; two European systems that harmed citizens badly enough to reach a court and bring down a government; and what ordinary compliant practice looks like day to day.

It is presented as a framework and its reasoning, led by Europe's own failures. It is not legal advice, the instructor is not a lawyer, and it does not describe the participants' national law. What transfers is their judgement, and this is said plainly on Day 1.

The thread costs no additional time. Because the cohort is comfortable with Python, the syntax teaching, guided first model and pipeline mechanics are removed, and that reclaimed time pays for it almost exactly.

## Assessment

| Instrument | When | Purpose |
|---|---|---|
| Entry diagnostic | Before or on Day 1 | Placement, not grading. Pitched at working-analyst level |
| Daily exit questions | End of each day | Confirms the day's key discipline landed |
| Capstone | Threaded across the week, presented Day 5 | Applied transfer, including the governance case |
| Final practical, 20 minutes | Day 5 | Method choice, evaluation design, interpretation, correcting three false claims |
| Exit self-assessment | Day 5 | Compared against the entry diagnostic; gives the organiser evidence of movement |
| Course evaluation | Day 5 | Feedback on delivery, pace and interpretation |

Formative assessment for a short professional course. Not an accredited competency certification, and not presented as one.

## Delivery requirements

**Laptops.** One per participant preferred, one per pair minimum, with Python 3.12 and the supplied requirements installed and tested before Day 1. Participants are asked to confirm the environment runs in advance. A no-code route and saved results cover any failure.

**Room.** Projector readable from the back row, power at every seat, seating for pairs that re-forms into five groups of four.

**Interpretation.** An Arabic interpreter briefed before Day 1, with the glossary and the first demonstration reviewed in advance. The European vocabulary — proportionality, purpose limitation, redress, fundamental rights — is harder to interpret consistently than the statistical terms and needs its own briefing time. Mode must be confirmed; the timetable assumes consecutive interpretation.

**Printing.** 20 handbooks plus five spares, double-sided A4. Alternatively distributed as a single self-contained HTML file that works offline on any device.

**Contingency.** Every worked example has recorded outputs, so any lesson can continue from saved results. Spark has a documented offline alternative, and the no-code workbook covers a total environment failure.

## Scope note

This programme delivers the contracted syllabus at practitioner depth: each method is taught to the point where a participant can apply it to a well-posed administrative problem, evaluate it honestly and state its limits. It does not produce specialists in any single method.

It covers analytics for public administration — service demand, resource planning, emergency response, road safety, records quality, inspection scheduling, administrative processing. It does not provide operational guidance on surveillance, biometric identification or individual-level risk scoring of people. For several of those applications the European position is that they are prohibited or tightly restricted, and describing that position is part of what the cohort asked for.
