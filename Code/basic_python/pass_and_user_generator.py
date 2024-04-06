def username_generator(first_name, last_name):
  if len(first_name) < 3:
    username = first_name + last_name[:4]
  elif len(last_name) < 4:
    username = first_name[:3] + last_name
  elif len(first_name) < 3 and len(last_name) < 4:
    username = first_name + last_name
  else:
    username = first_name[:3] + last_name[:4]
  return username

print("User name: " + username_generator("Abe", "Simpson"))

def password_generator(username):
  password = ""
  for index_username in range(len(username)):
    password = password + username[index_username - 1]
  return password

print("Password: " + password_generator(username_generator("Abe", "Simpson")))

