
def guess(range_start, range_end):
  guessed_corretly = False
  low = range_start
  high = range_end

  print(f"think in a number between {range_start} and {range_end}")
  count = 0
  while not high == low:
    mid = (low+high)//2
    print(f'is it higher then {mid}?')
    response = input("[y]/n")
    if response.lower() == "y" or response =="":
      low = mid + 1
    else:
      high = mid
    count = count + 1
    print(f'{low}-{high}')
  print(f'you though about {low}')
  print(f'guessed with {count} attempts')

guess(0, 100)
  

