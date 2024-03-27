# Write your max_key function here:
def max_key(my_dictionary):
  max_value = 0
  expected_key = None
  for key in my_dictionary:
    if max_value <= my_dictionary[key]:
      max_value = my_dictionary[key]
      expected_key = str(key)
  return expected_key

# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"
print(max_key({1:2, 2:3}))