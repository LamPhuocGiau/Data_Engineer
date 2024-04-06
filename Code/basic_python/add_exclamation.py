
def add_exclamation(word):
  
  if len(word) >= 20:
    return word
  else:
    index = len(word)
    while index < 20:
      word += "!"
      index += 1
    return word

print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn