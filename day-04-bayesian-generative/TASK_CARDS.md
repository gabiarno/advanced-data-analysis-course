# Pair task cards

Use the runnable examples first, then adapt them. Swap roles every 10–15 minutes. Ask for help before spending more than five minutes blocked.

## A — Update a probability (40 minutes)

Run section 1. Identify prior, observed defects and posterior parameters. Change the prior to Beta(1,1) in a new cell. Compare means. Then compute Beta(18,202) for 16 defects in 200 items under the original prior. Compare credible interval widths. Expected original posterior: Beta(10,110), mean 0.0833.

## B — Can we trust a chain? (45 minutes)

Run section 2. Compare four retained-chain means with the exact mean. Inspect trace movement and lag-1 correlations. Run one chain with proposal_sd=.001 if time permits. Explain why very high acceptance may still produce slow exploration. Expected original pooled interval is close to [0.041,0.139], not an exact identical value on every environment.

## C — Simulate and state limits (50 minutes)

Run sections 3–4. Compare a credible interval for p with a predictive interval for a future count. Compare synthetic service-time summaries with the source. Write one use and two limitations of synthetic records. Report a finding, uncertainty and required next check.
