def count_char_x (word, x):
  count = 0
  for char in word:
    if x == char:
      count += 1
  return count
  
print(count_char_x("mississippi", "s"))