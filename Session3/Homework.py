print('Homework')
curr_year = 2020

birth_year = input('Which year were you born in?: ')
birth_day = int(input('Which day were you born on?: '))
birth_month = input('Which month were you born in?: ')

is_birth_year_numeric = birth_year.isnumeric()
print(type(is_birth_year_numeric))
print(is_birth_year_numeric)
if not is_birth_year_numeric: 
  print(f'"{birth_year}"is not a year. Try again in numeric form by typing a year please ')
  exit('year is not numeric')
else:
  birth_year = int(birth_year)
  print(f"So you were born in {birth_year}. cool ")


if birth_year > curr_year:
  print(f" Oh so you're from the future then. Definitely not possible. Try again please.")
  exit("future year")

months = ("January" ,"February" ,"March" ,"April" ,"May", "June" ,"July" ,"August" ,"September" ,"October" ,"November" ,"December" )
is_it_correct = birth_month in months
if not is_it_correct:
  print(f"{birth_month} is not in the correct format. Try again please ")
  exit("{birth_month} is not in right format")
index = months.index(birth_month) 
print(index)

print(f'Ok! your birthdate is {birth_year}-{birth_month}-{birth_day}')










