
def doNothing():
  """ Example function that does nothing """
  pass

doNothing()

# TIP uncommenting multiple lines
#
# To select multiple lines put the cursor in the begining of a line, hold [shift] and press [arrow down] multiple times
# Select multiple commented lines and press ctrl+ / to uncomment 


def printSum(numA, numB):
  """ print the sum of two numbers """
  the_sum = numA + numB
  print(the_sum)

printSum(2, 3)
printSum(10, 3)
printSum(12, 3)
printSum(2, 13)


def returnSum(numA, numB):
  """ return the sum of two numbers """
  return numA + numB

returned_value = returnSum(2,3)
print(returned_value)





