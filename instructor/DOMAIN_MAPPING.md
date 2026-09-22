# Domain mapping — retail and logistics to public administration

The cohort is Ministry of Interior personnel. Every dataset in this course is currently framed as retail orders, delivery routes and customer support messages. That framing costs the participants a translation on every single exercise, and it signals a generic course bought off a shelf.

This document re-frames every scenario for public administration. **The numbers do not change.** Each mapping is a relabelling of synthetic data whose statistical structure, expected answers and recorded results stay exactly as validated. A "unit" becomes a "document processed"; 122 rows are still 122 rows and the answer is still EUR 10,210.

## How far this mapping is implemented

| Layer | State |
|---|---|
| What the instructor says in the room | **Re-framed here** — use this document |
| Printed workbook and handbook scenarios | **Re-framed** in the participant material |
| Capstone scenarios | **Re-framed** in `participant/CAPSTONE.md` |
| Column names inside the notebooks and CSV | **Not changed** — see below |

The notebooks still contain `retail_orders.csv`, `channel`, `units`, `unit_price`, `distance_km`. Renaming those means editing five days of notebooks, their solutions, their recorded results and their figures, then re-running everything from clean kernels. That work is specified in the backlog at the end of this document. It was not done here because this environment has no scientific Python installed, and shipping unvalidated notebooks would be worse than shipping honestly-labelled ones.

**In the meantime, say it out loud.** At the start of each lab: *"This column is called `units`. In your work it is the number of documents processed in one request. The analysis is identical."* Participants who write code are entirely capable of holding that mapping; it takes one sentence per lab.

## The constraint that shapes every scenario

Every scenario below concerns **resources, places, processes or documents**. None of them scores individuals.

That is deliberate and it is itself teaching content. European practice draws a hard line between allocating resources and scoring people — see `european-practice/CASE_STUDIES.md`, case 3. Building the whole week on the resource side of that line means the participants spend five days practising the form of analytics that is lawful, uncontroversial and immediately useful, and meet the other side of the line as a governed discussion with real case law rather than as a lab exercise.

If a participant raises a person-scoring application from their own work — and someone will — the answer is the framework, the two Dutch cases and the parking list. Not an improvised exercise.

---

## Day 1 — service-centre requests

**Current:** a retail order table. **Becomes:** a service-centre request log from public counters and the online portal.

| Current column | Becomes | Meaning |
|---|---|---|
| `order_id` | Request reference | One row is one service request |
| `date` | Date received | 120 consecutive dates |
| `channel` | Channel — `Counter` or `Online` | Two values missing |
| `units` | Documents processed | One invalid negative value, one legitimate bulk submission of 80 |
| `unit_price` | Fee per document, EUR | Three missing |

**The scenario.** A directorate operates public service counters and an online portal. It wants to report processing volume and fees collected by channel, to support a decision about opening counter hours. The extract has quality problems.

**The business rules, restated.** Requests have a positive document count; reversals and cancellations belong in a separate table, so a negative count is invalid here. Duplicate records are export errors. A missing fee is unrecorded, not a free service. The 80-document submission is a legitimate bulk filing from an institution and stays in the main report.

**Every expected answer is unchanged:** 122 raw rows, 2 duplicates, 3 missing fees, 2 missing channels, 1 invalid count, 119 valid, 116 with a known fee, EUR 10,210 recorded, Counter 6,310 / Online 3,700 / Unknown 200.

**Why it is a better scenario.** The decision at the end — is the counter channel really outperforming the portal — is a genuine public-administration question, and the honest answer (different volumes, incomplete fee data, no causal claim available) is exactly the answer a directorate needs to hear before reallocating staff.

**European hook.** The fee data is administrative data collected for revenue purposes. Using it for channel-performance analysis is a compatible purpose. Using it to identify individual applicants for any other purpose is not. Purpose limitation, in one concrete sentence.

---

## Day 2 — scheduled inspection visits

**Current:** delivery route duration and delay classification. **Becomes:** scheduled civil-protection or building-safety inspection visits.

| Current | Becomes |
|---|---|
| 400 delivery routes | 400 scheduled inspection rounds |
| `distance_km` | Travel distance for the round, km |
| `planned_stops` | Number of premises scheduled |
| `duration_min` | Total round duration, minutes |
| "delayed", over 85 minutes | "overran the scheduled slot", over 85 minutes |

**The scenario.** An inspection unit schedules rounds of premises visits. Rounds that overrun cause cancelled appointments later in the day. The unit wants to predict, before dispatch, which rounds will overrun, so it can rebalance the schedule.

**Available at decision time:** travel distance and number of premises. **Not available:** the actual duration, which is the outcome.

**Expected results unchanged:** 300/100 split, baseline MAE 24.34 minutes, model MAE 8.43, 9 missed overruns and 2 false alarms in the classification test.

**Why it is a better scenario.** The error costs are concrete and asymmetric in a way participants will recognise. A missed overrun cancels a citizen's appointment. A false alarm wastes an inspector's half-day. Which is worse is a genuine policy question with no universal answer — which is precisely the discussion the confusion-matrix activity needs.

**European hook.** This is resource allocation applied to premises. Note explicitly in class that the *same statistical machinery* pointed at residents rather than buildings would be a different legal object entirely. Then run the childcare-benefits case.

---

## Day 3 — emergency call volume and incident report routing

**Current:** daily product demand, plus support-message classification. **Becomes:** daily emergency call volume, plus routing of written incident reports to the correct unit.

| Current | Becomes |
|---|---|
| 210 days of product demand | 210 days of emergency call counts for one control room |
| 28-day chronological holdout | Unchanged |
| Weekly seasonality | Weekly pattern — call volume varies by day of week |
| 24 support messages, 5 categories | 24 written incident reports, routed to the responsible unit |

**The scenario, forecasting.** A control room wants next week's daily call volume to set shift sizes. It currently staffs to last week's average.

**The scenario, text.** Written reports arrive through a public portal and must reach the correct operational unit within minutes. Misrouting delays response.

**Expected results unchanged:** weekly-repeat baseline MAE 5.53, ARIMA(1,1,1) MAE 22.11, 16 training and 8 test messages.

**Why it is a better scenario.** Call-volume forecasting for staffing is one of the most common and least controversial analytics applications in any interior ministry, and the seasonal-baseline lesson — the cheap method beats the sophisticated one — is directly actionable.

**European hook, and this is the strongest one in the week.** AI Act Annex III explicitly covers the evaluation and dispatch prioritisation of emergency first-response services. This exercise, deployed for real in Europe, would be a high-risk system with a defined obligation set: bias examination, logging, human oversight with authority to override, accuracy and robustness requirements. Say it while the lab is on screen.

Note carefully the distinction for participants: forecasting **how many calls** a district will receive is planning. Prioritising **which caller** gets a response first is dispatch prioritisation, which is the Annex III item. Both are legitimate; only one carries the obligation set.

**A caution on the text lab.** Route to *units*, never to a judgement about the person reporting. And LED Article 7 applies with force here — incident narratives are full of assessments recorded as though they were facts. That is a data-quality point before it is a legal one.

---

## Day 4 — records quality sampling

**Current:** manufacturing defect rate. **Becomes:** a quality audit of issued documents or processed records.

| Current | Becomes |
|---|---|
| Defect probability `p` | Proportion of processed records containing an error |
| Prior Beta(2,18) | Prior belief from previous audit rounds: about 10% |
| 8 defective in 100 | 8 records with an error in a sample of 100 |
| Posterior Beta(10,110) | Unchanged, mean about 0.0833 |
| Future batch of 50 | The next 50 records to be audited |
| Synthetic service durations | Synthetic processing times, for sharing with an external supplier |

**The scenario.** A directorate audits a sample of processed records each quarter. The service standard says the error rate must stay below 10%. This quarter's sample shows 8 errors in 100. Does that breach the standard, or is it within normal variation?

**The added decision step.** Compute the posterior probability that the true error rate exceeds 0.10, and state the action it triggers. This is the point where the Bayesian day becomes useful to a manager rather than interesting to a statistician.

**Expected results unchanged.**

**Why it is a better scenario.** Sampling against a service standard is real, recurring public-administration work, and "is this a real deterioration or just noise" is a question managers get wrong constantly in both directions.

**European hook.** SyRI. The court's objection was verifiability. Ask: if this audit result triggers an intervention, can the affected unit see the method and check it? Also the synthetic-data point — generating synthetic processing times to share with a supplier does not by itself discharge a privacy obligation, and rare records are both the hardest to reproduce faithfully and the most identifying.

---

## Day 5 — national-scale transaction records

**Current:** 1,000 delivery routes, partitioned aggregation over six records. **Becomes:** service transactions across regional offices.

| Current | Becomes |
|---|---|
| 1,000 routes, split by id modulo 5 | 1,000 service transactions across regional offices |
| Six records in the partition demo | Six transaction records across two regional partitions |
| Partitions | Regional offices — a natural and correct partition key |
| MLlib duration model | Processing-time model, same features |

**The scenario.** Transaction records are held per regional office and no longer fit comfortably on one machine. The question is whether distributed processing is warranted, and whether the model built on it is any good.

**Expected results unchanged.**

**Why it is a better scenario.** Regional partitioning is how public-sector data actually arrives — separate systems per region, per directorate, per legacy platform — so the shuffle discussion becomes concrete.

**A teaching point the re-skin unlocks.** The existing notebook splits train and test by `id modulo 5`. With regional data that is visibly the wrong split: the model would see every region in training, so the test set cannot show whether it generalises to a region it has not seen. Ask the group what the right split is. This is a better version of the grouped-split lesson than the original framing supports, and it costs nothing.

**European hook.** DPIA and FRIA as design tools, and procurement — regional systems are usually vendor-supplied, so the evidence requirements belong in the contract.

---

## Capstone scenarios

Re-framed in `participant/CAPSTONE.md`. All five sit on the resource side of the line:

1. **Inspection scheduling** — which rounds will overrun, to rebalance the schedule.
2. **Service-centre demand** — counter volumes per office per day, to plan staffing.
3. **Correspondence routing** — written public correspondence to the responsible unit.
4. **Records quality** — has the error rate in processed records genuinely moved?
5. **Road safety** — where collisions concentrate, to prioritise engineering and enforcement resources by location.

Participants are encouraged to bring a problem from their own work instead. If what they bring is a person-scoring problem, do not refuse it — reframe it with them. "Which individuals are high risk" almost always has a resource-shaped sibling: which locations, which times, which process steps, which document types. That reframing conversation is one of the most valuable things they can take home, and it is exactly the move European practice has converged on.

---

## Backlog: completing the re-skin in the notebooks

Not done here; specified so it can be picked up.

| Step | Effort | Notes |
|---|---|---|
| Regenerate `datasets/retail_orders.csv` with the Day 1 column names above and **identical values** | 1 h | Values must not change, or every recorded result and expected answer breaks |
| Update column references across Day 1 notebooks, solutions and answer key | 2 h | Mechanical rename |
| Update the synthetic generators in Days 2–5 notebooks — variable names and narrative text only | 3 h | The generators are seeded; do not touch the seeds or the distributions |
| Re-run everything from clean kernels via `scripts/check_notebook_kernels.py` | 1 h | Requires the full environment and Java 17 for the Spark lab |
| Diff the new recorded results against the committed ones | 1 h | **Every number must be identical.** Any difference means the re-skin changed behaviour and must be reverted |
| Update the five slide plans and regenerate the decks | 2 h | Figures must match the plans exactly |

Total about 10 hours. The final diff step is the one that matters: a relabelling that changes a number is not a relabelling.
