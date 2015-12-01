
import math

triangle_1 = """
3
"""

triangle_2 = """
3
7 4
"""

triangle_small = """
3
7 4
2 4 6
8 5 9 3
"""

triangle_big = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

class treeNode:
  def __init__(self, val):
    val = int(val)
    self.value = val
    self.max_value = val # possible max
    self.next_num = -1 # max if take this path down
  def __repr__(self):
    return str(self.value)

def parse_triangle_text(triangle_text):
  lines = triangle_text.split('\n')
  rows = []
  for line in lines:
    line = line.strip()
    if line == '':
      continue
    items = line.split(' ')
    row = []
    for item in items:
      row.append(treeNode(item))
    rows.append(row)
  return rows

def find_max_total(triangle):
  rows = parse_triangle_text(triangle)
  num_of_rows = len(rows)
  if num_of_rows == 0:
    return -1
  elif num_of_rows == 1:
    return rows[0][0].max_value
  else:
    for i in range(len(rows)-1):
      row_index = len(rows) - i - 2  # current triangle row index
      for col_index in range(row_index+1):
        # find the max value and the next value for a node (triangle top)
        # this triangle has only 3 nodes
        top   = rows[row_index][col_index]
        left  = rows[row_index+1][col_index]
        right = rows[row_index+1][col_index+1]
        if left.max_value >= right.max_value:
          top.max_value = top.value + left.max_value
          top.next_num = left.value
        else:
          top.max_value = top.value + right.max_value
          top.next_num = right.value
    return rows[0][0].max_value

if __name__ == '__main__':
  #print find_max_total(triangle_1)
  #print find_max_total(triangle_2)
  #print find_max_total(triangle_small)
  print find_max_total(triangle_big)

