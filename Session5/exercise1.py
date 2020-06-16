print('exercise 5.1')

# import a function that we defined in other file
from .user_input import input_number_in_range_with_retry

# take a look at the function input_number_in_range_with_retry in user_input.py

# how does it differs from the previous versions?

birth_day = input_number_in_range_with_retry("insert the day that you were born in", 1, 31)

birth_month = input_number_in_range_with_retry("insert the month that you were born in", 1, 12)

print(f'your birthday is {birth_day}/{birth_month}')
