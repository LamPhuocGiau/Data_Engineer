
def make_spoonerism(word1, word2):
  
  The_first_char_of_word1 = word1[0]
  The_second_char_of_word2 = word2[0]
  remain_of_word1 = word1[1:]
  remain_of_word2 = word2[1:]
  spoonerism_word = The_second_char_of_word2 + remain_of_word1 + " " + The_first_char_of_word1 + remain_of_word2
  return spoonerism_word

print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a