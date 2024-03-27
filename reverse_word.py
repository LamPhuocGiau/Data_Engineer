
def reverse_string(word):
  reverse_word = ""
  index = -1
  while index >= -len(word):
    reverse_word += word[index]
    index = index - 1
  return reverse_word 

print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print