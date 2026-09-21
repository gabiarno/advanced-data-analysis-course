# Day 5: Big Data and Advanced Models

## Presentation brief

16:9 professional training deck. All text English. White or warm-white background, dark navy text, teal accent. Large readable type (titles about 36pt, body at least 24pt), ample whitespace, one idea per slide. No decorative stock photos, invented logos, or generic AI imagery. Use editable charts, tables and conceptual diagrams where specified. Exact numeric values must remain unchanged. Label synthetic results clearly. Never invent data series to draw an empirical chart. Keep detailed explanations in speaker notes. Audience: 20 participants from Saudi Arabia attending in Genoa, English delivery with Arabic interpretation. No cultural stereotypes. Preserve short task instructions and notebook paths. Include pause-for-interpretation guidance in notes rather than on every slide.

## Narrative arc

Introduce the question and essential concepts, demonstrate a working example, run pair activities, interpret evidence and close with a short review. The deck supports the five-hour timetable, including two 15-minute breaks and interpretation time.

## Slide 1: Big Data and Advanced Models

Visible copy:
Day 5
Computation, evaluation and limitations

Visual: Minimal typographic cover

Speaker notes: Explain the practical focus and the small scale of classroom examples. Distributed concepts do not imply a distributed classroom cluster.

## Slide 2: When one machine becomes limiting

Visible copy:
Memory and compute constraints
Data arrival rate and format
Coordination and transfer costs

Visual: Two-column needs/costs comparison

Speaker notes: There is no universal row-count threshold. Small workloads can be faster in a simple local tool.

## Slide 3: Partitioned aggregation

Visible copy:
Partition 1: A15, B20
Partition 2: C15, B3
Combined: A15, B23, C15

Visual: Editable partition/reduction diagram

Speaker notes: Use the six-record exercise. This local demonstration explains the algorithm and does not run Hadoop.

## Slide 4: Hadoop and Spark

Visible copy:
HDFS: distributed storage
YARN: resource management
MapReduce: processing framework
Spark: a separate execution engine

Visual: Editable four-row comparison table

Speaker notes: Spark can integrate with parts of the Hadoop ecosystem. Keep ecosystem components distinct.

## Slide 5: Spark execution

Visible copy:
Transformations build an execution plan
Actions request results
Grouping may require a shuffle

Visual: Compact editable plan with transformation/action labels

Speaker notes: Our local[2] session uses two local threads. It is not a two-machine cluster or a scalability benchmark.

## Slide 6: Lab A: DataFrame and SQL

Visible copy:
40 minutes
Open day-05-big-data/spark_student.ipynb
Run sections 1–2
Compare aggregation results

Visual: Task slide

Speaker notes: Spark must already be installed. Use the offline activity and recorded outputs if startup fails.

## Slide 7: Aggregation results

Visible copy:
A: 5,000 orders, 250,000 revenue
B: 5,000 orders, 255,000 revenue
Mean amount: 50 versus 51

Visual: Editable table with exact counts, totals and means

Speaker notes: These amounts are synthetic numeric units, not a real business currency. SQL and DataFrame aggregates agree in the recorded run.

## Slide 8: Driver memory

Visible copy:
collect() brings result rows to the driver
A two-row aggregate is small
A huge source table may exhaust memory

Visual: Short explanation with source/result row-count contrast

Speaker notes: Ask participants why the same API call has different risk for a small result and a very large source. Keep this tied to the demonstrated aggregation.

## Slide 9: Break

Visible copy:
15 minutes

Visual: Plain break slide

Speaker notes: State the return time. The next lab fits a Spark model.

## Slide 10: Spark MLlib pipeline

Visible copy:
Planned distance and stops
VectorAssembler builds a feature vector
Linear regression predicts duration

Visual: Editable three-stage pipeline diagram

Speaker notes: Feature assembly does not select features or prevent leakage automatically. The target remains separate.

## Slide 11: Lab B: Spark regression

Visible copy:
45 minutes
Run section 3
Check 800 training and 200 test rows
Compare model and baseline

Visual: Task slide

Speaker notes: The notebook uses a predetermined split suitable only for this synthetic independent example. Stop the Spark session at the end.

## Slide 12: Spark model results

Visible copy:
Model MAE: about 2.248 minutes
Baseline MAE: about 20.227 minutes

Visual: Editable two-bar chart with units and synthetic-data qualifier

Speaker notes: Small numerical differences across environments may occur. This verifies a local teaching workflow, not production performance.

## Slide 13: Break

Visible copy:
15 minutes

Visual: Plain break slide

Speaker notes: Give the return time. The last block includes a short advanced-model demonstration and assessment.

## Slide 14: A small neural network

Visible copy:
Hidden layers: 16 and 8 units
Nonlinear transformations
Training loss differs from test accuracy

Visual: Editable network architecture diagram with layer sizes

Speaker notes: The notebook uses a small multilayer perceptron, not large-scale deep learning. Scaling uses training data.

## Slide 15: Neural-network example

Visible copy:
Linear test accuracy: 82.7%
Neural-network test accuracy: 84.7%
One synthetic split

Visual: Editable two-row comparison with modest emphasis

Speaker notes: This difference does not prove a general advantage or statistical significance. The architectures were fixed before test evaluation.

## Slide 16: Adversarial generation

Visible copy:
Generator creates candidate samples
Discriminator distinguishes reference and generated samples
Both update during training

Visual: Editable two-model feedback diagram

Speaker notes: Our actual training loop is a one-dimensional restricted toy. It is not an image GAN or a deep generator.

## Slide 17: The generator misses variability

Visible copy:
Target mean / SD: 2 / 0.6
Generated mean / SD: about 2.10 / 0.287

Visual: Editable comparison table with standard deviation highlighted

Speaker notes: The mean is close while spread is much too small. Treat this as a useful failure, not successful convergence.

## Slide 18: Final practical assessment

Visible copy:
20 minutes in pairs
Choose methods and evaluation strategies
Interpret two results
Correct three deployment claims

Visual: Task slide pointing to assessments/FINAL_PRACTICAL.md

Speaker notes: This follows the 10-minute briefing and 20-minute notebook exploration. Use the rubric for formative feedback rather than certification.

## Slide 19: Group reporting

Visible copy:
Five groups
One recommendation per group
Include evidence and a limitation

Visual: Simple reporting prompt

Speaker notes: Allow about two minutes of speaking and three minutes for interpretation and feedback per group. Fit reporting into the planned 25 minutes.

## Slide 20: Course review

Visible copy:
Data quality affects conclusions
Evaluation must match intended use
Complexity needs evidence
Uncertainty remains part of decisions

Visual: Four concise closing statements

Speaker notes: Invite each participant to name one method they can explain and one next learning step. Close with the practical limits of the course examples.
