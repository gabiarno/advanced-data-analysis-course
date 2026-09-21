# Pair task cards

Use the runnable examples first, then adapt them. Swap roles every 10–15 minutes. Ask for help before spending more than five minutes blocked.

## A — Same question, two Spark interfaces (40 minutes)

Open spark_student.ipynb and run sections 1–2. Check the 10,000-row count. Compare DataFrame and SQL aggregates. Change the SQL to calculate average amount. Expected: A has 5,000 orders and 250,000 revenue; B has 5,000 and 255,000. Discuss why collecting this two-row result is different from collecting a billion-row source.

## B — Train on Spark (45 minutes)

Run section 3. Identify input features and the label. Check 800 training and 200 test rows. Compare model MAE with the training-mean baseline. Explain what VectorAssembler does. Spark should be stopped at the end; restart by rerunning from section 1 if you need another run.

## C — Inspect an advanced model (50 minutes)

After the 10-minute briefing, run the neural-network section in student.ipynb and inspect the saved GAN result (or run it if time permits). Explain why the generator's standard deviation being too small is a failure to reproduce diversity. Use the final 20 minutes for the practical assessment in ../assessments/FINAL_PRACTICAL.md.

Optional later extension: rerun the GAN with a different seed and compare failures. This is a sensitivity exercise, not evidence that the generator is production-ready.
