
import math
import string

def get_chain_length(n):
  if n <= 1:
    return 1
  if n % 2 == 0:
    n = n / 2
  else:
    n = 3*n + 1
  return get_chain_length(n) + 1

def find_longest_chain_under_N(n):
  max_chain_num = -1
  max_chain_length = 0
  for i in xrange(1, n, 1):
    chain_length = get_chain_length(i)
    if chain_length > max_chain_length:
      max_chain_length = chain_length
      max_chain_num = i
  #print max_chain_num
  #print max_chain_length
  return max_chain_num

if __name__ == '__main__':
  #print find_longest_chain_under_N(3)
  print find_longest_chain_under_N(1000000)

