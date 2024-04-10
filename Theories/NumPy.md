# NumPy
## Table of contents
    - [Introduction](#Introduction)
    - [Numpy arrays](#Numpy-arrays)
    - [Create an array from csv](#Create-an-array-from-csv)
    - [Operations with numpy arrays](#Operations-with-numpy-arrays)
    - [Two dimensional arrays](#Two-dimensional-arrays)
    - [Selecting elements from a 1D array](#Selecting-elements-from-a-1D-array)
    - [Selecting elements from a 2D array](#Selecting-elements-from-a-2D-array)
    - [Logical operatios with array](#Logical-operatios-with-array)
    - [NumPy and mean](#NumPy-and-mean)
    - [Mean and logical operations](#Mean-and-logical-operations)
    - [Caculating of 2D array](#Caculating-of-2D-array)
    - [Outliersa](#Outliersa)
    - [Sorting and outliers](#Sorting-and-outliers)
    - [Numpy and median](#Numpy-and-median)
    - [Mean Vs. meadian](#Mean Vs. meadian)
    - [Percentiles](#ercentiles)
    - [Numpy and standard deviation](#Numpy-and-standard-deviation)
    - [Introduction](#Introduction)

```
import numpy as np
```
## Numpy arrays
```
my_list = [1, 2, 3, 4, 5, 6]
my_array = np.array(my_list)
```
## Create an array from csv
```
csv_array = np.genfromtxt('sample.csv', delimiter=',')
```
## Operations with numpy arrays

Addition, subtraction, multiplication, and division, square, square root.

```
my_list = [1, 2, 3, 4, 5, 6]
my_list_plus_2 = my_list + 2
my_list_square = my_list ** 2
my_list_square_root = np.sqrt(my_list)
## Two dimensional arrays
```
Adding or subtracting arrays.

```
a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])
a + b
result: array([ 7,  9, 11, 13, 15])
```

## Selecting elements from a 1D array
```
a = np.array([5, 2, 7, 0, 11])
>>> a[0]
5 
>>> a[-1]
11
>>> a[-2]
0
>>> a[:3]
array([5, 2, 7])
>>> a[-3:]
array([7, 0, 11])
```
## Selecting elements from a 2D array

A 2-d array is a[row,column] where a is the array.

```
a = np.array([[32, 15, 6, 9, 14], 
              [12, 10, 5, 23, 1],
              [2, 16, 13, 40, 37]])
```
>>> a[2,1]
16
>>> a[:,0]
array([32, 12,  2])
>>> a[1,:]
array([12, 10,  5, 23,  1])
>>> a[0,0:3]
array([32, 15,  6])

## Logical operatios with array

```
>>> a = np.array([10, 2, 2, 4, 5, 3, 9, 8, 9, 7])
>>> a > 5
array([True, False, False, False, False, False, True, True, True, True], dtype=bool)
>>> a[a > 5]
array([10, 9, 8, 9, 7])
>>> a[(a > 5) | (a < 2)]
array([10, 9, 8, 9, 7])
```
## NumPy and mean
```
>>> survey_array = np.array(survey_responses)
>>> np.mean(survey_array)
5.220
```
## Mean and logical operations
a logical operator will evaluate each item in an array to see if it matches the specified condition. If the item matches the given condition, the item will evaluate as True and equal 1. If it does not match, it will be False and equal 0. mean value will be equivalent to the total number of True items divided by the total array length.
```
>>> np.mean(survey_array > 8)
0.2
```

## Caculating of 2D array

## Outliers

## Sorting and outliers

## Numpy and median

## Mean Vs. meadian

## Percentiles

## Numpy and standard deviation