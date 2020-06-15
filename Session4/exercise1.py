print('exercise 4.1')
from datetime import datetime

today_day = datetime.today().day
today_month = datetime.today().month
print(f'today is {today_day}/{today_month}')

def input_number_in_range (message, range_start, range_end):
  """ Get a number from user and check if is in the expected range """
  input_str = input(message)
  if not input_str.isnumeric():
    print('please type a numeric value')
    exit()
  else:
    input_number = int(input_str)

  if input_number > range_end or input_number < range_start:
    print(f'the value must be between {input_number} and {range_end}')
  return input_number

# # get the month and check if it is in the correct range
# bd_month = input('type the month of your birthday\n')
# if not bd_month.isnumeric():
#   print('please type a numeric value')
#   exit()
# else:
#   bd_month = int(bd_month)

# if bd_month > 12 or bd_month < 1:
#   print('the value must be between 1 and 12')

birth_day = input_number_in_range("insert the day that you were born in", 1, 31)
birth_month = input_number_in_range("insert the month that you were born in", 1, 12)

print(f'your birthday is {birth_day}/{birth_month}')

if birth_day == today_day and birth_month == today_month:
  print('Happy birthday!')
else:
  # TODO print how many days for the user birthday (assignment 4.2)
  pass





# Assignment 4.1

# Create a function named:
# > inputNumberInRange
# with parameters
# - message : shown to the user while asking for input
# - range_star : minimum accepted value
# - range_end  : maximun accepted value
# that function must reads data from the user, 
#  - check if is a number,  if not it should print an error message and exit
#  - check if it is in the range, if not it should print an error message and exit




