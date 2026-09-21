# Day 3 — Time series and text analysis

## Outcomes and preparation

Learners will preserve time order, compare forecasts with naive baselines, recognise trend and seasonality, explain ARIMA at a conceptual level, and run a text-classification pipeline. Time series and NLP are separate applications today; neither depends on the other.

Install the updated core requirements and run the complete worked notebook before class. It generates 210 daily demand observations and includes 16 training/8 test English messages. No external dataset or language model download is needed.

## Timetable

| Minutes | Activity |
|---|---|
| 0–20 | Recap test-set protection; sort a few example dates |
| 20–50 | Demonstrate trend, weekly seasonality and chronological holdout |
| 50–90 | Lab A: compute baselines; guided ARIMA and decomposition |
| 90–105 | Compare errors; explain why complex models can lose |
| 105–120 | Break |
| 120–150 | Demonstrate text representation and classification |
| 150–195 | Lab B: classify messages and inspect ambiguity |
| 195–210 | Break |
| 210–260 | Pair challenge: training-only forecast validation and text failure cases |
| 260–285 | Five groups report evaluation choices and limitations |
| 285–300 | Exit questions and recap |

## Instructor explanations

### 1. Time order changes evaluation

Say: “Imagine it is the last date in the training period. What information can we really see?” Point to the boundary. No subsequent observation is available. A random split can let a model learn patterns from the future and make evaluation unrealistically easy. Keep the last 28 days as a final holdout.

Our rows are regularly spaced daily observations. Real series may have gaps, duplicates, changed definitions or events. First verify frequency and provenance; do not assume missing dates mean zero demand.

### 2. Trend, seasonality and cycles

Trend is a sustained direction over time. Seasonality repeats at a known calendar-related interval; the synthetic series has a seven-day pattern. Cycles need not have a fixed period. A moving average smooths variation but is not automatically a full decomposition. Additive decomposition represents observed values as trend plus seasonal component plus residual. A residual is what this decomposition did not explain; it is not proof of random noise.

The seven-day period is known from the teaching generator, not inferred from a population. Lag-7 correlation alone cannot prove seasonality because trend also induces correlation. Decomposition is fitted on training data only.

### 3. Baselines and ARIMA

Last-value forecasting repeats the most recent observation. The weekly baseline repeats the last seven values in sequence. These cheap methods are essential benchmarks.

ARIMA has three orders: p uses previous observations, d differences the series, and q models dependence on previous errors. Differencing subtracts earlier observations to reduce certain nonstationary patterns. The fixed ARIMA(1,1,1) demonstration does not explicitly represent weekly seasonality; a seasonal model would require additional specification and validation. Do not claim ARIMA must win.

The shaded forecast interval is model-based and depends on assumptions. It is not a guarantee about actual coverage. One 28-day test window is a limited evaluation; real deployment would require multiple rolling origins and monitoring. Changing orders after observing this test contaminates its role as a final check. For the exercise, use a validation window cut from training data.

### 4. Text becomes numeric input

Say: “The classifier does not read these sentences like a human. We turn words and short word sequences into numeric features.” TF-IDF weights terms using counts and document frequency; logistic regression learns associations with labels. The vectoriser belongs inside the fitted pipeline so test vocabulary statistics do not leak into training.

Delivery and billing are operational categories, not sentiment. The small authored test is intentionally easy and shares vocabulary with training; high scores would not establish real-world performance. Some messages concern both categories. A forced single label can conceal ambiguity. Unknown words may contribute no features.

### 5. Language limitations

English results cannot be extrapolated to Arabic. A real Arabic workflow needs representative labelled Arabic messages, appropriate handling of script and linguistic variation, suitable tokenisation and evaluation by people who understand the language. The interpreter may translate the task aloud; that does not validate an Arabic model.

## Common questions and recovery

“Why does the baseline beat ARIMA?” Model assumptions and seasonal structure matter more than complexity. This is a useful result, not a broken lesson.

“Can I try another ARIMA order?” Yes on training/validation data; keep a new final test untouched for a fresh claim.

“Does 100% on eight messages mean success?” No; the test is too small and artificial to support deployment.

If statsmodels fails to install, baseline and NLP sections still run when the ARIMA cell is skipped. Use saved ARIMA results and figures for discussion; describe this explicitly as a fallback, not a successful live model run.

## Classroom routine

20 participants, 10 pairs, five groups for reporting. Swap keyboard and explanation roles every 10–15 minutes. Explain one idea, pause for Arabic interpretation, demonstrate a few lines, then let pairs repeat. All written materials are English. Confirm that participants can use English task cards or arrange interpreter-reviewed support.

Each timetable totals 300 minutes including two 15-minute breaks. There are 135 minutes of protected practice. For 300 contact minutes, add 30 minutes of supported practice and put breaks outside those hours. Confirm the contractual interpretation.

Use worked.ipynb for rehearsal; student.ipynb contains the same runnable examples plus challenges. Beginners change and interpret working code rather than typing everything from scratch. Stronger participants use the extensions. Read worked_RESULTS.md for verified outputs and open the executed notebook for saved numerical results. Figures are in figures/.

Do not rush through every line. The goal is for each pair to explain a result, a limitation and a next step. If the interpreter needs more time, reduce extension work, not the foundational lab or break.
