def middle_element(my_list):
  if len(my_list) % 2 == 0:
    total = my_list[int(len(my_list)/2)] + my_list[int(len(my_list)/2) - 1]
    return total / 2
  else:
    return my_list[int(len(my_list)/2)]

print(middle_element([5, 2, -10, -4, 4, 5]))