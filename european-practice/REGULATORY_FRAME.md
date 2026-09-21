# How Europe governs public-sector data analysis

Instructor reference. This is the legal and methodological frame behind "how it is done in Europe". It is written for a public-administration audience, not for lawyers.

> **Verify before delivery.** The content below reflects instruments in force as of the 2026 preparation date, including transition dates that were still running. Regulation in this area moves, and a directive is applied through each member state's own transposing law. Check the current position on the official sources listed at the end before teaching, and tell participants plainly that you are describing a framework, not giving legal advice.

## The one-sentence version

European practice does not treat data protection as a constraint bolted onto good analysis. It codifies most of what good analysis already requires — state your purpose before you collect, use no more data than the purpose needs, evaluate honestly, document what you did, keep a human answerable for the decision, and be able to explain it to the person affected.

Teach it that way. The course already teaches baselines, honest evaluation and stated limitations. The European frame is the same discipline written into law.

## Four instruments, and which one applies

The most common mistake is to assume GDPR covers everything. For an interior ministry it frequently does not.

| Instrument | What it governs | When it applies to you |
|---|---|---|
| **GDPR** — Regulation (EU) 2016/679 | General processing of personal data | Administrative processing: civil registry, licensing, permits, HR, service delivery, public correspondence |
| **Law Enforcement Directive (LED)** — Directive (EU) 2016/680 | Processing by competent authorities for the prevention, investigation, detection or prosecution of criminal offences, or the execution of criminal penalties | Police, criminal investigation, criminal records — a **separate regime**, applied through each member state's national transposing law |
| **AI Act** — Regulation (EU) 2024/1689 | Placing on the market and use of AI systems, by risk tier | Any AI system, including several uses that are specifically named for law enforcement and migration |
| **Convention 108+** — Council of Europe, CETS 223 | Data protection, as a treaty | The bridge instrument: it is open to states that are not EU or Council of Europe members, so it is the realistic reference point for a non-EU administration |

The same ministry routinely operates under more than one at once. A traffic authority issuing licences is under GDPR; the same authority's criminal enforcement work is under the LED.

### Why the LED matters more than people expect

Two of its requirements have no everyday GDPR equivalent, and both are directly about data quality — which makes them excellent teaching material for this course rather than a legal aside.

**Distinguish categories of data subject** (LED Art. 6). The controller must distinguish, as far as possible, between suspects, convicted persons, victims and witnesses or other parties. In data terms: these are different populations and must be flagged as such. A model trained without that distinction is a model that treats a witness like a suspect.

**Distinguish fact from assessment** (LED Art. 7). Personal data based on facts must be distinguished, as far as possible, from data based on personal assessments. In data terms: an officer's opinion recorded in a free-text field is not an observation. If it enters a model as a feature, the model learns the opinion.

**Limits on automated decisions** (LED Art. 11). A decision based solely on automated processing which produces an adverse legal effect is prohibited unless authorised by law with appropriate safeguards, including at minimum the right to human intervention.

These three are the most transferable ideas in the whole European frame, and they are analytical points as much as legal ones.

## The AI Act, by risk tier

The structure is what matters. Four tiers, and the obligations follow the risk, not the technology.

### Prohibited (Art. 5)

Several prohibitions name law-enforcement and public-authority uses specifically:

- **Social scoring** by or on behalf of public authorities, leading to detrimental treatment that is unrelated or disproportionate to the original context.
- **Individual crime-risk prediction** based solely on profiling or on assessing personality traits. There is a carve-out where the system supports a human assessment already based on objective, verifiable facts directly linked to criminal activity.
- **Untargeted scraping of facial images** from the internet or CCTV to build or expand facial recognition databases.
- **Emotion inference** in the workplace and in education, outside medical or safety purposes.
- **Biometric categorisation** to infer race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation.
- **Real-time remote biometric identification** in publicly accessible spaces for law enforcement, except in narrowly listed situations and subject to prior authorisation.

This is the part of the answer to "how is it done in Europe" that participants are least likely to expect: for a defined set of applications the European answer is that they are not done at all.

### High-risk (Annex III)

Annex III lists areas where a system is high-risk by default. Several are squarely interior-ministry business: **law enforcement**; **migration, asylum and border control**; **administration of justice**; **biometrics**; **critical infrastructure**; and — directly relevant to this course's Day 3 — **the evaluation and dispatch prioritisation of emergency first-response services, including police, firefighters and medical aid**.

That last one is worth pausing on in class. The emergency-call forecasting exercise on Day 3 is a teaching example on synthetic data. Deployed for real, in Europe, it would sit in a high-risk category with a defined obligation set.

High-risk obligations include risk management, **data governance including examination for bias** (Art. 10), technical documentation, **automatic logging** (Art. 12), transparency to deployers (Art. 13), **human oversight** by people with the competence and authority to act (Art. 14), and accuracy, robustness and cybersecurity (Art. 15).

Deployers have their own obligations (Art. 26): operate the system per its instructions, assign oversight to competent people with the authority to override, ensure input data is relevant and sufficiently representative, monitor operation, and keep logs.

**Public authorities deploying an Annex III high-risk system must also carry out a fundamental rights impact assessment** (Art. 27) — see below.

### Limited risk and minimal risk

Limited risk carries transparency duties: people must be told when they are interacting with an AI system, and certain generated content must be marked. Everything else is minimal risk with no specific obligations.

### Timeline

In force 1 August 2024. Prohibitions and AI-literacy duties applied from 2 February 2025; general-purpose AI obligations from 2 August 2025; most Annex III high-risk obligations from 2 August 2026; embedded high-risk systems under Annex I from 2 August 2027. Confirm the current state of these dates and of any amendment before teaching.

## The two assessments

Participants will meet these as documents. They are worth teaching as project design tools, because that is what they are.

**DPIA — Data Protection Impact Assessment** (GDPR Art. 35; LED Art. 27). Required where processing is likely to result in a high risk to rights and freedoms — which systematic large-scale evaluation of personal aspects generally is. It asks: what is the purpose, is the processing necessary and proportionate to it, what are the risks to individuals, and what measures address them.

**FRIA — Fundamental Rights Impact Assessment** (AI Act Art. 27). Required of deployers that are bodies governed by public law, for Annex III high-risk systems. It asks additionally: which categories of person are affected, what specific harms are foreseeable for them, what human oversight is in place, and what happens when the system is wrong.

The honest teaching point: a DPIA or FRIA done properly forces exactly the questions this course has been asking all week — what is the baseline, who is in the data, who is missing, what does each error cost, and who is accountable when it fails. A team that cannot answer the course's questions cannot complete these documents.

## The principles that actually bite

For a ministry planning an analytics project, these constrain design more than any specific article.

| Principle | What it means in practice | The design consequence |
|---|---|---|
| **Purpose limitation** | Data collected for one purpose may not simply be reused for an incompatible one | You cannot repurpose an administrative registry into an enforcement targeting tool without a legal basis. This surprises people more than anything else on this page. |
| **Data minimisation** | Only data adequate, relevant and limited to the purpose | "Collect everything and let the model choose" is not available. Feature selection becomes a legal question as well as a statistical one. |
| **Storage limitation** | Kept no longer than necessary | Your training set has an expiry date. Plan for retraining on a shrinking history. |
| **Accuracy** | Reasonable steps to correct or erase inaccurate data | Data-quality work is an obligation, not housekeeping. This is Day 1 of the course. |
| **Necessity and proportionality** | The interference must be no more than the aim requires | The legal test is not "is it useful" but "is it necessary, and is there a less intrusive way". |
| **Transparency and explanation** | The person affected can find out what happened | If you cannot explain a decision to the person it was made about, you cannot deploy it. |
| **Accountability** | You must be able to demonstrate compliance | Undocumented good practice does not count. Write it down as you go. |

Necessity and proportionality is the one to spend time on. It is the analytical habit European public bodies are trained into: before asking whether a model works, ask whether the intervention is warranted at all and whether a less intrusive method would achieve the same aim.

## Beyond the law: European public-sector data practice

Not everything in "how Europe does it" is regulation.

**Official statistics discipline.** The European Statistics Code of Practice frames quality across dimensions including relevance, accuracy and reliability, timeliness and punctuality, coherence and comparability, and accessibility and clarity. Public bodies are expected to publish methodology alongside figures, and to publish revisions when figures change. The transferable habit: a number without its method and its revision history is not an official figure.

**Open by default, with justified exceptions.** Public administrations are generally expected to publish non-sensitive data and to document what is withheld and why.

**Independent supervision.** Every member state has a data protection authority that can investigate and fine public bodies, and the European Data Protection Supervisor oversees EU institutions. Supervision is external, not internal to the ministry.

**Procurement as a control point.** Much public-sector AI arrives through vendors. European practice increasingly puts the evaluation requirements into the procurement contract — the vendor must supply the evidence, and the buyer must know what evidence to demand. This links directly to the course's vendor-critique activity.

## How to teach this to this cohort

**Present Europe's failures as European failures.** The two case studies in `CASE_STUDIES.md` are both Dutch, both recent, and both caused serious harm to citizens. Lead with them. A framework presented through its own failures is credible; a framework presented as a model to copy is a lecture, and this audience did not ask for a lecture — they asked how it is done.

**Describe, do not prescribe.** Participants work in a different legal system. The useful transfer is the reasoning — why purpose limitation exists, what the SyRI court actually objected to, why the AI Act separates risk tiers — not the article numbers. Say explicitly on Day 1: *we are going to show you the European approach and where it came from, including where Europe got it wrong; what transfers to your context is your judgement, not ours.*

**Keep it methodological.** Every European element in this course attaches to an existing analytical activity — see `DAILY_INTEGRATION.md`. None of it is a standalone compliance lecture, and it should never become one.

**You are not a lawyer.** Say so once, early. When a question goes beyond the framework, use the parking list and the standard sentence: *I want to verify that rather than give you an inaccurate answer.*

## Scope note for the instructor

This course teaches analytics for public administration: service demand, resource planning, emergency response, road safety, records quality, inspection planning and administrative processing. It does not provide operational guidance on surveillance, biometric identification or individual-level risk scoring of people.

That is not a gap in the material — for several of those applications, describing the European position *is* the content, and the European position is that they are prohibited or tightly restricted. Where a participant's real work touches them, the useful answer is the framework, the case law and the parking list, not an improvised lab.

## Official sources

Verify against these rather than against summaries, including this one.

- [Regulation (EU) 2016/679 (GDPR)](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [Directive (EU) 2016/680 (Law Enforcement Directive)](https://eur-lex.europa.eu/eli/dir/2016/680/oj)
- [Regulation (EU) 2024/1689 (AI Act)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- [Council of Europe Convention 108+ (CETS 223)](https://www.coe.int/en/web/data-protection/convention108-and-protocol)
- [European Data Protection Board — guidelines and opinions](https://www.edpb.europa.eu/)
- [European Statistics Code of Practice](https://ec.europa.eu/eurostat/web/quality/european-quality-standards/european-statistics-code-of-practice)
