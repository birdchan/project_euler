
import math
import string

def get_divisors(n):
  if n < 1:
    return []
  divisors = []
  up_to = int(math.sqrt(n)) + 1
  for i in xrange(1, up_to, 1):
    if n % i == 0:
      divisors.append(i)
      if i != n/i:
        divisors.append(n/i)
  return divisors

def find_first_triangle_num_having_over_n_divisors(n):
  triangle_number = 0
  count = 1
  while True:
    triangle_number += count
    divisors = get_divisors(triangle_number)
    #print divisors
    if len(divisors) > n:
      return triangle_number
    # increment
    count += 1

if __name__ == '__main__':
  #print find_first_triangle_num_having_over_n_divisors(5)
  print find_first_triangle_num_having_over_n_divisors(500)

