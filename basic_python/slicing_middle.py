def remove_middle(my_list, start, end):
 return my_list[:start] + my_list[end + 1:]


print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))