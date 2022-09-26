# Filename: p4.py
# Author: Michael Bell
# Date Created: 09/25/2022
# Date Last Modified: 09/25/2022
# Email: msb5390@gmail.com

# From ProjectEuler.net
# Largest palindrome product
# Problem 4
#
# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

palindromes = []
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        k = i * j
        if isPalindrome(k):
            if palindromes and k < max(palindromes):
                break
            else:
                palindromes.append(k)
                print(k)
            
palindromes.sort()
print('Largest palindrome:', palindromes[-1])
