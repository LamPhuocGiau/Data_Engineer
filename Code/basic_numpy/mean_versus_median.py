import numpy as np

time_spent = np.genfromtxt('file.csv', delimiter=',')

print(time_spent)
minutes_mean = np.mean(time_spent)
minutes_median = np.median(time_spent)
print(minutes_mean)
print(minutes_median)
best_measure = minutes_median