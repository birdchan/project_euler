
import math

def get_sum_of_the_squares(n):
  sum = 0
  for i in range(1, n+1, 1):
    sum += math.pow(i, 2)
  return int(sum)

def get_square_of_the_sum(n):
  sum = 0
  for i in range(1, n+1, 1):
    sum += i
  return int(math.pow(sum, 2))

def get_diff(n):
  return get_square_of_the_sum(n) - get_sum_of_the_squares(n)

if __name__ == '__main__':
  #print get_diff(10)
  print get_diff(100)

