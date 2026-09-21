# Execution evidence and remaining environment check

## Passed

All five worked notebooks for Days 2–5 were schema-validated with nbformat and their code cells executed sequentially in fresh Python namespaces. This includes the separate Spark SQL/MLlib notebook, which ran with Java 17 and PySpark 4.0.1. The four exercise-solution notebooks were checked by the same direct-execution method. Each starts from its complete worked example, not a pre-existing state.

Meaningful checks include disjoint train/test indices, chronological forecasting boundaries, ARIMA convergence, the analytic Beta posterior versus sampled estimates, agreement of Spark SQL/DataFrame aggregates, finite generator outputs and Spark model improvement over its baseline. Saved text results and SVG figures are included in each day folder.

## Not passed / still required

The fresh Jupyter-kernel launch was attempted but failed before running any cell because local network-interface discovery was not permitted in this workspace. This was an environment startup failure, not a successful Jupyter test. Browser rendering, the actual instructor/participant laptop configuration and teaching time with interpretation remain to be checked.

Use scripts/check_notebook_kernels.py in the prepared classroom environment after following SETUP.md. No claim of classroom readiness or advanced instructor competence follows from code execution alone.

## Versions

Python 3.12.14; NumPy 2.3.5; pandas 2.2.3; matplotlib 3.10.8; scikit-learn 1.8.0; SciPy 1.17.0; statsmodels 0.14.6; PySpark 4.0.1; Java 17; nbformat 5.10.4. See requirements files. Execution date: 2026-09-21.
