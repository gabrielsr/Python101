print('exercise 4.1')
from datetime import datetime

today_day = datetime.today().day
today_month = datetime.today().month
today_year = datetime.today().year
print(f'today is {today_day}/{today_month}')


# get the day and check if it is in the correct range
bd_day = input('type the day of your birthday\n')
if not bd_day.isnumeric():
  print('please type a numeric value')
  exit()
else:
  bd_day = int(bd_day)

if bd_day > 31 or bd_day < 1:
  print('the value must be between 1 and 31')

# get the month and check if it is in the correct range
bd_month = input('type the month of your birthday\n')
if not bd_month.isnumeric():
  print('please type a numeric value')
  exit()
else:
  bd_month = int(bd_month)

if bd_month > 12 or bd_month < 1:
  print('the value must be between 1 and 12')

# get the month and check if it is in the correct range
bd_year = input('type the year of your birthday\n')
if not bd_year.isnumeric():
  print('please type a numeric value')
  exit()
else:
  bd_year = int(bd_year)

if bd_year > today_year or bd_year < today_year-120:
  print(f'the value must be between {today_year} and {today_year-120}')
  exit()

print(f'your birthday is {bd_day}/{bd_month}/')

if birth_day == today_day and birth_month == today_month:
  print('Happy birthday!')
else:
  # TODO print how many days for the user birthday (assignment 4.2)
  pass


# Assignment 4.1

# Create a function named:
# > input_number_in_range
# with parameters
# - message : shown to the user while asking for input
# - range_star : minimum accepted value
# - range_end  : maximun accepted value
# that function must reads data from the user, 
#  - check if is a number,  if not it should print an error message and exit
#  - check if it is in the range, if not it should print an error message and exit

# Calling our input_number_in_range function after it is ready:
# birth_day = input_number_in_range("insert the day that you were born in", 1, 31)
# birth_month = input_number_in_range("insert the month that you were born in", 1, 12)



