def append_sum(my_list):
  my_list.append(sum(my_list[-2:]))
  my_list.append(sum(my_list[-2:]))
  my_list.append(sum(my_list[-2:]))
  return my_list

print(append_sum([1, 1, 2]))