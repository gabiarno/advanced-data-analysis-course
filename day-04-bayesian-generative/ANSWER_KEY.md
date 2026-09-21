# Instructor answer key

## Worked answers

Original posterior Beta(10,110), mean 0.08333, 95% credible interval approximately [0.0410,0.1387], posterior probability p>0.10≈0.2375. Uniform prior Beta(1,1) gives Beta(9,93), mean≈0.08824. The stronger original prior pulls toward its own mean differently.

For 16/200 and Beta(2,18), posterior is Beta(18,202), mean≈0.08182. Compute its interval in solutions.ipynb and compare widths. A larger representative sample at a similar rate narrows uncertainty in this example.

Original chain means are approximately 0.0831–0.0842; lag-1 correlations approximately 0.78 indicate dependence. Trace agreement and an exact comparison are useful but do not replace full diagnostics for real models. A tiny proposal often increases acceptance while slowing exploration; it may fail to move far enough from the starting state.

Posterior-predictive simulation gives about 8.32 defects per future 100 and a central simulated interval of 2–17. This describes future counts, not the value of p. Service-time samples have similar means but different extrema; matching a histogram does not establish privacy or preserve unmodelled relationships.

## Exit check and key

1. Prior versus posterior? Before versus after incorporating current evidence, under the model.
2. Is 8/100 the same as a distribution over p? No, it is a sample proportion.
3. Why can an MCMC chain repeat a value? The proposal was rejected.
4. Does high acceptance guarantee mixing? No.
5. Are synthetic data automatically private? No.

## Marking guide

10 points: correct workflow 2; calculations 2; interpretation 2; limitation 2; clear explanation 2. Use this for formative feedback, not certification. Numerical reference values are recorded in worked_RESULTS.md; Spark has spark_worked_RESULTS.md.
