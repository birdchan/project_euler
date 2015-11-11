
import math
import string

# m is horizontal
# n is vertical
# 
# m, i ->
# 
# ? ? ? ? 1
# ? ? ? 4 1
# ? ? 6 3 1
# ? 4 3 2 1
# 1 1 1 1 1
# 

def print_matrix(matrix):
  for row in matrix:
    print row
  print
  return

def build_matrix(m, n):
  # init
  matrix = []
  for j in range(n+1):
    row = []
    for i in range(m+1):
      row.append(0)
    matrix.append(row)
  # go from bottom right corner, to top left
  # square by square
  max_matrix_side = max(m, n)
  for cnt in range(max_matrix_side+1):
    # bottom corner case, no work needed
    if cnt == 0:
      matrix[m][n] = 1
      continue
    # normal case
    dest_i = m - cnt
    dest_j = n - cnt
    # detect this coz the matrix may not be a square
    perform_col_task = True
    perform_row_task = True
    if dest_i < 0:
      dest_i = 0
      perform_col_task = False
    if dest_j < 0:
      dest_j = 0
      perform_row_task = False
    # work our way in for this square
    if perform_row_task:
      for i in range(cnt):
        my_i = m - i
        if my_i == m:
          matrix[my_i][dest_j] = 1
        else:
          # sum of the right one and the bottom one
          matrix[my_i][dest_j] = matrix[my_i+1][dest_j] + matrix[my_i][dest_j+1]
    if perform_col_task:
      for j in range(cnt):
        my_j = n - j
        if my_j == n:
          matrix[dest_i][my_j] = 1
        else:
          # sum of the right one and the bottom one
          matrix[dest_i][my_j] = matrix[dest_i+1][my_j] + matrix[dest_i][my_j+1]
    # top left corner for this square
    matrix[dest_i][dest_j] = matrix[dest_i+1][dest_j] + matrix[dest_i][dest_j+1]
  # return
  return matrix

def find_num_of_routes(m, n):
  matrix = build_matrix(m, n)
  return matrix[0][0]

if __name__ == '__main__':
  #print find_num_of_routes(2, 2)
  #print find_num_of_routes(3, 3)
  #print find_num_of_routes(10, 10)
  #print find_num_of_routes(15, 15)
  print find_num_of_routes(20, 20)

