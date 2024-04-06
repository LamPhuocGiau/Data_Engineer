
def sum_values(my_dictionary):
  sum = 0
  for item in my_dictionary:
    sum += my_dictionary[item]
  return sum

print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6