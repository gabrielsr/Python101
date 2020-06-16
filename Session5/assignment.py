from .user_input import input_number_in_range_with_retry
import random

# now have fun for a while...
def guess(range_start, range_end):
  """ Try to guess the number choosen by the player """
  low = range_start # the lowest possible number
  high = range_end # the highest possible number
  print(f'Think in a number between {range_start} and {range_end}. It ')
  input('press enter to continue...')
  tries = 0
  while not high == low:
    # the hint is the middle between high and low.
    mid = (low+high)//2
    print(f'Is it higher then {mid}?')
    response = input("[y]/n")
    if response.lower() == "y" or response =="":
      low = mid + 1
    else:
      high = mid
    tries = tries + 1
    print(f'Hum. So it is between {low} - {high}')
  print(f'you though about {low}')
  print(f'guessed with {tries} attempts')
  return tries


def give_hint(range_start, range_end):
  """ Choose a number and let the player guess. Give some feedback at each guess """
  # generate a random number inside the range
  number = random.randint(range_start, range_end)
  print('now it is your turn. I will choose a number and you guess.\n')
  print('Type a number. I will say if it higher than the number that I "thought".\n\n')
  tries = 0
  while True: # while True will repeat until find a break
    tries = tries + 1
    guess = input_number_in_range_with_retry('is it higher than... ', range_start, range_end)
    if guess == number:
      print("You're right!")
      break # end the while loop
    elif number > guess:
      print(f"Yes. It's higher than {guess}")
    else:
      print("Noup. It's lower")
  return tries

def check_score(guesses, hints):
  """ Check score and see who is the winner. """
  if guesses < hints:
    print(f'{guesses} against {hints} the machine wins!')
  elif guesses > hints:
    print(f'{hints} against {guesses}. You got lucky this time.')
  else:
    print(f'{hints} against {guesses}. Lets call it a draw.')
  
# Game
print("Let's start. ")
guesses = guess(0, 20)
hints = give_hint(0, 20)
check_score(guesses, hints)



