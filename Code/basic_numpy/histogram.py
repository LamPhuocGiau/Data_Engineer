import codecademylib3
import numpy as np
# Write matplotlib import here:
from matplotlib import pyplot as plt
commutes = np.genfromtxt('commutes.csv', delimiter=',')

# Plot histogram here:
plt.hist(commutes, range = (20, 50), bins = 6)
plt.show()