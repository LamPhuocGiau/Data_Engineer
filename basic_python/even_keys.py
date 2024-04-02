
def sum_even_keys(my_dictionary):
  sum = 0
  for key in my_dictionary:
    if key % 2 == 0:
      sum += my_dictionary[key]
  return sum

print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6