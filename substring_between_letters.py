
def substring_between_letters(word, start, end):
  start_index = word.find(start)
  end_index = word.find(end)
  substring = ""
  x = start_index + 1
  if start_index == -1 or end_index == -1:
    return word
  else:
    while x < end_index:
      substring += word[x]
      x += 1
    return substring
  

print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"