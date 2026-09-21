# Reference 2 — Python and pandas for this course

Everything here appears in the course notebooks. Copy from this page freely.

## Getting started

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/retail_orders.csv')
```

If `read_csv` cannot find the file, you opened Jupyter from the wrong folder. Open it from the repository root.

## Looking at a table

```python
df.head()             # first five rows
df.shape              # (rows, columns)
df.info()             # column names, types, non-null counts
df.describe()         # numeric summary
df.columns            # column names
df['channel'].unique()          # distinct values
df['channel'].value_counts()    # counts per value
```

## Selecting and filtering

```python
df['units']                      # one column
df[['units', 'unit_price']]      # several columns
df.loc[df['units'] > 10]         # rows matching a condition
df.loc[df['units'] > 10, 'unit_price']       # condition plus column
df.loc[(df['units'] > 10) & (df['channel'] == 'Store')]   # two conditions
```

Use `&` for and, `|` for or, and put each condition in its own brackets. Python's `and` / `or` do not work on columns.

## Data quality

```python
df.duplicated().sum()            # count exact duplicate rows
df.drop_duplicates()             # remove them
df.isna().sum()                  # missing values per column
df.dropna(subset=['unit_price']) # drop rows missing a price
df['channel'].fillna('Unknown')  # label missing categories
```

Do not fill missing numbers with zero unless zero is genuinely the right value.

## Creating and aggregating

```python
df['revenue'] = df['units'] * df['unit_price']

df['revenue'].sum()
df['revenue'].mean()
df['revenue'].median()
df['revenue'].std()
df['revenue'].quantile([0.25, 0.75])

df.groupby('channel')['revenue'].sum()
df.groupby('channel').agg(orders=('order_id', 'count'),
                          revenue=('revenue', 'sum'))
```

Sums and means skip missing values silently. That is why you report how many rows contributed.

## Dates

```python
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')
df.set_index('date').resample('D')['units'].sum()   # daily totals
```

## Charts

```python
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(totals.index, totals.values)
ax.set_title('Store revenue exceeds online by EUR 2,610 (synthetic data)')
ax.set_xlabel('Channel')
ax.set_ylabel('Recorded revenue (EUR, priced orders only)')
plt.tight_layout()
```

A chart without labelled axes and a stated finding is not finished.

## Modelling, the standard shape

```python
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

X = df[['distance_km', 'planned_stops']]
y = df['duration_min']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42)

model = Pipeline([
    ('impute', SimpleImputer(strategy='median')),
    ('fit', LinearRegression()),
])
model.fit(X_train, y_train)
predictions = model.predict(X_test)
mean_absolute_error(y_test, predictions)
```

Put every preprocessing step inside the `Pipeline`. That is what stops the held-out data influencing training.

```python
baseline = np.full_like(y_test, y_train.mean(), dtype=float)
mean_absolute_error(y_test, baseline)     # always compute this
```

## Classification

```python
from sklearn.metrics import confusion_matrix, classification_report

confusion_matrix(y_test, predictions)     # rows actual, columns predicted
print(classification_report(y_test, predictions))
```

Reading the matrix, with classes ordered [0, 1]:

|  | Predicted 0 | Predicted 1 |
|---|---|---|
| **Actual 0** | correct negative | false alarm |
| **Actual 1** | missed event | correct positive |

## Time series, splitting correctly

```python
train = series.iloc[:-28]        # everything except the last 28 days
test  = series.iloc[-28:]        # the last 28 days

last_value = np.repeat(train.iloc[-1], len(test))          # naive baseline
weekly     = np.tile(train.iloc[-7:].values, 4)[:len(test)]  # seasonal naive
```

Never use `train_test_split` on a time series.

## Fixing the common errors

| Message | What it means | Fix |
|---|---|---|
| `ModuleNotFoundError` | The package is not in this kernel's environment | Install requirements into the environment the kernel uses |
| `FileNotFoundError` | Wrong working directory | Start Jupyter from the repository root |
| `NameError: 'df' is not defined` | You skipped a cell, or restarted the kernel | Restart the kernel and run all cells in order |
| `KeyError: 'revenue'` | The column does not exist yet, or is misspelled | Check `df.columns` |
| `SettingWithCopyWarning` | You are editing a slice of another frame | Use `.copy()` when you create the subset |
| `ValueError: could not convert string to float` | A numeric column contains text | Inspect with `df['col'].unique()` |
| Chart does not appear | An earlier cell raised an exception | Scroll up and fix the first error, not the last |

## Two habits that prevent most problems

1. **Restart the kernel and run all cells** before you trust a result. Notebooks keep old variables alive; a result that only works in your current session is not reproducible.
2. **Print the shape after every filter.** `print(df.shape)` costs nothing and catches the moment you silently dropped half your data.
