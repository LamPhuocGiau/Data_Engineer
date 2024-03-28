# Write your frequency_dictionary function here:
def frequency_dictionary(words):
  expected_dict = {}
  value = 1
  for word in words: 
    if word in expected_dict.keys():
      value += 1
      expected_dict.update({word: value})
    else:
      value = 1
      expected_dict.update({word: 1})
  return expected_dict
# Uncomment these function calls to test your  function:
# print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
# print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}
print(frequency_dictionary([0,0,0,1,4,5,5,5]))