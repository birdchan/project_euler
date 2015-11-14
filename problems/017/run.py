
import math

digit_map = [
  {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
  },
  {
    1: 'ten',
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
  },
]

teens_map = {
  11: 'eleven',
  12: 'twelve',
  13: 'thirteen',
  14: 'fourteen',
  15: 'fifteen',
  16: 'sixteen',
  17: 'seventeen',
  18: 'eighteen',
  19: 'nineteen',
}

def add_more_digit_sub_maps(digit_map):
  ones_map = digit_map[0]
  hundreds_map = {}
  for i in range(9):
    hundreds_map[i+1] = [ones_map[i+1], 'hundred']
  thousands_map = {}
  for i in range(9):
    thousands_map[i+1] = [ones_map[i+1], 'thousand']
  digit_map.append(hundreds_map)
  digit_map.append(thousands_map)
  return digit_map

def get_num_string_len(n):
  n_str = str(int(n))
  return len(n_str)

def chop_first_digit_off(n):
  n_str = str(int(n))
  if len(n_str) > 1:
    return int(n_str[1:])
  else:
    return 0

def get_english_words(n):
  global digit_map
  global teens_map 
  words = []
  left_nonzero_digit_place = get_num_string_len(n)
  need_and = False
  if n > 100:
    need_and = True
  for digit_place in range(left_nonzero_digit_place, 0, -1):
    n_str = str(n).zfill(digit_place)
    my_digit = int(n_str[0])
    if get_num_string_len(n) == 2 and n > 10 and n <= 19:  # teens...
      if need_and:
        words.append('and')
        need_and = False   # we already consumed this
      words.append(teens_map[n])
      n = chop_first_digit_off(n)
      n = chop_first_digit_off(n) # one more time
      continue
    if my_digit != 0:
      if need_and and get_num_string_len(n) <= 2:
        words.append('and')
        need_and = False   # we already consumed this
      my_words = digit_map[digit_place-1][my_digit]  # lookup
      if isinstance(my_words, (list, tuple)):  # add to words
        words += my_words
      else:
        words.append(my_words)
      n = chop_first_digit_off(n)

  # our complete word list
  return words

def list_nums_in_words(start, end):
  for i in range(start, end+1):
    print get_english_words(i)

def count_letters(words):
  sum = 0
  for w in words:
    sum += len(w)
  return sum

def number_letter_count(n):
  words = get_english_words(n)
  num = count_letters(words)
  return num

if __name__ == '__main__':
  digit_map = add_more_digit_sub_maps(digit_map)
  #list_nums_in_words(1, 1000)
  #print number_letter_count(342)
  #print number_letter_count(115)

  sum = 0
  for i in range(1000):
    sum += number_letter_count(i+1)
  print sum

