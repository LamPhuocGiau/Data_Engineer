
def check_for_name(sentence, name):
  uniform_sentence = sentence.lower()
  uniform_name = name.lower()
  if uniform_name in uniform_sentence:
    return True
  else:
    return False


print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False