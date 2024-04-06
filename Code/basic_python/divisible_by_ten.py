# use if loop

def divisible_by_ten(num):
  if num % 10 == 0:
    return True
  else:
    return False

# should print True
print(divisible_by_ten(20))
# should print False
print(divisible_by_ten(25))

# Use for loop

def divisible_by_ten(nums):
  count = 0
  for temp in nums:
    if (temp % 10 == 0):
      count += 1
  return count

print(divisible_by_ten([20, 25, 30, 35, 40]))