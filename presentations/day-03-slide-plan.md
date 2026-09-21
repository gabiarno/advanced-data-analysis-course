# Day 3: Time Series and Text Analysis

## Presentation brief

16:9 professional training deck. All text English. White or warm-white background, dark navy text, teal accent. Large readable type (titles about 36pt, body at least 24pt), ample whitespace, one idea per slide. No decorative stock photos, invented logos, or generic AI imagery. Use editable charts, tables and conceptual diagrams where specified. Exact numeric values must remain unchanged. Label synthetic results clearly. Never invent data series to draw an empirical chart. Keep detailed explanations in speaker notes. Audience: 20 participants from Saudi Arabia attending in Genoa, English delivery with Arabic interpretation. No cultural stereotypes. Preserve short task instructions and notebook paths. Include pause-for-interpretation guidance in notes rather than on every slide.

## Narrative arc

Introduce the question and essential concepts, demonstrate a working example, run pair activities, interpret evidence and close with a short review. The deck supports the five-hour timetable, including two 15-minute breaks and interpretation time.

## Slide 1: Time Series and Text Analysis

Visible copy:
Day 3
Two practical applications

Visual: Minimal typographic cover

Speaker notes: Explain that forecasting and NLP are separate applications today. Both require appropriate evaluation.

## Slide 2: Time order and forecasting

Visible copy:
210 daily observations
182 training observations
28 final-test observations

Visual: Editable chronological split diagram

Speaker notes: All observations are synthetic. Training ends 1 July 2026 and the test begins 2 July 2026.

## Slide 3: Trend and seasonality

Visible copy:
Trend describes sustained movement
Seasonality repeats at a known interval
This example has a seven-day pattern

Visual: Illustrative trend and seasonal sketch labelled conceptual

Speaker notes: The seven-day pattern comes from the teaching generator. A lag correlation alone does not prove seasonality.

## Slide 4: Forecast baselines

Visible copy:
Last-value forecast repeats the latest value
Weekly-repeat forecast repeats the last seven values

Visual: Editable comparison table

Speaker notes: Both methods use only training observations. A simple baseline can be competitive.

## Slide 5: ARIMA components

Visible copy:
p: autoregressive terms
d: differencing
q: moving-average error terms

Visual: Large plain-language labels

Speaker notes: The fixed ARIMA(1,1,1) is a demonstration, not a tuned optimum. It does not explicitly model weekly seasonality.

## Slide 6: Lab A: Forecast evaluation

Visible copy:
40 minutes
Open day-03-time-series-nlp/student.ipynb
Run sections 1–3
Compare three predeclared forecasts

Visual: Task slide

Speaker notes: Mark the training/test boundary before executing models. Use saved results if statsmodels setup is unavailable.

## Slide 7: Forecast errors in the example

Visible copy:
Last value: 22.38
Weekly repeat: 5.53
ARIMA: 22.11
MAE in demand units

Visual: Editable bar chart with exact values

Speaker notes: The weekly baseline wins on this one synthetic test window. This illustrates why complexity does not guarantee a better forecast.

## Slide 8: Forecast uncertainty

Visible copy:
Intervals depend on model assumptions
One test window gives limited evidence
Future observations remain unavailable during fitting

Visual: Short text beside an illustrative interval labelled conceptual

Speaker notes: Avoid calling a model interval a guarantee. Real work should evaluate multiple rolling origins and monitor changes.

## Slide 9: Break

Visible copy:
15 minutes

Visual: Plain break slide

Speaker notes: State the return time. The next block is a separate text-classification application.

## Slide 10: Message categorisation

Visible copy:
Categories: delivery and billing
16 training messages
8 authored test messages

Visual: Editable table with one delivery and one billing example

Speaker notes: These are English toy messages. The task is topic categorisation rather than sentiment analysis.

## Slide 11: Text representation

Visible copy:
TF-IDF converts text into numeric features
Logistic regression learns category associations
Training text defines the vocabulary

Visual: Compact editable process diagram

Speaker notes: The vectoriser belongs inside the training pipeline. The model does not understand sentences in the human sense.

## Slide 12: Lab B: Text classification

Visible copy:
45 minutes
Run section 4
Compare actual and predicted labels
Discuss ambiguous messages

Visual: Task slide

Speaker notes: Ask pairs to identify words that make this authored example easy. A forced category can conceal ambiguity.

## Slide 13: The limits of a perfect toy score

Visible copy:
8 of 8 test messages correct
Tiny authored sample
Shared vocabulary makes the task easy

Visual: Large 8/8 beside two limitations

Speaker notes: The result does not establish production accuracy. It provides no evidence about Arabic-language performance.

## Slide 14: Arabic-language evaluation

Visible copy:
Representative labelled Arabic messages
Suitable language processing
Review of ambiguity and domain variation

Visual: Short checklist

Speaker notes: The interpreter supports classroom understanding. Translation of instructions does not validate an Arabic NLP model.

## Slide 15: Break

Visible copy:
15 minutes

Visual: Plain break slide

Speaker notes: Give the return time. Pairs will design a better evaluation.

## Slide 16: Pair challenge: Development validation

Visible copy:
50 minutes
Reserve the last 14 training days for validation
Compare baselines without using final-test data
List requirements for Arabic message analysis

Visual: Task slide with 168 development / 14 validation / 28 test diagram

Speaker notes: The validation split comes only from the original training period. Keep the final test untouched for further selection.

## Slide 17: Day 3 review

Visible copy:
Why preserve chronology?
When can a baseline win?
What does the English text test fail to establish?

Visual: Three discussion questions

Speaker notes: Ask each group for an evaluation choice and a limitation. Use the recorded solutions to close the session.
