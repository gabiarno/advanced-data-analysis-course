# Seven-day instructor preparation plan

Assumption: 5–6 hours of preparation each day. This availability is not confirmed. If fewer hours are available, prioritise the core demonstrations and request help with advanced sessions. One week does not establish advanced expertise.

## Delivery adaptation

Read CLASSROOM_AND_INTERPRETER.md and rehearse with pauses for Arabic interpretation. Use INTERPRETER_GLOSSARY.md for the pre-course briefing. The cohort has 20 participants; plan 10 working pairs and five reporting groups. Keep every code demonstration short enough to repeat after interpretation.

## Before studying

Ask the organiser for: contact hours versus breaks; audience roles and prerequisites; class size; learner computers and installation rights; internet access; official slides/labs; assessment requirements; and the expected technical depth. Offer the entry diagnostic before the course. Agree any change in scope explicitly.

## Daily preparation

| Preparation day | Study and practice | Evidence of readiness |
|---|---|---|
| 1 | 1h setup; 2h Day 1 worked notebook; 1h student tasks; 1h teach-back | Explain every cleaning choice and interpret each chart without reading notes. |
| 2 | 1h train/test concepts; 2h first-model notebook; 1h metrics and baselines; 1h rehearsal | Explain X, y, fit, predict, MAE, baseline and leakage. |
| 3 | 2h classification/trees/forests; 1h cross-validation/tuning; 1h clustering/PCA; 1h rehearsal | Distinguish supervised and unsupervised tasks, training error and validation error. Full labs pending. |
| 4 | 2h series and temporal validation; 1h ARIMA; 1h NLP; 1h rehearsal | Explain why future observations cannot enter past training data. Full labs pending. |
| 5 | 2h Bayesian example; 1h MCMC intuition; 1h generative-data discussion; 1h rehearsal | Explain prior, likelihood and posterior; identify limits of a small demonstration. Full labs pending. |
| 6 | 2h Spark setup and SQL; 1h distributed-computing concepts; 1h neural networks/GANs; 1h rehearsal | Run the planned Spark demo and explain why a local demo is not a performance benchmark. Full labs pending. |
| 7 | 2h all-lab run; 2h difficult explanations; 1h timing and fallback check | All labs run from clean kernels; limitations and unanswered questions documented. |

## First-model vocabulary

- **Observation:** one row or case.
- **Feature (X):** information available when making a prediction.
- **Target (y):** the outcome we want to predict.
- **Training:** estimating a model from examples.
- **Prediction:** applying the fitted model to an input.
- **Test set:** held-out examples used for final evaluation, not repeated model selection.
- **Baseline:** a simple reference method, such as always predicting the training mean.
- **MAE:** average absolute prediction error, in the target's units.
- **Overfitting:** learning patterns that do not generalise to new observations.
- **Leakage:** using information during modelling that would not legitimately be available.

## Teaching language

Opening: “Our goal is to connect each method to a question, an evaluation strategy and a limitation.”

Before code: “What do you expect this operation to change? What should stay the same?”

When uncertain: “I want to verify that detail rather than give you an inaccurate answer. I will record the question and follow up.”

When a demo fails: “Let us inspect the saved output and the reasoning, then isolate the environment issue.”

Before progressing: ask learners to explain one result in plain language. Silence is not evidence of understanding.

## Readiness gate

Do not call a session ready until you can run it from a clean environment, explain its assumptions, answer its exercise questions, and recover using saved results. If the advanced sessions fail this gate, seek a co-instructor or agree a narrower scope with the organiser.
