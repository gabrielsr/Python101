print('exercise 2.1')

curr_year = 2020

# get birth date
birth_year = input('which year were you born?: ')
months = input('what month were you born in?: ')
#creating strings using fstrings
out = f'cool. You were born in {months} {birth_year} '
print(out) #reaching the user

out = birth_year + '. ok. '
print(out)

# The next line give us an error!




# beacuse birth_year is a string
print(type(birth_year))

# we can convert
birth_year = int(birth_year)
years_ago = curr_year - birth_year
out = f'So it was only {years_ago} years ago?! Jez'
print(out)