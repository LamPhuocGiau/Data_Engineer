
def x_length_words(sentence, x):
  list_of_sentence = sentence.split()
  for word in list_of_sentence:
    if len(word) < x:
      return False
    else:
      return True


print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True