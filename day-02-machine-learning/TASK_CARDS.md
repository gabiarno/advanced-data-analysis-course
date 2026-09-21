# Pair task cards

Use the runnable examples first, then adapt them. Swap roles every 10–15 minutes. Ask for help before spending more than five minutes blocked.

## A — Is the prediction useful? (40 minutes)

Open student.ipynb, sections 1–2. Run the setup, identify features and targets, and check the 300/100 split. Record baseline and regression MAE. Explain the difference in one sentence. Expected model MAE is about 8.43 minutes versus 24.34 for the baseline. Do not claim every error is below 8.43.

## B — Which mistakes matter? (45 minutes)

Run section 3. Locate the training-fold validation scores and identify the model selected before testing. Read the confusion matrix with a partner. Count missed delays and false alarms. Write one operational consequence of each. Expected: 9 missed delays, 2 false alarms. Explain why a higher training score alone is insufficient.

## C — Explore without inventing meaning (50 minutes)

Follow the short clustering/PCA walkthrough. Run section 4. Record cluster sizes and retained variance. Then compare tree depths 1, 3 and 8 on training folds only, using the exercise solution as support. Prepare a group report: chosen evaluation method, result, limitation. Extension: compare k=2 and k=4, explaining why both partitionings require validation against the intended use.
