

# *args is a special notation in python to take all argument
def input_number_in_range_with_retry(*args):
  """ Get a number from user and check if is in the expected range. If the input is not what we expect, try again """
  input_number = None
  
  while input_number == None:
    input_number = input_number_in_range(*args)
  return input_number

def input_number_in_range (message, range_start, range_end):
  """ Get a number from user and check if is in the expected range """
  input_str = input(message)
  if not input_str.isnumeric():
    print('please type a numeric value')
    return None
  else:
    input_number = int(input_str)

  if input_number > range_end or input_number < range_start:
    print(f'the value must be between {range_start} and {range_end}')
    return None
  else:
    return input_number
  