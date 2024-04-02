def exponents(bases, powers):
  index_bases = 0
  new_list = []
  while index_bases < len(bases):
    index_powers = 0
    while index_powers < len(powers):
      num_power = bases[index_bases] ** powers[index_powers]
      new_list.append(num_power)
      index_powers += 1
    index_bases += 1
  return new_list

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))