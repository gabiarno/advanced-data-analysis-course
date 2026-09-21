# Pair task cards

Use the runnable examples first, then adapt them. Swap roles every 10–15 minutes. Ask for help before spending more than five minutes blocked.

## A — Forecast without seeing the future (40 minutes)

Run sections 1–3. Mark the split date. Write down the three forecast MAEs. Explain why the weekly baseline can outperform ARIMA(1,1,1). Expected: 182 training observations, 28 test observations. Do not change model orders using final-test errors.

## B — Read the text model critically (45 minutes)

Run section 4. Compare actual and predicted categories for eight messages. Identify shared words that make the toy task easy. Try two ambiguous new messages; discuss the forced label without treating those unlabelled messages as an accuracy test. Explain why this is topic classification, not sentiment analysis.

## C — Design a better evaluation (50 minutes)

Use the final 14 days of train as a development validation window. Build last-value and weekly-repeat forecasts from the earlier part of train only. Compare their MAEs. Then list three requirements for an Arabic-message classifier. Prepare a short report stating what the English demonstration cannot establish.
