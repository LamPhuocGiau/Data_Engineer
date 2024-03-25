def delete_starting_evens(my_list):
  index = 0
  while  index < len(my_list):
    if my_list[index] % 2 == 0:
      my_list.pop(index)
    else:
      break
  return my_list
#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))