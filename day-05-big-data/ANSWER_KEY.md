# Instructor answer key

## Worked answers

Partition totals: A=15, B=23, C=15. Adding (A,4) yields A=19. Matching keys must be combined across partial results. The local simulation is not Hadoop execution.

Spark: 10,000 rows, 5,000 per region. A revenue 250,000 and mean 50; B revenue 255,000 and mean 51. SQL and DataFrame results agree. `filter` is a transformation; `count`, `show` and `collect` are actions. Collecting a large source can exhaust driver memory.

Spark regression: 800 training and 200 test rows. Recorded model MAE≈2.248 versus baseline≈20.227 minutes, with small environment-related variation possible. VectorAssembler creates a vector from numeric features; it does not select features or validate leakage.

Small neural network: held-out accuracy≈0.847 versus 0.827 for the linear model. This single synthetic split is not a general claim about neural networks or statistical significance.

Toy GAN: target mean/sd=2/0.6; generated final mean/sd≈2.10/0.287. The mean is near the target but spread is much too small. Treat this as an instructive failure to reproduce variability, not successful convergence. The generator and discriminator update, but the toy is neither deep nor suitable for realistic data synthesis.

## Exit check and key

1. Is local[2] a two-machine cluster? No, it uses two local worker threads.
2. Why can groupBy be expensive? Matching keys may need data movement/shuffling.
3. Is training loss test performance? No.
4. What do generator and discriminator do? Generate samples and distinguish generated/reference samples.
5. Does a close mean prove good synthetic data? No; spread, tails, dependencies and other criteria matter.

## Marking guide

10 points: correct workflow 2; calculations 2; interpretation 2; limitation 2; clear explanation 2. Use this for formative feedback, not certification. Numerical reference values are recorded in worked_RESULTS.md; Spark has spark_worked_RESULTS.md.
