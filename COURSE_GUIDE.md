# Course guide

**Default delivery:** the coding route at working-analyst level, per [the programme](PROGRAMME.md) and [the day-of runbook](instructor/RUNBOOK.md). [The no-code route](instructor/NO_CODE_DELIVERY.md), with its [participant workbook](participant/NO_CODE_WORKBOOK.md) and [facilitator answers](instructor/NO_CODE_ANSWER_KEY.md), remains available as a fallback for individual non-coders, environment failure, or a cohort that contradicts the briefing.

## Delivery context

20 participants from Saudi Arabia, attending in person in Genoa. English instruction with Arabic interpretation. **Confirmed:** Ministry of Interior personnel who work with Python, at working-analyst rather than beginner level, and not IT professionals; they have asked to learn how this work is done in Europe. Interpretation mode remains unconfirmed. Start with [classroom and interpreter guidance](instructor/CLASSROOM_AND_INTERPRETER.md); the schedule assumes consecutive interpretation until confirmed.

## Start here

1. Read [the audience fit review](instructor/AUDIENCE_FIT_REVIEW.md) — what the confirmed cohort changed, and what is still open.
2. Read [the Spanish quick guide](instructor/GUIA_RAPIDA_ES.md) for how this repository is organised and what to decide first.
3. Read [the preparation plan](instructor/PREPARATION_PLAN.md) and [the European practice material](european-practice/), which is new and needs rehearsal.
4. Follow [environment setup](SETUP.md) and run [your first model](instructor/first_model.ipynb).
5. Rehearse [Day 1](day-01-eda/TEACHING_GUIDE.md) with [the domain mapping](instructor/DOMAIN_MAPPING.md) beside you, then run the worked notebook and student exercises.
6. Send [the pre-course pack](participant/PRE_COURSE_PACK.md) and [the diagnostic](assessments/ENTRY_DIAGNOSTIC.md) as early as possible, and read the returns before finalising Day 1.
7. Keep [the day-of runbook](instructor/RUNBOOK.md) and [the question bank](instructor/QUESTION_BANK.md) to hand while teaching.
8. Have [the no-code route](instructor/NO_CODE_DELIVERY.md) prepared as the fallback, not the plan.

## Scope and status

The supplied outline covers EDA, machine learning, time series, NLP, Bayesian inference, generative models, and big data. This is a broad syllabus. The plan below is a proposed introductory delivery depth, subject to agreement with the organiser; it does not replace a contracted advanced course without that agreement.

[CURRICULUM_REVIEW.md](CURRICULUM_REVIEW.md) maps every line of the brochure to the material that delivers it, records the two genuine gaps (no real dataset, and visualisation taught only implicitly before this revision), and specifies ten recommended additions with their time cost. [PROGRAMME.md](PROGRAMME.md) is the version to send to the organiser.

| Day | Topics | Current materials |
|---|---|---|
| 1 | Python, EDA, visualisation, descriptive statistics, correlation, outliers | Teaching guide, timed task cards, student notebook, worked notebook, dataset and answer key |
| 2 | Regression, classification, trees, forests, clustering, PCA, validation and tuning | Guide, tasks, worked/student/solution notebooks, answer key and results |
| 3 | Time series, decomposition, seasonality, ARIMA; separate NLP activity | Guide, tasks, worked/student/solution notebooks, answer key and results |
| 4 | Bayes, distributions, posterior inference, MCMC, generative models | Guide, tasks, worked/student/solution notebooks, answer key and results |
| 5 | Distributed computing, Hadoop/MapReduce, Spark/SQL/MLlib, deep learning, GANs | Guide, tasks, worked/student/solution notebooks, answer key and results |

Days 2–5 now include runnable labs, detailed instructor explanations, pair task cards, exercise solutions and exit questions with answers. Day 5 also has a separate Spark lab and an offline fallback. The final practical assessment and rubric are in assessments/. The worked/solution code has been executed locally; see KERNEL_VALIDATION.md for execution results and the remaining Jupyter startup check. Classroom timing and the actual learner environments remain unverified.

Participant-facing material is in [participant/](participant/): a printable handbook, two reference cards, a draft English–Arabic glossary, the week-long capstone brief, pre- and post-course packs, the course evaluation and an exit self-assessment. Build it with `python scripts/build_participant_handbook.py`.

Canva designs exist for Days 1, 2, 3 and 5; Day 4 does not have one yet, and three of the four do not match their plans' slide counts. `python scripts/build_slide_decks.py` generates plain PowerPoint decks for all five days from the same plans, which cover the Day 4 gap, work offline, and give the Canva review pass something to check against. Both routes are indexed in [presentations/README.md](presentations/README.md).

## Timing assumption

Each day occupies 300 minutes, including two 15-minute breaks: 270 minutes of teaching and activities, or 22.5 contact hours across the course. If the contract requires 25 contact hours, add 30 teaching minutes per day and schedule breaks outside those hours. Confirm this before finalising the timetable.

## Delivery principles

- Run every example before teaching it and save a local copy of the repository.
- Use synthetic data for exercises; results illustrate methods, not real business evidence.
- Basic task first; extension task for faster participants. Pair stronger programmers with beginners only with both participants' agreement.
- Record unanswered questions and verify them later. Do not invent an explanation.
- If the cohort is already advanced, escalate the mismatch before delivery; introductory notes are insufficient.

## Official references

- [pandas introductory tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html): loading, selecting, plotting and summarising tables.
- [scikit-learn common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html): split before fitting preprocessing, prevent leakage and use pipelines.

These links are supporting documentation, not required reading in full before Day 1.
