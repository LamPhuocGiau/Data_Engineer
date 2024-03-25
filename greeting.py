def add_greetings(names):
  name_list = []
  for individual in names:
    name_list.append("Hello, " + individual)
  return name_list

print(add_greetings(["Owen", "Max", "Sophie"]))