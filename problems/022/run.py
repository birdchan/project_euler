
import csv

def get_name_score(name):
  score = 0
  for ch in name:
    score += ord(ch.lower()) - ord('a') + 1
  return score

def find_total_name_scores_from_file(filename):
  # read/parse from file
  names = []
  with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
      names = row  # just one row in this file
  names.sort()
  # calc/add name scores
  total_score = 0
  for i, name in enumerate(names):
    position = i+1
    name_score = get_name_score(name)
    total_score += position * name_score

  return total_score

###################################################
if __name__ == '__main__':
  filename = "p022_names.txt"
  print find_total_name_scores_from_file(filename)

