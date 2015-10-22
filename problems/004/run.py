
import math

def is_palindromic(num):
  s = str(num)
  mid_index = int(math.floor(len(s)/2))  # middle is fine
  for i in range(mid_index):
    if s[i] != s[-(i+1)]:
      return False
  return True

def get_largest_palindromic():
  largest = -1
  for i in range(100, 1000, 1):
    for j in range(100, 1000, 1):
      product = i * j
      if product < largest: # small num, forget it
        continue
      if is_palindromic(product):
        largest = product
  return largest

if __name__ == '__main__':
  print get_largest_palindromic()

