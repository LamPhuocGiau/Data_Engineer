def max_num(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  else:
    return "It's a tie!"

print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(5, 2, 5))
# should print "It's a tie!"

# use another loop + function
def max_num(nums):
  index = 1
  max_num = nums[0]
  while index < len(nums):
    
    if max_num <= nums[index]:
      max_num = nums[index]
    index +=1
  return max_num

print(max_num([50, -10, 0, 75, 20]))