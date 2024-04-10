import numpy as np

allergy_trials = np.array([[6, 1, 3, 8, 2], 
                           [2, 6, 3, 9, 8], 
                           [5, 2, 6, 9, 9]])
total_mean = np.mean(allergy_trials)

trial_mean = np.mean(allergy_trials, axis = 1)

patient_mean = np.mean(allergy_trials, axis = 0)
print(total_mean)
print(trial_mean)
print(patient_mean)