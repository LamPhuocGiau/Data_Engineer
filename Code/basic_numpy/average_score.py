import numpy as np

test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])
test_3_fixed = test_3 + 2
total_grade = test_1 + test_2 + test_3_fixed
print(total_grade)
final_grade = total_grade/3
print(final_grade)