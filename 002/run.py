
def get_next_fib_num(a, b):
  return a + b

def get_sum_of_even_fib_nums(upper):
  a = 1
  b = 2
  sum = b  # since 2 is even
  next_fib = get_next_fib_num(a, b)
  while next_fib < upper:
    if next_fib % 2 == 0:
      sum += next_fib
    a = b
    b = next_fib
    next_fib = get_next_fib_num(a, b)
  return sum

if __name__ == '__main__':
  #print get_sum_of_even_fib_nums(100)
  print get_sum_of_even_fib_nums(4000000)

