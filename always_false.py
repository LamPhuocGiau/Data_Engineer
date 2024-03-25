def always_false(num):
  if num >= 0 or num < 0:
    return False
  else:
    return True

print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False