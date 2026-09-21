# Day 4: Bayesian Analysis and Generative Models

## Presentation brief

16:9 professional training deck. All text English. White or warm-white background, dark navy text, teal accent. Large readable type (titles about 36pt, body at least 24pt), ample whitespace, one idea per slide. No decorative stock photos, invented logos, or generic AI imagery. Use editable charts, tables and conceptual diagrams where specified. Exact numeric values must remain unchanged. Label synthetic results clearly. Never invent data series to draw an empirical chart. Keep detailed explanations in speaker notes. Audience: 20 participants from Saudi Arabia attending in Genoa, English delivery with Arabic interpretation. No cultural stereotypes. Preserve short task instructions and notebook paths. Include pause-for-interpretation guidance in notes rather than on every slide.

## Narrative arc

Introduce the question and essential concepts, demonstrate a working example, run pair activities, interpret evidence and close with a short review. The deck supports the five-hour timetable, including two 15-minute breaks and interpretation time.

## Slide 1: Bayesian Analysis and Generative Models

Visible copy:
Day 4
Updating uncertainty

Visual: Minimal typographic cover

Speaker notes: Introduce an inspection example rather than beginning with equations. All data and scenarios are synthetic.

## Slide 2: The unknown defect probability

Visible copy:
p represents a stable defect probability
Inspect 100 items
Observe 8 defects

Visual: Editable count illustration or a simple 8/100 fraction

Speaker notes: Distinguish a probability parameter from a count. Independence and representativeness are modelling assumptions.

## Slide 3: Prior, likelihood and posterior

Visible copy:
Prior: beliefs before current evidence
Likelihood: compatibility of data with parameter values
Posterior: updated distribution

Visual: Compact editable Bayes relationship diagram

Speaker notes: Posterior is proportional to likelihood times prior. Explain each term separately, allowing interpretation.

## Slide 4: An exact update

Visible copy:
Prior: Beta(2,18)
Data: 8 defects and 92 non-defects
Posterior: Beta(10,110)

Visual: Editable equation with clearly labelled terms

Speaker notes: The prior mean is 10% and the posterior mean is approximately 8.33%. The prior parameters are not automatically literal historical counts.

## Slide 5: Posterior uncertainty

Visible copy:
Posterior mean: 8.33%
95% credible interval: 4.10%–13.87%
Probability p > 10%: 23.75%

Visual: Editable interval graphic with exact endpoints

Speaker notes: Interpret these statements under the model and prior. The credible interval concerns p, not the count in the next batch.

## Slide 6: Lab A: Prior sensitivity

Visible copy:
40 minutes
Open day-04-bayesian-generative/student.ipynb
Compare Beta(2,18) with Beta(1,1)
Repeat with 16 defects in 200 items

Visual: Task slide

Speaker notes: Pairs calculate and explain changes to means and interval widths. A larger comparable sample narrows uncertainty in this example.

## Slide 7: Break

Visible copy:
15 minutes

Visual: Plain break slide

Speaker notes: Give the return time. The next demonstration introduces sampling-based inference.

## Slide 8: Metropolis sampling

Visible copy:
Propose a nearby probability
Compare posterior densities
Accept the proposal or retain the current value

Visual: Editable branching diagram with accept/stay paths

Speaker notes: The notebook runs a real MCMC chain. Out-of-range proposals are rejected, and repeated states are legitimate.

## Slide 9: Why use an exact reference?

Visible copy:
Beta inference has an exact answer here
The exact distribution lets us check sampled estimates
MCMC becomes useful for harder models

Visual: Simple comparison of exact versus sampled estimates

Speaker notes: MCMC is unnecessary for this basic calculation but useful pedagogically. Do not generalise success in one dimension to complex models.

## Slide 10: Chain diagnostics

Visible copy:
Compare several starting points
Inspect traces and dependence
High acceptance can still mean slow exploration

Visual: Illustrative trace sketch labelled conceptual

Speaker notes: The recorded lag-1 correlations are around 0.78. Full real-world diagnostics also include R-hat, effective sample size and Monte Carlo error.

## Slide 11: Lab B: Chain behaviour

Visible copy:
45 minutes
Run section 2
Compare chain means with 0.0833
Inspect a tiny proposal step

Visual: Task slide

Speaker notes: The small-step extension may move slowly despite high acceptance. Use saved results if runtime becomes a distraction.

## Slide 12: Break

Visible copy:
15 minutes

Visual: Plain break slide

Speaker notes: Give the return time. Next we distinguish parameter uncertainty from future outcomes.

## Slide 13: Posterior predictive simulation

Visible copy:
Draw p from its posterior
Draw a future defect count given p
Repeat to describe possible outcomes

Visual: Editable two-stage sampling diagram

Speaker notes: This represents parameter uncertainty plus variability in a future batch. It differs from simply multiplying credible-interval endpoints by a batch size.

## Slide 14: The next batch of 100

Visible copy:
Mean simulated count: 8.32
Central 95% simulated interval: 2–17 defects

Visual: Large values with clear count units

Speaker notes: These are simulation outputs for the teaching model. They do not prescribe an operational policy without costs and assumptions.

## Slide 15: Synthetic service durations

Visible copy:
Fit a positive-duration distribution
Generate new observations
Compare spread and tails

Visual: Two labelled distribution sketches marked illustrative

Speaker notes: The notebook uses a simple lognormal model, not a GAN. Similar marginal summaries do not establish privacy or preserve relationships.

## Slide 16: Pair challenge: Simulation limits

Visible copy:
50 minutes
Run predictive and service-time simulations
Distinguish probability from count intervals
Explain one use and two limitations

Visual: Task slide

Speaker notes: Use sections 3–4 and the answer key. Groups should state what additional checks a real application needs.

## Slide 17: Day 4 review

Visible copy:
How does evidence update a prior?
Why can MCMC repeat a value?
What can synthetic data fail to preserve?

Visual: Three discussion questions

Speaker notes: Accept plain-language answers before technical vocabulary. Tomorrow the course connects computation with more complex models.
