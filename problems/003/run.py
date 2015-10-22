
import math

def is_prime(num):
  if num < 2:
    return False
  for i in range(num):
    if i < 2:
      continue
    if num % i == 0:
      return False
  return True

def get_largest_prime_factor(num):
  upper = int(math.ceil(math.sqrt(num)))
  prime_factor = -1
  # using ceil, coz range will bump it down by 1
  for i in range(upper):
    if i < 2: # not a prime for sure
      continue
    if num % i != 0:  # not a factor
      continue
    if not is_prime(i): # a bit expensive check
      continue
    prime_factor = i
  return prime_factor

if __name__ == '__main__':
  #print get_largest_prime_factor(13195)
  print get_largest_prime_factor(600851475143)

