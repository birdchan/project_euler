
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

def sum_ints_cannot_be_written_as_sum_of_two_abundant_nums():
  # find all abundant ints <= 28123
  abundant_nums = set()
  for i in range(28123):
    n = i+1
    divisors = find_proper_divisors(n)
    if sum(divisors) > n:
      abundant_nums.add(n)
  # numbers written as the sum of two abundant numbers
  sum_of_two_abundant_nums = set()
  for n1 in abundant_nums:
    for n2 in abundant_nums:
      if n1+n2 <= 28123:
        sum_of_two_abundant_nums.add(n1+n2)
  # find the diff
  #range(28123) - sum_of_two_abundant_nums
  positive_ints = range(1, 28123+1)
  my_list = [item for item in positive_ints if item not in sum_of_two_abundant_nums]
  return sum(my_list)

###################################################
if __name__ == '__main__':
  print sum_ints_cannot_be_written_as_sum_of_two_abundant_nums()

