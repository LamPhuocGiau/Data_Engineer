import numpy as np
cupcakes = np.array([2, 0.75, 2, 1, 0.5])
recipes = np.genfromtxt('recipes.csv', delimiter = ',')
print(recipes)
eggs = recipes[:,2]
print(eggs)
print(eggs == 1)
cookies = recipes[2, :]
print(cookies)
double_batch = cupcakes * 2
print(double_batch)
grocery_list = cookies + double_batch
print(grocery_list)