# Final practical — rubric and model response

20 points: task/method fit 4; split and baseline 4; correct numerical interpretation 4; limitations 6 (two per manager claim); actionable next step 2. Use 14/20 as an optional formative target, not an accredited pass standard. Accept justified alternative methods.

A strong response proposes temporal forecasting evaluated on future-held-out windows against a seasonal naive baseline; delayed-route classification using pre-dispatch features and representative held-out data against a majority or operational-rule baseline; and a text-classification pipeline evaluated on representative labelled messages, fitted without vocabulary leakage.

Example interpretations: weekly-repeat MAE 5.53 versus fixed nonseasonal ARIMA 22.11 in one synthetic window; logistic classifier misses 9 out of 43 actual delayed routes in its synthetic test. These results do not establish performance on real operations.

Correct the claims: 100% on eight authored English messages is weak evidence and says nothing about Arabic performance; the toy GAN matches the mean approximately but standard deviation 0.287 is much smaller than target 0.6; local Spark execution demonstrates functionality, not cluster scalability.

Next step: obtain representative, appropriately governed operational data; agree error costs; reserve a suitable evaluation set and run a documented pilot. Any concrete, justified next step addressing a stated limitation merits credit.
