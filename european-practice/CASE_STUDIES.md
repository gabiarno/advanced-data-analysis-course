# European case studies

Four cases, all from European public administration. Two are failures that caused real harm, one is a legal boundary, one is ordinary practice that worked. Use them as discussion material, not as slides to read aloud.

> Verify the details against primary sources before teaching. Summaries of well-known cases drift, including this one.

---

## 1. SyRI — the Netherlands, 2014–2020

**What it was.** *Systeem Risico Indicatie*: a Dutch government system that linked data held by different public bodies — employment, benefits, tax, housing, education, debt — to generate risk scores indicating which individuals were more likely to be committing benefit or tax fraud. It was deployed in selected neighbourhoods, several of them low-income.

**What happened.** A coalition of civil-society organisations and individuals challenged the enabling legislation. On 5 February 2020 the District Court of The Hague held that the SyRI legislation violated Article 8 of the European Convention on Human Rights, the right to respect for private life. The system was stopped.

**What the court actually objected to.** This is the part worth teaching, because it is not what people assume.

The court accepted that combating fraud is a legitimate aim. It did not rule that risk models are inherently unlawful. It failed the **fair balance** test — the proportionality assessment between the legitimate aim and the interference with private life — because the legislation lacked sufficient safeguards and, critically, because the system was **not transparent or verifiable**. The risk model and the indicators were not disclosed, so neither the affected individuals nor the court could check whether it worked or whether it discriminated. The court also noted the risk of unintended discriminatory effects given deployment in specific neighbourhoods.

**The transferable lessons.**

1. **Unverifiable is a legal defect, not just a technical one.** A model nobody outside the team can inspect cannot be shown to be proportionate.
2. **Where you deploy is part of what you built.** Applying a general model only in poor neighbourhoods produces a discriminatory effect regardless of what the features are.
3. **Linking datasets across purposes is the risky step**, more than the modelling. Each dataset was collected lawfully for its own purpose. The interference arose from combining them.

**The classroom question.** *If your model works, can a person outside your team verify that claim? If not, on what basis should anyone accept it?*

---

## 2. The Dutch childcare benefits scandal — the Netherlands, roughly 2013–2021

**What it was.** The Dutch tax administration used a risk-classification model to select childcare-benefit claims for fraud investigation. Selected families faced aggressive recovery proceedings and were often required to repay large sums immediately.

**What happened.** Tens of thousands of families were wrongly accused. Many were driven into serious debt; a substantial number of children were placed in state care. The Dutch data protection authority found unlawful and discriminatory processing and fined the tax administration. A parliamentary inquiry was highly critical, and the government resigned in January 2021.

**What went wrong, in analytical terms.** Nearly every failure this course warns about, in one system.

| The failure | What it looked like here |
|---|---|
| A protected attribute used as a feature | Nationality and dual nationality functioned as risk indicators |
| No meaningful human review | Model output drove enforcement with little independent assessment |
| Error costs wildly asymmetric and ignored | A false positive meant financial ruin for a family; it was treated as a routine review |
| No route to challenge | Affected families could not find out why they had been selected |
| Feedback loop | Investigating a group produces findings in that group, which confirms the model |
| Suspicion recorded as fact | Administrative flags hardened into treatment as established fraud |

That last row is exactly what LED Article 7 — distinguish facts from personal assessments — exists to prevent.

**The transferable lessons.**

1. **Removing the protected attribute is not sufficient, and including it is indefensible.** Proxies remain; but using the attribute directly removes any argument.
2. **The cost of a false positive is the cost to the person, not the cost to the department.** A review that costs the ministry an hour can cost a family their home.
3. **A system with no appeal route has no error-correction mechanism.** It cannot learn that it is wrong.
4. **Enforcement targeting creates its own evidence.** If you only investigate group A, you only find fraud in group A. The model is then "validated" by its own bias.

**The classroom question.** *In your own area, what does a false positive cost the person it lands on — and who currently measures that?*

---

## 3. The boundary the AI Act drew afterwards

The two cases above happened before the AI Act existed. They substantially shaped it.

The Act's prohibition on **social scoring by public authorities**, and its prohibition on **predicting individual criminal risk based solely on profiling or personality traits**, are direct legislative responses to this class of system. Its **Annex III** classification of law enforcement, migration and border control as high-risk, and its **Article 27** requirement that public deployers complete a fundamental rights impact assessment, are the procedural response.

The line the Act draws is worth stating precisely, because it is narrower than participants often expect:

- **Prohibited:** a system that predicts whether a *person* will commit an offence, based solely on profiling or personality traits.
- **High-risk but permitted with obligations:** analysis supporting a human assessment that is already grounded in objective, verifiable facts directly linked to criminal activity. Also: resource allocation, demand forecasting, and risk assessment of *places, premises or assets* rather than persons.

**The transferable lesson.** European practice has largely converged on a distinction between **scoring people** and **allocating resources**. Forecasting how many emergency calls a district will receive on Friday night is ordinary planning. Scoring which residents are likely to offend is not. The statistics can look similar; the legal and ethical treatment is not remotely similar.

This distinction is the organising idea of the whole European thread in this course, and it is worth writing on the board on Day 1.

---

## 4. What ordinary good practice looks like

Failure cases teach the boundaries. They do not show participants what a competent European public-sector analytics project actually looks like day to day. Sketch this as the counterweight, and be explicit that it is a composite of standard practice rather than one named project.

A typical, uncontroversial deployment — say, forecasting demand at vehicle-registration offices to plan staffing:

1. **Purpose stated and recorded first.** Reduce waiting times at service counters. Written down before any data is requested.
2. **Necessity check.** Would published aggregate statistics, or a simpler rule, achieve this? Documented answer.
3. **Minimisation.** The forecast needs counts per office per day. It does not need applicant identities. The project uses aggregated counts, which takes most of the legal risk out of the design.
4. **DPIA where personal data is involved.** In this design, largely avoided by aggregating first — which is itself the point.
5. **Baseline and honest evaluation.** Compared against last week's counts and a seasonal repeat, on a chronological holdout.
6. **Published methodology.** How the forecast is produced, its known error range, and its limitations.
7. **Human oversight.** Managers set staffing; the forecast is an input. Someone can override it and that override is logged.
8. **Monitoring and a stop condition.** Error tracked monthly against the baseline. An agreed threshold at which the system is withdrawn and reviewed.
9. **Named owner.** A person, not a team mailbox.

**The transferable lesson, and the one to end on.** Steps 1 to 3 removed more risk than steps 4 to 9 combined. Most of the European discipline is applied *before* anyone opens a notebook — in deciding what the purpose is, whether the work is necessary, and what the minimum data to achieve it is. By the time you are choosing a model, the important governance decisions have already been made.

---

## Using these in class

**Day 1** — Case 4, the ordinary project. Establishes purpose-first thinking before any method is taught.

**Day 2** — Case 2, the childcare benefits scandal, immediately after the confusion matrix. Participants have just counted false positives; this is what a false positive can mean.

**Day 3** — Case 3, the prohibited-versus-high-risk line, alongside the emergency-call forecasting work, which is itself in Annex III.

**Day 4** — Case 1, SyRI, alongside the discussion of uncertainty and evidence. The court's objection was about verifiability, which is a Day 4 idea.

**Day 5** — All four, briefly, as the frame for the capstone and the production-readiness segment.

**Format.** Ten minutes each: four minutes describing the case, then the classroom question to groups, then interpreted feedback. Do not narrate all the detail on this page in the room — most of it is here so that you can answer follow-up questions rather than read it out.
