
def every_other_letter(word):
  every_other_letter = ""
  index = 0
  while index < len(word):
    every_other_letter += word[index]
    index += 2
  return every_other_letter

print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 