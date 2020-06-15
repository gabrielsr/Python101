
def input_number_in_range (message, range_start, range_end):
  """ Get a number from user and check if is in the expected range """
  input_str = input(message)
  if not input_str.isnumeric():
    print('please type a numeric value')
    exit()
  else:
    input_number = int(input_str)

  if input_number > range_end or input_number < range_start:
    print(f'the value must be between {input_number} and {range_end}')
  return input_number
  