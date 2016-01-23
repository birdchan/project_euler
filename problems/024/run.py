
import math

def kth_permutation(alphabets, k):
  data = alphabets
  order = n = len(alphabets)

  # step 1 - Find factoradic of k
  factoradic = [0] * n
  for j in range(1, n+1):
    factoradic[order-j] = k % j
    k /= j

  # step 2 - Convert factoradic to permuatation
  temp = [0] * n
  for i in range(n):
    factoradic[i] += 1
    temp[i] = factoradic[i]

  data[n-1] = 1  # right-most element is set to 1
  
  i = n - 2
  while i >= 0:
    data[i] = temp[i]
    j = i + 1
    while j < n:
      if data[j] >= data[i]:
        data[j] += 1
      # increment
      j += 1
    # decrement
    i -= 1

  for i in range(n):
    data[i] -= 1
    
  return data

###################################################
if __name__ == '__main__':
  #alphabets = ['0', '1', '2', '3']
  #print kth_permutation(alphabets, 8)
  alphabets = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  #print kth_permutation(alphabets, 0)
  #print kth_permutation(alphabets, 1)
  #print kth_permutation(alphabets, 2)
  #print kth_permutation(alphabets, 3)
  #print kth_permutation(alphabets, 4)
  str_list = map(str, kth_permutation(alphabets, 999999))
  print ''.join(str_list)

