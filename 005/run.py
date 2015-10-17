
import math

def get_factors(n):
  if n < 2:
    return {}
  factors = {}
  while n > 1:
    for i in range(2, n+1, 1): # 2 to n inclusive
      if n % i == 0:
        if not factors.has_key(i):
          factors[i] = 0
        # increase count
        factors[i] += 1
        # update n
        n = n / i
        # start from 2 and up, break the for loop
        break
  return factors

def get_smallest_multiple(n):
  common_factors = {}
  for i in range(1, n+1, 1): # 1 to n inclusive
    factors = get_factors(i)
    for k, v in factors.items():
      if not common_factors.has_key(k):
        common_factors[k] = v
      else:
        if v > common_factors[k]:
          common_factors[k] = v
  # calculate the product
  product = 1
  for k, v in common_factors.items():
    product = product * math.pow(k, v)
  
  return int(product)

if __name__ == '__main__':
  #for i in range(1, 11, 1):
  #  print str(i) + ' : ' + str(get_factors(i))
  #print get_smallest_multiple(10)
  print get_smallest_multiple(20)

