
import math
import string

def trace(m, n, i, j):
  if i>=m and j>=n:
    return 1
  # paths
  num_of_paths = 0
  if i<m: # go right
    num_of_paths += trace(m, n, i+1, j)
  if j<n: # go down
    num_of_paths += trace(m, n, i, j+1)
  return num_of_paths

def find_num_of_routes(m, n):
  return trace(m, n, 0, 0)

if __name__ == '__main__':
  print find_num_of_routes(2, 2)
  print find_num_of_routes(3, 3)
  print find_num_of_routes(10, 10)
  print find_num_of_routes(15, 15)
  #print find_num_of_routes(20, 20)

