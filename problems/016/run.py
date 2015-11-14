
import math

def get_sum_of_digits(num):
  sum = 0
  string = str(num)
  for i in range(len(string)):
    sum += int(string[i])
  return sum

def get_power_digit_sum(n):
  num = int(math.pow(2, n))
  sum = get_sum_of_digits(num)
  return sum

if __name__ == '__main__':
  #print get_power_digit_sum(15)
  print get_power_digit_sum(1000)

