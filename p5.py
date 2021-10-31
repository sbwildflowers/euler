""" 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? """

divisible = False
num = 2520

while divisible == False:
    divisible = True
    for i in range(20, 1, -1):
        if num%i != 0:
            divisible = False
            break
    if divisible == True:
        print(num)
        break
    else:
        num += 20
    
