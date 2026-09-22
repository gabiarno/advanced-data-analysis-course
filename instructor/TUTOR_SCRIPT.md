# A good analysis earns its place in a decision

## Complete English tutor script | Five-day workshop

For 20 experienced analysts who already use Python. Five hours daily, including two 15-minute breaks. English delivery with Arabic interpretation. Venue: Genoa. Context: participants from Saudi Arabia's Ministry of Interior, seeking useful additional techniques and hands-on analytical practice.

This is the single speaking document. It brings together the opening, explanations, demonstrations, activity instructions, questions, likely responses, debriefs, transitions and closing for every day. The existing day-level TEACHING_GUIDE files remain the technical reference; RUNBOOK is the older coding timetable; QUESTION_BANK holds extra questions. Follow this script and the revised PROGRAMME for this delivery. The no-code pack is now a fallback, not the default route.

Read the paragraphs labelled **Say** aloud or adapt them to your natural voice. Bracketed directions are for you, not the audience. A script can prepare your interventions, but cannot predict every participant answer: the response branches below cover the likely misunderstandings. Do not fill every minute with speech. Quiet thinking, running a cell, discussing a result and waiting for interpretation are part of the lesson.

### Your manner in the room

Be warm, direct and curious. Invite challenge without putting people on the spot. Say “Let's check that together” more often than “That is wrong.” Ask about their actual analytical work rather than their job titles. Use participants' names when they offer them. Avoid jokes that depend on accent, religion or national stereotypes. Keep the style conversational and participatory. Geography is not a learning objective.

Use fictional service appointments, facilities inspections, logistics and aggregate workloads as transfer cases. The original notebooks still use retail orders, delivery routes and service messages. Say explicitly when you move from their numerical examples to a public-service analogy. Do not rename a measured variable and pretend the model has been validated for a different task. We are not using ministry records or drawing conclusions about operational policing.

### Timing and setup

Each day: 0–15 retrieval challenge; 15–30 worked example; 30–80 Workshop A; 80–100 peer review; 100–115 break; 115–130 demonstration; 130–180 Workshop B; 180–195 debrief; 195–210 break; 210–270 Workshop C; 270–290 reports (Day 5 final practical); 290–300 exit and close. This protects 180 minutes for workshops and peer review. All timings include interpretation. In each fifteen-minute demonstration, use only the essential explanation, a small code example and interpretation; the longer explanation paragraphs below are prompts to draw on during practice, not a compulsory lecture. Speak in short chunks, normally one or two sentences, then pause. Do not make the interpreter hold a paragraph of equations in memory.

Ten pairs work at laptops; two pairs form each of five reporting groups. One partner operates, the other checks and explains; swap at a natural checkpoint, not halfway through a calculation. Someone may prefer to explain first. Do not force a public coding demonstration. Every participant writes an individual final answer.

Before class, run only the demonstrations you will use. Keep each worked_RESULTS file open; for Day 1 use the answer key and worked notebook. Copy the repository locally. The tutor preparation plan in this script is: rehearse Days 1–2 on preparation days 1–3; Day 3 on preparation day 4; Day 4 on day 5; Day 5 and the capstone on day 6; perform a translated rehearsal and technical checks on day 7. Ask the organiser whether the five daily hours include breaks; this script provides 22.5 contact hours, not 25.

### Reusable lines for the whole week

**When a cell fails:** “Let's keep the analytical question in view. I have the saved output here. We can interpret it now and fix the environment at the break.” [Allow at most one minute of debugging.]

**When you do not know:** “That is a useful question, and I want to give you a reliable answer. I'll write it down, check it and come back to you tomorrow.” [Record an owner and return time; do not promise an answer before checking.]

**When the room goes quiet:** “Take thirty seconds to write your own answer. Then compare with the person next to you. I'll ask for two different views.”

**When someone answers incorrectly:** “I can see the reasoning. Let's look at the denominator together. Which cases are included in that percentage?”

**When one person dominates:** “Thank you. Let's hear from a group that has not spoken yet. You can agree, disagree or add a limitation.”

**When interpretation takes longer:** “We'll leave the optional experiment for later and protect the time for your analysis. Keep your result and one question ready.” [Drop extensions; do not rush interpretation or remove the breaks.]

**When asked what is new here:** “Let's test a technique against a problem you already recognise. The value is what it adds to your analysis, not where it comes from.”

---

## Day 1 | Before we trust the dashboard

### 0–15 | Meet the people, then the problem

**Say:** “Good morning, everyone. Welcome to Genoa. This week we are going to work as an analysis team. You already use Python and work with data, so we won't spend the morning introducing variables or explaining what a spreadsheet is. We will spend our time on the difficult part: deciding whether an analysis is good enough to support an action.”

[Pause for interpretation. Introduce yourself truthfully; do not claim experience you do not have.]

**Say:** “Before I show you anything, tell the person next to you about one analysis you actually do. What information arrives? What do you produce? Who uses the result? Please keep it general; we don't need names, real records or confidential details.”

[Allow three minutes plus interpretation. Invite three brief examples, not twenty introductions. Write the decisions on a board.]

**Say:** “I hear a common pattern: a report is useful only if someone can do something with it. By Friday, each group will have a short proposal for one of those decisions. It should be clear enough for a manager to act on, and honest enough for another analyst to challenge.”

**Ask:** “Which is most familiar to you: cleaning and charts, forecasting, or training predictive models?” [Show of hands; adjust extensions. This is experience mapping, not an exam.]

**Say:** “There is no prize for finishing first. A good contribution might be a line of Python, a question about a missing value, or noticing that our conclusion is too strong. We need all three.”

### 15–30 | A result you could put your name to

**Say:** “Imagine a service manager says: 'The dashboard says one office is slower. Should I move staff?' Your first answer should probably be a question. Are the offices doing comparable work? Did the reporting period change? Are unresolved cases missing from the calculation? A beautiful dashboard cannot answer a poorly defined comparison.”

**Ask:** “What would you check before showing that chart to a director?” [Accept units, period, missingness, definitions, workload and denominator.]

**Say:** “Let's test those habits on a small retail dataset. This is a teaching example, not a ministry dataset. The transferable skill is auditing the evidence. We have orders, quantities, prices and channels. First inspect; then decide; then change. If you clean while you are still discovering what a column means, it is easy to remove the very thing you should have investigated.”

[Open Day 1 worked notebook. Show shape, head, types and missing-value counts; leave each output visible during interpretation.]

**Say:** “A duplicate-looking row is a question, not automatically an error. Here the teaching rules confirm two accidental duplicates. A negative sales quantity is invalid in this particular sales table. In a returns table, it might be perfectly valid. The business definition comes before the filter.”

**Say:** “And this 80-unit order? It looks unusual. We know it is a valid bulk order, so we keep it. Outlier detection gives us candidates for review; it does not give us permission to erase inconvenient observations.”

**Ask:** “If a price is missing, what would entering zero mean?”

**If they say ‘it lets the calculation run’:** “It does, but it also says the item was free. That is a new claim. We need to distinguish not recorded from genuinely zero.”

**Say:** “A useful habit is to write a small decision log: what I found, what I did, why, and how many rows were affected. Another analyst should be able to reproduce your result without guessing your intentions.”

### 30–80 | Data-quality clinic

**Say:** “Open day-01-eda/student.ipynb. Audit first; document what each issue means before editing. Ask your partner to challenge one rule.”

[Format: Pairs investigate, then exchange one disputed cleaning decision. Follow the 50-minute activity pattern in workshops/ACTIVITY_CARDS.md; all instructions and discussion allow for interpretation.]

**Say:** “Your output is: A five-line audit with row counts, actions and reasons. Before running the experiment, write what you expect to happen. At the end, show which assumption you changed and explain the result to your partner.”

**While circulating, ask:** “Which rule would change if this were a returns table?”

**Facilitator check:** 122 raw; 2 duplicates; 1 invalid quantity; 119 valid; 116 priced. Keep the confirmed bulk order.

**Support line:** “Use the prepared cell or saved result, then explain why it answers the question.” **Stretch line:** “Change one assumption and predict its effect before running. Would your recommendation change?”


### 80–100 | Debrief: follow the rows

[Peer review first: 5 minutes reading another pair\'s output,8 checking its evidence,5 discussing feedback and 2 writing a revision. Use the lines below as prompts during this exchange, not an additional lecture.]

**Say:** “Let's reconcile the counts. We start with 122 rows. Removing two duplicates and one invalid sale leaves 119 valid orders. Three valid orders have no price, so 116 contribute to known revenue. Two records have no channel; we show Unknown rather than make them disappear.”

**Ask:** “Which of those numbers belongs beside a revenue chart?” [Expected: priced count and missing-price caveat; valid count is useful context.]

**Say:** “Notice how much work happens before modelling. This is not a beginner's chore. Getting these definitions right is part of senior analytical work.”


### 100–115 | Break

**Say:** “Let's take fifteen minutes. Save your notebook and return ready to compare approaches.”

### 115–130 | Give the numbers a fair comparison

**Say:** “The known total is EUR 10,210. Store contributes EUR 6,310, Online EUR 3,700 and Unknown EUR 200. That tells us where the recorded revenue sits. It does not yet tell us which channel performs better.”

**Ask:** “What could make a channel total larger?” [More orders, larger orders, different products, the bulk order, missingness.]

**Say:** “Store has 60 priced orders and Online has 54. Mean known revenue per priced order is about EUR 105.17 and EUR 68.52 respectively. Those are different comparisons from total revenue. Neither establishes that moving a customer from one channel to the other changes spending.”

[Show a bar chart with a zero baseline and labelled units. Then show the original distribution plot.]

**Say:** “A mean is useful, but a few large orders can pull it upwards. The median describes the middle order. Standard deviation and the interquartile range describe different aspects of spread. Rather than recite definitions, ask what decision the summary serves. A manager planning capacity might need the upper tail as much as the average.”

**Say:** “Use bars for category comparisons, a line for change over time, a histogram for a distribution and a scatterplot for two numerical quantities. These are starting choices, not rigid rules. Give your chart a title that makes a defensible point, label the units, and state the population. If a bar starts above zero, its length can exaggerate a modest difference.”

**Ask:** “Would you put 'Store is the best channel' on this chart?”

**If someone says yes:** “What does best mean: revenue, margin, cost to serve, growth or satisfaction? Let's choose the measure before the claim.”

### 130–180 | Chart makeover

**Say:** “Make a channel chart from the cleaned data. Your partner has one minute to explain it without help. Revise whatever they misunderstood. Then compare the main result with the labelled bulk-order sensitivity.”

[Format: Pairs become an analyst and a busy service manager; switch halfway. Follow the 50-minute activity pattern in workshops/ACTIVITY_CARDS.md; all instructions and discussion allow for interpretation.]

**Say:** “Your output is: Before/after chart and a caption explaining one improvement. Before running the experiment, write what you expect to happen. At the end, show which assumption you changed and explain the result to your partner.”

**While circulating, ask:** “Can the chart be correct but still encourage the wrong decision?”

**Facilitator check:** Known revenue EUR 10,210; missing prices excluded. A total is not a causal channel comparison.

**Support line:** “Use the prepared cell or saved result, then explain why it answers the question.” **Stretch line:** “Change one assumption and predict its effect before running. Would your recommendation change?”


### 180–195 | Compare approaches

**Say:** “Let's hear two different approaches. What did each assume? Which evidence supports the result? Write one change you would make after hearing the other pair.” [Select two brief reports, interpret and resolve one misconception.]

### 195–210 | Break

**Say:** “Fifteen minutes. Save your work; afterwards we will test a further assumption.”

### 210–270 | The ranking reversal

**Say:** “Use Day 1 of workshops/experiments.ipynb. Guess the faster team overall and within each case type before running. Try common case mixes of 20%,50% and 80% complex work. Then write the briefing and choose your capstone decision.”

[Format: Predict privately, calculate in pairs, then compare reasoning in fours. Follow the 60-minute activity pattern in workshops/ACTIVITY_CARDS.md; all instructions and discussion allow for interpretation.]

**Say:** “Your output is: A comparison under observed and common mixes; a decision and its owner. Before running the experiment, write what you expect to happen. At the end, show which assumption you changed and explain the result to your partner.”

**While circulating, ask:** “What would you request before comparing two offices?”

**Facilitator check:** Pooled means A 12/B 23.3; at 50/50 A 20/B 16.5. B is faster within both types. Different workload mixes reverse the pooled ranking.

**Support line:** “Use the prepared cell or saved result, then explain why it answers the question.” **Stretch line:** “Change one assumption and predict its effect before running. Would your recommendation change?”


### 270–290 | Five short reports

**Say:** “Each group has five minutes including interpretation. Give your main finding and the strongest limitation. We will take one short challenge if time allows.”

**Useful feedback:** “Your conclusion matches your evidence.” / “You have named a limitation; now tell us what action it changes.” / “That is a causal statement. What extra design would support it?”

### 290–300 | Close

**Say:** “Write your own answer: what is one cleaning decision you would document differently after today? Then add one sentence to your capstone: the decision we want to improve is…”

**Closing:** “Tomorrow we will ask a model to predict something. Keep today's habits. A predictive score still depends on definitions, missing data and a fair comparison.”

---

## Day 2 | Is this model useful, or just impressive?

### 0–15 | Put the decision on the board

**Say:** “Yesterday we asked whether the report was trustworthy. Today we ask whether a prediction is useful. Think of a facilities team planning tomorrow's visits. An estimate of duration could help allocate capacity. A warning that a visit may run late could support a different action. Those are related questions, but they are not the same prediction task.”

**Ask:** “Who would act on the prediction? What information exists at that moment?” [Have pairs name one available and one unavailable input.]

**Say:** “Our notebook uses independent synthetic delivery routes. Distance and planned stops are inputs; actual duration is an outcome. Keep that setting intact. We will discuss how its evaluation would need to change for future service appointments.”

### 15–30 | Train, compare, then test

**Say:** “Regression predicts a number. Classification predicts a category. Clustering groups similar observations without an outcome label. These names are helpful only after we have written the question. Predicting minutes is regression. Predicting a delayed flag is classification.”

[Open Day 2 student notebook, sections 1–2. Point to inputs, outcome and the split.]

**Say:** “We have 400 synthetic routes. We set aside 100 and use 300 for development. Inside development, cross-validation lets us compare choices. The final test has a different job: checking the chosen procedure on examples it has not used for those choices.”

**Ask:** “What happens if we keep looking at the final test and adjusting until we like it?”

**Expected response line:** “Exactly: the test is quietly becoming part of development. The score may still be a number, but it no longer has the interpretation we promised.”

**Say:** “A random split is reasonable in this independently generated teaching case. It is not a universal default. For next month's appointments, we should normally simulate the past-to-future boundary; if repeated entities appear, we must also think about group overlap.”

**Say:** “Before the model, we need a baseline. Here the baseline predicts a training-derived average duration. It is deliberately simple. If our elaborate method cannot improve on that, the extra complexity has not earned its place.”

[Demonstrate fit and predict.]

**Say:** “Fit learns from the training examples. Predict applies what was learned. Mean absolute error, or MAE, is the average size of the prediction error in the original units. If errors are five, ten and fifteen minutes, MAE is ten minutes. It does not promise every route is within ten minutes.”

**Say:** “Notice that the imputer sits inside the pipeline. It learns the filling values from the training part of each fold. If we computed them from the whole dataset first, held-out information would influence the process.”

### 30–80 | Predict, run, explain

**Say:** “Open Day 2 student notebook. Predict whether regression will beat the training-mean baseline. Run the example. Explain the difference and identify one feature that would arrive too late for dispatch.”

[Format: Both partners write a prediction before the operator runs the model. Follow the 50-minute activity pattern in workshops/ACTIVITY_CARDS.md; all instructions and discussion allow for interpretation.]

**Say:** “Your output is: Prediction, observed result and a two-sentence explanation. Before running the experiment, write what you expect to happen. At the end, show which assumption you changed and explain the result to your partner.”

**While circulating, ask:** “What would make the improvement operationally irrelevant?”

**Facilitator check:** Saved MAE 24.34 vs 8.43 minutes. The synthetic evaluation does not establish real-service performance.

**Support line:** “Use the prepared cell or saved result, then explain why it answers the question.” **Stretch line:** “Change one assumption and predict its effect before running. Would your recommendation change?”


### 80–100 | Numbers without salesmanship

[Peer review first: 5 minutes reading another pair\'s output,8 checking its evidence,5 discussing feedback and 2 writing a revision. Use the lines below as prompts during this exchange, not an additional lecture.]

**Say:** “The recorded example gives MAE about 24.34 minutes for the baseline and 8.43 for the model. That is a substantial improvement on this synthetic test. It is not yet evidence of the same improvement in your service.”

**Ask:** “What else would an operational owner ask?” [Error distribution, busy periods, costs, representativeness, availability, monitoring.]

**Say:** “We can be pleased with a result and still be careful about its scope. That is how we make an analysis credible.”


### 100–115 | Break

**Say:** “Let's take fifteen minutes. Save your notebook and return ready to compare approaches.”

### 115–130 | Different mistakes, different consequences

**Say:** “Imagine two predictions. One warns of a delay that never happens. The other misses a delay that does happen. Both are mistakes, but they may create very different costs. Accuracy puts them in the same total. Your decision may not.”

[Draw or show the confusion matrix. Rows actual; columns predicted.]

**Say:** “In our saved test, 55 routes are correctly predicted on time; two are false alarms; nine delays are missed; 34 delays are detected. Read those as events before turning them into percentages.”

**Ask:** “For recall of delayed routes, do we divide by all routes or all actual delays?”

**Response:** “All actual delays: 34 out of 43, about 79.1%. Precision asks a different question: of the 36 alerts, 34 were correct, about 94.4%. Neither is the same as accuracy, which is 89% here.”

**Say:** “A tree makes a sequence of feature-based decisions. Greater depth can fit more detail, including noise. A forest combines many randomised trees and can reduce some instability. Logistic regression is another useful baseline classifier. None of these names guarantees a winner.”

**Say:** “We compare candidates on development data. Maximum depth is a hyperparameter: a setting we choose around the learning process. Training performance shows fit to examples already seen; validation performance is closer to the question of generalisation. A gap is a warning to investigate, not a mathematical verdict that every deep tree is bad.”

### 130–180 | The cost negotiation

**Say:** “Use the classification results. Negotiate which error matters more. Compare missed-delay cost 100/false-alarm 20 with missed-delay 1/false-alarm 20. Prepare a recommendation on the supplied fixed predictions.”

[Format: One partner owns the service decision; the other owns the model. Swap the cost assumptions, not the final-test threshold. Follow the 50-minute activity pattern in workshops/ACTIVITY_CARDS.md; all instructions and discussion allow for interpretation.]

**Say:** “Your output is: Cost comparison and explicit assumptions agreed by both roles. Before running the experiment, write what you expect to happen. At the end, show which assumption you changed and explain the result to your partner.”

**While circulating, ask:** “Which costs or consequences did this simple calculation omit?”

**Facilitator check:** Model 940 vs baseline 4,300; under changed costs 49 vs 43. These are illustrative error costs, not measured benefits.

**Support line:** “Use the prepared cell or saved result, then explain why it answers the question.” **Stretch line:** “Change one assumption and predict its effect before running. Would your recommendation change?”


### 180–195 | Compare approaches

**Say:** “Let's hear two different approaches. What did each assume? Which evidence supports the result? Write one change you would make after hearing the other pair.” [Select two brief reports, interpret and resolve one misconception.]

### 195–210 | Break

**Say:** “Fifteen minutes. Save your work; afterwards we will test a further assumption.”

### 210–270 | Model review panel

**Say:** “Use Day 2 of workshops/experiments.ipynb. Compare thresholds on validation data at missed-event costs 10,50,100. Fix the policy and threshold before opening the final cell. Another pair challenges the split, baseline and cost choice. Keep the original clustering/PCA walkthrough to ten minutes.”

[Format: Two pairs exchange roles as proposing team and reviewers. Follow the 60-minute activity pattern in workshops/ACTIVITY_CARDS.md; all instructions and discussion allow for interpretation.]

**Say:** “Your output is: A threshold decision record, one final evaluation and one unresolved limitation. Before running the experiment, write what you expect to happen. At the end, show which assumption you changed and explain the result to your partner.”

**While circulating, ask:** “What evidence would make the review panel approve a limited pilot?”

**Facilitator check:** Choose using validation only. Test results describe the fixed procedure. Do not select another threshold from final-test performance.

**Support line:** “Use the prepared cell or saved result, then explain why it answers the question.” **Stretch line:** “Change one assumption and predict its effect before running. Would your recommendation change?”


### 270–290 | Report like a colleague

**Say:** “Give us your chosen method, the evidence used to choose it and the most costly mistake. Please say 'on this evaluation' rather than 'this model is best'.”

**If asked about explainability:** “A feature-importance result can help us understand model behaviour. It does not by itself tell us what would happen if we intervened on that feature. Correlated inputs also complicate attribution. We should inspect explanations alongside performance and domain knowledge.”

### 290–300 | Close

**Say:** “Individually, write one example of leakage and one reason a more accurate model might still be the worse decision. Tomorrow the order of the observations will become central: what can we honestly know before the future arrives?”

---

## Day 3 | The future arrives one day at a time

### 0–15 | Start with a real planning question

**Say:** “Suppose a service centre needs next week's staffing plan by Thursday afternoon. A forecast produced on Friday may be accurate and still arrive too late. Forecasting starts with the decision time, the forecast horizon and the information available at that cutoff.”

**Ask:** “In your work, do you usually predict the next day, next week or next month? What changes the demand?” [Accept calendar effects, policy changes, campaigns and recording changes; do not assume a specific Saudi working week.]

**Say:** “The weekly pattern in our synthetic dataset is a teaching design. For a real service, we would inspect its actual working calendar, holidays and changes. We would not copy another country's calendar assumptions.”

### 15–30 | Give simple forecasts a fair chance

[Show the ordered series, train/test boundary and training decomposition.]

**Say:** “Trend is a sustained direction. Seasonality repeats at a known period. A cycle need not have a fixed period. A rolling mean can help us see the series, but a smooth line is not automatically a complete decomposition.”

**Say:** “We have 210 daily observations. The final 28 form our holdout; the earlier 182 are for development. Before fitting anything, check frequency, missing dates and definitions. A day without a record might mean zero activity, a closed office or a collection failure. Those are different situations.”

**Ask:** “Why not shuffle the dates and use the same random split as yesterday?”

**Expected:** “Because that could let the procedure learn from the future while pretending to predict the past. Our evaluation should resemble the way the service will use the forecast.”

**Say:** “Our first baseline repeats the last value. The second repeats the latest week. Neither sounds sophisticated, which is exactly why they are useful comparisons.”

**Say:** “ARIMA combines previous values, differencing and past-error structure. The letters are less important than its assumptions. In ARIMA(p,d,q), p controls autoregressive terms, d differencing and q moving-average error terms. The fixed (1,1,1) example does not explicitly represent the weekly seasonal structure. It is a demonstration, not a tuned champion.”

**Ask:** “If the simple weekly rule wins, has the lesson failed?”

**Say:** “No. We have learned something useful about this data and these choices. The job is not to defend the complicated model.”

### 30–80 | Forecast comparison desk

**Say:** “Run the predeclared Day 3 forecasts. Explain why the weekly rule wins in the saved example. Use training-only validation for any changes. No points for a better final-test score obtained by repeated tuning.”

[Format: Pairs propose a forecast; another pair checks the evidence behind the choice. Follow the 50-minute activity pattern in workshops/ACTIVITY_CARDS.md; all instructions and discussion allow for interpretation.]

**Say:** “Your output is: Comparison with baseline, cutoff date and limitation. Before running the experiment, write what you expect to happen. At the end, show which assumption you changed and explain the result to your partner.”

**While circulating, ask:** “Would the same method necessarily win during a policy change?”

**Facilitator check:** Saved weekly MAE 5.53; last 22.38; fixed ARIMA 22.11. Complexity does not guarantee improvement.

**Support line:** “Use the prepared cell or saved result, then explain why it answers the question.” **Stretch line:** “Change one assumption and predict its effect before running. Would your recommendation change?”


### 80–100 | More than one lucky window

[Peer review first: 5 minutes reading another pair\'s output,8 checking its evidence,5 discussing feedback and 2 writing a revision. Use the lines below as prompts during this exchange, not an additional lecture.]

**Say:** “In the recorded example, weekly MAE is about 5.53, last-value MAE 22.38 and ARIMA MAE 22.11. Those results belong to one final window. A service might behave differently in a peak month.”

[Draw three expanding training windows with the next window held out.]

**Say:** “Rolling-origin evaluation repeats the practical question at several historical cutoffs: what could we have forecast then? Fit the procedure using the past at each cutoff and evaluate the next window. Reserve a final period for the final claim. The original diagram explains the design. In Workshop C, the added experiment will execute four historical origins before checking a separate final holdout.”


### 100–115 | Break

**Say:** “Let's take fifteen minutes. Save your notebook and return ready to compare approaches.”

### 115–130 | Text is messy for good reasons

**Say:** “A request might say, 'The appointment was cancelled and I still haven't received my refund.' Is that scheduling or payment? A person can mean two things at once. Our database may ask for one label. Sometimes the limitation is in the task definition before it is in the model.”

[Show the notebook's English delivery/billing messages.]

**Say:** “The teaching pipeline turns words and short sequences into numerical features, using TF-IDF. It then fits a classifier. TF-IDF gives weights based on term frequency and document frequency. It is not the same as a human reading the request. The vectoriser belongs inside the pipeline so the training stage learns its vocabulary without test information.”

**Say:** “Our categories are delivery and billing, not positive and negative sentiment. Keep that distinction clear. A polite message can describe a serious service failure.”

**Ask:** “What should happen when a message is ambiguous?” [Human review, multiple labels, clarification or a documented routing rule.]

**Say:** “Embeddings offer another numerical representation, and language models can produce or classify text in more flexible ways. The workflow still needs a defined task, representative evaluation, handling of uncertainty and a person responsible for mistakes. We are not making an API call or validating a language model in this course.”

**Say:** “English results do not validate Arabic performance. Translation of today's instruction helps us learn together; it does not create an evaluated Arabic classifier. A real implementation would need representative language data and review by people who understand the relevant usage.”

### 130–180 | Write a case that challenges the classifier

**Say:** “Run the Day 3 text pipeline. Write one multi-topic message and one ambiguous message. Exchange them before running predictions. Compare human judgement with the model and agree an escalation rule.”

[Format: Pairs exchange two authored messages; the other pair must explain the labels and uncertainty. Follow the 50-minute activity pattern in workshops/ACTIVITY_CARDS.md; all instructions and discussion allow for interpretation.]

**Say:** “Your output is: Two test cases, observed predictions and a human-review rule. Before running the experiment, write what you expect to happen. At the end, show which assumption you changed and explain the result to your partner.”

**While circulating, ask:** “Is the problem the algorithm, the categories or missing context?”

**Facilitator check:** Delivery/billing is not sentiment. Eight easy English cases do not establish broader language performance.

**Support line:** “Use the prepared cell or saved result, then explain why it answers the question.” **Stretch line:** “Change one assumption and predict its effect before running. Would your recommendation change?”


### 180–195 | Compare approaches

**Say:** “Let's hear two different approaches. What did each assume? Which evidence supports the result? Write one change you would make after hearing the other pair.” [Select two brief reports, interpret and resolve one misconception.]

### 195–210 | Break

**Say:** “Fifteen minutes. Save your work; afterwards we will test a further assumption.”

### 210–270 | Backtesting relay

**Say:** “Use Day 3 of workshops/experiments.ipynb. Run four development origins; inspect each window before the average. Fix the method before final evaluation. Then discuss message counts available at a forecast cutoff and update the capstone split.”

[Format: One partner checks the time boundaries; the other checks the error table. Swap at the second origin. Follow the 60-minute activity pattern in workshops/ACTIVITY_CARDS.md; all instructions and discussion allow for interpretation.]

**Say:** “Your output is: Origin-by-origin results, method choice and one final score. Before running the experiment, write what you expect to happen. At the end, show which assumption you changed and explain the result to your partner.”

**While circulating, ask:** “Which window would you investigate even if the average looked good?”

**Facilitator check:** Each training history stops at its origin. Final 14 days remain separate until selection is complete.

**Support line:** “Use the prepared cell or saved result, then explain why it answers the question.” **Stretch line:** “Change one assumption and predict its effect before running. Would your recommendation change?”


### 270–290 | Compare the reasoning

**Say:** “Tell us one thing your evaluation protects against and one thing it does not. A good answer might be, 'We respect time order, but we have not tested a policy change.'”

### 290–300 | Close

**Say:** “Write a short response to this manager: 'Eight out of eight means we can deploy.' Keep it constructive. Explain the next evidence you would request rather than simply saying no. Tomorrow we will give uncertainty a more explicit role in the decision.”

---

## Day 4 | We do not know the rate exactly. Can we still act?

### 0–15 | Uncertainty is part of the answer

**Say:** “Suppose a facilities team inspects one hundred comparable items and finds eight defects. You can report eight percent in the inspected sample. But the manager's question is usually about the process or the next batch. Is the underlying rate acceptably low? Do we inspect more? We need to separate what we observed from what we infer.”

**Ask:** “Would eight defects in one hundred and eighty in one thousand give you the same confidence?” [Same observed rate, different information amount; avoid saying larger always fixes biased sampling.]

**Say:** “More observations can reduce uncertainty under a suitable model. More biased observations can also make us confidently wrong. Sampling quality still matters.”

### 15–30 | Bayes without the mystique

**Say:** “A prior describes our uncertainty before these observations. The likelihood describes how compatible the observations are with possible parameter values. The posterior updates the uncertainty using both. In symbols, posterior is proportional to likelihood times prior. The proportionality just means we normalise the result so total probability is one.”

[Point to a prior/posterior density graphic. Define the horizontal axis as a possible underlying rate, not an item count.]

**Say:** “We use a Beta prior with parameters two and eighteen. Its mean is ten percent. We observe eight defects and ninety-two non-defects. For this model, the update adds these counts: the posterior is Beta(10,110), with mean about 8.33%.”

**Ask:** “Why not exactly eight percent?”

**Response:** “Because the prior and the observations both contribute. The prior's influence depends on its concentration relative to the information in the observations. Those two prior numbers are modelling choices; they are not necessarily twenty actual inspected items.”

**Say:** “The credible interval is roughly 4.1% to 13.9%. Under this model and prior, it contains 95% of posterior probability for the underlying rate. It is not a guarantee about tomorrow, and it is not the interval for the number of defects in the next batch.”

**Say:** “The assumptions matter: comparable items, a representative sample and a process stable enough to describe with a common rate. If the supplier or inspection process changed halfway through, we might need a different model.”

### 30–80 | Estimate, reveal, update

**Say:** “Open Day 4 student notebook. Predict whether the posterior mean will be exactly 8%. Run the update, change the prior, then increase the sample. Discuss interval width as well as the mean.”

[Format: Everyone writes an initial estimate; pairs explain how evidence changes it. Follow the 50-minute activity pattern in workshops/ACTIVITY_CARDS.md; all instructions and discussion allow for interpretation.]

**Say:** “Your output is: Before/after belief statement with modelling assumptions. Before running the experiment, write what you expect to happen. At the end, show which assumption you changed and explain the result to your partner.”

**While circulating, ask:** “When would collecting more of the same data fail to help?”

**Facilitator check:** Original 10/120=8.33%; uniform prior 9/102=8.82%; larger sample 18/220=8.18%.

**Support line:** “Use the prepared cell or saved result, then explain why it answers the question.” **Stretch line:** “Change one assumption and predict its effect before running. Would your recommendation change?”


### 80–100 | Probability is not a policy on its own

[Peer review first: 5 minutes reading another pair\'s output,8 checking its evidence,5 discussing feedback and 2 writing a revision. Use the lines below as prompts during this exchange, not an additional lecture.]

**Say:** “The posterior mean is below ten percent, yet the probability of exceeding ten percent can still matter. These are different summaries. The action also depends on the cost of inspection, the cost of missing a problem and the decision-maker's agreed tolerance.”

**Ask:** “Who should own that action threshold?” [Operational decision owner with relevant technical/governance input; not silently chosen to make the model look useful.]


### 100–115 | Break

**Say:** “Let's take fifteen minutes. Save your notebook and return ready to compare approaches.”

### 115–130 | MCMC: see whether the sampler explores

**Say:** “Here we already know the exact posterior, so we do not need Markov chain Monte Carlo to solve the problem. We use it because having the exact answer makes the sampler easier to check.”

**Say:** “The Metropolis sampler starts at a possible rate, proposes a nearby value, compares posterior density and either moves or stays. It sometimes accepts a less likely proposal; that helps it explore. A repeated value is a legitimate part of the chain, not a missing record.”

[Show a trace, then an overlaid distribution. Pause before changing views.]

**Say:** “We run four chains from different starting points and discard the initial warm-up in this demonstration. We inspect movement, agreement and autocorrelation. If successive draws are very similar, ten thousand draws do not contain ten thousand independent pieces of information.”

**Ask:** “Would a very high acceptance rate automatically be good?”

**Response:** “Not necessarily. Very small proposals may be accepted often while moving too slowly. More iterations do not automatically fix poor exploration.”

**Say:** “Our recorded chain means are close to the exact mean. That is reassuring for this example, but agreement of means alone is not a convergence certificate. Real analyses need stronger diagnostics, including effective sample size and suitable chain-comparison measures. We will not pretend today's simple checks validate an arbitrary complex model.”

### 130–180 | Sampler detective

**Say:** “Compare the MCMC traces and exact posterior. Investigate a very small proposal scale if time permits. List two reassuring signs and one check missing from the demonstration.”

[Format: Pairs inspect evidence; another pair plays the sceptical reviewer. Follow the 50-minute activity pattern in workshops/ACTIVITY_CARDS.md; all instructions and discussion allow for interpretation.]

**Say:** “Your output is: Evidence-based verdict on the approximation, with limits. Before running the experiment, write what you expect to happen. At the end, show which assumption you changed and explain the result to your partner.”

**While circulating, ask:** “What would you check before simply adding more iterations?”

**Facilitator check:** Similar means alone do not prove convergence. High acceptance can accompany poor movement.

**Support line:** “Use the prepared cell or saved result, then explain why it answers the question.” **Stretch line:** “Change one assumption and predict its effect before running. Would your recommendation change?”


### 180–195 | Compare approaches

**Say:** “Let's hear two different approaches. What did each assume? Which evidence supports the result? Write one change you would make after hearing the other pair.” [Select two brief reports, interpret and resolve one misconception.]

### 195–210 | Break

**Say:** “Fifteen minutes. Save your work; afterwards we will test a further assumption.”

### 210–270 | The decision hearing

**Say:** “Use Day 4 of workshops/experiments.ipynb. Compare priors and 20%/30% policy triggers. Explain a changed decision without pretending one policy is mathematically mandatory. Spend fifteen minutes on the original predictive/generative results and finish the capstone uncertainty statement.”

[Format: A group of four rotates analyst, decision owner, reviewer and reporter. Follow the 60-minute activity pattern in workshops/ACTIVITY_CARDS.md; all instructions and discussion allow for interpretation.]

**Say:** “Your output is: Probability, policy and action written as three separate statements. Before running the experiment, write what you expect to happen. At the end, show which assumption you changed and explain the result to your partner.”

**While circulating, ask:** “Who should justify and approve the action threshold?”

**Facilitator check:** Probability of rate>10% is distinct from the policy probability trigger. Generated data do not establish privacy or real-world validity.

**Support line:** “Use the prepared cell or saved result, then explain why it answers the question.” **Stretch line:** “Change one assumption and predict its effect before running. Would your recommendation change?”


### 270–290 | Defend an action, not a percentage

**Say:** “Give us the probability, the policy assumption and the resulting action as three separate statements. That makes it possible for someone to disagree with the policy without misunderstanding the calculation.”

### 290–300 | Close

**Say:** “Write two sentences: one about the unknown rate, one about a future batch. Use the right units in each. Tomorrow we finish with scale, deployment and your proposals.”

---

## Day 5 | What would it take to use this on Monday?

### 0–15 | Start with the bottleneck

**Say:** “Today we will hear some powerful tool names. Before we use them, let's ask what problem they solve. If a task runs comfortably on a laptop and meets the service deadline, a distributed system may add complexity without improving the decision. If it cannot meet the workload, we need evidence about where the bottleneck sits.”

**Ask:** “What makes an analysis difficult in your setting: size, update frequency, inconsistent sources, slow approval, or something else?” [Separate organisational from computing constraints.]

**Say:** “An architecture decision should respond to the actual constraint. 'Big data' is not a prize you win by having many rows.”

### 15–30 | Combine results correctly

[Show the local partition example in Day 5 worked notebook.]

**Say:** “We divide records, calculate partial results and combine matching keys. Sums combine naturally. Counts do too. Means require care: combine the sums and counts, then divide. Averaging averages can give the wrong answer when groups differ in size.”

**Say:** “A separate hand example: one partition has two A orders worth one hundred euros; another has eight worth three hundred and twenty. Their means are fifty and forty. The overall mean is forty-two, not forty-five. The partition sizes matter.”

**Say:** “Hadoop is an ecosystem. HDFS is distributed storage, YARN manages resources, and MapReduce is a processing framework. Spark is a separate execution engine that can work with Hadoop components. Running today's local partition simulation does not mean we have run a Hadoop cluster.”

[If tested, open spark_worked notebook and show the small aggregation. Otherwise use saved output and state that.]

**Say:** “In Spark, transformations describe work and actions request results. Grouping may require data to move between partitions, which is called a shuffle. Collect brings results back into the driver's memory. Collecting two aggregate rows is different from collecting a huge raw table.”

### 30–80 | Human partitions, then Python

**Say:** “First calculate the common A-channel mean from 2 orders/EUR 100 and 8 orders/EUR 320. Then use the original Spark SQL/DataFrame example or saved fallback. Explain what moves between workers and what collect does.”

[Format: Each pair receives a partition summary; two pairs combine results before checking in code. Follow the 50-minute activity pattern in workshops/ACTIVITY_CARDS.md; all instructions and discussion allow for interpretation.]

**Say:** “Your output is: Correct combined mean, reconciled query output and a memory explanation. Before running the experiment, write what you expect to happen. At the end, show which assumption you changed and explain the result to your partner.”

**While circulating, ask:** “What would break if one partition were much larger than the others?”

**Facilitator check:** Combined mean 42, not 45. The full Spark example is separate: A 5,000/EUR 250,000; B 5,000/EUR 255,000.

**Support line:** “Use the prepared cell or saved result, then explain why it answers the question.” **Stretch line:** “Change one assumption and predict its effect before running. Would your recommendation change?”


### 80–100 | What has the laptop actually proved?

[Peer review first: 5 minutes reading another pair\'s output,8 checking its evidence,5 discussing feedback and 2 writing a revision. Use the lines below as prompts during this exchange, not an additional lecture.]

**Say:** “Our local run shows that the example can execute in this environment. It is not a cluster benchmark. For a production choice, ask for representative volumes, runtime, memory, reliability, cost and who will operate it.”

**Ask:** “Which evidence would change your mind about needing Spark?” [A measured single-machine solution meeting requirements, or a demonstrated constraint requiring more resources.]


### 100–115 | Break

**Say:** “Let's take fifteen minutes. Save your notebook and return ready to compare approaches.”

### 115–130 | A more advanced model still owes us evidence

**Say:** “Spark MLlib provides modelling tools in the Spark environment. In our example, VectorAssembler packs numerical inputs into a vector, the pipeline fits a regression model, and we compare it with a training-derived baseline on held-out data.”

**Say:** “The saved regression MAE is about 2.248 compared with 20.227 for the baseline. The synthetic split uses an identifier rule; it is a teaching arrangement for independent data, not the right default for a time-dependent operational service.”

[Show the local neural network comparison, clearly labelled as a different task.]

**Say:** “A neural network combines numerical transformations in layers. Nonlinear activations allow nonlinear relationships. Training loss is not test accuracy. More layers or training passes do not automatically make a model more useful. Our small example compares a fixed neural model with a linear classifier on a curved synthetic problem.”

**Say:** “The recorded accuracies are about 0.847 and 0.827. That small difference needs context: representative testing, uncertainty, costs and maintenance. Also, do not compare those accuracies with the regression MAEs: the tasks and units are different.”

**Say:** “A generative adversarial network has a generator producing candidates and a discriminator trying to distinguish generated from reference data. Our toy adversarial example updates both, but it is one-dimensional and not a deep image model. It targets mean 2 and standard deviation 0.6; the recorded output is around 2.10 and 0.287. The mean looks close while the spread is too narrow. That is a useful failure to notice.”

### 130–180 | An incident in the pilot

**Say:** “Use Day 5 of workshops/experiments.ipynb. With the stated 12-minute limit, find the two-week trigger and decide who acts. Then inspect the original MLlib/neural/GAN results; explain why their headline metrics are insufficient.”

[Format: One pair operates the pilot; another is the review team. Follow the 50-minute activity pattern in workshops/ACTIVITY_CARDS.md; all instructions and discussion allow for interpretation.]

**Say:** “Your output is: Incident note: evidence, uncertainty, action, owner and return-to-service condition. Before running the experiment, write what you expect to happen. At the end, show which assumption you changed and explain the result to your partner.”

**While circulating, ask:** “What changes if true outcomes arrive two weeks late?”

**Facilitator check:** The stated monitoring rule first triggers at week 7. It does not identify a cause. GAN spread 0.287 vs target 0.6 reveals a problem despite similar means.

**Support line:** “Use the prepared cell or saved result, then explain why it answers the question.” **Stretch line:** “Change one assumption and predict its effect before running. Would your recommendation change?”


### 180–195 | Compare approaches

**Say:** “Let's hear two different approaches. What did each assume? Which evidence supports the result? Write one change you would make after hearing the other pair.” [Select two brief reports, interpret and resolve one misconception.]

### 195–210 | Break and reset

**Say:** “Take fifteen minutes. Afterwards, we will hear your proposals. You don't need a polished sales pitch. We need a clear decision, credible evidence and a next step.”

### 210–230 | Finish the capstone

**Say:** “Use these twenty minutes and the six headings in the capstone brief: decision, method, data, evaluation, limitation and next step. Each group chooses a spokesperson, but everyone keeps an individual page. Check that you have not promised a result your evidence does not support.”

[Walk around; help narrow proposals.]

**If a proposal is too broad:** “What is the smallest useful decision you could improve in two weeks? Start there. You can describe the larger ambition as a later step.”

### 230–265 | Five presentations

**Say:** “Each group has seven minutes: three minutes speaking, three for interpretation and one for feedback. Please speak in short sections and let the interpreter finish. Lead with the service decision.”

**Feedback template:** “The strongest part of your proposal is [specific evidence or decision]. Before moving forward, I would clarify [one concrete missing assumption]. Your next step is clear when [owner, action and timing].”

**Questions to choose from:** “What will you compare against?” / “What exists at the decision cutoff?” / “What would make you stop?” / “How will a colleague reproduce your result?” / “What would change your recommendation?”

### 265–270 | Written peer feedback

**Say:** “Write one specific suggestion for another group: what evidence would make their proposal stronger? Give them the note. Keep it practical and constructive.”

### 270–290 | Individual final practical

**Say:** “This last exercise is individual. It checks your analytical judgement, not your speed at typing. You have five minutes for the translated instructions and fifteen to write. You may use your handbook. If you write in Arabic, we will review it with the interpreter.”

**Read the scenario:** “A service team wants to predict tomorrow's delayed visits using historical records. A vendor reports 96% accuracy. Predicting every visit on time gives 95%. Name the method and the decision. Give one input available at scheduling time. Propose an evaluation split and baseline, and say what further evidence you would request. Correct these three claims: '96% proves usefulness'; 'synthetic guarantees privacy'; 'running Spark locally proves scale'. Finish with a next step, an owner and a measurable stop condition.”

[Use the 10-point final rubric in NO_CODE_ANSWER_KEY: despite its filename, it assesses the common judgement outcomes for this Python-supported course. Do not grade programming that was not requested by the assessment.]

### 290–300 | Close the week

**Say:** “At the start we asked what you do with data. I hope you now have a few sharper questions to take back: What is the decision? What information is available then? What is the baseline? What does the result leave uncertain? Who owns the next action?”

**Say:** “Please complete the feedback and exit self-assessment. Tell us what helped, what moved too quickly and what you would like to practise next. For your own follow-up, write one action you will take in the next two weeks and who you need to involve.”

**Final words:** “Thank you for the examples, questions and thoughtful disagreements this week. You do not need to use every technique we discussed. Choose the ones that answer your problem, keep the evidence traceable, and make the next decision a little better.”

---

## Facilitation authority and further questions

The workshop cards in workshops/ACTIVITY_CARDS.md specify the varied formats, exact task, deliverable, facilitator checks and discussion prompt. Use their Lab A/B/C instructions in place of older notebook task timings. The notebook experiments are real runnable additions, with recorded results in workshops/RESULTS.md.

For every task: ask participants to predict, investigate, change one assumption, explain and exchange feedback. If the cohort already knows the main technique, use the stretch question and demand a stronger evaluation or counterexample. Do not substitute a longer lecture for completed practice.

Data are synthetic and cases are clearly labelled. There is no need to add real datasets or a regional storyline to meet these workshop objectives. Do not claim the techniques are unique to Europe.
