# Where the European material goes, day by day

The European thread is not a sixth day and not a compliance lecture. It attaches to analytical activities that already exist.

> **The timetable changed under this document.** It was written against the earlier 300-minute structure (labs of 40/45/50 minutes). `PROGRAMME.md` now runs workshops A/B/C at 50/50/60 minutes with 20 minutes of peer review — 180 protected practical minutes — and `instructor/TUTOR_SCRIPT.md` and `workshops/ACTIVITY_CARDS.md` hold the current minute-by-minute plan. The content below and the size of the trade still hold; the exact placements need re-fitting to the workshop cards before delivery. That is about two hours of work and it has not been done.

## The time trade, stated honestly

Each day is already a full 300 minutes. Nothing can be added without removing something. Fortunately the two changes cancel out almost exactly.

The cohort is confirmed as comfortable with Python and not beginners. That makes a substantial block of each day redundant — the syntax teaching, the guided first model, the pipeline mechanics, the line-by-line walkthroughs. Reclaiming that time pays for the European content, and the two roughly balance.

| Day | Removed, because the cohort does not need it | Freed | European content added | Net |
|---|---|---|---:|---|---|
| 1 | Python-for-tables syntax block; slow chart mechanics | 30 min | Purpose-first framing, Case 4, the people-versus-places line | 30 min | 0 |
| 2 | Guided first-model walkthrough; `fit`/`predict` explanation | 30 min | Case 2, error cost to the person, protected attributes and proxies | 30 min | 0 |
| 3 | Pipeline construction mechanics; tokenisation detail | 25 min | Annex III and emergency dispatch, purpose limitation, Case 3 | 25 min | 0 |
| 4 | MCMC implementation detail, kept as concept and diagnostics | 25 min | Case 1 (SyRI) and verifiability, necessity and proportionality | 25 min | 0 |
| 5 | Spark setup and API mechanics; participants can read the code | 40 min | DPIA and FRIA as design tools, procurement and vendor evidence, capstone governance | 40 min | 0 |

Total European content: about 150 minutes across the week, roughly one hour per day less than a standalone module would cost, because it replaces material this cohort does not need.

**If a day runs late, the European segment is not the thing to cut.** It is the differentiator this cohort asked for. Cut an extension task, as the runbook already says.

## Day 1 — purpose before data

**Where:** opening frame (5 min), then a 25-minute block replacing the Python-syntax segment.

**Content.**

- The organising distinction, written on the board and left there all week: **scoring people** versus **allocating resources**. European practice treats these very differently even when the statistics look identical.
- Case 4, the ordinary project. Walk the nine steps. Land the closing point: steps 1–3 removed more risk than 4–9 combined, and all three happen before anyone opens a notebook.
- Purpose limitation, in one concrete example: data collected for a licensing registry cannot simply be repurposed for enforcement targeting. This surprises people more than anything else in the week.
- The data-quality principle as a legal obligation, not housekeeping — which is exactly what Lab A is about.

**Attach to:** the data audit. After participants finish the audit, ask which of the quality problems they found would matter legally and not just statistically.

**Say once, early:** *We are going to show you the European approach and where it came from, including where Europe got it badly wrong. What transfers to your context is your judgement, not ours. I am not a lawyer and this is a framework, not legal advice.*

## Day 2 — what an error costs the person

**Where:** immediately after the confusion matrix, 30 minutes.

**Content.**

- Case 2, the Dutch childcare benefits scandal. Participants have just counted false positives; this is what a false positive can cost.
- The six-row failure table from the case study, worked through against the confusion matrix still on screen.
- Protected attributes and proxies: removing the attribute does not remove the effect; including it removes any defence. Postcode, surname, language of correspondence and prior contact frequency are all proxies in ordinary administrative data.
- Feedback loops in enforcement: investigate only group A, find fraud only in group A, "validate" the model on its own bias.
- LED Article 6 and 7 as analytical requirements — distinguish categories of data subject, and distinguish fact from assessment. An officer's free-text opinion is not an observation, and it must not become a feature.

**Attach to:** the error-cost activity. Rerun the cost comparison with the cost to the affected person substituted for the cost to the department, and see whether the preferred model changes. It usually does, which is the whole point.

**Classroom question:** *In your area, what does a false positive cost the person it lands on, and who currently measures that?*

## Day 3 — the line, and the forecast that sits on it

**Where:** 15 minutes before the forecasting lab, 10 minutes after the text work.

**Content.**

- Annex III includes the evaluation and dispatch prioritisation of emergency first-response services. Today's forecasting exercise, deployed for real in Europe, would be high-risk with a defined obligation set. Say this while the lab is on screen; it lands far harder than an abstract list.
- Case 3, the prohibited-versus-high-risk boundary. Forecasting call volume for a district is planning. Scoring residents is not. Same statistics, entirely different treatment.
- High-risk obligations that are analytical rather than legal: bias examination in the data (Art. 10), logging (Art. 12), human oversight by someone with authority to override (Art. 14), accuracy and robustness (Art. 15).
- On the text work: purpose limitation applied to free text. Incident narratives collected for record-keeping are not automatically available as model training data for a different purpose. And LED Art. 7 again — narrative text is dense with assessments recorded as if they were facts.

**Attach to:** the rolling-evaluation design activity. Add one requirement to the design: what would you log, so that someone could audit this decision in two years?

## Day 4 — verifiability and proportionality

**Where:** 25 minutes, replacing MCMC implementation detail. Keep MCMC as concept and diagnostics.

**Content.**

- Case 1, SyRI. The court accepted that fighting fraud is legitimate and did not rule risk models unlawful. It failed the fair-balance test, substantially because the system was not transparent or verifiable.
- Verifiability as the day's theme. Day 4 is about stating uncertainty honestly; the SyRI objection is the legal form of the same idea. A model nobody outside the team can inspect cannot be shown to be proportionate.
- Necessity and proportionality as a test that comes *before* accuracy. Not "does it work" but "is it necessary, and is there a less intrusive way to achieve the same aim".
- Automated decisions: LED Art. 11 prohibits a solely automated adverse decision unless authorised by law with safeguards including human intervention. Connect to the posterior-to-action rule the participants just built — the probability informs a human decision; it does not make one.
- Synthetic data and privacy: generating synthetic data does not by itself discharge a privacy obligation. Rare records are the ones most at risk of reproduction, and rare records identify people.

**Attach to:** the probability-to-action activity. Add: who makes the decision your rule feeds, what can they see, and can the affected person find out why?

**Classroom question:** *If your model works, can someone outside your team verify that claim?*

## Day 5 — the documents, and the capstone

**Where:** 40 minutes across the day, replacing Spark setup and API mechanics.

**Content.**

- DPIA and FRIA introduced as **project design tools**, not paperwork. Walk the questions each asks. Make the point explicitly: a team that cannot answer this course's questions — what is the baseline, who is in the data, who is missing, what does each error cost, who is accountable — cannot complete either document. The course has been teaching the content of a FRIA all week without calling it that.
- Procurement as the control point. Most public-sector AI arrives through a vendor. European practice puts the evidence requirements into the contract: the vendor supplies the evidence, and the buyer has to know what to demand. This is the vendor-critique activity with a purchase order attached.
- Independent supervision: an external authority can investigate and fine a public body. Oversight is not internal.
- Production readiness, rewritten in European terms: monitoring, logging, a stop condition, a named human owner, an appeal route for the affected person.

**Attach to:** the capstone. Every capstone must now answer three governance questions alongside its six existing headings — see below.

## The capstone additions

Three questions added to the capstone one-pager. They cost about ten minutes of writing and they are the clearest demonstration to the organiser that the European thread was actually taught.

1. **People or resources?** Does your proposal score individuals, or allocate resources? If it scores individuals, what would the European position be, and what changes if you reframe it as a resource question?
2. **Purpose and minimisation.** What is the stated purpose, was the data collected for that purpose, and what is the least data that achieves it?
3. **Oversight and redress.** Who makes the final decision, what can they see, what can they override, and how does an affected person find out and challenge it?

## What this does not cover

This thread teaches a framework and its reasoning. It does not make anyone competent to complete a DPIA or FRIA for a live system, it is not legal advice, and it does not address the participants' own national law, which is the framework that actually governs their work. Say all three plainly. The value on offer is the reasoning and the failure cases, and that value is real without overstating it.
