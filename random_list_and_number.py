
import random

random_list = []

random_list = [random.randint(1, 100) for i in range(101)]


print(random_list)
randomer_number = random.choice(random_list)
print(randomer_number)

# import ... Syntax: This syntax imports a module or package into your current namespace. 
# import math
# Here, all functions and variables from the math module are imported.But they need to be accessed using the module name as a prefix, like math.sqrt()
# from ... import ... Syntax: This syntax allows you to import specific attributes (functions, classes, variables) from module
# from math import sqrt
# Now, you can directly use sqrt() without needing to prefix it with math.