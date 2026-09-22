# Entry diagnostic — 12 minutes

Placement, not grading. The cohort is confirmed as comfortable with Python and working at analyst level, so this is pitched to discriminate *within* that range rather than to check whether people can code. It should not be easy.

Send it before the course with the pre-course pack, or run it in the Day 1 opening. Share the questions separately from the key.

---

## Part A — working with data

**1.** A table of service requests has one row per request. A directorate asks for "the number of customers served". What is the first thing you need to establish?
A: the total row count; B: whether a requester can appear in more than one row; C: the date range.

**2.** A numeric fee column contains missing values. Which statement is most defensible?
A: fill them with the column mean, since it does not change the average; B: fill them with zero, since no fee was recorded; C: leave them missing, report how many, and state that totals cover only priced rows.

**3.** You filter a dataframe and then assign to a column of the result. Python warns you about setting a value on a copy. What is the actual risk?
A: the code will crash on the next run; B: your assignment may not affect the object you think it does; C: nothing, the warning is cosmetic.

## Part B — evaluation

**4.** You have three years of daily call volumes and want to forecast next week. How should you split the data?
A: randomly, 80/20; B: hold out the most recent period; C: randomly, but stratified by day of week.

**5.** Records belong to 40 regional offices, several rows per office. You want to know whether the model works for an office it has not seen. Split by:
A: random rows; B: office, so all of an office's rows sit on one side; C: date.

**6.** A classifier reports 96% accuracy. 4% of cases are the positive class. What have you learned?
A: the model is strong; B: essentially nothing — predicting the majority class always scores 96%; C: that the classes need rebalancing before anything else.

**7.** Missing an overrunning inspection round costs a cancelled citizen appointment. A false alarm costs an inspector half a day. Which metric should lead?
A: accuracy; B: precision; C: recall; D: it depends on how the two costs compare, and you have to establish that first.

**8.** You tune a model, check the test score, adjust, and check again — four times. What is the status of that test score?
A: valid, the test set was never trained on; B: optimistic, because model selection has now used it; C: valid if you used cross-validation during tuning.

## Part C — interpretation and judgement

**9.** A forecast comes with a 95% interval. Which reading is correct?
A: 95% of future values will fall inside it; B: it reflects the model's uncertainty under its own assumptions, which may not hold; C: the forecast is right 95% of the time.

**10.** A vendor states their system is 99% accurate. Name the two questions you would ask first.

_______________________________________________________________

**11.** A model trained on records from investigated cases is used to decide which cases to investigate next. What goes wrong over time?

_______________________________________________________________

**12.** An analysis shows collisions concentrate at eight junctions. A colleague concludes those junctions are dangerous by design. What would you need before accepting that?

_______________________________________________________________

---

## Part D — self-report

Not scored. Answer honestly; it changes how the week is pitched, not how you are judged.

- How often do you write Python? *Daily · Weekly · Occasionally · Rarely*
- Which of these have you used? *pandas · matplotlib · scikit-learn · statsmodels · SQL · Spark · none*
- Have you built a model that someone else then used to make a decision? *Yes · No*
- What kind of decisions does your work support?
- What would make this week worth your time?

---

## Instructor key

**1** B — without knowing whether requesters repeat, a row count is not a person count. **2** C. **3** B. **4** B. **5** B. **6** B. **7** D — any single-metric answer is incomplete; the cost comparison comes first. **8** B. **9** B.

**10** Strong answers name any two of: what is the baseline; how was the data split; how large is the test set; how many times has it been used; is the test data representative of our population; what does each error type cost.

**11** A feedback loop. The model learns from cases that were investigated, which were selected by the previous policy. Investigating group A produces findings in group A, which appears to confirm the model. It cannot learn about cases nobody looked at. This is the mechanism behind the Dutch childcare benefits failure covered on Day 2.

**12** Exposure — traffic volume at each junction. Eight junctions with the most collisions may simply be the eight busiest. Also: the time window, whether reporting practice differs by location, and whether the concentration exceeds what chance would produce.

## Reading the results

Questions 1–3 are foundational; at this cohort's stated level, most should get all three. Questions 4–8 are the evaluation core and are where the course spends most of its time — struggles here confirm the planned pitch is right. Questions 9–12 test judgement rather than technique; these are the ones that separate a competent analyst from one ready to advise a decision-maker, and 11 and 12 specifically preview the European thread.

**If most participants answer 4–8 correctly**, move faster through evaluation mechanics and go deeper on the European material, rolling-origin backtesting and explainability. Say so to the organiser.

**If 4–8 are mixed**, the programme is pitched correctly as written.

**If most struggle with 1–3**, the briefed profile does not match the room. Do not silently re-pitch the whole week — use the no-code route for the affected participants, keep the coding route for the rest, and raise the mismatch with the organiser the same day, in writing.

Do not equate a score with professional competence, and do not infer ability from title, nationality or English fluency.
