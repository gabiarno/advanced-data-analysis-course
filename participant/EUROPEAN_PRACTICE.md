# Reference 4 — How Europe does it

A framework and its reasoning, for public-sector analysis. This is not legal advice, it does not describe your national law, and your instructor is not a lawyer. What is worth taking home is the reasoning and the failure cases.

## The idea underneath all of it

European practice does not treat data protection as a set of rules bolted onto good analysis. It mostly writes down what good analysis already requires: state your purpose before you collect, use no more data than the purpose needs, evaluate honestly, document what you did, keep a human answerable for the decision, and be able to explain it to the person affected.

Everything in this course has been teaching that. The European frame is the same discipline, made enforceable.

## The one distinction to remember

> **Allocating resources is treated very differently from scoring people.**

Forecasting how many emergency calls a district will receive on Friday night is ordinary planning. Scoring which residents are likely to offend is not. The statistics can look nearly identical. The legal and ethical treatment is not remotely similar.

Where the statistics are the same, ask which of the two you are actually doing. Most person-scoring questions have a resource-shaped sibling — which locations, which times, which process steps, which document types — and the resource version is usually both more useful and far less fraught.

## Which rules apply to what

A frequent surprise: the general data protection regulation does not cover everything a ministry does.

| Instrument | Covers | Typical ministry use |
|---|---|---|
| **GDPR** (Regulation 2016/679) | General personal data processing | Registries, licensing, permits, HR, service delivery |
| **Law Enforcement Directive** (Directive 2016/680) | Processing by competent authorities for criminal purposes | Police and criminal investigation — a **separate regime** |
| **AI Act** (Regulation 2024/1689) | AI systems, by risk tier | Anything from a forecast to a biometric system |
| **Convention 108+** (Council of Europe) | Data protection, as a treaty | Open to states outside the EU |

The same ministry usually operates under more than one at once.

### Two requirements worth stealing regardless of jurisdiction

From the Law Enforcement Directive, and both are data-quality points before they are legal ones:

- **Distinguish categories of person** — suspects, convicted persons, victims, witnesses. These are different populations. A model that does not separate them treats a witness like a suspect.
- **Distinguish fact from assessment** — an officer's recorded opinion is not an observation. If it enters a model as a feature, the model learns the opinion and then launders it as evidence.

Free-text narrative fields are where this goes wrong most often.

## The AI Act in one page

Obligations follow the risk, not the technology.

**Prohibited.** Social scoring by public authorities. Predicting individual criminal risk based solely on profiling or personality traits. Untargeted scraping of facial images to build recognition databases. Emotion inference at work or in education. Biometric categorisation inferring sensitive characteristics. Real-time remote biometric identification in public spaces for law enforcement, outside narrow authorised exceptions.

For this set of applications, the European answer is that they are not done.

**High-risk.** A list — Annex III of the Act — of areas that are high-risk by default. It includes law enforcement, migration and border control, administration of justice, biometrics, critical infrastructure, and **the evaluation and dispatch prioritisation of emergency first-response services**. The Day 3 forecasting exercise sits next to that last one.

Obligations include bias examination in the data, technical documentation, automatic logging, human oversight by someone with the competence and authority to override, and accuracy and robustness requirements. Public bodies deploying these systems must also complete a fundamental rights impact assessment.

**Limited risk.** Tell people they are interacting with an AI system.

**Minimal risk.** No specific obligations.

## The principles that actually constrain a project

| Principle | The design consequence |
|---|---|
| **Purpose limitation** | You cannot repurpose an administrative registry for a different enforcement purpose without a legal basis |
| **Data minimisation** | "Collect everything and let the model choose" is not available; feature selection becomes a legal question too |
| **Storage limitation** | Your training set expires; plan for a shrinking history |
| **Accuracy** | Data-quality work is an obligation, not housekeeping |
| **Necessity and proportionality** | Not "is it useful" but "is it necessary, and is there a less intrusive way" |
| **Transparency** | If you cannot explain the decision to the person it was made about, you cannot deploy it |
| **Accountability** | Undocumented good practice does not count |

Necessity and proportionality is the one that changes how projects start. Before asking whether the model works, European practice asks whether the intervention is warranted at all.

## Two European failures worth knowing

Both are Dutch, both recent, both caused real harm to citizens. They shaped the law that followed.

### SyRI — stopped by a court in 2020

A system linking employment, benefits, tax, housing and debt data to score individuals for likely fraud, deployed in selected low-income neighbourhoods.

The District Court of The Hague held that the enabling legislation violated Article 8 of the European Convention on Human Rights. The court accepted that fighting fraud is legitimate and did not rule risk models unlawful. It failed the proportionality test — largely because the system was **not transparent or verifiable**. Nobody outside the project could check whether it worked or whether it discriminated.

**Take away:** unverifiable is a legal defect, not only a technical one. And where you deploy is part of what you built — applying a general model only in poor neighbourhoods produces a discriminatory effect whatever the features are.

### The childcare benefits scandal

A risk-classification model selected childcare-benefit claims for fraud investigation. Nationality and dual nationality functioned as risk indicators. Tens of thousands of families were wrongly accused, many ruined financially, and children were taken into state care. The tax administration was fined and the government resigned in 2021.

Almost every failure this course warns about appeared in one system: a protected attribute used as a feature, no meaningful human review, error costs measured for the department rather than the citizen, no route to challenge, a feedback loop where investigating one group produced findings only in that group, and suspicion hardening into recorded fact.

**Take away:** the cost of a false positive is the cost to the person it lands on. A review that costs the department an hour can cost a family their home.

## What good ordinary practice looks like

A forecast of demand at service offices, to plan staffing:

1. Purpose written down before any data is requested.
2. Necessity checked — would published aggregates or a simple rule do?
3. Minimised — the forecast needs counts per office per day, not identities. Aggregate first.
4. Impact assessment where personal data is involved.
5. Baseline and honest evaluation on a chronological holdout.
6. Methodology published, with its error range.
7. Human oversight — managers decide staffing; the forecast is an input, and overrides are logged.
8. Monitoring, with an agreed threshold at which the system is withdrawn.
9. A named owner. A person, not a mailbox.

**Steps 1 to 3 removed more risk than steps 4 to 9 combined.** Most of the discipline is applied before anyone opens a notebook.

## Three questions for your capstone

Answer these alongside your six existing headings.

1. **People or resources?** Does your proposal score individuals or allocate resources? If it scores individuals, what changes if you reframe it as a resource question?
2. **Purpose and minimisation.** What is the stated purpose, was the data collected for that purpose, and what is the least data that achieves it?
3. **Oversight and redress.** Who makes the final decision, what can they see, what can they override, and how does an affected person find out and challenge it?

## Questions to take back to work

- What is the stated purpose of this system, written down, before we start?
- Was this data collected for that purpose?
- What is the least data that achieves it?
- Are we scoring people or allocating resources?
- What does a false positive cost the person it lands on?
- Can someone outside our team verify that this works?
- Who can override it, and is the override recorded?
- How does an affected person find out a decision was made, and challenge it?
- Who owns this by name, and what would make us switch it off?
