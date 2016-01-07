import argparse
import os
import time

path = './problems/'

def print_one_solution(path, dirname):
  start_time = time.time()
  print "// --------------------------------"
  os.chdir(path + dirname)
  print "python " + path + dirname + '/' + 'run.py'
  os.system('python run.py')
  os.chdir('../../')
  end_time = time.time()
  time_delta = "%.3f" % (end_time-start_time)
  print "Time spent: " + str(time_delta) + " seconds"
  print

def print_solutions(path, level):
  if level == None:
    for dirname in os.listdir(path):
      print_one_solution(path, dirname)
  else:
    dirname = "%03d" % (level)
    print_one_solution(path, dirname)
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-l', '--level', dest="level", type=int, help='level number', required=False)
  args = parser.parse_args()
  print_solutions(path, args.level)

