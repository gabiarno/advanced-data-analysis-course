# Curriculum review — brochure promises against current materials

**Audience update:** the cohort already uses Python. The current delivery follows instructor/TUTOR_SCRIPT.md, with guided notebook experiments and a conversational participant handbook. No-code materials are retained as a fallback.

**Earlier delivery adaptation after this review:** a complete paper-based route now exists in [instructor/NO_CODE_DELIVERY.md](instructor/NO_CODE_DELIVERY.md), with [participant activities](participant/NO_CODE_WORKBOOK.md) and [answers](instructor/NO_CODE_ANSWER_KEY.md). It preserves the existing handbook, capstone and technical notebooks. This route teaches evaluation and decisions; it does not certify independent implementation.

Reviewed on 2026-09-21 against the LPC Training brochure *Advanced Data Analysis Techniques* (5 days, category "Data Science & Visualisation"). This document records what the brochure commits to, where the repository already delivers it, what is missing, and what should be added. It is a planning document for the instructor and the organiser, not classroom material.

## Summary judgement

The five day folders are substantively complete and unusually careful: every method is paired with a baseline, an evaluation strategy and a stated limitation. That discipline is the strongest asset here and should not be diluted.

Three things stand between the current state and a delivery that exceeds expectations:

1. **The brochure sells communication and visualisation; the materials teach modelling.** The course category is "Data Science & Visualisation" and two of six objectives are about presenting insight to stakeholders. Charts currently appear as by-products of labs. Nothing teaches chart choice, chart design, or how to structure a briefing.
2. **The brochure sells real-world data; every dataset is synthetic.** This is a defensible pedagogical choice and it is documented honestly, but "interactive examples and exercises drawn from practice and the real world" is a written promise. One real open dataset closes it.
3. **Nothing exists that a participant takes away.** All material is instructor-facing. There is no handbook, no reference card, no pre-course pack, no evaluation form — and the brochure's own Day 5 outline ends with "Course evaluation and recap".

Items 1 and 3 are closed by this change. Item 2 and the teaching additions in the backlog below are specified but not yet implemented.

## Traceability: brochure promise to delivered material

Use this table with the organiser. It is the fastest way to demonstrate that the contracted outline is covered, and it makes the two genuine gaps visible on our terms rather than theirs.

| Brochure line | Where it is delivered | Status |
|---|---|---|
| EDA definition and importance | day-01-eda/TEACHING_GUIDE.md §1 | Covered |
| Python for data analysis, basic syntax | instructor/first_model.ipynb, day-01 student.ipynb | Covered |
| Visualisation and exploration with Python libraries | day-01 labs; charts throughout | **Partial — see gap V1** |
| Central tendency, dispersion, correlation | day-01 guide, slides 9–10, 15 | Covered |
| Outlier detection and treatment | day-01 IQR review, bulk-order decision | Covered |
| ML definition and role | day-02 guide §1 | Covered |
| ML algorithms and their uses | day-02, participant method-selection card | Covered |
| Regression, classification | day-02 labs A and B | Covered |
| Decision trees, random forests | day-02 §5, Lab C | Covered |
| Clustering, dimensionality reduction | day-02 §6, Lab C | Covered |
| Cross-validation and hyperparameter tuning | day-02 §2 and §5 | Covered |
| Time-series definition, types, challenges | day-03 §1 | Covered |
| Decomposition and trend analysis | day-03 §2 | Covered |
| Seasonality and periodicity | day-03 §2 | Covered |
| ARIMA | day-03 §3 | Covered |
| NLP definition **and its link to time-series data** | day-03 Lab B (NLP only) | **Gap — see N1** |
| Bayesian statistics and applications | day-04 §1 | Covered |
| Bayes' theorem and probability distributions | day-04 §1 | Covered |
| Bayesian modelling and inference for decisions | day-04 §2 | **Partial — see B1** |
| MCMC | day-04 §3 | Covered |
| Generative models and synthetic data | day-04 Lab B, day-05 toy GAN | Covered |
| Big data and distributed computing | day-05 §1 | Covered |
| MapReduce and Hadoop ecosystem | day-05 §1 | Covered |
| Apache Spark and Spark SQL | day-05 §2, spark_worked.ipynb | Covered |
| Deep learning applied to big data | day-05 §4 | Covered (introductory, labelled as such) |
| GANs and applications | day-05 toy GAN | Covered (introductory, labelled as such) |
| **Objective:** make informed business decisions | final practical; day-02 cost discussion | Covered |
| **Objective:** present insights to stakeholders with assurance | day-01 Task C (three sentences) | **Gap — see V1, V2** |
| **Objective:** communicate insights clearly and effectively | scattered | **Gap — see V1, V2** |
| **Objective:** apply skills to real-world projects | synthetic labs only | **Gap — see R1, C1** |
| **Audience:** business leaders, strategic planners | all labs are coding labs | **Gap — see A1** |
| Day 5: course evaluation and recap | day-05 timetable line only | **Closed by this change** |

## Gaps and what closes them

### V1 — Visualisation is assumed, not taught (highest priority)

The brochure category is "Data Science & Visualisation". Participants will expect to leave able to build a better chart than they build today. Currently they will leave able to interpret one honestly, which is not the same promise.

*Closed by:* `participant/CHEATSHEET_METHODS.md` chart-selection section and the Day 1 and Day 5 communication segments in `PROGRAMME.md`. The teaching content sits in the participant handbook so it needs no new notebook.

### V2 — No structured briefing practice

Every day ends with "five groups report one finding". There is no taught structure for what a finding is. Participants who present badly on Day 1 will present badly on Day 5.

*Closed by:* the one-page briefing template (finding / evidence / limitation / next step / what would change my mind) in the handbook, introduced Day 1 and reused as the reporting format every day. Same time cost, visibly better output.

### R1 — No real data anywhere

*Recommended:* bundle one small real open dataset with a clear licence, used once, on Day 3 or in the capstone. Candidates that are small, licensed for reuse and free of personal data: a national statistics office monthly series, an open transport punctuality extract, or an open energy-demand series. It must be downloaded and committed before travel — do not plan to fetch it in the classroom.

*Effort:* half a day, including licence check and one lab rewrite. *Not implemented here* — the dataset choice should be made by the instructor, and an uncleared licence is worse than no real data.

### C1 — The final practical is 20 minutes

The brochure promises application to "real-world data analysis projects". A 20-minute written exercise at the end of Day 5 does not read as a project.

*Closed by:* `participant/CAPSTONE.md` — a thread that starts Day 1 and is worked in the existing reporting slots, so it consumes no extra timetable. Participants choose either their own work problem or a provided scenario.

### N1 — The brochure's NLP-to-time-series link is explicitly contradicted

The brochure says "Definition of Natural Language Processing (NLP) and its link to time series data". The Day 3 guide says: "Time series and NLP are separate applications today; neither depends on the other."

That is an honest statement about the current labs, but it contradicts a contracted line. It is also easy to fix truthfully, because the link is real: support messages arrive with timestamps, so message volume is a time series, category share moves over time, and a text-derived signal can become a feature in a forecast.

*Recommended:* a 10-minute bridging segment at the end of Day 3 Lab B using the existing 24 messages plus their arrival dates — count messages per day by category, plot the two series, and discuss when a text-derived feature legitimately enters a forecast and when it leaks. No new dependency, no new dataset.

*Effort:* two hours. *Not implemented here* — it needs a notebook cell and a validation run.

### B1 — Bayesian content never reaches a decision

Day 4 estimates a defect rate well. The brochure says "Bayesian modelling and inference for data-driven decisions", and the audience explicitly includes business leaders.

*Recommended:* extend Lab A by 10 minutes — given the posterior, compute the probability that the defect rate exceeds the contractual threshold, and state the action that probability triggers. Two lines of code on the existing posterior. This is the moment the Bayesian day pays for itself for a non-technical attendee.

*Effort:* one hour.

### A1 — No route through the course for a non-coding attendee

The brochure invites "Business Leaders & Decision Makers" and "Strategic Planners & Consultants". Every lab requires typing Python. Pairing helps, but a non-coder paired with a non-coder is a lost pair.

*Closed for no-code delivery by:* the self-contained five-day NO_CODE_WORKBOOK, separate facilitator answers and NO_CODE_DELIVERY schedule. Rotating keyboard roles alone did not close this gap. No participant depends on a coding partner. Share the revised outcomes with the organiser; coding implementation remains optional.

## Recommended additions to the syllabus

These go beyond the brochure. Each is proposed because a practitioner-level 2026 audience will notice its absence, not to pad the programme. The numbered time estimates total 180 minutes, excluding the capstone already scheduled. These are proposed additions, not extra blocks to stack onto the 300-minute day. The no-code route integrates selected topics into its existing activities.

| # | Addition | Day | Time | Why it earns its place |
|---|---|---|---|---|
| 1 | **Chart choice and chart repair** — pick the right form, then fix three bad charts | 1 | 30 min | Delivers the "Visualisation" half of the course category. Provides explicit practice matching charts to questions. |
| 2 | **The one-page briefing** — finding, evidence, limitation, next step | 1 | 15 min | Turns five days of group reporting into deliberate practice. Reused daily at no extra cost. |
| 3 | **Permutation importance and partial dependence** — what the model used, and how | 2 | 30 min | "Why did it predict that?" is the first question any stakeholder asks. Its absence is conspicuous at practitioner level. |
| 4 | **Rolling-origin backtesting** | 3 | 25 min | The Day 3 guide already says real deployment needs multiple rolling origins, then evaluates on one window. Closing that loop is the single most useful forecasting skill here. |
| 5 | **Text-to-time-series bridge** (gap N1) | 3 | 10 min | Delivers a contracted brochure line. |
| 6 | **Posterior to decision** (gap B1) | 4 | 10 min | Delivers a contracted brochure line for the non-technical audience. |
| 7 | **Synthetic data, privacy and governance** | 4 | 20 min | The course generates synthetic data all week without once discussing why organisations do it. Relevant to both Saudi PDPL and EU GDPR contexts. A differentiator, and cheap. |
| 8 | **Where LLMs and embeddings fit** — conceptual, no API, no download | 3 or 5 | 20 min | An audience booking an advanced analytics course in 2026 that hears nothing about language models will record that as a gap, fairly or not. Frame it as: what changes, what does not, and why evaluation discipline matters more rather than less. |
| 9 | **From notebook to production** — monitoring, drift, retraining, ownership | 5 | 20 min | The final practical asks participants to rebut "we are ready for production" without anyone having defined production readiness. |
| 10 | **Bring your own problem clinic** | 5 | in capstone slot | The segment senior attendees remember. Costs no new timetable — it is the capstone reporting slot. |

Ethics and bias are deliberately not a separate block. They are more credible distributed through the existing material: the leakage discussion on Day 2, the representativeness limitation on Day 3, the prior-choice discussion on Day 4, and the governance segment on Day 4.

## Implementation backlog, in priority order

| Priority | Item | Effort | State |
|---|---|---|---|
| 1 | Participant handbook, cheat sheets, packs, evaluation | — | **Done in this change** |
| 2 | Instructor runbook, question bank, Spanish orientation | — | **Done in this change** |
| 3 | Generated slide decks from the five existing plans | — | **Done in this change** (`scripts/build_slide_decks.py`) — covers Day 4, which Canva does not |
| 4 | Additions 4 and 5 — backtesting and the text-to-series bridge (Day 3) | 1 day | Specified |
| 5 | Addition 3 — explainability (Day 2) | 0.5 day | Specified |
| 6 | Additions 6 and 7 — decision and governance (Day 4) | 0.5 day | Specified |
| 7 | Addition 9 — production readiness (Day 5) | 0.5 day | Specified |
| 8 | R1 — one licensed real dataset | 0.5 day | Specified, needs instructor decision |
| 9 | Addition 8 — LLM and embedding segment | 0.5 day | Specified |
| 10 | Day 4 Canva design, and a slide-by-slide review of all decks against the plans | 1 day | Open — Days 1, 3 and 5 do not match their plans' slide counts, and Day 2 still carries template text |

## Open questions for the organiser

Ask these before finalising the programme. Several were already listed in `instructor/PREPARATION_PLAN.md`; the ones marked new arise from this review.

1. Contact hours: 22.5 teaching hours plus breaks, or 25 hours excluding breaks?
2. Interpretation mode: consecutive or simultaneous? The whole timetable depends on this.
3. Technical split of the cohort: how many attendees write code today? *(new — drives gap A1)*
4. Laptops: participant-owned or venue-supplied? Do they have installation rights? Is there a corporate proxy?
5. Printing: will the venue print 20 handbooks, or do we bring them? *(new)*
6. Does LPC require its own slide template, cover and certificate? *(new — affects the generated decks)*
7. Is a certificate of attendance expected, and who issues it? *(new)*
8. May participants bring their own work data to the capstone, and under what confidentiality terms? *(new — affects gap C1)*
9. Is a post-course report to the organiser expected?
