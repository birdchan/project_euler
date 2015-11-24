
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

def get_rotations(n):
  rotations = []
  s = str(n)
  for i in range(len(s)):
    rotations.append(s[i:len(s)] + s[0:i])
  return rotations

def all_rotations_are_prime(rotations, primes_bucket):
  for rotation in rotations:
    if not int(rotation) in primes_bucket:
      return False
  return True

def count_circular_primes_below(n):
  prime_bucket = create_a_bucket_with_primes(n)
  count = 0
  for i in range(2, n+1, 1):
    rotations = get_rotations(i)
    if all_rotations_are_prime(rotations, prime_bucket):
      count += 1
  return count

if __name__ == '__main__':
  #print count_circular_primes_below(100)
  #print count_circular_primes_below(1000)
  #print count_circular_primes_below(10000)
  #print count_circular_primes_below(100000)
  print count_circular_primes_below(1000000)

