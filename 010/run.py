
import math

def create_a_bucket_with_primes(n):
  bucket = {}
  for i in range(2, n+1, 1):
    bucket[i] = 1
  up_to = int(math.ceil(math.sqrt(n)))
  for multiplier in range(2, up_to, 1):
    if not bucket.has_key(multiplier):  # multiples of 2 took care of multiples of 4
      continue
    # cross out the multiples of this multiplier
    curr_multiple = multiplier
    while curr_multiple < n:
      curr_multiple += multiplier
      if bucket.has_key(curr_multiple):
        del bucket[curr_multiple]
  return bucket

def find_sum_of_primes_below(n):
  my_dict = create_a_bucket_with_primes(n)
  primes = my_dict.keys()
  primes.sort()
  return sum(primes)

if __name__ == '__main__':
  #print find_sum_of_primes_below(10)
  print find_sum_of_primes_below(2000000)

