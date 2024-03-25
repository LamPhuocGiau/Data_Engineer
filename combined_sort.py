def combine_sort(my_list1, my_list2):
  combined_list = my_list1 + my_list2
  combined_list.sort()
  return combined_list

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))