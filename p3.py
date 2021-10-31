""" The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ? """

import math
target = 600851475143

def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True

for i in range(int(math.sqrt(target))+1,2,-1):
    if target%i == 0:
        if isPrime(i) == True:
            largestPrimeFound = i
            break

print(largestPrimeFound)
