
import math

def find_proper_divisors(n):
  if n < 1:
    return []
  divisors = []
  up_to = int(math.sqrt(n)) + 1
  for i in xrange(1, up_to, 1):
    if n % i == 0:
      divisors.append(i)
      if i != n/i and i != 1:
        divisors.append(n/i)
  return divisors

def find_sum_of_all_amicable_numbers_below(num):
  if num <= 0:
    return 0
  amicable_numbers = set()
  lookup_sum_of_divisors = {} # map_sum_n[220] = 284
  for i in range(num):
    # get d(a)=b, sum of proper divisors of a
    a = i+1
    if not lookup_sum_of_divisors.has_key(a):
      proper_divisors = find_proper_divisors(a)
      lookup_sum_of_divisors[a] = sum(proper_divisors)
    b = lookup_sum_of_divisors[a]
    # get d(b)
    if not lookup_sum_of_divisors.has_key(b):
      proper_divisors = find_proper_divisors(b)
      lookup_sum_of_divisors[b] = sum(proper_divisors)
    # d(b) == a and a != b, save these two numbers
    if lookup_sum_of_divisors[b] == a and a != b:
      amicable_numbers.add(a)
      amicable_numbers.add(b)

  return sum(amicable_numbers)

###################################################
if __name__ == '__main__':
  #print find_sum_of_all_amicable_numbers_below(300)  # 220 and 284
  print find_sum_of_all_amicable_numbers_below(10000)

