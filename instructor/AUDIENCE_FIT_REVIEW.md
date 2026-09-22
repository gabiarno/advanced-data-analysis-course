# Audience fit review — confirmed cohort

Reviewed against commit `9a57450`, the no-code delivery pack.

## What we now know

| | Previously assumed | Confirmed |
|---|---|---|
| Who | Unknown; possibly non-technical | Ministry of Interior personnel, Saudi Arabia |
| Python | Unknown; assumed possibly none | They work with Python; not beginners |
| Background | Unknown | Domain and decision-making staff, **not** IT professionals |
| Explicit request | None recorded | To learn how this work is done in Europe |

Three of these change the material, and the fourth adds a requirement that was entirely absent.

## What the new profile broke

**The no-code route was the default.** It was a reasonable decision under uncertainty and the material is good, but as the default it now under-serves the room. A cohort that codes, put through a paper course, will conclude — correctly — that the course was not designed for them.

**The coding route was pitched at beginners.** Day 1 taught `df['units']` selects a column. The diagnostic asked for the result of `len([4, 7, 9])`. The pre-course pack said no prior experience was needed. For working analysts that is not merely redundant, it is mildly insulting, and it consumes the time the interesting material needs.

**Every scenario was retail and logistics.** Orders, delivery routes, customers, support tickets. For interior-ministry staff that is a translation tax on every exercise and a strong signal of a generic course.

**Nothing addressed European practice.** The single thing the cohort explicitly asked for did not exist anywhere in the repository.

**The audience assumption cut the other way too.** The previous revision added pair roles and a whole route to protect non-coders. Worth keeping as a fallback, but it is no longer what the room needs.

## What this revision changed

### The defaults flipped

`PROGRAMME.md` is rewritten around the coding route at working-analyst level. `instructor/NO_CODE_DELIVERY.md` is reframed as a fallback with four named situations where it is still the right choice — individual non-coders, environment failure, a cohort that contradicts the briefing, and specific activities where paper beats code. Nothing was deleted.

`assessments/ENTRY_DIAGNOSTIC.md` is rewritten: twelve questions pitched to discriminate within an analyst-level cohort, including three open judgement questions and a self-report section. It is deliberately not easy. `participant/PRE_COURSE_PACK.md` requires a working Python environment again, with a request to confirm it runs before travel.

### The European thread, which is new

`european-practice/` holds three instructor documents — the regulatory frame, four case studies, and a day-by-day integration plan. `participant/EUROPEAN_PRACTICE.md` is the participant-facing version, bound into the handbook as its fourth reference card. The bilingual glossary gains a governance section and three new interpreter ambiguities.

It is methodology, not a compliance module: every element attaches to an analytical activity that already exists. It leads with two European failures — SyRI and the Dutch childcare benefits scandal — because a framework presented through its own failures is credible and a framework presented as a model to copy is a lecture.

**It costs no extra time.** Because the cohort codes, the syntax teaching, guided first model and pipeline mechanics come out, freeing roughly the 150 minutes the European content needs. `DAILY_INTEGRATION.md` shows the trade day by day.

### The domain re-skin

`instructor/DOMAIN_MAPPING.md` re-frames all five days for public administration: service-centre requests, inspection scheduling, emergency call volume, records quality sampling, regional transaction records. **Every number is unchanged** — these are relabellings of synthetic data whose structure, expected answers and recorded results stay exactly as validated.

The capstone scenarios are re-skinned and three governance questions added to the one-pager.

### One structural decision

Every scenario sits on the **resource allocation** side of the European distinction, never the **scoring people** side. That is deliberate and it is content rather than avoidance: for several person-scoring applications the European position is that they are prohibited or tightly restricted, so describing that position is the answer the cohort asked for. Participants meet those applications as a governed discussion with real case law instead of as a lab exercise.

If a participant brings a person-scoring problem from their own work, the guidance is to reframe it with them rather than refuse it. Most have a resource-shaped sibling.

## What was not done, and why

**The notebooks still say `retail_orders.csv`.** Completing the re-skin means editing five days of notebooks, solutions, recorded results and figures, then re-running everything from clean kernels and diffing every number. This environment has no scientific Python installed, so none of that could be validated. Shipping unvalidated notebooks would be worse than shipping honestly-labelled ones with a spoken mapping. Costed at about 10 hours in `DOMAIN_MAPPING.md`.

In the meantime the instructor says one sentence at the start of each lab: *"This column is called `units`; in your work it is documents processed. The analysis is identical."* A cohort at this level handles that without difficulty.

**The slide plans and decks still carry the retail framing**, and the Canva decks still have their outstanding review items plus the missing Day 4 design.

**The six recommended teaching modules remain specified, not implemented**, for the same validation reason. With the confirmed profile their priority has shifted: rolling-origin backtesting and explainability matter more to this cohort than they did to an unknown one.

**No real dataset.** Still open, still needs a licence decision.

## Merged with the workshop revision

This review was written against `9a57450`. While it was open, `main` gained two substantial commits — a tutor script, an illustrated PDF handbook built from `participant/handbook_content.json`, a rewritten participant handbook with the earlier one preserved as `HANDBOOK_TECHNICAL_REFERENCE.md`, fifteen activity cards, and five executed experiments in `workshops/`.

That work independently delivers several items this review had only specified: rolling-origin backtesting, validation-based cost thresholds, case-mix reversal and monitoring triggers, all executed with recorded results. Those rows in the backlog are closed by it, not by this change.

The merge took the newer versions of every shared file. Two consequences worth knowing:

- **The timetable moved.** Workshops now run 50/50/60 minutes with 20 minutes of peer review. `european-practice/DAILY_INTEGRATION.md` was written against the older structure; its content holds but its placements need re-fitting to the activity cards, which is roughly two hours and has not been done.
- **The no-code workbook is no longer bound into the printed handbook.** That was a deliberate choice on `main` and it was preserved.

## An open disagreement to settle

`PROGRAMME.md` on `main` says: *"The venue does not make these methods uniquely European. Local examples can be used if helpful, but geography is not a teaching objective."*

That is correct about methods and about examples, and the sentence was kept. But the cohort's stated request was to learn how this work is done in Europe, and there is a reading of that request which is neither geography nor decoration: the **governance framework** around public-sector analysis genuinely differs, and for ministry staff it is substantive. That is what `european-practice/` contains — not European-flavoured examples.

The merge keeps both, with the European material scoped explicitly to governance rather than geography. **If the intent was to drop the European thread rather than to scope it, say so and it comes out** — it is self-contained in `european-practice/`, `participant/EUROPEAN_PRACTICE.md`, one section of `PROGRAMME.md` and one line in the build script. This is a judgement about what the client asked for, and it is not the instructor's to make alone.

## What the instructor must verify before delivery

1. **The regulatory content is current.** Regulation moves and a directive applies through each member state's transposing law. Check the official sources at the end of `REGULATORY_FRAME.md`, not summaries — including that one.
2. **The three limits are stated on Day 1.** Not a lawyer; a framework rather than legal advice; and it does not describe the participants' own national law, which is what governs their work.
3. **The interpreter has the governance vocabulary.** Proportionality, purpose limitation, redress, fundamental rights, and the three new ambiguities in the glossary need their own briefing time.
4. **The diagnostic results are read before Day 1 is finalised.** A confirmed profile is a briefing, not a guarantee. `ENTRY_DIAGNOSTIC.md` sets out what each pattern of results means, including when to switch routes and tell the organiser.

## Revised questions for the organiser

The earlier list stands, minus the ones now answered. Newly relevant:

1. Are all 20 participants at the stated level, or is there a range? A mixed room is manageable but should be planned, not discovered.
2. Can participants install Python on their official laptops, or are they locked down? This now materially affects the default route.
3. Which directorates are represented? It determines which of the five domain scenarios to lead with.
4. Is the European content expected to be described, or does the organiser expect guidance applicable to their own legal framework? These are very different deliverables and only the first is in scope.
5. Does the ministry expect any written output from the week — a summary of the capstones, a cohort report?
6. Still open from before: contact hours, interpretation mode, printing, LPC branding, certificates.
