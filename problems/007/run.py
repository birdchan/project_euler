
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

def get_nth_prime(n):
  curr_sample_size = 1
  primes = []
  while len(primes) < n:
    curr_sample_size *= 100  # make our sample size bigger
    my_dict = create_a_bucket_with_primes(curr_sample_size)
    primes = my_dict.keys()
  # we have enough primes, so get the nth prime
  primes.sort()
  return primes[n-1]

if __name__ == '__main__':
  #print get_nth_prime(6)
  print get_nth_prime(10001)

