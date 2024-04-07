# Pandas
## Table of contents
  - [Introduction to Pandas](#Introduction-to-Pandas)
  - [Aggregates in Pandas](#Aggregates-in-Pandas)
  - [Multiple table in Pandas](Aggregates-in-Pandas)
## Introduction to Pandas

## Aggregates in Pandas

## Multiple table in Pandas
**Inner Merge**.

The .merge() method looks for columns that are common between two DataFrames.

```
new_df = pd.merge(orders, customers)
```
Joining more than two DataFrames.

```
big_df = orders.merge(customers)\
    .merge(products)
```
Rename the columns for merging when columns of DataFrame the same name. But they are different meaning
```
pd.merge(
    orders,
    customers.rename(columns={'id': 'customer_id'}))
```
