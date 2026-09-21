# Day 1: Exploratory Data Analysis

## Presentation brief

16:9 professional training deck. All text English. White or warm-white background, dark navy text, teal accent. Large readable type (titles about 36pt, body at least 24pt), ample whitespace, one idea per slide. No decorative stock photos, invented logos, or generic AI imagery. Use editable charts, tables and conceptual diagrams where specified. Exact numeric values must remain unchanged. Label synthetic results clearly. Never invent data series to draw an empirical chart. Keep detailed explanations in speaker notes. Audience: 20 participants from Saudi Arabia attending in Genoa, English delivery with Arabic interpretation. No cultural stereotypes. Preserve short task instructions and notebook paths. Include pause-for-interpretation guidance in notes rather than on every slide.

## Narrative arc

Introduce the question and essential concepts, demonstrate a working example, run pair activities, interpret evidence and close with a short review. The deck supports the five-hour timetable, including two 15-minute breaks and interpretation time.

## Slide 1: Exploratory Data Analysis

Visible copy:
Day 1
Advanced Data Analysis Techniques

Visual: Minimal typographic cover, ample whitespace

Speaker notes: Introduce the practical course. Pause for Arabic interpretation before moving on.

## Slide 2: Today’s practical outcome

Visible copy:
Inspect a table
Explain cleaning choices
Report a qualified finding

Visual: One large question beside a small sample data table

Speaker notes: The aim is a defensible description of data. Explain that all course examples are synthetic.

## Slide 3: Working in pairs

Visible copy:
10 pairs
Swap keyboard and explanation roles
Ask for help when blocked

Visual: Simple numbered instructions

Speaker notes: There are 20 participants. Demonstrate a short step, allow interpretation, then invite pairs to repeat it.

## Slide 4: The order table

Visible copy:
One row represents one order
Columns describe date, channel, units and price
122 raw rows

Visual: Editable table with columns order_id, channel, units, unit_price and two illustrative labelled rows

Speaker notes: Open student.ipynb. Ask participants to identify the observation and explain why a repeated customer would not necessarily mean a duplicate order.

## Slide 5: Python operations for a table

Visible copy:
df['units'] selects a column
df[df['units'] > 0] filters rows
groupby combines records by category

Visual: Three large readable code lines with plain-language annotations

Speaker notes: Explain brackets and comparisons slowly. Keep the code visible until interpretation finishes.

## Slide 6: A data-quality audit

Visible copy:
2 exact duplicate records
3 missing prices
2 missing channels
1 non-positive quantity

Visual: Four aligned rows, no decorative dashboard

Speaker notes: These are counts in the raw synthetic dataset. Ask which problems require a business rule before changing anything.

## Slide 7: Lab A: Data audit

Visible copy:
40 minutes
Open day-01-eda/student.ipynb
Count rows, duplicates and missing values
Explain one issue

Visual: Large task instructions with the filename on its own line

Speaker notes: Use TASK_CARDS.md activity A. Check that pairs find 122 rows and distinguish invalid negative units from a valid bulk order.

## Slide 8: Cleaning decisions

Visible copy:
Remove documented export duplicates
Exclude the invalid quantity
Keep unknown prices missing
Label missing channels Unknown

Visual: Two-column decision/reason table

Speaker notes: The exercise defines returns in a separate table, so negative units are invalid here. Missing price does not mean a free order.

## Slide 9: Mean and median

Visible copy:
Values: 10, 12, 13, 15, 100
Mean: 30
Median: 13

Visual: Editable five-value dot plot or simple table with the two statistics

Speaker notes: Ask which statistic changes most when the large observation changes. Neither measure is universally better.

## Slide 10: Dispersion and unusual values

Visible copy:
Standard deviation describes spread around the mean
IQR describes the middle half
A flag requests investigation

Visual: Distribution sketch explicitly labelled illustrative

Speaker notes: Explain that an unusual value may be valid. The 80-unit bulk order stays in the main report.

## Slide 11: Break

Visible copy:
15 minutes

Visual: Quiet typographic break slide

Speaker notes: Confirm the return time aloud. The provisional daily schedule includes this break.

## Slide 12: Lab B: Descriptive summary

Visible copy:
45 minutes
Clean with documented rules
Calculate revenue
Create one labelled chart

Visual: Numbered instructions with room for a demonstration

Speaker notes: Pairs should reach 119 valid orders and 116 priced orders. Ask each pair to explain one cleaning choice.

## Slide 13: Revenue coverage

Visible copy:
119 valid orders
116 orders with known revenue
Recorded revenue: EUR 10,210

Visual: Large figures with a visible qualifier: priced orders only

Speaker notes: Three valid orders have unknown prices. The recorded revenue does not represent a complete revenue total for every valid order.

## Slide 14: Recorded revenue by channel

Visible copy:
Store: EUR 6,310
Online: EUR 3,700
Unknown: EUR 200

Visual: Editable horizontal bar chart with exact values and EUR units

Speaker notes: Synthetic data, priced orders only. A larger total may reflect more orders or higher order values and does not establish causality.

## Slide 15: Association and causation

Visible copy:
Revenue equals units multiplied by price
The units–revenue association partly follows from this formula
A causal claim requires more evidence

Visual: Formula and one short explanatory annotation

Speaker notes: Avoid treating correlation as a reason to change commercial strategy. Invite participants to name a possible alternative explanation.

## Slide 16: Break

Visible copy:
15 minutes

Visual: Quiet typographic break slide

Speaker notes: Give the return time and remind pairs which notebook they need next. Pause for interpretation.

## Slide 17: Pair challenge: Management briefing

Visible copy:
50 minutes
Compare channels
Review the bulk order
Write a finding, a limitation and a next step

Visual: A simple three-line response template

Speaker notes: Use Task C. Combine pairs into five groups for reporting, with one finding per group.

## Slide 18: Day 1 review

Visible copy:
Why does missing differ from zero?
When can an unusual order remain valid?
What limits our revenue comparison?

Visual: Three spaced discussion questions

Speaker notes: Use the answer key after participants respond. Tomorrow we will predict outcomes and evaluate on unseen examples.
