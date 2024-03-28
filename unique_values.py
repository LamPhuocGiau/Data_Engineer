
def unique_values(my_dictionary):
  list_unique_value = []
  for value in my_dictionary.values():
    if value not in list_unique_value:
      list_unique_value.append(value)
  return len(list_unique_value)

print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1