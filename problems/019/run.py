
import math

class dateBot:

  def __init__(self, y, m, d, weekday):
    self.year = y
    self.month = m  # Jan=1, Feb=2, etc
    self.day = d
    self.weekday = weekday # Sun=0, Mon=1, etc

  def getNumOfDaysInMonth(self):
    m = self.month
    y = self.year
    leap_year_feb_days = 29
    non_leap_year_feb_days = 28
    if m == 2: # Feb
      is_leap_year = (y % 4 == 0)
      is_on_a_century = (y % 100 == 0)
      is_on_a_century_div_by_400 = (y % 400 == 0)
      if is_on_a_century_div_by_400:
        return leap_year_feb_days
      if is_on_a_century:
        return non_leap_year_feb_days
      if is_leap_year:
        return leap_year_feb_days
      return non_leap_year_feb_days
    if m in [4, 6, 9, 11]:
      return 30
    else:
      return 31

  def increment_day(self):
    self.day += 1
    self.weekday += 1
    days_in_current_month = self.getNumOfDaysInMonth()
    if self.day > days_in_current_month:
      self.increment_month()
      self.day = 1
    if self.weekday > 6: # Sat=6
      self.weekday = 0

  def increment_month(self):
    self.month += 1
    if self.month > 12:
      self.increment_year()
      self.month = 1

  def increment_year(self):
    self.year += 1

  def getFullDate(self):
    return "%4d%02d%02d" % (self.year, self.month, self.day)

  def getDay(self):
    return self.day

  def getWeekday(self):
    return self.weekday

###################################################
if __name__ == '__main__':
  date_bot = dateBot(1900, 1, 1, 1) # 1 Jan 1900 was a Monday
  count = 0
  curr_date_str = ''
  start_count_str = '19010101'
  start_count_flag = False
  stop_count_str = '20001231'
  while True:
    date_bot.increment_day()
    full_date_str = date_bot.getFullDate()
    if full_date_str == start_count_str:
      start_count_flag = True
    if not start_count_flag:
      continue
    if date_bot.getWeekday() == 0 and date_bot.getDay() == 1:
      count += 1
    if full_date_str == stop_count_str:
      break
  print count


