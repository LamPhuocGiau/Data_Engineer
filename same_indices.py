def same_values(list1, list2):
  index = 0
  index_list = []
  while index < len(list1):
    if list1[index] == list2[index]:
      index_list.append(index)
    index += 1
  return index_list


print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))