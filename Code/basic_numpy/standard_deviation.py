import numpy as np

pumpkin = np.array([68, 1820, 1420, 2062, 704, 1156, 1857, 1755, 2092, 1384])

acorn_squash = np.array([20, 43, 99, 200, 12, 250, 58, 120, 230, 215])

pumpkin_avg = np.mean(pumpkin)
pumpkin_std = np.std(pumpkin)
acorn_squash_avg = np.mean(acorn_squash)
acorn_squash_std = np.std(acorn_squash)
if pumpkin_std > acorn_squash_std:
  winner = pumpkin
else:
  winner = acorn_squash
print(pumpkin_avg)
print(pumpkin_std)
print(acorn_squash_avg)
print(acorn_squash_std)
