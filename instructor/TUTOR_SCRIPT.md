# A good analysis earns its place in a decision

## Complete English tutor script | Five-day workshop

For 20 experienced analysts who already use Python. Five hours daily, including two 15-minute breaks. English delivery with Arabic interpretation. Venue: Genoa. Context: participants from Saudi Arabia's Ministry of Interior, interested in practical approaches used in Spain and Europe.

This is the single speaking document. It brings together the opening, explanations, demonstrations, activity instructions, questions, likely responses, debriefs, transitions and closing for every day. The existing day-level TEACHING_GUIDE files remain the technical reference; RUNBOOK is the older coding timetable; QUESTION_BANK holds extra questions. Follow this script and the revised PROGRAMME for this delivery. The no-code pack is now a fallback, not the default route.

Read the paragraphs labelled **Say** aloud or adapt them to your natural voice. Bracketed directions are for you, not the audience. A script can prepare your interventions, but cannot predict every participant answer: the response branches below cover the likely misunderstandings. Do not fill every minute with speech. Quiet thinking, running a cell, discussing a result and waiting for interpretation are part of the lesson.

### Your manner in the room

Be warm, direct and curious. Invite challenge without putting people on the spot. Say “Let's check that together” more often than “That is wrong.” Ask about their actual analytical work rather than their job titles. Use participants' names when they offer them. Avoid jokes that depend on accent, religion or national stereotypes. A workshop with a Spanish teaching feel means conversational explanations, worked examples, discussion and practical feedback here; it does not mean that everyone in Spain teaches the same way.

Use fictional service appointments, facilities inspections, logistics and aggregate workloads as transfer cases. The original notebooks still use retail orders, delivery routes and service messages. Say explicitly when you move from their numerical examples to a public-service analogy. Do not rename a measured variable and pretend the model has been validated for a different task. We are not using ministry records or drawing conclusions about operational policing.

### Timing and setup

Each day: 0–20 opening; 20–50 explanation/demo; 50–90 Lab A; 90–105 debrief; 105–120 break; 120–150 explanation/demo; 150–195 Lab B; 195–210 break; 210–260 Lab C/project; 260–285 reports; 285–300 close. Day 5 replaces the last 90 minutes as specified below. All blocks include interpretation. In a 30-minute explanation block, budget about 12–15 minutes of English, the same for interpretation and any remaining time for a short response. Speak in short chunks, normally one or two sentences, then pause. Do not make the interpreter hold a paragraph of equations in memory.

Ten pairs work at laptops; two pairs form each of five reporting groups. One partner operates, the other checks and explains; swap at a natural checkpoint, not halfway through a calculation. Someone may prefer to explain first. Do not force a public coding demonstration. Every participant writes an individual final answer.

Before class, run only the demonstrations you will use. Keep each worked_RESULTS file open; for Day 1 use the answer key and worked notebook. Copy the repository locally. The tutor preparation plan in this script is: rehearse Days 1–2 on preparation days 1–3; Day 3 on preparation day 4; Day 4 on day 5; Day 5 and the capstone on day 6; perform a translated rehearsal and technical checks on day 7. Ask the organiser whether the five daily hours include breaks; this script provides 22.5 contact hours, not 25.

### Reusable lines for the whole week

**When a cell fails:** “Let's keep the analytical question in view. I have the saved output here. We can interpret it now and fix the environment at the break.” [Allow at most one minute of debugging.]

**When you do not know:** “That is a useful question, and I want to give you a reliable answer. I'll write it down, check it and come back to you tomorrow.” [Record an owner and return time; do not promise an answer before checking.]

**When the room goes quiet:** “Take thirty seconds to write your own answer. Then compare with the person next to you. I'll ask for two different views.”

**When someone answers incorrectly:** “I can see the reasoning. Let's look at the denominator together. Which cases are included in that percentage?”

**When one person dominates:** “Thank you. Let's hear from a group that has not spoken yet. You can agree, disagree or add a limitation.”

**When interpretation takes longer:** “We'll leave the optional experiment for later and protect the time for your analysis. Keep your result and one question ready.” [Drop extensions; do not rush interpretation or remove the breaks.]

**When asked how this works in Spain:** “I can show you documented Spanish examples and the working method we are practising. Organisations differ. Let's separate an example, a recommended practice and a claim about what every organisation does.”

---

## Day 1 | Before we trust the dashboard

### 0–20 | Meet the people, then the problem

**Say:** “Good morning, everyone. Welcome to Genoa. This week we are going to work as an analysis team. You already use Python and work with data, so we won't spend the morning introducing variables or explaining what a spreadsheet is. We will spend our time on the difficult part: deciding whether an analysis is good enough to support an action.”

[Pause for interpretation. Introduce yourself truthfully; do not claim experience you do not have.]

**Say:** “Before I show you anything, tell the person next to you about one analysis you actually do. What information arrives? What do you produce? Who uses the result? Please keep it general; we don't need names, real records or confidential details.”

[Allow three minutes plus interpretation. Invite three brief examples, not twenty introductions. Write the decisions on a board.]

**Say:** “I hear a common pattern: a report is useful only if someone can do something with it. By Friday, each group will have a short proposal for one of those decisions. It should be clear enough for a manager to act on, and honest enough for another analyst to challenge.”

**Ask:** “Which is most familiar to you: cleaning and charts, forecasting, or training predictive models?” [Show of hands; adjust extensions. This is experience mapping, not an exam.]

**Say:** “There is no prize for finishing first. A good contribution might be a line of Python, a question about a missing value, or noticing that our conclusion is too strong. We need all three.”

### 20–50 | A result you could put your name to

**Say:** “Imagine a service manager says: 'The dashboard says one office is slower. Should I move staff?' Your first answer should probably be a question. Are the offices doing comparable work? Did the reporting period change? Are unresolved cases missing from the calculation? A beautiful dashboard cannot answer a poorly defined comparison.”

**Ask:** “What would you check before showing that chart to a director?” [Accept units, period, missingness, definitions, workload and denominator.]

**Say:** “Let's test those habits on a small retail dataset. This is a teaching example, not a ministry dataset. The transferable skill is auditing the evidence. We have orders, quantities, prices and channels. First inspect; then decide; then change. If you clean while you are still discovering what a column means, it is easy to remove the very thing you should have investigated.”

[Open Day 1 worked notebook. Show shape, head, types and missing-value counts; leave each output visible during interpretation.]

**Say:** “A duplicate-looking row is a question, not automatically an error. Here the teaching rules confirm two accidental duplicates. A negative sales quantity is invalid in this particular sales table. In a returns table, it might be perfectly valid. The business definition comes before the filter.”

**Say:** “And this 80-unit order? It looks unusual. We know it is a valid bulk order, so we keep it. Outlier detection gives us candidates for review; it does not give us permission to erase inconvenient observations.”

**Ask:** “If a price is missing, what would entering zero mean?”

**If they say ‘it lets the calculation run’:** “It does, but it also says the item was free. That is a new claim. We need to distinguish not recorded from genuinely zero.”

**Say:** “A useful habit is to write a small decision log: what I found, what I did, why, and how many rows were affected. Another analyst should be able to reproduce your result without guessing your intentions.”

### 50–90 | Lab A: audit before editing

**Say:** “Open Day 1's student notebook. Work on the audit section first. In the next forty minutes, I want a short quality report: starting rows, duplicates, missing prices, missing channels and invalid quantities. Next to each issue, write a proposed rule. Do not delete the bulk order. If you finish early, ask which rules would change for a returns dataset.”

[10 minutes inspect, 15 agree rules, 10 calculate, 5 write findings. Circulate.]

**At the first checkpoint, say:** “Please show your partner the original row count and the current row count. If they differ, can you explain every removed row?”

**At the second checkpoint, ask quietly:** “What would someone misunderstand if they saw only your final table?”

**If a pair is blocked by syntax:** “Use the matching worked cell, then explain why it is the right operation. Today I am checking your judgement, not your ability to remember a method name.”

**At five minutes remaining:** “Stop adding checks. Choose the two issues that most affect the interpretation and write them clearly.”

### 90–105 | Debrief: follow the rows

**Say:** “Let's reconcile the counts. We start with 122 rows. Removing two duplicates and one invalid sale leaves 119 valid orders. Three valid orders have no price, so 116 contribute to known revenue. Two records have no channel; we show Unknown rather than make them disappear.”

**Ask:** “Which of those numbers belongs beside a revenue chart?” [Expected: priced count and missing-price caveat; valid count is useful context.]

**Say:** “Notice how much work happens before modelling. This is not a beginner's chore. Getting these definitions right is part of senior analytical work.”

**Break line:** “Let's take fifteen minutes. Before you leave, save your notebook. We'll return to what the cleaned data can actually tell us.”

### 120–150 | Give the numbers a fair comparison

**Say:** “The known total is EUR 10,210. Store contributes EUR 6,310, Online EUR 3,700 and Unknown EUR 200. That tells us where the recorded revenue sits. It does not yet tell us which channel performs better.”

**Ask:** “What could make a channel total larger?” [More orders, larger orders, different products, the bulk order, missingness.]

**Say:** “Store has 60 priced orders and Online has 54. Mean known revenue per priced order is about EUR 105.17 and EUR 68.52 respectively. Those are different comparisons from total revenue. Neither establishes that moving a customer from one channel to the other changes spending.”

[Show a bar chart with a zero baseline and labelled units. Then show the original distribution plot.]

**Say:** “A mean is useful, but a few large orders can pull it upwards. The median describes the middle order. Standard deviation and the interquartile range describe different aspects of spread. Rather than recite definitions, ask what decision the summary serves. A manager planning capacity might need the upper tail as much as the average.”

**Say:** “Use bars for category comparisons, a line for change over time, a histogram for a distribution and a scatterplot for two numerical quantities. These are starting choices, not rigid rules. Give your chart a title that makes a defensible point, label the units, and state the population. If a bar starts above zero, its length can exaggerate a modest difference.”

**Ask:** “Would you put 'Store is the best channel' on this chart?”

**If someone says yes:** “What does best mean: revenue, margin, cost to serve, growth or satisfaction? Let's choose the measure before the claim.”

### 150–195 | Lab B: make one useful chart

**Say:** “Apply your agreed cleaning rules. Calculate revenue, compare the channels and make one chart for a busy manager. Your caption must say that it uses priced orders. Then compare mean and median. Finally, run a labelled sensitivity check without the bulk order. Keep the main result with the valid order included.”

[15 minutes calculations, 15 chart, 10 sensitivity, 5 caption.]

**While circulating:** “If I cover the chart title, can I still tell what is counted? If I show only the title, is its claim stronger than the data?”

**For faster pairs:** “Look at how the channel ranking changes under your sensitivity check. Explain what you learned without calling the alternative the cleaned truth.”

**Before the break:** “Save both views and label them. We will use them to practise a recommendation, not to choose the prettier answer.”

### 210–260 | Lab C: the director has three minutes

**Say:** “Here is our meeting. A director asks, 'Should we invest more in stores?' You have three minutes, and the director will not read your notebook. Work in groups of four. Lead with the decision, give one finding, show the evidence, name a limitation and recommend a next step. Add one thing that would change your mind.”

**Model the tone:** “'Store has more known revenue in this sample, but a bulk order and missing prices affect the comparison. I would not change the budget from these totals alone. First I would recover the missing prices and compare a longer period, including costs and order mix.' That is a useful answer. It moves the work forward without pretending we have proved more than we have.”

[10 minutes briefing, 10 peer challenge, 10 revision, 20 capstone selection.]

**Say:** “For your capstone, choose a service-planning problem: appointment demand, processing times, maintenance workload or request routing. You may also use a generalised problem from your work. Write the decision, its owner and when the decision is made. Avoid 'use AI to improve services'. Tell us what someone would do differently on Monday.”

### 260–285 | Five short reports

**Say:** “Each group has five minutes including interpretation. Give your main finding and the strongest limitation. We will take one short challenge if time allows.”

**Useful feedback:** “Your conclusion matches your evidence.” / “You have named a limitation; now tell us what action it changes.” / “That is a causal statement. What extra design would support it?”

### 285–300 | Close

**Say:** “Write your own answer: what is one cleaning decision you would document differently after today? Then add one sentence to your capstone: the decision we want to improve is…”

**Closing:** “Tomorrow we will ask a model to predict something. Keep today's habits. A predictive score still depends on definitions, missing data and a fair comparison.”

---

## Day 2 | Is this model useful, or just impressive?

### 0–20 | Put the decision on the board

**Say:** “Yesterday we asked whether the report was trustworthy. Today we ask whether a prediction is useful. Think of a facilities team planning tomorrow's visits. An estimate of duration could help allocate capacity. A warning that a visit may run late could support a different action. Those are related questions, but they are not the same prediction task.”

**Ask:** “Who would act on the prediction? What information exists at that moment?” [Have pairs name one available and one unavailable input.]

**Say:** “Our notebook uses independent synthetic delivery routes. Distance and planned stops are inputs; actual duration is an outcome. Keep that setting intact. We will discuss how its evaluation would need to change for future service appointments.”

### 20–50 | Train, compare, then test

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

### 50–90 | Lab A: earn the improvement

**Say:** “Run the regression and baseline sections. Record both MAEs and explain them in minutes. Your output is two sentences: what improved, and what the evaluation still does not establish. Then inspect the feature list and identify any information that would arrive too late in a real use case.”

[10 minutes run, 10 interpret, 10 feature audit, 10 compare with a partner.]

**Checkpoint:** “Which part of the data produced the baseline value? If the answer is the test set, stop and check.”

**For faster pairs:** “Design an evaluation for repeated visits to the same sites over several months. You do not need to invent records. Draw the boundaries and explain the leakage you are avoiding.”

### 90–105 | Numbers without salesmanship

**Say:** “The recorded example gives MAE about 24.34 minutes for the baseline and 8.43 for the model. That is a substantial improvement on this synthetic test. It is not yet evidence of the same improvement in your service.”

**Ask:** “What else would an operational owner ask?” [Error distribution, busy periods, costs, representativeness, availability, monitoring.]

**Say:** “We can be pleased with a result and still be careful about its scope. That is how we make an analysis credible.”

**Break:** “Fifteen minutes. When we come back, we will stop treating all errors as equal.”

### 120–150 | Different mistakes, different consequences

**Say:** “Imagine two predictions. One warns of a delay that never happens. The other misses a delay that does happen. Both are mistakes, but they may create very different costs. Accuracy puts them in the same total. Your decision may not.”

[Draw or show the confusion matrix. Rows actual; columns predicted.]

**Say:** “In our saved test, 55 routes are correctly predicted on time; two are false alarms; nine delays are missed; 34 delays are detected. Read those as events before turning them into percentages.”

**Ask:** “For recall of delayed routes, do we divide by all routes or all actual delays?”

**Response:** “All actual delays: 34 out of 43, about 79.1%. Precision asks a different question: of the 36 alerts, 34 were correct, about 94.4%. Neither is the same as accuracy, which is 89% here.”

**Say:** “A tree makes a sequence of feature-based decisions. Greater depth can fit more detail, including noise. A forest combines many randomised trees and can reduce some instability. Logistic regression is another useful baseline classifier. None of these names guarantees a winner.”

**Say:** “We compare candidates on development data. Maximum depth is a hyperparameter: a setting we choose around the learning process. Training performance shows fit to examples already seen; validation performance is closer to the question of generalisation. A gap is a warning to investigate, not a mathematical verdict that every deep tree is bad.”

### 150–195 | Lab B: choose with the right evidence

**Say:** “Run the classification section. Find where the candidate is selected and confirm that the decision uses validation results. Then read the final confusion matrix in ordinary language. Use a fictional cost of 100 units per missed delay and 20 per false alarm. Compare the model with predicting every route on time.”

[15 minutes inspect/run, 15 error-cost calculation, 10 decision, 5 write limitation.]

**Prompt:** “The model cost is 940 units under these assumptions; the always-on-time baseline is 4,300. Now make missed delays cost only one unit. What happens?”

**Expected:** “The model costs 49 and the baseline 43. The preferred option changes. Those invented costs are a sensitivity exercise, not measured savings.”

**Say:** “Do not adjust the classification threshold on these test results. Use validation data to choose a threshold before a fresh final evaluation.”

### 210–260 | Lab C: a little tuning, a lot of judgement

**Say:** “First compare tree depths one, three and eight using training folds only, as the pair challenge specifies. Record training accuracy and validation F 1. These are different metrics; do not subtract them as if they were a formal overfitting measure. Look for improving fit with disappointing validation, and explain cautiously.”

[20 minutes tree challenge, 10 guided clustering/PCA, 10 capstone, 10 report preparation.]

**Clustering explanation:** “With clustering, we decide what similarity means through features, scaling and the method. Asking k-means for three groups produces three groups; it does not prove nature contains exactly three. Before acting on a segment, ask whether it is stable and whether it supports a legitimate, useful action.”

**PCA explanation:** “PCA builds directions that retain variation. A two-dimensional display may be convenient while losing important information. Explained variance is not prediction accuracy, and a clear picture is not proof that a segmentation is meaningful.”

**Say:** “For the capstone, add the target, the baseline and two features available when the decision is made. If it is not a prediction problem, say so. Do not force every useful project into machine learning.”

### 260–285 | Report like a colleague

**Say:** “Give us your chosen method, the evidence used to choose it and the most costly mistake. Please say 'on this evaluation' rather than 'this model is best'.”

**If asked about explainability:** “A feature-importance result can help us understand model behaviour. It does not by itself tell us what would happen if we intervened on that feature. Correlated inputs also complicate attribution. We should inspect explanations alongside performance and domain knowledge.”

### 285–300 | Close

**Say:** “Individually, write one example of leakage and one reason a more accurate model might still be the worse decision. Tomorrow the order of the observations will become central: what can we honestly know before the future arrives?”

---

## Day 3 | The future arrives one day at a time

### 0–20 | Start with a real planning question

**Say:** “Suppose a service centre needs next week's staffing plan by Thursday afternoon. A forecast produced on Friday may be accurate and still arrive too late. Forecasting starts with the decision time, the forecast horizon and the information available at that cutoff.”

**Ask:** “In your work, do you usually predict the next day, next week or next month? What changes the demand?” [Accept calendar effects, policy changes, campaigns and recording changes; do not assume a specific Saudi working week.]

**Say:** “The weekly pattern in our synthetic dataset is a teaching design. For a real service, we would inspect its actual working calendar, holidays and changes. We would not copy another country's calendar assumptions.”

### 20–50 | Give simple forecasts a fair chance

[Show the ordered series, train/test boundary and training decomposition.]

**Say:** “Trend is a sustained direction. Seasonality repeats at a known period. A cycle need not have a fixed period. A rolling mean can help us see the series, but a smooth line is not automatically a complete decomposition.”

**Say:** “We have 210 daily observations. The final 28 form our holdout; the earlier 182 are for development. Before fitting anything, check frequency, missing dates and definitions. A day without a record might mean zero activity, a closed office or a collection failure. Those are different situations.”

**Ask:** “Why not shuffle the dates and use the same random split as yesterday?”

**Expected:** “Because that could let the procedure learn from the future while pretending to predict the past. Our evaluation should resemble the way the service will use the forecast.”

**Say:** “Our first baseline repeats the last value. The second repeats the latest week. Neither sounds sophisticated, which is exactly why they are useful comparisons.”

**Say:** “ARIMA combines previous values, differencing and past-error structure. The letters are less important than its assumptions. In ARIMA(p,d,q), p controls autoregressive terms, d differencing and q moving-average error terms. The fixed (1,1,1) example does not explicitly represent the weekly seasonal structure. It is a demonstration, not a tuned champion.”

**Ask:** “If the simple weekly rule wins, has the lesson failed?”

**Say:** “No. We have learned something useful about this data and these choices. The job is not to defend the complicated model.”

### 50–90 | Lab A: compare without peeking again

**Say:** “Run the series, baseline and ARIMA sections. Record the three MAEs. Do not try new orders after looking at the final test and then claim the same test is untouched. For experimentation, split a validation window from the training period as the challenge specifies.”

[15 minutes run, 10 compare, 10 draw the development boundary, 5 note assumptions.]

**Checkpoint:** “Point to the last date each forecast is allowed to see. If you cannot point to it, your evaluation is not yet clear.”

**If ARIMA fails:** “Use the saved ARIMA output and continue with the baseline calculations. We are analysing recorded results for that method, not claiming a successful run on this machine.”

### 90–105 | More than one lucky window

**Say:** “In the recorded example, weekly MAE is about 5.53, last-value MAE 22.38 and ARIMA MAE 22.11. Those results belong to one final window. A service might behave differently in a peak month.”

[Draw three expanding training windows with the next window held out.]

**Say:** “Rolling-origin evaluation repeats the practical question at several historical cutoffs: what could we have forecast then? Fit the procedure using the past at each cutoff and evaluate the next window. Reserve a final period for the final claim. Today our diagram is an evaluation design; the original notebook does not automatically execute a full rolling backtest.”

**Break:** “Let's pause for fifteen minutes. After the break we will work with information that arrives as sentences rather than numbers.”

### 120–150 | Text is messy for good reasons

**Say:** “A request might say, 'The appointment was cancelled and I still haven't received my refund.' Is that scheduling or payment? A person can mean two things at once. Our database may ask for one label. Sometimes the limitation is in the task definition before it is in the model.”

[Show the notebook's English delivery/billing messages.]

**Say:** “The teaching pipeline turns words and short sequences into numerical features, using TF-IDF. It then fits a classifier. TF-IDF gives weights based on term frequency and document frequency. It is not the same as a human reading the request. The vectoriser belongs inside the pipeline so the training stage learns its vocabulary without test information.”

**Say:** “Our categories are delivery and billing, not positive and negative sentiment. Keep that distinction clear. A polite message can describe a serious service failure.”

**Ask:** “What should happen when a message is ambiguous?” [Human review, multiple labels, clarification or a documented routing rule.]

**Say:** “Embeddings offer another numerical representation, and language models can produce or classify text in more flexible ways. The workflow still needs a defined task, representative evaluation, handling of uncertainty and a person responsible for mistakes. We are not making an API call or validating a language model in this course.”

**Say:** “English results do not validate Arabic performance. Translation of today's instruction helps us learn together; it does not create an evaluated Arabic classifier. A real implementation would need representative language data and review by people who understand the relevant usage.”

### 150–195 | Lab B: find where the neat answer breaks

**Say:** “Run the text pipeline. Inspect the eight test examples and their predictions. Then write two new ambiguous examples. Predict their labels and describe why those predictions might be inadequate. Your task is not to make the accuracy number look worse; it is to understand where the system needs a better policy.”

[15 minutes run, 15 ambiguity experiment, 10 review rule, 5 write a finding.]

**Checkpoint:** “Did you ask for the category the model was trained to predict, or a different task? A delivery/billing classifier cannot answer every service question just because the input is text.”

**If someone celebrates 100%:** “It got these eight authored examples right. That is the exact claim we can make. What would your next test need to contain before you trusted it on ordinary incoming requests?”

### 210–260 | Lab C: connect the message to the calendar

**Say:** “Spend twenty minutes comparing last-value and weekly forecasts on the last fourteen days of the training period. Keep the final 28 days out of this decision. Then we will connect text to time.”

[20 minutes notebook challenge; 10 minutes text/time discussion; 10 capstone; 10 report preparation.]

**Say:** “Messages have arrival times. We can count total requests or categories by day. Monday's teaching counts are two billing, three delivery and one uncertain. Tuesday has one, five and two. Wednesday has three, four and one. Totals are six, eight and eight. The delivery shares are 50%, 62.5% and 50%.”

**Ask:** “Can Wednesday's completed daily count enter a forecast issued Wednesday morning?”

**Response:** “No. Tuesday's count can enter only if it was actually available before the forecast cutoff. Also, if our classifier changes, the category series may change even when the real workload does not. Record model versions and definition changes.”

**Say:** “Add a time boundary to your capstone. Write what will be available, when, and what you will keep for evaluation. If you work with text, add the rule for uncertain or multi-topic requests.”

### 260–285 | Compare the reasoning

**Say:** “Tell us one thing your evaluation protects against and one thing it does not. A good answer might be, 'We respect time order, but we have not tested a policy change.'”

### 285–300 | Close

**Say:** “Write a short response to this manager: 'Eight out of eight means we can deploy.' Keep it constructive. Explain the next evidence you would request rather than simply saying no. Tomorrow we will give uncertainty a more explicit role in the decision.”

---

## Day 4 | We do not know the rate exactly. Can we still act?

### 0–20 | Uncertainty is part of the answer

**Say:** “Suppose a facilities team inspects one hundred comparable items and finds eight defects. You can report eight percent in the inspected sample. But the manager's question is usually about the process or the next batch. Is the underlying rate acceptably low? Do we inspect more? We need to separate what we observed from what we infer.”

**Ask:** “Would eight defects in one hundred and eighty in one thousand give you the same confidence?” [Same observed rate, different information amount; avoid saying larger always fixes biased sampling.]

**Say:** “More observations can reduce uncertainty under a suitable model. More biased observations can also make us confidently wrong. Sampling quality still matters.”

### 20–50 | Bayes without the mystique

**Say:** “A prior describes our uncertainty before these observations. The likelihood describes how compatible the observations are with possible parameter values. The posterior updates the uncertainty using both. In symbols, posterior is proportional to likelihood times prior. The proportionality just means we normalise the result so total probability is one.”

[Point to a prior/posterior density graphic. Define the horizontal axis as a possible underlying rate, not an item count.]

**Say:** “We use a Beta prior with parameters two and eighteen. Its mean is ten percent. We observe eight defects and ninety-two non-defects. For this model, the update adds these counts: the posterior is Beta(10,110), with mean about 8.33%.”

**Ask:** “Why not exactly eight percent?”

**Response:** “Because the prior and the observations both contribute. The prior's influence depends on its concentration relative to the information in the observations. Those two prior numbers are modelling choices; they are not necessarily twenty actual inspected items.”

**Say:** “The credible interval is roughly 4.1% to 13.9%. Under this model and prior, it contains 95% of posterior probability for the underlying rate. It is not a guarantee about tomorrow, and it is not the interval for the number of defects in the next batch.”

**Say:** “The assumptions matter: comparable items, a representative sample and a process stable enough to describe with a common rate. If the supplier or inspection process changed halfway through, we might need a different model.”

### 50–90 | Lab A: see what changes the conclusion

**Say:** “Run the exact update. Then use the notebook challenge to replace the prior with Beta(1,1) for the same observations. Next keep the original prior but use sixteen defects in two hundred. Compare posterior means and interval widths. Explain the changes in a sentence; do not just paste the numbers.”

[10 minutes original, 10 alternative prior, 10 larger sample, 10 interpretation.]

**Tutor checks:** Original mean 10/120≈8.33%; alternative prior mean 9/102≈8.82%; sixteen out of two hundred with original prior gives 18/220≈8.18%. Compute interval widths in the notebook, rather than inventing them.

**Say:** “Now use this supplied result: the posterior probability that the underlying rate exceeds ten percent is about 23.75%. For this fictional exercise, additional inspection is triggered if that probability exceeds twenty percent. Would you act?”

**Expected:** “Yes under this stated rule. If the agreed threshold were thirty percent, the answer would change. Neither threshold is an industry or legal standard.”

### 90–105 | Probability is not a policy on its own

**Say:** “The posterior mean is below ten percent, yet the probability of exceeding ten percent can still matter. These are different summaries. The action also depends on the cost of inspection, the cost of missing a problem and the decision-maker's agreed tolerance.”

**Ask:** “Who should own that action threshold?” [Operational decision owner with relevant technical/governance input; not silently chosen to make the model look useful.]

**Break:** “Fifteen minutes. Afterwards, we will see how sampling can approximate a distribution when the exact calculation is harder.”

### 120–150 | MCMC: see whether the sampler explores

**Say:** “Here we already know the exact posterior, so we do not need Markov chain Monte Carlo to solve the problem. We use it because having the exact answer makes the sampler easier to check.”

**Say:** “The Metropolis sampler starts at a possible rate, proposes a nearby value, compares posterior density and either moves or stays. It sometimes accepts a less likely proposal; that helps it explore. A repeated value is a legitimate part of the chain, not a missing record.”

[Show a trace, then an overlaid distribution. Pause before changing views.]

**Say:** “We run four chains from different starting points and discard the initial warm-up in this demonstration. We inspect movement, agreement and autocorrelation. If successive draws are very similar, ten thousand draws do not contain ten thousand independent pieces of information.”

**Ask:** “Would a very high acceptance rate automatically be good?”

**Response:** “Not necessarily. Very small proposals may be accepted often while moving too slowly. More iterations do not automatically fix poor exploration.”

**Say:** “Our recorded chain means are close to the exact mean. That is reassuring for this example, but agreement of means alone is not a convergence certificate. Real analyses need stronger diagnostics, including effective sample size and suitable chain-comparison measures. We will not pretend today's simple checks validate an arbitrary complex model.”

### 150–195 | Lab B: investigate, do not admire the plot

**Say:** “Run the sampler and compare its retained distribution with the exact posterior. Look at the four traces and the reported autocorrelation. Explain what evidence supports the approximation and what would make you distrust it. If you have time, try the small proposal scale in the extension and compare movement.”

[15 minutes run/inspect, 15 compare, 10 optional proposal change or saved-output critique, 5 conclusion.]

**While circulating:** “Could two chains have similar means and still explore badly? What part of the trace would help you answer?”

**If execution is slow:** “Use the saved chain summaries for the core task. A shortened run can illustrate movement, but it is not automatically an equally reliable numerical result.”

### 210–260 | Lab C: the next batch and the generated dataset

**Say:** “To simulate the next batch, first draw a possible rate from the posterior, then draw a binomial count for one hundred future items. We include uncertainty about the rate and randomness in the batch itself. The recorded simulation has mean about 8.32 defects and a central 95% predictive interval of roughly two to seventeen.”

**Ask:** “Why can't we simply read the rate's credible interval as a count interval?” [Different random quantities and additional outcome variability.]

[15 minutes predictive simulation, 15 generated-duration critique, 10 capstone, 10 briefing preparation.]

**Say:** “The final notebook section fits a lognormal distribution to positive service durations and generates new values. A simple statistical distribution is a generative model too. Generative does not have to mean a deep neural network.”

**Say:** “Compare the centre, spread and tails. A close mean can hide missing long-duration cases. A realistic-looking marginal distribution does not show that relationships between variables are preserved. Artificial data are not automatically anonymous, safe to share or suitable for every use.”

**Capstone instruction:** “Add an uncertainty statement and an action rule. Who approves the rule? What evidence would lead you to inspect more, wait or stop?”

### 260–285 | Defend an action, not a percentage

**Say:** “Give us the probability, the policy assumption and the resulting action as three separate statements. That makes it possible for someone to disagree with the policy without misunderstanding the calculation.”

### 285–300 | Close

**Say:** “Write two sentences: one about the unknown rate, one about a future batch. Use the right units in each. Tomorrow we finish with scale, deployment and your proposals.”

---

## Day 5 | What would it take to use this on Monday?

### 0–20 | Start with the bottleneck

**Say:** “Today we will hear some powerful tool names. Before we use them, let's ask what problem they solve. If a task runs comfortably on a laptop and meets the service deadline, a distributed system may add complexity without improving the decision. If it cannot meet the workload, we need evidence about where the bottleneck sits.”

**Ask:** “What makes an analysis difficult in your setting: size, update frequency, inconsistent sources, slow approval, or something else?” [Separate organisational from computing constraints.]

**Say:** “An architecture decision should respond to the actual constraint. 'Big data' is not a prize you win by having many rows.”

### 20–50 | Combine results correctly

[Show the local partition example in Day 5 worked notebook.]

**Say:** “We divide records, calculate partial results and combine matching keys. Sums combine naturally. Counts do too. Means require care: combine the sums and counts, then divide. Averaging averages can give the wrong answer when groups differ in size.”

**Say:** “A separate hand example: one partition has two A orders worth one hundred euros; another has eight worth three hundred and twenty. Their means are fifty and forty. The overall mean is forty-two, not forty-five. The partition sizes matter.”

**Say:** “Hadoop is an ecosystem. HDFS is distributed storage, YARN manages resources, and MapReduce is a processing framework. Spark is a separate execution engine that can work with Hadoop components. Running today's local partition simulation does not mean we have run a Hadoop cluster.”

[If tested, open spark_worked notebook and show the small aggregation. Otherwise use saved output and state that.]

**Say:** “In Spark, transformations describe work and actions request results. Grouping may require data to move between partitions, which is called a shuffle. Collect brings results back into the driver's memory. Collecting two aggregate rows is different from collecting a huge raw table.”

### 50–90 | Lab A: make two routes agree

**Say:** “Run the Spark aggregation and SQL example if your environment is ready. Confirm that the two approaches produce the same totals. If Spark is not ready, use the offline activity and saved result. Explain where partial results combine and what would happen if you collected the whole raw dataset.”

[15 minutes run, 10 reconcile, 10 execution/memory discussion, 5 written result.]

**Tutor checks:** Saved 10,000-row aggregation: A 5,000 orders/EUR 250,000/mean 50; B 5,000/EUR 255,000/mean 51. These are not the figures from the separate small partition example.

**Say:** “The important part is that you can explain both the number and how the system obtains it. Running a cell successfully is only one part of that.”

### 90–105 | What has the laptop actually proved?

**Say:** “Our local run shows that the example can execute in this environment. It is not a cluster benchmark. For a production choice, ask for representative volumes, runtime, memory, reliability, cost and who will operate it.”

**Ask:** “Which evidence would change your mind about needing Spark?” [A measured single-machine solution meeting requirements, or a demonstrated constraint requiring more resources.]

**Break:** “Fifteen minutes. After the break we will compare advanced models with the same discipline we used for the first baseline.”

### 120–150 | A more advanced model still owes us evidence

**Say:** “Spark MLlib provides modelling tools in the Spark environment. In our example, VectorAssembler packs numerical inputs into a vector, the pipeline fits a regression model, and we compare it with a training-derived baseline on held-out data.”

**Say:** “The saved regression MAE is about 2.248 compared with 20.227 for the baseline. The synthetic split uses an identifier rule; it is a teaching arrangement for independent data, not the right default for a time-dependent operational service.”

[Show the local neural network comparison, clearly labelled as a different task.]

**Say:** “A neural network combines numerical transformations in layers. Nonlinear activations allow nonlinear relationships. Training loss is not test accuracy. More layers or training passes do not automatically make a model more useful. Our small example compares a fixed neural model with a linear classifier on a curved synthetic problem.”

**Say:** “The recorded accuracies are about 0.847 and 0.827. That small difference needs context: representative testing, uncertainty, costs and maintenance. Also, do not compare those accuracies with the regression MAEs: the tasks and units are different.”

**Say:** “A generative adversarial network has a generator producing candidates and a discriminator trying to distinguish generated from reference data. Our toy adversarial example updates both, but it is one-dimensional and not a deep image model. It targets mean 2 and standard deviation 0.6; the recorded output is around 2.10 and 0.287. The mean looks close while the spread is too narrow. That is a useful failure to notice.”

### 150–195 | Lab B: prepare the pilot conditions

**Say:** “Use fifteen minutes to run or inspect the MLlib result and compare its baseline. Use ten minutes to inspect the neural and toy generator results; do not spend the whole session waiting for optional training. Then use twenty minutes to draft the conditions for a pilot.”

**Say:** “Your pilot needs a decision owner, a current baseline, a representative test, an error measure that matters, human review where needed, a monitoring schedule and a clear stop rule. Give the stop rule an action and an owner. 'Monitor the model' is too vague. What do you measure, how often, and who pauses it?”

**Ask:** “Suppose the model remains statistically accurate, but its output arrives after the scheduling meeting. Has it succeeded?” [No: timeliness and usability are part of the service requirement.]

**Say:** “Use a limited pilot to learn about the whole process, not only the model. Keep a way to return to the existing process while you investigate a failure.”

### 195–210 | Break and reset

**Say:** “Take fifteen minutes. Afterwards, we will hear your proposals. You don't need a polished sales pitch. We need a clear decision, credible evidence and a next step.”

### 210–225 | Finish the capstone

**Say:** “Use the six headings in the capstone brief: decision, method, data, evaluation, limitation and next step. Each group chooses a spokesperson, but everyone keeps an individual page. Check that you have not promised a result your evidence does not support.”

[Walk around; help narrow proposals.]

**If a proposal is too broad:** “What is the smallest useful decision you could improve in two weeks? Start there. You can describe the larger ambition as a later step.”

### 225–260 | Five presentations

**Say:** “Each group has seven minutes: three minutes speaking, three for interpretation and one for feedback. Please speak in short sections and let the interpreter finish. Lead with the service decision.”

**Feedback template:** “The strongest part of your proposal is [specific evidence or decision]. Before moving forward, I would clarify [one concrete missing assumption]. Your next step is clear when [owner, action and timing].”

**Questions to choose from:** “What will you compare against?” / “What exists at the decision cutoff?” / “What would make you stop?” / “How will a colleague reproduce your result?” / “What would change your recommendation?”

### 260–280 | Individual final practical

**Say:** “This last exercise is individual. It checks your analytical judgement, not your speed at typing. You have five minutes for the translated instructions and fifteen to write. You may use your handbook. If you write in Arabic, we will review it with the interpreter.”

**Read the scenario:** “A service team wants to predict tomorrow's delayed visits using historical records. A vendor reports 96% accuracy. Predicting every visit on time gives 95%. Name the method and the decision. Give one input available at scheduling time. Propose an evaluation split and baseline, and say what further evidence you would request. Correct these three claims: '96% proves usefulness'; 'synthetic guarantees privacy'; 'running Spark locally proves scale'. Finish with a next step, an owner and a measurable stop condition.”

[Use the 10-point final rubric in NO_CODE_ANSWER_KEY: despite its filename, it assesses the common judgement outcomes for this Python-supported course. Do not grade programming that was not requested by the assessment.]

### 280–285 | One last misconception

**Say:** “A one-point accuracy improvement may or may not be useful. We need to know the mistakes, their costs and whether the test resembles the intended use. The correct professional response is neither blind enthusiasm nor automatic rejection. It is a clear request for the evidence needed to decide.”

### 285–300 | Close the week

**Say:** “At the start we asked what you do with data. I hope you now have a few sharper questions to take back: What is the decision? What information is available then? What is the baseline? What does the result leave uncertain? Who owns the next action?”

**Say:** “Please complete the feedback and exit self-assessment. Tell us what helped, what moved too quickly and what you would like to practise next. For your own follow-up, write one action you will take in the next two weeks and who you need to involve.”

**Final words:** “Thank you for the examples, questions and thoughtful disagreements this week. You do not need to use every technique we discussed. Choose the ones that answer your problem, keep the evidence traceable, and make the next decision a little better.”

---

## A short, grounded Spain/Europe discussion to use during Day 1 Lab C

**Say:** “You asked how work is approached here. Two public examples are useful. Spain's INE describes its commitment to the European Statistics Code of Practice and a quality framework. Spain's datos.gob.es publishes guidance on making public data better documented and easier to reuse. Those are documented reference points, not proof that every organisation follows an identical process.”

**Say:** “For this workshop, we translate that quality emphasis into a practical routine: agree the question and definitions, inspect the data, build a reproducible analysis, invite a colleague to challenge it, and record the decision and limitations. This routine is our teaching proposal. You can adapt it to your own service responsibilities and approval process.”

**Ask:** “Which part already happens in your team? Which part would be difficult to introduce? Let's compare practical constraints rather than compare countries.”

Sources, checked 21 September 2026:

- INE, Quality: https://www.ine.es/dyngs/MYP/es/index.htm?cid=35
- datos.gob.es, Practical guide to improving open-data quality: https://datos.gob.es/es/documentacion/guia-practica-para-la-mejora-de-la-calidad-de-datos-abiertos

## Accuracy notes for the tutor

- Do not confuse the original notebook datasets with the separate hand-calculation examples in the fallback workbook.
- Keep synthetic data labelled; the Spanish sources above are reference examples, not the source of the classroom numerical data.
- The interpretation and activity blocks are real timetable commitments. Rehearse rather than assuming the script fills them automatically.
- This script does not make the tutor an expert in every model. Use the technical guides and question bank for preparation; verify unfamiliar claims instead of improvising.
- No legal-compliance conclusion or claim of endorsement by a Spanish, European or Saudi authority is made by this course.
