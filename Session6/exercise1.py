print('Exercise 6.1')

# the following code prints a calendar
# print the week days
i = 0
week_days = ('m', 't', 'w', 't', 'f', 's', 's')
while i < 7:
  print(week_days[i], end='\t')
  i+=1
print()

# print the days
i = 1
while i <= 31:
  print(f'{i}', end='\t')
  if i % 7 == 0: # lets start another week
    print()
  i += 1 # increment by one, i = i + 1
print()

# as is, the printed callendar always start with the 1st day on Monday. Lets change that

# Assignment

# Part 1
# based on the code above create a function  that prints a calendar of a month that starts in a week day passed as a parameter

# Exemple: 
# print_calendar('w')
# > prints:
# m   t   w   t   f   s   s
#         1   2   3   4   5
# 6   7   8   9   10  11  12
# 13  14  15  16  17  18  19
# 20  21  22  23  24  25  26
# 27  28  29  30  31
#

# tips: 
# - you will need to print empty 'cells' before printing the numbers
# - you can use print(' ', end='\t') por printitng empty cells for days that appears in the calendar before the init of the month.
# - you will need to change the if i % 7 == 0: line.

def print_calendar(week_day):
  """ Prints the calendar of the month that starts on a 'week_day' """
  return


# Part 2
# Create another version of the function that doesn't use while loops but use 'while' loops instead. 


# Challenge
# Evolve your print_calendar function for accepting holidays as a parameters and print some distinction for a day that is a holiday

# Challenge 2. 
# Can you create a version of the function that uses recursive calls instead of 'for' or 'while' loops?  
