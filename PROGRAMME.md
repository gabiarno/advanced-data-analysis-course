# Advanced Data Analysis Techniques — programme

Five days, in person, Genoa. English delivery with Arabic interpretation. 20 participants.

This is the document to send to the organiser and to hand to participants on Day 1. It states what each day delivers, what participants produce, and how they will know they have learned it. Every session listed here is backed by runnable material in this repository.

## How this course is run

**Practitioner-level, not lecture-level.** Each day is 300 minutes: about 90 minutes of explanation and demonstration, 135 minutes of protected hands-on practice, 45 minutes of interpretation and reporting, and two 15-minute breaks. Participants spend more time working than listening.

**Everything is evaluated.** No method is shown without a baseline to compare it against, a stated evaluation strategy, and an explicit limitation. Participants leave able to challenge a result, not only produce one.

**Pairs with two real roles.** Participants work in 10 pairs. One drives the keyboard; the other checks the result and writes the briefing. Roles swap every 10–15 minutes, so every participant both codes and communicates. A participant who does not write code has a defined and assessed job from the first hour.

**Reproducible and offline.** All exercises run on a laptop with no internet connection, no cloud account and no GPU, once the environment is installed. Every worked example has been executed and its output recorded, so a failed laptop never stops a lesson.

**Honest data.** Practice datasets are synthetic and generated with published rules, so results are reproducible and no confidential or personal data is involved. Participants are told this explicitly and are taught what synthetic results can and cannot support — a discipline that transfers directly to their own data.

## What participants take away

- A printed handbook with the full course content, their own recorded results, and reference cards they will use after the course.
- A one-page method-selection card: which technique fits which question, which metric evaluates it, and its most common failure.
- A completed capstone briefing on a problem from their own work or a supplied scenario.
- Runnable notebooks for every method covered, which work on their own machine after the course.
- A 30-day follow-up plan.

## Learning outcomes

By the end of the course, participants can:

1. Audit a dataset for quality problems and document defensible cleaning decisions.
2. Choose an appropriate analytical method for a stated business question, and justify the choice.
3. Evaluate a model honestly, against a baseline, using a split that respects how the data arose.
4. Recognise and prevent the common failures: leakage, overfitting, contaminated test sets and evaluation on unrepresentative data.
5. Build and interpret time-series forecasts, text classifiers, Bayesian updates and distributed queries.
6. Present a quantitative finding to a non-technical stakeholder with its evidence, its limitation and a next step.
7. State what a result does not establish — reliably and without prompting.

Outcome 7 is the one that distinguishes this course. It is assessed every day.

## Day 1 — Exploratory data analysis and communicating findings

*Understand the data before modelling it, and explain what you found.*

| Session | Content |
|---|---|
| Opening | Course frame, pair roles, entry diagnostic |
| Concept | What EDA is, why it precedes modelling, Python for tabular data |
| **Lab A (40 min)** | Audit a 122-row order table: rows, duplicates, missing values, invalid quantities |
| Concept | Central tendency, dispersion, correlation; outliers that are errors versus outliers that are real |
| **Lab B (45 min)** | Apply documented cleaning rules, compute revenue, build one labelled chart |
| **Concept (new)** | Chart choice: matching chart form to question. Then repair three deliberately bad charts. |
| **Concept (new)** | The one-page briefing: finding, evidence, limitation, next step, what would change my mind |
| **Lab C (50 min)** | Produce a management briefing on channel performance; capstone problem chosen |
| Close | Group reporting, exit check |

Participants produce: a documented data audit, one publication-quality chart, and their first briefing.

Key discipline: *missing is not zero, an outlier is not automatically an error, and association is not cause.*

## Day 2 — Machine learning for decisions

*Predict something, then prove the prediction is worth trusting.*

| Session | Content |
|---|---|
| Concept | What machine learning is; supervised versus unsupervised; what information exists at decision time |
| Concept | The split before the algorithm: train, validate, test, and why the order matters |
| **Lab A (40 min)** | Regression on delivery duration; compare against a baseline using MAE |
| Concept | Classification, confusion matrices, precision and recall, and the cost of each error type |
| **Lab B (45 min)** | Classify delayed routes; count missed delays and false alarms; state the operational consequence |
| Concept | Decision trees, random forests, cross-validation and hyperparameter tuning |
| **Concept (new)** | Explainability: permutation importance and partial dependence — what the model used and how |
| **Lab C (50 min)** | Clustering and PCA walkthrough, then tree-depth comparison on training folds only |
| Close | Group reporting, exit check |

Participants produce: an evaluated regression model, an evaluated classifier with an error-cost argument, and a written model-selection justification.

Key discipline: *a model that beats no baseline has not been shown to work, and a test set inspected repeatedly is no longer a test set.*

## Day 3 — Time series and natural language

*Data with an order, and data without a table.*

| Session | Content |
|---|---|
| Concept | Time-series types and challenges; why time order changes evaluation |
| Concept | Trend, seasonality, periodicity, decomposition |
| **Lab A (40 min)** | Naive and seasonal-naive baselines; guided decomposition and ARIMA |
| **Concept (new)** | Rolling-origin backtesting: evaluating a forecast the way it will actually be used |
| Concept | NLP: turning text into features; the text-classification pipeline |
| **Lab B (45 min)** | Classify support messages; inspect the cases the model gets wrong and why |
| **Concept (new)** | The link between text and time: message volume as a series, and when a text-derived feature legitimately enters a forecast |
| **Concept (new)** | Where embeddings and language models fit — what changes, what does not, and why evaluation matters more, not less |
| **Lab C (50 min)** | Validate a forecast using training data only; find and explain a text failure case |
| Close | Group reporting, exit check |

Participants produce: a backtested forecast with a baseline comparison, and a text classifier with a documented failure analysis.

Key discipline: *never train on the future, and a perfect score on eight examples is not evidence.*

## Day 4 — Bayesian analysis and generative models

*Reasoning with uncertainty, and manufacturing data responsibly.*

| Session | Content |
|---|---|
| Concept | Bayesian thinking: prior, likelihood, posterior; probability distributions |
| **Lab A (40 min)** | Update a defect probability exactly; compare the effect of different priors |
| **Concept (new)** | From posterior to decision: the probability that the rate exceeds a contractual threshold, and the action it triggers |
| Concept | Credible intervals, and parameter uncertainty versus outcome variability |
| Concept | MCMC in three actions: propose, compare, accept or stay |
| **Lab B (45 min)** | Run four chains; inspect traces, chain means and autocorrelation against the exact answer |
| Concept | Generative models and synthetic data |
| **Concept (new)** | Synthetic data governance: legitimate uses, the privacy claims it does not automatically support, and what to check before sharing |
| **Lab C (50 min)** | Simulate a future batch; generate and critique synthetic service durations |
| Close | Group reporting, exit check |

Participants produce: a posterior-based recommendation with a stated decision threshold, and a critique of a synthetic dataset.

Key discipline: *a credible interval describes a model's belief, not a guarantee, and synthetic data inherits every flaw of the data that generated it.*

## Day 5 — Big data, advanced models and the capstone

*Scale, and what it takes to put any of this into production.*

| Session | Content |
|---|---|
| Concept | When one machine stops being enough; distributed computing, partitioned aggregation |
| Concept | The Hadoop ecosystem, MapReduce, and where Spark sits relative to it |
| **Lab A (40 min)** | Spark DataFrame and Spark SQL aggregation; confirm the two agree |
| Concept | Spark MLlib pipelines |
| **Lab B (45 min)** | Fit and evaluate an MLlib model against a baseline |
| Concept | Deep learning applied to big data; GANs — generator and discriminator |
| **Concept (new)** | From notebook to production: monitoring, drift, retraining, and who owns the model |
| **Capstone (50 min)** | Complete and present the briefing on your own problem or a supplied scenario |
| Close | Final practical assessment, course evaluation, recap and next steps |

Participants produce: a Spark query and an evaluated MLlib model, and the finished capstone briefing.

Key discipline: *running locally proves the code works, not that the system scales; and a model that nobody monitors is a model that is quietly failing.*

## Assessment

| Instrument | When | Purpose |
|---|---|---|
| Entry diagnostic, 8 questions | Before or on Day 1 | Placement, not grading. Sets the depth of support. |
| Daily exit questions | End of each day | Confirms the day's key discipline landed. |
| Capstone briefing | Threaded across the week, presented Day 5 | Applied transfer to the participant's own context. |
| Final practical, 20 minutes | Day 5 | Method choice, evaluation design, interpretation, correcting three false claims. |
| Exit self-assessment | Day 5 | Compared against the entry diagnostic, gives the organiser evidence of movement. |
| Course evaluation | Day 5 | Participant feedback on delivery, pace and interpretation. |

This is formative assessment for a short professional course. It is not an accredited competency certification, and is not presented as one.

## Delivery requirements

**Room:** projector readable from the back row, power at every seat, seating that allows pairs to share one screen and then re-form into five groups of four.

**Laptops:** one per participant preferred, one per pair minimum. Python 3.12 installed with the supplied requirements before Day 1. A zero-install fallback is prepared for participants who cannot install software.

**Interpretation:** an Arabic interpreter briefed before Day 1, with the glossary and the first demonstration reviewed in advance. Mode must be confirmed — the timetable assumes consecutive interpretation.

**Printing:** 20 handbooks, double-sided, plus five spare. Alternatively the handbook is distributed as a single self-contained HTML file that works offline on any device.

**Contingency:** every worked example has recorded outputs, so any lesson can continue from saved results if an environment fails. Spark has a documented offline alternative.

## Scope note

The brochure describes a broad syllabus. This programme delivers it at a practitioner-introductory depth: each method is taught to the point where a participant can apply it to a well-posed problem, evaluate it honestly and state its limits. It does not produce specialists in any single method, and it does not claim to. If the cohort proves more advanced than expected, the extension tasks in each day's task cards provide additional depth; a materially different depth requires an agreed change of scope before delivery.
