
#Create a function days_between(date1, date2) that calculates the number of days between two different dates. 
# Each date should be a tuple (year, month, day). So you should call your function 
def days_between(date1, date2):
  """ calculates the number of days between two different dates. """
  print(f'date1 is {date1[2]}/{date1[1]}/{date1[0]}')
  print(f'date2 is {date2[2]}/{date2[1]}/{date2[0]}')
  return None

# Days between 1st of Jan, 2000 and 1st of Jan, 2020
days = days_between((2000, 1, 1), (2020, 1,1))
print(days)