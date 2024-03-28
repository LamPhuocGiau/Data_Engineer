
def word_length_dictionary(words):
  expected_dictionary = {}
  for word in words:
    num_word = len(word)
    expected_dictionary.update({word:num_word})
  return expected_dictionary


print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}