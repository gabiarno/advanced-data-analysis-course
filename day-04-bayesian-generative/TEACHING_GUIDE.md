# Day 4 — Bayesian inference and generative modelling

## Outcomes and preparation

Learners will update a probability estimate using a prior and data, interpret a credible interval, distinguish parameter uncertainty from future outcome variability, observe a real MCMC chain, and generate synthetic data with stated limitations.

Rehearse the exact Beta-Binomial calculation first. The MCMC code is a guided demonstration; learners need to understand propose/accept/reject, not derive the algorithm. Core dependencies are NumPy, SciPy, pandas and matplotlib.

## Timetable

| Minutes | Activity |
|---|---|
| 0–20 | Probability refresher: rate versus count |
| 20–50 | Demonstrate prior, likelihood and posterior |
| 50–90 | Lab A: update defect probability and compare priors |
| 90–105 | Explain credible intervals and assumptions |
| 105–120 | Break |
| 120–150 | Demonstrate MCMC with an exact reference |
| 150–195 | Lab B: inspect traces, chain means and autocorrelation |
| 195–210 | Break |
| 210–260 | Pair challenge: future-batch simulation and synthetic durations |
| 260–285 | Five groups report uncertainty and limitations |
| 285–300 | Exit questions and recap |

## Instructor explanations

### 1. Start with the unknown quantity

We want p, an unknown defect probability under a stable inspection process. The count of defects in n items is a Binomial observation under independence and a common p. The Beta distribution is a distribution over probabilities between zero and one. It is not a distribution of item counts.

Bayes' theorem updates prior plausibility using the likelihood of the observations: posterior is proportional to likelihood times prior. The normalising constant makes total probability one. This example has an exact formula, so no numerical inference is necessary for the basic update.

Prior Beta(2,18) has mean 2/20=0.10. Observe 8 defective and 92 non-defective items. The posterior is Beta(2+8,18+92)=Beta(10,110), with mean 10/120≈0.0833. The prior concentration a+b describes its strength in this update. Do not say the prior literally records 20 inspected items unless that is how it was constructed.

### 2. Interpret rather than just calculate

The 95% equal-tailed credible interval contains 95% of posterior probability for p under this model and prior. It is not a guarantee and is not interchangeable with a frequentist confidence-interval interpretation. State assumptions: representative sample, comparable items and a stable defect mechanism. If the process changes halfway through, one common p may be inappropriate.

Ask: “Why is the posterior mean not exactly 8%?” Expected: both prior and observations contribute. More observations usually reduce the prior's relative influence; the exact effect depends on the model and data.

### 3. Explain MCMC in three actions

Propose a nearby probability. Compare its posterior density with the current state's density. Accept or stay. Symmetric proposals make the ratio simple; out-of-range proposals are rejected. Staying at a state is part of the Markov chain, not a missing measurement. The first 2,000 draws are discarded in this demonstration as warm-up; that number is not a universal rule.

We run four chains from dispersed starting points and compare the retained distributions with the known exact posterior. Inspect traces, chain means, interval estimates and lag-1 correlation. High autocorrelation means consecutive draws carry overlapping information. High acceptance alone is not sufficient: tiny proposals can be accepted often while moving slowly.

These are educational checks. They do not replace rank-normalised R-hat, effective sample size, Monte Carlo standard error and sampler-specific diagnostics in a real analysis. Agreement in this one-dimensional example does not validate an arbitrary complex model.

### 4. Predict future observations

First sample p from its posterior. Then sample a future count from Binomial(100,p). This includes uncertainty about p and random variation within a batch. A 95% interval for a probability cannot be read as a 95% interval for a count. Decision-making also needs costs and actions: a posterior tail probability alone does not dictate an inspection policy.

### 5. Generative models

A generative model specifies a way to sample observations. Today we fit a lognormal distribution to positive service durations, then draw new durations. This simple statistical model is generative; it is not a deep model. Deep generative families include GANs and other architectures, but “generative” does not imply realism, privacy or causal validity.

Compare histograms, means, spread and tails. Even a close marginal distribution would not preserve correlations with missing variables. Synthetic data may still reveal information about training records or omit minority patterns. Our source is synthetic already, so this lab does not test privacy protection.

## Common questions and recovery

“Why MCMC when Beta sampling exists?” To see how sampling-based inference works while having an exact answer for comparison.

“Do more iterations guarantee convergence?” No. Proposal quality, geometry and diagnostics matter.

“Can generated data replace observed evidence?” They can support simulations and testing under assumptions; they do not create new empirical evidence.

If MCMC is slow, show saved results and use fewer iterations for an explicitly rough live demonstration. Do not reuse the full-run accuracy claim for a shorter run without checking it.

## Classroom routine

20 participants, 10 pairs, five groups for reporting. Swap keyboard and explanation roles every 10–15 minutes. Explain one idea, pause for Arabic interpretation, demonstrate a few lines, then let pairs repeat. All written materials are English. Confirm that participants can use English task cards or arrange interpreter-reviewed support.

Each timetable totals 300 minutes including two 15-minute breaks. There are 135 minutes of protected practice. For 300 contact minutes, add 30 minutes of supported practice and put breaks outside those hours. Confirm the contractual interpretation.

Use worked.ipynb for rehearsal; student.ipynb contains the same runnable examples plus challenges. Beginners change and interpret working code rather than typing everything from scratch. Stronger participants use the extensions. Read worked_RESULTS.md for verified outputs and open the executed notebook for saved numerical results. Figures are in figures/.

Do not rush through every line. The goal is for each pair to explain a result, a limitation and a next step. If the interpreter needs more time, reduce extension work, not the foundational lab or break.
