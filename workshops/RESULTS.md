# Recorded workshop results

All code cells executed in sequence in a fresh Python namespace. This checks the computations, not Jupyter kernel startup on learner laptops. All cases are synthetic and separate from the original course notebooks.

## Code cell 1

```text
```

## Code cell 2

```text
team    type  count  mean_minutes  total_minutes
   A routine     90          10.0          900.0
   A complex     10          30.0          300.0
   B routine     10           8.0           80.0
   B complex     90          25.0         2250.0
Observed mix means: {'A': 12.0, 'B': 23.3}
Common mix means: {'A': 20.0, 'B': 16.5}
```

## Code cell 3

```text
 threshold  false_alarms  misses  cost
       0.1           107       3   685
       0.2            75       8   775
       0.3            46      16  1030
       0.4            29      25  1395
       0.5            17      32  1685
       0.6             9      39  1995
       0.7             1      51  2555
       0.8             1      59  2955
       0.9             0      67  3350
Selected using validation only: 0.1
```

## Code cell 4

```text
{'test_n': 240, 'selected_threshold': 0.1, 'selected_cost': 600, 'default_0.5_cost': 1700, 'always_negative_cost': 3800}
```

## Code cell 5

```text
method   last  weekly
origin               
56      22.01    6.01
70      16.55    3.72
84      17.23    4.45
98      16.45    4.57
Mean validation MAE: {'last': 18.06, 'weekly': 4.69}
Chosen method: weekly
```

## Code cell 6

```text
Final 14-day MAE: 3.4
```

## Code cell 7

```text
         prior   mean  low95  high95  P(rate>10%)  act_at_20%  act_at_30%
       uniform 0.0882 0.0416  0.1501       0.3094        True        True
      moderate 0.0833 0.0410  0.1387       0.2375        True       False
strong concern 0.1400 0.0956  0.1912       0.9589        True        True
```

## Code cell 8

```text
 week  mae_minutes  breach  two_week_trigger
    1          7.8   False             False
    2          8.1   False             False
    3          7.5   False             False
    4          9.2   False             False
    5         10.1   False             False
    6         13.5    True             False
    7         14.1    True              True
    8          8.4   False             False
Trigger weeks: [7]
```
