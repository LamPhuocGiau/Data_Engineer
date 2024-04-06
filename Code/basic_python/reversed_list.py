def reversed_list(list1, list2):
  index = 0
  while index < len(list1):
    if list1[index] != list2[-(index + 1)]:
      return False
    index += 1
  return True
    

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))