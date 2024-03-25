import random
name = "Richard"
question = "Is today weekend?"
answer = ""
random_number = random.randint(1,12)
print("Random number:", random_number)
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidely so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My source say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Yes, it is"
elif random_number == 11:
  answer = "No, it isn't"
elif random_number == 12:
  answer = "I don't sure"
else:
  answer = "Error"
if len(question) == 0:
  print("The user hasn't question")
else:
  if name == "":
    print("Question: " + question)
    print("Magic 8-Ball's answer:", answer)
  else:
    print(name + " ask: " + question)
    print("Magic 8-Ball's answer:", answer)
