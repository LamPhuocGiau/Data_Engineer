def odd_indices(my_list):
  index = 0
  odd_list = []
  while index < len(my_list):
    if index % 2 == 0:
      index += 1
    else:
      odd_list.append(my_list[index])
      index += 1
  return odd_list


#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))