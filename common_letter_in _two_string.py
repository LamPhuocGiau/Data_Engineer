# method 1

def common_letters(string_one, string_two):
  temp_string = []
  for letter_string_one in string_one:
    
    if letter_string_one in string_two and letter_string_one not in temp_string:
      temp_string.append(letter_string_one)
  return temp_string

print(common_letters("banana", "cream"))

# method2

# def common_letters(string_one, string_two):
#   temp1 = set(string_one)
#   temp2 = list(temp1)
#   temp3 = list(string_two)
#   common_string = []
#   index = 0
#   while temp2[index] in temp3 and index < len(temp2):
#     common_string.append(temp2[index])
#     index += 1
#   return common_string
# print(common_letters("banana", "cream"))
    


