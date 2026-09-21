# Retail orders — synthetic teaching data

Generated with NumPy seed 42. No real people, customers or organisations are represented. The 120 original orders cover 120 successive dates from 2026-01-01; two exact duplicate export records produce 122 rows.

| Field | Meaning |
|---|---|
| order_id | Identifier for an order |
| date | Recorded order date |
| channel | Online or Store; two missing values |
| units | Quantity; one deliberately invalid negative value, one valid bulk order of 80 |
| unit_price | Price per unit in EUR; three missing prices |

Business rules for this exercise: orders have positive quantities; returns belong in a separate table. Duplicate records are export errors. Missing prices are unknown, not free products. The bulk order is valid and should remain unless a separate sensitivity analysis is explicitly labelled.

Synthetic patterns are useful for practising operations but do not support business claims about real markets. Day 1 calculations are descriptive, not a future-model validation workflow.
