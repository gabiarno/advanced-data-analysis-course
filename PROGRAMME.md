# Advanced Data Analysis | A practical workshop

## Make the next decision better

You already work with data and use Python. This week gives you room to take the next step: test more demanding methods, question promising results and turn the evidence into a recommendation someone can use.

We will work as a small analysis team. Expect short explanations, prepared notebooks, experiments with selected parameters and plenty of discussion. You do not need to be a software developer. You do need to be willing to explain why you trust an answer.

The group consists of 20 participants from Saudi Arabia's Ministry of Interior, meeting in Genoa. Teaching is in English with Arabic interpretation. Public-service examples concern appointment capacity, facilities maintenance, processing times and request routing. Existing numerical notebooks retain their clearly labelled synthetic retail, logistics and service examples.

## What we will work on

| Day | Our question | What we will do | What you will leave with |
|---|---|---|---|
| 1 | Can we trust this report? | Audit data in Python, make a fair comparison and improve a chart | A documented audit and a short management briefing |
| 2 | Is the prediction useful? | Compare regression and classification with baselines, explore validation and error costs, discuss clustering/PCA | A model-selection argument with clear limitations |
| 3 | What could we know at the time? | Compare forecasts, respect time order, classify text and investigate ambiguity | An evaluation design and a human-review rule |
| 4 | Can we act under uncertainty? | Update a probability, inspect MCMC and critique generated data | A recommendation linking probability, assumptions and action |
| 5 | What would a pilot need? | Explore partitioned aggregation and Spark, compare advanced models and present proposals | A one-page pilot proposal with an owner and stop condition |

The governance thread described below runs through all five days, attached to the analytical activity of each one.

The advanced ideas stay in the course: trees and forests, tuning, dimensionality reduction, ARIMA, Bayesian inference, MCMC, Spark/MLlib, neural networks and a toy adversarial generator. We teach them through prepared examples and analytical decisions. This is broad practical coverage, not specialist mastery of every method or distributed production engineering.

## How the room will work

Ten pairs work at laptops. One person operates while the other checks and explains; swap at a useful checkpoint. Two pairs form each reporting group. Faster pairs take an extension; everyone is responsible for the interpretation.

The core route uses Python. Saved outputs and the paper workbook keep the analysis moving if an environment fails. There is no need to turn a classroom problem into a long live debugging session.

Each day lasts 300 minutes including two 15-minute breaks. Workshops A/B/C occupy 50/50/60 minutes, with 20 additional minutes for peer review: 180 protected practical minutes. Short demonstrations total 30 minutes including interpretation. The remaining 60 minutes cover warm-up, debrief, reporting and exit work. All timings include interpretation. Follow the exact schedule in the activity cards.

Day 5 uses Workshop C for 20 minutes of final preparation,35 for five interpreted presentations and 5 for peer feedback. Minutes 270–290 are the individual practical; 290–300 are feedback and closing. Each participant keeps an individual written proposal.

This provides 22.5 contact hours across the week. If 25 are required, place breaks outside five teaching hours and extend the practice blocks by 30 minutes daily.

## What good work looks like

You can explain the data-quality decisions, select a method for a specific question, compare with a baseline, avoid leakage, interpret uncertainty and describe a sensible next action. You can also recognise what the evidence does not establish.

The entry discussion helps us adjust the support. Daily individual exit answers and the final practical check judgement rather than memorised syntax. The capstone develops across the week: decision, method, data, evaluation, limitation and next step. Assessment is formative; the course is not an accredited competency certification.

## What makes the workshop worth your time

The value is practical: try a technique, change an assumption, compare results and defend an action. The venue does not make these methods uniquely European. Local examples can be used if helpful, but geography is not a teaching objective.

## How this work is governed in Europe

There is one sense in which "how it is done in Europe" has real content, and it is not the examples. A baseline is a baseline anywhere. What genuinely differs is the governance around public-sector analysis, and for people who work in a ministry that is substantive rather than decorative.

We cover four things, alongside the practical work rather than as a separate lecture:

- **Which rules apply to which processing.** General data protection is not the whole picture; processing for criminal-justice purposes sits under a separate regime, and AI systems are treated by risk tier. Several uses relevant to an interior ministry are named explicitly, and a few are not permitted at all.
- **The principles that shape a project's design.** Purpose stated before collection, minimisation, necessity and proportionality, and being able to explain a decision to the person it was made about. These constrain what you build more than any single article does.
- **Two European failures.** A Dutch fraud-scoring system stopped by a court in 2020, and a benefits risk model that wrongly accused tens of thousands of families and brought down a government in 2021. Both are studied for what went wrong analytically, not as compliance anecdotes.
- **One distinction worth carrying home.** European practice treats allocating resources very differently from scoring individuals, even where the statistics are nearly identical. Forecasting how many calls arrive on Friday is planning. Scoring which residents will offend is not.

This is a framework and its reasoning, not legal advice and not a description of your own national law. The tutor is not a lawyer and says so on the first morning. What transfers to your context is your judgement.

The material is in [european-practice/](european-practice/) for the tutor and [the participant reference](participant/EUROPEAN_PRACTICE.md) for the room. It replaces syntax teaching this group does not need rather than extending the timetable.

Five additional executable experiments address case-mix reversal, validation-based cost thresholds, rolling-origin backtesting, sensitivity of Bayesian decisions and monitoring triggers. Synthetic cases are sufficient for these objectives; a real-data case is optional, not a missing requirement for this delivery.

Use [the activity cards](workshops/ACTIVITY_CARDS.md) for fifteen varied workshops and [the experiment notebook](workshops/experiments.ipynb) for the additional techniques. They replace parts of existing labs rather than extending the timetable.

## Before the first morning

Bring a tested Python environment or arrange to share one. Bring a generalised analytical problem rather than confidential records. The tutor has worked examples and recorded results available as a fallback. Confirm interpretation mode and rehearse the pace.

Read the [participant handbook](participant/HANDBOOK.md), [illustrated PDF](dist/participant-handbook.pdf), [tutor script](instructor/TUTOR_SCRIPT.md) and [activity cards](workshops/ACTIVITY_CARDS.md). Existing slide files still need their separate visual review.
