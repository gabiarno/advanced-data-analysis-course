# Course guide

## Delivery context

20 participants from Saudi Arabia, attending in person in Genoa. English instruction with Arabic interpretation. Technical level and interpretation mode remain unconfirmed. Start with [classroom and interpreter guidance](instructor/CLASSROOM_AND_INTERPRETER.md); the schedule assumes consecutive interpretation until confirmed.

## Start here

1. Read [the preparation plan](instructor/PREPARATION_PLAN.md).
2. Follow [environment setup](SETUP.md).
3. Run [your first model](instructor/first_model.ipynb).
4. Rehearse [Day 1](day-01-eda/TEACHING_GUIDE.md), then run the worked notebook and student exercises.
5. Use [the diagnostic](assessments/ENTRY_DIAGNOSTIC.md) to check prerequisites before delivery.

## Scope and status

The supplied outline covers EDA, machine learning, time series, NLP, Bayesian inference, generative models, and big data. This is a broad syllabus. The plan below is a proposed introductory delivery depth, subject to agreement with the organiser; it does not replace a contracted advanced course without that agreement.

| Day | Topics | Current materials |
|---|---|---|
| 1 | Python, EDA, visualisation, descriptive statistics, correlation, outliers | Teaching guide, timed task cards, student notebook, worked notebook, dataset and answer key |
| 2 | Regression, classification, trees, forests, clustering, PCA, validation and tuning | Guide, tasks, worked/student/solution notebooks, answer key and results |
| 3 | Time series, decomposition, seasonality, ARIMA; separate NLP activity | Guide, tasks, worked/student/solution notebooks, answer key and results |
| 4 | Bayes, distributions, posterior inference, MCMC, generative models | Guide, tasks, worked/student/solution notebooks, answer key and results |
| 5 | Distributed computing, Hadoop/MapReduce, Spark/SQL/MLlib, deep learning, GANs | Guide, tasks, worked/student/solution notebooks, answer key and results |

Days 2–5 now include runnable labs, detailed instructor explanations, pair task cards, exercise solutions and exit questions with answers. Day 5 also has a separate Spark lab and an offline fallback. The final practical assessment and rubric are in assessments/. Slide decks are still pending. The worked/solution code has been executed locally; see KERNEL_VALIDATION.md for execution results and the remaining Jupyter startup check. Classroom timing and the actual learner environments remain unverified.

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
