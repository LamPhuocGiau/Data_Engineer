def every_three_nums(start):
  if start <= 100:
    return list(range(start, 101, 3))
  else:
    return list("")
print(every_three_nums(91))
print(every_three_nums(101))