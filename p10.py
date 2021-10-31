""" The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million. """

import math

def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

sumOfPrimes = sum([x for x in range(2,2000000) if isPrime(x) == True])

print(sumOfPrimes)
