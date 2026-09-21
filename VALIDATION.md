# Validation record

Code cells executed sequentially in fresh Python namespaces on 2026-09-21, using Python 3.12.14, NumPy 2.3.5, pandas 2.2.3, matplotlib 3.10.8 and scikit-learn 1.8.0. Numerical/data-quality assertions passed. Notebooks use standard nbformat 4 JSON. Full Jupyter UI execution and graphical rendering have not been verified; rehearse in the classroom environment. Student solution cells are intentionally blank. This paragraph records the initial Day 1 check. Days 2–5 execution is now documented separately in KERNEL_VALIDATION.md and each day’s worked_RESULTS.md; solution results are in solutions_RESULTS.md.

## day-01-eda/worked.ipynb

```text
order_id       date channel  units  unit_price
   O0000 2026-01-01  Online      4        10.0
   O0001 2026-01-02   Store      6        20.0
   O0002 2026-01-03   Store      6        10.0
   O0003 2026-01-04  Online     -2        20.0
   O0004 2026-01-05  Online      7        20.0
Rows and columns: (122, 5)
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 122 entries, 0 to 121
Data columns (total 5 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   order_id    122 non-null    object 
 1   date        122 non-null    object 
 2   channel     120 non-null    object 
 3   units       122 non-null    int64  
 4   unit_price  119 non-null    float64
dtypes: float64(1), int64(1), object(3)
memory usage: 4.9+ KB
Exact duplicate rows: 2
Missing values:
order_id      0
date          0
channel       2
units         0
unit_price    3
dtype: int64
Non-positive quantities: 1
Valid orders: 119
Rejected orders: 1
Orders with unknown revenue: 3
Recorded revenue, priced orders only (EUR): 10210.0
            units  unit_price      revenue
count  119.000000  116.000000   116.000000
mean     5.117647   17.198276    88.017241
std      7.246480    5.606238   114.585983
min      1.000000   10.000000    10.000000
25%      3.000000   10.000000    40.000000
50%      4.000000   15.000000    75.000000
75%      6.000000   20.000000   120.000000
max     80.000000   25.000000  1200.000000
         order_count  priced_orders  recorded_revenue  mean_order_revenue  median_order_revenue
channel                                                                                        
Online            56             54            3700.0               68.52                  60.0
Store             61             60            6310.0              105.17                  80.0
Unknown            2              2             200.0              100.00                 100.0
Review fences: -1.5 10.5
order_id       date channel  units  unit_price  revenue
   O0007 2026-01-08   Store     80        15.0   1200.0
Pearson correlations:
            units  unit_price  revenue
units       1.000      -0.023    0.966
unit_price -0.023       1.000    0.211
revenue     0.966       0.211    1.000

```

## instructor/first_model.ipynb

```text
   distance_km  stops
0    23.444725      3
1    13.727475      6
2    25.899340      2
3    21.223673      6
4     3.731143      4
Target: delivery duration in minutes
Training rows: 180 Test rows: 60
Baseline test MAE: 17.03 minutes
Linear model test MAE: 3.99 minutes
Learned coefficients: {'distance_km': np.float64(2.2462059481357817), 'stops': np.float64(3.562579270013763)}
Intercept: 16.19 minutes
Predicted duration: 49.3 minutes
     actual  predicted
24     76.6       76.3
6      75.9       78.7
93     47.5       46.8
109   102.2       98.6
104    79.8       79.9

```
