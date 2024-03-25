def double_index(my_list, index):
  if index < len(my_list) and index > - len(my_list):
   
    my_list[index] = my_list[index] * 2
    return my_list
  else:
    return my_list
    

print(double_index([3, 8, -10, 12], 2))