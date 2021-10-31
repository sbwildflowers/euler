""" A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers. """

def isPalindrome(num):
    forwards = str(num)
    backwards = str(num)[::-1]
    if forwards == backwards:
       return True
    else:
        return False

pal = 0
for i in range(999,99,-1):
    for t in range(990,99,-11):
        if isPalindrome(i*t) == True:
            if i*t > pal:
                pal = i*t

print(pal)

 
