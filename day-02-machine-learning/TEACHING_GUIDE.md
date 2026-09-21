# Day 2 — Machine learning for decisions

## Outcomes and preparation

Learners will distinguish regression, classification and clustering; evaluate a model against a baseline; read a confusion matrix; explain overfitting; and recognise why preprocessing belongs inside validation. Trees, forests, tuning and PCA receive guided coverage.

Before class, run instructor/first_model.ipynb and this day's worked notebook. Practise explaining `fit`, `predict`, `X`, `y`, training, validation and test. No new dataset download is required: the notebook generates 400 synthetic independent routes. Distance and planned stops are available before departure; duration and delayed status are outcomes.

## Timetable

| Minutes | Activity |
|---|---|
| 0–20 | Recap EDA; identify inputs and targets in the route example |
| 20–50 | Demonstrate split, baseline and regression, with interpretation |
| 50–90 | Lab A: reproduce the regression evaluation and explain MAE |
| 90–105 | Compare pair explanations and discuss leakage |
| 105–120 | Break |
| 120–150 | Demonstrate classification, confusion matrix and validation |
| 150–195 | Lab B: compare candidate validation results and interpret errors |
| 195–210 | Break |
| 210–260 | Lab C: 10-minute clustering/PCA walkthrough, then guided exploration and reporting preparation |
| 260–285 | Five groups give one finding and one limitation |
| 285–300 | Exit questions and recap |

## Instructor explanations

### 1. Start with a question

Say: “We want to estimate travel duration before dispatch. What information exists at that moment?” Accept planned distance and stops. Reject actual arrival time and measured duration as inputs. Pause for interpretation.

Regression predicts a number, classification predicts a category, and clustering groups similar observations without target labels. The same operational setting can support different questions. Here delayed means duration above 85 minutes; it is a teaching threshold, not an industry standard.

Ask: “Can we use duration to predict whether duration exceeds 85?” Answer: the relationship is mechanically known after the event, but using it for a pre-dispatch prediction leaks the outcome.

### 2. Explain the split before the algorithm

Hold out 100 routes; use 300 for learning and validation. Cross-validation partitions only those 300, repeatedly fitting on some folds and evaluating on another. A final held-out test serves a different purpose. If we repeatedly change the model after inspecting test scores, that test becomes part of development.

The imputer is inside the pipeline so each validation fold uses a median learned from its training portion. Filling from all rows before splitting would allow held-out information to influence training. A fixed random seed makes the demonstration repeatable; it does not make a flawed evaluation correct.

### 3. Make MAE concrete

If three predictions have absolute errors 5, 10 and 15 minutes, MAE is 10 minutes. Errors do not cancel because we take absolute values. It is an average, not a promise that every prediction is within 10 minutes. A baseline tells us whether the model adds value over a simple rule. Production value also depends on error costs and representativeness.

### 4. Read a confusion matrix aloud

Rows are actual classes and columns predicted classes, ordered [0,1]. Top left: correctly identified not delayed. Top right: false alarm. Bottom left: missed delay. Bottom right: correctly identified delay. Precision asks how many alerts are correct; recall asks how many actual delays were detected. F1 balances precision and recall but does not encode all business costs.

Ask: “If a missed delay costs more than a false alarm, is accuracy enough?” Expected: no; inspect recall, error counts and costs. Any threshold choice must use development data, not the final test.

### 5. Trees, forests and tuning

A tree makes successive feature-based decisions. More depth allows more detailed patterns, including noise. A forest averages many randomised trees to reduce some instability; it is not guaranteed to win. A hyperparameter such as maximum depth is a setting chosen outside fitted split thresholds. Grid search compares a short list on training folds. Its best validation score is a selection statistic and may be optimistic; the final test remains separate.

The example selects among logistic regression, a tree, a forest and a tuned forest on validation F1 before final testing. It does not prove one family is generally superior.

### 6. Clustering and PCA

K-means assigns points to centres; choosing k=3 does not discover three true customer types. Scaling matters because distance-based methods depend on units. PCA finds directions of variation; retaining one component from two loses information. Explain the reported variance ratio as retained variation, not predictive accuracy.

## Common questions and recovery

“Why not use all rows for training?” We need an honest evaluation of generalisation. Later deployment training may use more data after evaluation choices are fixed.

“Why does cross-validation show negative MAE?” The software maximises scores; the notebook reverses the sign for readability.

“Why do results change with a seed?” Samples, folds and randomised models vary. A fixed seed supports teaching, not proof of robustness.

If a learner cannot finish tuning, use the saved validation table and ask them to select a model using only that table. If explanations take longer, use a live walk-through of PCA rather than requiring independent implementation.

## Classroom routine

20 participants, 10 pairs, five groups for reporting. Swap keyboard and explanation roles every 10–15 minutes. Explain one idea, pause for Arabic interpretation, demonstrate a few lines, then let pairs repeat. All written materials are English. Confirm that participants can use English task cards or arrange interpreter-reviewed support.

Each timetable totals 300 minutes including two 15-minute breaks. There are 135 minutes of protected practice. For 300 contact minutes, add 30 minutes of supported practice and put breaks outside those hours. Confirm the contractual interpretation.

Use worked.ipynb for rehearsal; student.ipynb contains the same runnable examples plus challenges. Beginners change and interpret working code rather than typing everything from scratch. Stronger participants use the extensions. Read worked_RESULTS.md for verified outputs and open the executed notebook for saved numerical results. Figures are in figures/.

Do not rush through every line. The goal is for each pair to explain a result, a limitation and a next step. If the interpreter needs more time, reduce extension work, not the foundational lab or break.
