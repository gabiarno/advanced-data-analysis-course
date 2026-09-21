# Day 5 — Big data and advanced models

## Outcomes and preparation

Learners will explain partitioned aggregation, run Spark DataFrame/SQL operations, evaluate a Spark MLlib model, distinguish distributed computing from a neural network, and explain generator/discriminator roles. Deep-learning and GAN coverage is introductory; local toy models do not demonstrate production-scale training.

Run both worked.ipynb and spark_worked.ipynb in advance. Spark requires the separate Spark requirements and Java 17. Confirm successful startup on the instructor laptop before class. No online accounts, GPUs or external datasets are required after installation. Use OFFLINE_ACTIVITY.md as a prepared fallback if a participant cannot start Spark.

## Timetable

| Minutes | Activity |
|---|---|
| 0–20 | Recap evaluation; discuss why a table may outgrow one machine |
| 20–50 | Explain partitions, Hadoop/MapReduce and Spark; demonstrate SQL |
| 50–90 | Lab A: Spark aggregation and SQL agreement |
| 90–105 | Compare results; explain actions and data movement |
| 105–120 | Break |
| 120–150 | Demonstrate feature assembly and a Spark MLlib pipeline |
| 150–195 | Lab B: run evaluation and compare a baseline |
| 195–210 | Break |
| 210–260 | 10-minute neural/GAN briefing, 20-minute guided notebook exploration, 20-minute final practical assessment |
| 260–285 | Five groups report final recommendations and limitations |
| 285–300 | Course recap, feedback and next steps |

## Instructor explanations

### 1. Big data is an engineering constraint

The issue is not a magic row count. Volume, arrival rate, format, computation and available memory matter. Distributed systems divide storage or computation across resources, adding coordination and data-transfer costs. Small tasks may run faster in pandas. Spark on two local threads is still one laptop.

Demonstrate partitioned totals using the six records in worked.ipynb. A map operation emits or transforms records; partial aggregation reduces intermediate volume; matching keys are brought together for final reduction. Hadoop is an ecosystem: HDFS stores distributed blocks, YARN manages resources and MapReduce is a processing framework. Spark is a separate engine and may integrate with Hadoop components. This notebook simulates the aggregation idea; it does not run Hadoop.

### 2. Spark execution

The DataFrame describes structured distributed data. Transformations such as filter or groupBy define work. Actions such as count, show or collect request results and trigger execution. Grouping often requires a shuffle to bring matching keys together. `collect()` retrieves all result rows into driver memory; it is safe here only because the aggregate has two rows. It is unsafe as a routine way to inspect very large tables.

SQL and the DataFrame API should describe equivalent operations. The exercise asserts that their small aggregate results agree. Query plans help inspect execution; they do not by themselves establish performance.

### 3. Spark MLlib

VectorAssembler packs numeric input columns into a feature vector. The Pipeline fits a linear regression using planned distance and stops. The target is duration. A predetermined synthetic split reserves 200 routes; 800 train the model. Compare final-test MAE with a training-mean baseline. The outcome is not used as an input.

The seeded generated data make this a repeatable teaching case. A split based on id modulo five is only for this independent synthetic setup. For future operational forecasting or repeated entities, choose time-aware or group-aware splits instead. Parallel numerical operations can yield small differences across environments.

### 4. Neural networks and scale are separate ideas

A neural network learns layers of numerical transformations. Hidden layers permit nonlinear relationships; an activation function provides nonlinearity. Training minimises an objective with iterative updates. An epoch is a pass through training examples. Training loss measures fit to training data; it is not held-out accuracy.

Our small network has hidden layers of 16 and 8 units. It uses early stopping with an internal validation portion of training data. The outer test remains separate. The two architectures are fixed before test evaluation. On the curved synthetic dataset a linear boundary has limitations, but this does not mean networks always win. Real deep models involve larger architectures, data requirements, compute and monitoring.

### 5. GAN roles and limits

The generator converts random input into candidate observations. The discriminator learns to distinguish reference observations from generated ones. Their objectives interact: discriminator improvement changes the feedback received by the generator. Training can oscillate or collapse to too little diversity.

The optional example has an affine Gaussian generator and a quadratic-feature logistic discriminator. Both actually update, but neither is a deep network. It generates a scalar, not an image or a realistic customer record. Show the parameter log and histogram; ask whether matching one distribution proves coverage of rare cases. Expected: no. Do not infer privacy from resemblance or artificial origin.

## Common questions and recovery

“Is Spark faster?” It depends on workload, partitioning, hardware and overhead; our lab is not a benchmark.

“Does Spark train every deep-learning model?” Spark MLlib and deep-learning frameworks serve different roles and integrations. This lab does not demonstrate distributed deep-learning training.

“Why Java for Python Spark?” Local PySpark communicates with the JVM-based Spark engine.

If startup fails, switch immediately to the offline partition/SQL activity and saved results. Do not consume the class installing a large package. Record the environment issue for follow-up and do not describe fallback work as a successful Spark execution.

## Classroom routine

20 participants, 10 pairs, five groups for reporting. Swap keyboard and explanation roles every 10–15 minutes. Explain one idea, pause for Arabic interpretation, demonstrate a few lines, then let pairs repeat. All written materials are English. Confirm that participants can use English task cards or arrange interpreter-reviewed support.

Each timetable totals 300 minutes including two 15-minute breaks. There are 135 minutes of protected practice. For 300 contact minutes, add 30 minutes of supported practice and put breaks outside those hours. Confirm the contractual interpretation.

Use worked.ipynb for rehearsal; student.ipynb contains the same runnable examples plus challenges. Beginners change and interpret working code rather than typing everything from scratch. Stronger participants use the extensions. Read worked_RESULTS.md for verified outputs and open the executed notebook for saved numerical results. Figures are in figures/.

Do not rush through every line. The goal is for each pair to explain a result, a limitation and a next step. If the interpreter needs more time, reduce extension work, not the foundational lab or break.
