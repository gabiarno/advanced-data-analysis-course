# Question bank — what participants will ask

Rehearse the answers out loud. A confident, short, honest answer builds more credibility than a long one, and "I'll verify that" is always available and never damaging when you actually follow up.

Answers are written as you would say them, with the interpretation pause implied after each idea.

## About the course and the data

**"Why is all the data synthetic? We wanted real-world examples."**
Because every result has to be reproducible on twenty laptops and none of us can share confidential data in a classroom. The methods, the evaluation and the mistakes are identical on real data — what changes is that real data is messier, and we discuss that messiness explicitly on each day. Your capstone uses a problem from your own work, which is where the realism comes in.

**"Will these methods work on our data?"**
The methods will run. Whether they work is an empirical question and the honest answer is that nobody can tell you from here. What this course gives you is the ability to find out properly — a baseline, a correct split and a metric that matches your costs.

**"Can you look at our actual data?"**
Not in the classroom, and not without a data agreement. But bring the problem to the capstone and we will design the evaluation together, which is the part that usually goes wrong.

**"Is this course going to make me a data scientist?"**
No, and you should be suspicious of any five-day course that says it will. It makes you someone who can apply these methods to a well-posed problem, evaluate them honestly, and tell when someone else's result is unreliable. That third one is worth more than people expect.

## Day 1 — EDA

**"Why not just delete all the rows with missing values?"**
Sometimes that is right. But consider why they are missing: if prices are missing more often for one channel, deleting them biases every channel comparison you make afterwards. Deletion is a decision that needs a justification, the same as any other.

**"Why not fill the missing prices with the average?"**
Because you then report a number as if it were measured. If you do impute, you must say so, and you must say what it did to your conclusion. On Day 2 we put imputation inside the pipeline, which is the version that does not corrupt the evaluation.

**"Which is better, mean or median?"**
Neither. They answer different questions. The mean answers "what if this were shared equally"; the median answers "what is typical". Report both when they differ a lot, because that difference is itself information.

**"Should we remove the 80-unit order? It is distorting the average."**
It is a real order. Removing it changes the question from "what happened" to "what happened excluding large orders", which may be a fair question — but then say that is what you are reporting. Removing valid data because it is inconvenient is how analyses become dishonest without anyone lying.

**"How do I know if an outlier is an error?"**
The data cannot tell you. The business rule tells you. A negative quantity is invalid here because the rule says returns live in another table. Without that rule, a negative quantity is just an unusual number.

## Day 2 — Machine learning

**"Why can't we train on all the data? More data is better."**
More training data usually is better — but then you have no honest way to estimate how the model performs on cases it has not seen. You need both. In deployment you may retrain on everything, after the evaluation decisions are fixed.

**"Our accuracy is 95%. Isn't that good?"**
Ask what fraction of cases are the common class. If 95% of routes are on time, then "always predict on time" scores 95% and catches zero delays. Accuracy is the metric that flatters a useless model most reliably.

**"Why does cross-validation show negative MAE?"**
scikit-learn maximises scores, so error metrics are negated. The notebook flips the sign back for readability. It is a software convention, not a result.

**"Which algorithm is best?"**
There is no general answer, and anyone who gives you one is selling something. For tabular data of this size, start with a linear model as your reference and a gradient-boosted tree as your strong candidate. Then compare them properly.

**"Why did the random forest lose to logistic regression?"**
It happens often, especially when the true relationship is close to linear and the dataset is small. This is exactly why you compare rather than assume. A forest is more flexible; flexibility is not free.

**"Results change when I change the random seed. Which one is correct?"**
All of them and none of them. The variation tells you how stable your estimate is. If your conclusion flips with the seed, your conclusion is not supported by this much data. Report across several seeds.

**"Can we use the test set to choose the model?"**
No — and this is the single most common way good teams get burned. Once you select on the test set, it measures how well you selected, not how well the model generalises. Use validation data to choose; keep the test set for one final look.

**"How many times can I look at the test set?"**
Realistically, once. Each additional look is a small amount of information leaking into your choices.

## Day 3 — Time series and NLP

**"Why can't I use a random split for a time series?"**
Because it lets the model learn from Thursday to predict Wednesday. At prediction time you will not have Thursday. The evaluation would be optimistic, and you would only find out in production.

**"ARIMA is the sophisticated method. Why did the simple baseline beat it?"**
Because the series has a strong weekly pattern and the ARIMA(1,1,1) we fitted does not represent seasonality. A seasonal model would do better. The general lesson is real though: cheap baselines are hard to beat, and a method being sophisticated is not evidence it is appropriate.

**"How do I choose p, d and q?"**
Systematically, on validation data cut from the training period — never by looking at the test window. Information criteria and diagnostic plots help. What you must not do is try orders until the test score improves.

**"Our text is in Arabic. Does this work?"**
The pipeline structure is the same. The tokenisation is not — Arabic morphology, orthographic variation and diacritics all matter, and a word-count approach built for English will underperform. You would need Arabic-appropriate preprocessing and, importantly, evaluation on Arabic data. That today's model scored 100% on English messages tells you nothing about Arabic.

**"Why not just use ChatGPT for the text classification?"**
For some tasks that is a reasonable option, and for some it is the wrong tool. The questions that decide it are the same ones we have been asking all week: what is your baseline, how are you evaluating it, on how many examples, and what does an error cost? A large model does not remove the need for an evaluation set — it makes it more important, because you cannot inspect what it is doing.

**"100% accuracy — the model is perfect?"**
It scored 100% on eight messages, in one language, written by one person. If I flipped a coin three times and got three heads, you would not conclude the coin has two heads. Same reasoning, and this is the claim you will be asked to correct in the final exercise.

## Day 4 — Bayesian

**"Isn't the prior just an opinion? That seems unscientific."**
It is an assumption, stated explicitly and open to challenge — which is more transparent than most analyses, where assumptions are buried in the method. The honest practice is to show the result under several priors. If the conclusion changes with the prior, say so; that is a finding.

**"What's the difference between a credible interval and a confidence interval?"**
A credible interval says: given this model and this prior, there is 95% posterior probability the parameter is in this range. A confidence interval is a statement about the long-run behaviour of the procedure, not about this particular interval. People interpret confidence intervals the Bayesian way all the time, which is precisely the confusion the Bayesian version avoids.

**"Why do we need MCMC when we got the exact answer?"**
Here we do not — the Beta-Binomial pair has a closed form, which is exactly why it is the right teaching example: you can check the sampler against the truth. For almost any realistic model there is no closed form, and sampling is the only route.

**"How do I know the chain has converged?"**
You never prove it. You check several things and stay suspicious: run multiple chains from different starts and see whether they agree, inspect the traces, look at autocorrelation and effective sample size. These are diagnostics of failure, not certificates of success.

**"Is synthetic data anonymous?"**
Not automatically. A generator trained on real records can reproduce them, particularly rare ones, and rare records are the ones most likely to identify someone. Synthetic data reduces risk if it is generated and tested carefully. Treating "synthetic" as a synonym for "safe to share" is a mistake regulators have already noticed.

## Day 5 — Big data

**"At how many rows do I need Spark?"**
There is no threshold. If it fits comfortably in memory and runs fast enough, use pandas — it will usually be faster, because you avoid the coordination overhead. Consider distribution when the data does not fit, when it arrives faster than one machine processes it, or when the computation itself is the bottleneck.

**"Is Spark better than Hadoop?"**
They are not the same kind of thing. Hadoop is an ecosystem — HDFS for storage, YARN for resources, MapReduce for processing. Spark is an execution engine that can use HDFS and YARN and generally replaces MapReduce. "Better than" is the wrong comparison.

**"We ran it locally on two threads and it was slow. Is Spark slow?"**
On this data, yes — because you paid the coordination cost and got no benefit. That is the point of the demonstration. Spark's advantage appears at a scale we cannot reproduce in this room, and I am not going to claim otherwise.

**"Can the GAN generate our data?"**
The toy GAN here generates one number from one distribution. It demonstrates the generator–discriminator mechanism and nothing more. Realistic tabular generation needs a different architecture, substantially more data, careful evaluation of the distribution rather than the mean, and a privacy assessment.

**"What about deep learning? Shouldn't we be using neural networks?"**
For tabular data of the size most organisations actually have, gradient-boosted trees usually match or beat neural networks with far less effort. Neural networks dominate for images, audio and text. Choose by the data type and the size, not by which sounds more advanced.

## The hard ones

**"Can we deploy what we built this week?"**
No. What you built is a demonstration on synthetic data. What you learned is how to evaluate the real version when you build it. Production needs representative and governed data, agreed error costs, monitoring, a retraining trigger and an owner.

**"How much will this improve our numbers?"**
Nobody can answer that without your data, and anyone who does is guessing. What you can say is: here is the baseline today, here is how we would measure improvement, and here is the pilot that would tell us.

**"Our vendor says their model is 99% accurate. Should we believe them?"**
Ask them four questions: what is the baseline, how was the data split, how many cases are in the test set, and how many times has that test set been used? A vendor who answers all four well is credible. One who cannot answer them has not done the work.

**"You said we cannot conclude anything. So what is the point?"**
We can conclude a great deal — we just have to say what the conclusion covers. "Store revenue is higher in this sample, for reasons we have not established" is a genuine finding and a useful one. What we avoid is the leap to "the store channel performs better, so shift the budget". That leap is where money gets lost.

**A question you genuinely cannot answer.**
*"I want to verify that rather than give you an inaccurate answer. I'll record it and come back to you tomorrow morning."* Write it on the parking list where everyone can see it. Then answer it. Doing this once, visibly and reliably, buys you more trust than answering ten questions confidently.
