import os
import time

path = './problems/'

def print_one_solution(path, dirname):
  start_time = time.time()
  print "// --------------------------------"
  cmd = "python " + path + dirname + '/' + 'run.py'
  print cmd
  os.system(cmd)
  end_time = time.time()
  time_delta = "%.3f" % (end_time-start_time)
  print "Time spent: " + str(time_delta) + " seconds"

def print_all_solutions(path):
  for dirname in os.listdir(path):
    print_one_solution(path, dirname)

if __name__ == '__main__':
  print_all_solutions(path)

