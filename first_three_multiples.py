def first_three_multiples(num):
  print("multiple of 1st number: ", num)
  print("multiple of 2st number: ", num * 2)
  print("multiple of 3st number: ", num * 3)
  return num * 3


first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0