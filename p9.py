""" A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc. """

import math

# roughly based on Babylonian method, though divisions are floored
# essentially if the Bablylonian reaches a result without also having reached a case where guess^2 == number then the answer has to be imperfect
def isPerfectSquare(number):
  guess = number // 4
  guesses = [guess]
  while guess**2 != number:
    guess = (guess + (number // guess)) // 2
    if guess in guesses:
      return False
    guesses.append(guess)
  return True

potentialABCs = [x for x in range(4,1000001) if isPerfectSquare(x) == True]

for num in potentialABCs:
    match = [x for x in potentialABCs if x != num and (x+num) in potentialABCs]
    if len(match) > 0:
        for m in match:
            a = math.sqrt(num)
            b = math.sqrt(m)
            c = math.sqrt(num + m)
            added =  a + b + c
            if added == 1000:
                print(a*b*c)





