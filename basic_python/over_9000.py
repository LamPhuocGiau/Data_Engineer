def over_nine_thousand(list):
  if len(list) > 0:
    sum = 0
    for num_list in list:
      if sum <= 9000:
        sum += num_list
      else:
        break
    return sum
  else:
    return 0
  
print(over_nine_thousand([8000, 900, 120, 5000]))