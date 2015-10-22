
import math

def find_abc():
  for a in range(1, 1000, 1):
    for b in range(a, 1000, 1):
      c = 1000 - a - b
      lhs = a*a + b*b
      rhs = c*c
      if lhs == rhs:
        return a*b*c
  return -1

if __name__ == '__main__':
  print find_abc()

