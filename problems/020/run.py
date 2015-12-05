
import math

def factor_out_x(n, x):
  count = 0
  while n % x == 0:
    n = n / x
    count += 1
  return [n, count]

def find_sum_of_digits(num):
  if num < 2:
    return 1
  numbers_to_multiply = []
  total_count_2 = 0
  total_count_5 = 0
  for i in range(1, num):
    n = i + 1
    [n, count_2] = factor_out_x(n, 2)
    [n, count_5] = factor_out_x(n, 5)
    total_count_2 += count_2
    total_count_5 += count_5
    if n > 1:
      numbers_to_multiply.append(n)
  if total_count_2 > total_count_5:
    numbers_to_multiply.append(int(math.pow(2, total_count_2-total_count_5)))
  elif total_count_5 > total_count_2:
    numbers_to_multiply.append(int(math.pow(5, total_count_5-total_count_2)))

  # straight calculation
  product = reduce(lambda a,b: a*b, numbers_to_multiply)
  digits = map(lambda x: int(x), str(product))  # tokenize
  return sum(digits)

###################################################
if __name__ == '__main__':
  #print find_sum_of_digits(10)
  print find_sum_of_digits(100)

