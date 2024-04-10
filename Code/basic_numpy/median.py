import numpy as np

large_set = np.genfromtxt('household_income.csv', delimiter=',')
small_set_median = 40500

large_set_median = np.median(large_set)
print(large_set_median)
