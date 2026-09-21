# Day 2: Machine Learning

## Presentation brief

16:9 professional training deck. All text English. White or warm-white background, dark navy text, teal accent. Large readable type (titles about 36pt, body at least 24pt), ample whitespace, one idea per slide. No decorative stock photos, invented logos, or generic AI imagery. Use editable charts, tables and conceptual diagrams where specified. Exact numeric values must remain unchanged. Label synthetic results clearly. Never invent data series to draw an empirical chart. Keep detailed explanations in speaker notes. Audience: 20 participants from Saudi Arabia attending in Genoa, English delivery with Arabic interpretation. No cultural stereotypes. Preserve short task instructions and notebook paths. Include pause-for-interpretation guidance in notes rather than on every slide.

## Narrative arc

Introduce the question and essential concepts, demonstrate a working example, run pair activities, interpret evidence and close with a short review. The deck supports the five-hour timetable, including two 15-minute breaks and interpretation time.

## Slide 1: Machine Learning

Visible copy:
Day 2
Prediction and evaluation

Visual: Minimal typographic cover

Speaker notes: Connect the session to yesterday’s data-quality decisions. Allow interpretation before introducing model vocabulary.

## Slide 2: The route prediction problem

Visible copy:
Predict duration before departure
Inputs: planned distance and stops
Outcome: actual duration

Visual: Editable input/outcome comparison

Speaker notes: Every feature must exist when the prediction is made. Actual arrival time would leak the outcome.

## Slide 3: Learning tasks

Visible copy:
Regression predicts a number
Classification predicts a category
Clustering groups similar cases

Visual: Three-row comparison table with operational examples

Speaker notes: Use duration, delayed status and route groups as examples. Keep classification and clustering clearly distinct.

## Slide 4: Training, validation and test

Visible copy:
400 synthetic routes
300 training rows
100 final-test rows
Cross-validation uses training rows only

Visual: Editable split diagram with 300/100 labels

Speaker notes: The random split is suitable for these independent synthetic examples. Real chronological or grouped data may require different splits.

## Slide 5: Preprocessing inside a pipeline

Visible copy:
Training folds determine imputation
Validation folds receive the fitted transformation
The final test stays separate

Visual: Compact editable pipeline diagram

Speaker notes: Explain fit versus transform. Fitting preprocessing on the entire table allows held-out information to influence development.

## Slide 6: Mean absolute error

Visible copy:
Absolute errors: 5, 10, 15 minutes
MAE: 10 minutes
Each prediction can have a different error

Visual: Editable calculation using three values

Speaker notes: MAE is an average in target units. It is not a guarantee that every future error is within the average.

## Slide 7: Lab A: Regression and baseline

Visible copy:
40 minutes
Open day-02-machine-learning/student.ipynb
Run sections 1–2
Explain both MAEs

Visual: Large task instructions

Speaker notes: Pairs reproduce the evaluation rather than typing a model from scratch. Ask why a simple baseline is necessary.

## Slide 8: Regression results

Visible copy:
Baseline MAE: 24.34 minutes
Model MAE: 8.43 minutes
Synthetic final-test data

Visual: Editable two-bar chart with a zero baseline and minute units

Speaker notes: The model improves this specific evaluation. Do not generalise its error rate to actual delivery operations.

## Slide 9: Break

Visible copy:
15 minutes

Visual: Plain break slide

Speaker notes: State the return time. Next we classify delays.

## Slide 10: Classification errors

Visible copy:
Rows: actual class
Columns: predicted class
Class 1 means delayed

Visual: Editable confusion matrix [[55,2],[9,34]] with clear row/column labels

Speaker notes: Explain all four cells. There are 9 missed delays and 2 false alarms in the recorded run.

## Slide 11: Precision and recall

Visible copy:
Precision: 34 / 36 = 94.4%
Recall: 34 / 43 = 79.1%
Different errors carry different costs

Visual: Two simple fraction calculations

Speaker notes: These figures refer to the delayed class in the synthetic test. Accuracy alone can conceal missed delays.

## Slide 12: Trees and random forests

Visible copy:
A tree uses successive decisions
Depth controls complexity
A forest combines randomised trees

Visual: Editable conceptual tree with clearly illustrative labels

Speaker notes: A more complex model can fit noise. Forests do not guarantee better results on every task.

## Slide 13: Validation and hyperparameters

Visible copy:
Compare candidates on training folds
Tune a small parameter grid
Select before final testing

Visual: Short ordered list

Speaker notes: The notebook compares logistic regression, a tree and forests. The best validation score can be optimistic because it supports selection.

## Slide 14: Lab B: Error interpretation

Visible copy:
45 minutes
Run section 3
Read the confusion matrix
Explain the cost of a missed delay

Visual: Task slide with the relevant notebook section

Speaker notes: Ask learners to distinguish model selection from final evaluation. Keep threshold experiments off the final test set.

## Slide 15: Break

Visible copy:
15 minutes

Visual: Plain break slide

Speaker notes: Give the return time. The final block explores groups and dimensionality.

## Slide 16: Clustering and scaling

Visible copy:
K-means groups observations by distance
Feature units affect distance
k = 3 is a demonstration choice

Visual: Illustrative cluster plot labelled conceptual

Speaker notes: No target labels define these groups. Business meaning requires further validation.

## Slide 17: Principal component analysis

Visible copy:
PCA summarises directions of variation
One component retains 53.1% in this example
Retained variation differs from predictive accuracy

Visual: Editable two-part bar: 53.1% retained, 46.9% omitted

Speaker notes: The values apply to the standardised synthetic training features. Explain the loss of information when compressing two dimensions to one.

## Slide 18: Pair challenge: Model comparison

Visible copy:
50 minutes
Explore clustering and PCA
Compare tree depths on training folds
Report one result and one limitation

Visual: Numbered instructions

Speaker notes: Use the worked solution when a pair is blocked. Include the short clustering/PCA walkthrough within this block.

## Slide 19: Day 2 review

Visible copy:
Which inputs leak the outcome?
Why keep the test separate?
Which error matters most to the decision?

Visual: Three discussion questions

Speaker notes: Use the answer key to correct misunderstandings. Link tomorrow’s chronological split to today’s evaluation principles.
