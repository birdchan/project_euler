
import math

def run_fib_up_to_digits(n):
  digit_cnt = 1
  i = 3
  f_n_1 = 1.0
  f_n_2 = 1.0
  while digit_cnt < n:
    f_n = f_n_1 + f_n_2
    # use floating decimals to store the "powers"
    if f_n > 10:
      digit_cnt += 1
      f_n /= 10.0
      f_n_1 /= 10.0
      f_n_2 /= 10.0
    # store values for the next calculation
    f_n_2 = f_n_1
    f_n_1 = f_n
    # print temp result
    #print i, f_n, digit_cnt
    # quit if reach goal
    if digit_cnt >= n:
      return i
    # increment counter
    i += 1

###################################################
if __name__ == '__main__':
  #print run_fib_up_to_digits(10)
  print run_fib_up_to_digits(1000)

