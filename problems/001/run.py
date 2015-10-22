
def get_sum_of_multiples(upper):
  sum = 0
  for i in range(upper):
    if i < 1: # not a natural number
      continue
    if i % 3 == 0 or i % 5 == 0:
      sum += i
  return sum

if __name__ == '__main__':
  #print get_sum_of_multiples(10)
  print get_sum_of_multiples(1000)

