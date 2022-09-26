# Filename: p5.py
# Author: Michael Bell
# Date Created: 09/25/2022
# Date Last Modified: 09/25/2022
# Email: msb5390@gmail.com

# From ProjectEuler.net
# Smallest multiple
# Problem 5
#
# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is *evenly divisible*
# by all of the numbers from 1 to 20?

# If the number is divisible by 20, it's automatically divisible
# by 1, 2, 4, 5, and 10 too.
# If the number is divisible by 18, it's also divisible by 3, 6 and 9.
# If the number is divisible by 16, it's divisible by 8.
# If the number is divisible by 14, it's divisible by 7.
#
# Need to check: 11, 12, 13, 14, 15, 16, 17, 18, 19, 20.

found = False
n = 20
check = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
while not found:
    found = True                # Manually set to False later if doesn't work.
    for num in check:
        if n % num:
            n += 20             # Must be multiple of 20: increment accordingly.
            found = False       # Wasn't evenly divisible by all, so next.
            break

print('The smallest positive number that is *evenly divisible* by')
print('all of the numbers from 1 to 20 is', n)
    
