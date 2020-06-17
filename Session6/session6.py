print('Session 6')

# Last session we used a while, lets review

got_number = False 

while not got_number: 
  input_str = input("type a number: ")
  got_number = input_str.isnumeric()
  # go back to the 'while' line, and check the condition
print('got a number')

# another way of creating a while is:
while True: 
  input_str = input("type another number: ")
  if(input_str.isnumeric()):
    break;
  # go back to the 'while' line, and check the condition
print('got another number')


# you can use while for indexing
i = 0
week_days = ('m', 't', 'w', 't', 'f', 's', 's')
while i < 7:
  print(week_days[i], end='\t')
  i+=1
print()

# you can use while for counting
i = 1
while i <= 31:
  print(f'{i}', end='\t')
  if i%7==0:
    print()
  i += 1 # increment by one, i = i + 1
print()

# But for indexing in counting generally using 'for in range'is a better idea

# this is a range
# x = range(0, 10)
# print(x)

# yeah by itself it doesn't do much

# you can covert it to a list
# print(list(x))

# but more inportant you can create a foor loop.
# for i in x:
#   print(i)

# or just 
# for i in range(0, 10):
#   print(i)


# lets say we want all i^2, i between 0 and 10.
# for i in range(0, 10):
#   print(i**2)

# or leap years
# for year in range(2000, 2020):
#   if(year % 4 == 0): # in fact, there is more to it
#     print(year)


# So you learnt that we can 'iterate' over ranges

# we can iterate over tuples as well

# week_days = ('mon', 'tue', 'wen')

# for i in range(0, 3):
#   print(week_days[i])

# for w in week_days:
#   print(w)


# You can do the same with while
# j = 0
# while j<=2:
#   print(week_days[j])

# Just one more thing ...
#
# Another form of repetition is 'recursive call'
# def subByOne(i):
#   print(i)
#   if(i < 0):
      # this is what we call the 'stop condition'
#     return
#   else:
#     subByOne(i-1)
# subByOne(10)
