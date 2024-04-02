def count_multi_char_x(word, x):
  sub_word = word.split(x)
 
  count = len(sub_word) - 1
  return count

print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1