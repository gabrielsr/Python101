print('Homework')
curr_year = 2020

birth_year = int(input('Which year were you born in?: '))
birth_day = int(input('Which day were you born on?: '))
birth_month = int(input('Which month were you born in?: '))

is_birth_year_numeric = birth_year.isnumeric()
print(type(is_birth_year_numeric))
print(is_birth_year_numeric)
if not is_birth_year_numeric: 
  print(f'"{birth_year}"is not a year. Try again in numeric form by typing a year please ')
  exit('year is not numeric')
  else:
    print(f' "So you were born in {birth_year}. cool ")


if birth_year > curr_year:
  print(f" Oh so you're from the future then. Definitely not possible. Try again please.")
  exit("future year")

months = ("January" ,"February" ,"March" ,"April" ,"May", "June" ,"July" ,"August" ,"September" ,"October" ,"November" ,"December" )
index = months.index("February")
print(index)
x = "March" in months

if not bd_month.isnumeric():
  print('please type a numeric value')
  exit()
else:
  bd_month = int(bd_month)








