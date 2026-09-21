# Advanced Data Analysis Techniques

**Default delivery while technical level is unknown:** use [the no-code delivery guide](instructor/NO_CODE_DELIVERY.md), [participant workbook](participant/NO_CODE_WORKBOOK.md) and [facilitator answers](instructor/NO_CODE_ANSWER_KEY.md). The five-day core can be completed on paper; notebooks are optional extensions.

English course materials for five days of in-person delivery in Genoa: 20 participants, with Arabic interpretation.

**Confirmed cohort:** Ministry of Interior personnel, Saudi Arabia. They work with Python and are not beginners; they are domain and decision-making staff rather than IT professionals, and they asked to learn how this work is done in Europe. The materials are pitched, framed and sequenced for that profile — see [the audience fit review](instructor/AUDIENCE_FIT_REVIEW.md).

## Start here

**Delivering the course?** Read [the Spanish quick guide](instructor/GUIA_RAPIDA_ES.md) — it explains how everything here is organised, in what order to use it, and what to decide first. Then work through [the seven-day preparation plan](instructor/PREPARATION_PLAN.md).

**Presenting to the organiser?** Send [the programme](PROGRAMME.md), and use the traceability table in [the curriculum review](CURRICULUM_REVIEW.md) to show the contracted outline is covered.

**Preparing the room?** [Classroom and interpreter guidance](instructor/CLASSROOM_AND_INTERPRETER.md), then [the day-of runbook](instructor/RUNBOOK.md).

**Setting up optional Python demonstrations?** [Environment setup](SETUP.md), then [your first model](instructor/first_model.ipynb).

**Building the slides?** [The presentation index](presentations/README.md) lists the Canva designs for Days 1, 2, 3 and 5, the generated decks for all five days, and what still needs reviewing.

## What is here

| | |
|---|---|
| [PROGRAMME.md](PROGRAMME.md) | The client-facing programme: outcomes, daily content, assessment, requirements |
| [CURRICULUM_REVIEW.md](CURRICULUM_REVIEW.md) | Brochure promises against delivered material; gaps, additions and the open questions for the organiser |
| [COURSE_GUIDE.md](COURSE_GUIDE.md) | Material status and delivery principles |
| [european-practice/](european-practice/) | GDPR, the Law Enforcement Directive, the AI Act; European case studies; daily integration |
| [instructor/](instructor/) | Audience fit review, domain mapping, day-of runbook, question bank, no-code fallback, Spanish orientation |
| [participant/](participant/) | Handbook, four reference cards, capstone, no-code workbook, pre- and post-course packs, evaluation forms |
| [day-01-eda/](day-01-eda/) … [day-05-big-data/](day-05-big-data/) | Teaching guides, task cards, notebooks, solutions and recorded results |
| [assessments/](assessments/) | Entry diagnostic, final practical and rubric |
| [presentations/](presentations/) | Five slide plans, the Canva design index and the deck review status |
| [dist/](dist/) | Generated deliverables: printable handbook and five slide decks |

## Presentations

[Open the Canva presentation index](presentations/README.md). Days 1, 2, 3 and 5 are linked. Day 4 is still pending. The index records remaining review issues and export status.

## Course map

| Day | Start here | Included |
|---|---|---|
| 1 | [EDA guide](day-01-eda/TEACHING_GUIDE.md) | Guide, tasks, student/worked notebooks and data |
| 2 | [Machine-learning guide](day-02-machine-learning/TEACHING_GUIDE.md) | Regression, classification, validation, trees/forests, clustering/PCA |
| 3 | [Time-series and NLP guide](day-03-time-series-nlp/TEACHING_GUIDE.md) | Baselines, decomposition, ARIMA and text classification |
| 4 | [Bayesian/generative guide](day-04-bayesian-generative/TEACHING_GUIDE.md) | Exact updating, MCMC, predictive simulation and synthetic data |
| 5 | [Big-data guide](day-05-big-data/TEACHING_GUIDE.md) | Spark SQL/MLlib, local neural network, toy GAN and fallback activity |

Days 1–5 each include a teaching guide, timed task cards, runnable student/worked notebooks, exercise solutions, an answer key with exit questions, and saved numerical results and figures. The [final practical assessment](assessments/FINAL_PRACTICAL.md) includes an [instructor rubric](assessments/FINAL_PRACTICAL_KEY.md).

## Producing the handouts

```bash
python -m pip install -r requirements-build.txt
python scripts/build_participant_handbook.py    # dist/participant-handbook.html
python scripts/build_slide_decks.py             # dist/slides/day-0N.pptx
```

The handbook is one self-contained file: print it to A4 double-sided, or send it as the online version. It works offline on any device. See [dist/README.md](dist/README.md).

## Status

[Execution evidence](KERNEL_VALIDATION.md) records successful code execution and the remaining Jupyter startup check. [Technical references](REFERENCES.md) support further preparation.

Still open: Day 4 has no Canva design, the Canva decks need their slide-by-slide review and three of them do not match their plans' slide counts, the generated decks need their visual placeholders replaced, the no-code route now includes text/time availability, posterior decisions, synthetic-data critique and production-readiness activities; advanced executable additions in [the curriculum review](CURRICULUM_REVIEW.md) remain a separate backlog, and no real dataset is included. Teaching and interpretation timing, audience fit, and classroom setup still require rehearsal.

The provisional schedule includes two 15-minute breaks within each five-hour day. Confirm whether the organiser instead requires five contact hours, excluding breaks. Technical level and interpretation mode are not yet confirmed. Advanced coverage requires an agreed scope and instructor rehearsal.

All practice data included here are synthetic. No participant information is required.
