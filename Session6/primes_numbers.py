print('Exercise 6.2')

import math

# study about for loops

# Execute the following code. Study it a little bit and 
# write a paragraph about it.
# Create a flowchart of check_if_prime.

def check_if_prime(primes_lower_than_n, n):
  """ Check if a number n is prime, providing a list of all primes lower then n """

  is_prime = True
  # is enoth to check until the square root of the number 
  limit = math.floor(math.sqrt(n))

  # check for all primes lower then n, until the sqrt of n
  for d in primes_lower_than_n:
    if d > limit:
      break
    if n%d == 0:
      is_prime = False
      break
  # no divisor found, n must be a prime
  if is_prime:
    print(f'{n} ', end=',')
    return True
  else:
    return False
  

def check_if_prime_range(end):
  """ Get all prime number lower than 'end' """
  primes = [2]
  # check every odd number, 3 or greater
  for n in range(3, end, 2):
    # starting from 3
    if check_if_prime(primes, n):
      # is prime, put in the list
      primes.append(n)
  print(primes)

check_if_prime_range(1000)