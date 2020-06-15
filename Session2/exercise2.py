print('exercise 2.2')
curr_day = 11
curr_month = 6
curr_year = 2020
name = input('Hi! What is your name, stranger? \n ') 
# this is a method
print(f"I'm honoured to make your acquaintance, Miss {name}")
print('\n\n\n')

# get birth date
birth_year = input(f'Which year were you born in, Miss {name}?: ')
birth_month = input(f'Which month were you born in, Miss {name}?: ')
birth_day = input(f'Which day were you born in, Miss {name}?: ')
age = curr_year-birth_year
print(f"So you're {age}. Wow." ) 

# what if we type something that is not a number?

# check if it is numeric
is_birth_year_numeric = birth_year.isnumeric()
print(type(is_birth_year_numeric))
print(is_birth_year_numeric)
if not is_birth_year_numeric: 
    print(f'"{birth_year}" is not a year, Miss {name}. This is wrong. Try again by typing a year ok? ')
    exit('year is not a number')

birth_year = int(birth_year)z
birth_day = int(birth_day)

# validating year
if birth_year > curr_year:
  print(f"whoa, {name.upper()}. Did you come from the future then? I don't think so.")
  exit('User from the future')
else if birth_year < curr_year:
  print(f"cool, you were born in birth_year." )

# The next line give us an error!
years_ago = curr_year - birth_year
out = f'So it was only {years_ago} years ago?! Jeez'
print(out)
print('\n\n\n')

 
#out = f'ok. You were born in {birth_year}-{birth_month- {birth_day}'

print(out)
#year - birth_year
#out = f'It was {} years ago'
