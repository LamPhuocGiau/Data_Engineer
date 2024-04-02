letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters (word):
  count = 0
  for letter in letters:
    if letter in word:
      count += 1
  return count
  
print(unique_english_letters("mississippi"))

print(unique_english_letters("Apple"))
