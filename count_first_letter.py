
def count_first_letter (names):
  letters = {}
  for last_name in names.keys():
    if last_name[0] not in letters:
      letters.update({last_name[0]: len(names[last_name])})
    else:
      letters[last_name[0]] += len(names[last_name])
  return letters

print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}