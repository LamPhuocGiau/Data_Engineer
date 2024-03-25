def larger_sum(st1, st2):
  sum_st1 = 0
  sum_st2 = 0
  for num_st1 in st1:
    sum_st1 += num_st1
  for num_st2 in st2:
    sum_st2 += num_st2
  if sum_st1 >= sum_st2:
    return st1
  else:
    return st2

print(larger_sum([1, 9, 5], [2, 3, 7]))