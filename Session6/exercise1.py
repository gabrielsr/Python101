from datetime import datetime

curr_year = datetime.today().year

people = [
  ('1982', 'January', '10'),
  ('1999', 'October', '10'),
  ('2010', 'November', '10'),
  ('2005', 'April', '10'),
  ('1998', 'March', '10'),
  ('2009', 'January', '10'),
  ('1973', 'May', '10')
]

#birth_year = int(input("insert your birday year\n"))

# this is a Python FOR loop
for person in people:
  print('lets calculate days since birthday for:')
  print(person)



