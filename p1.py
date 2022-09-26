# Filename: p1.py
# Author: Michael Bell
# Date Created: 09/24/2022
# Date Last Modified: 09/24/2022
# Email: msb5390@gmail.com

# From PrjectEuler.net
# Multiples of 3 or 5
# Problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

# Sum multiples of 3:
sum_3s = 0
for i in range(3, 1000, 3):
    sum_3s += i

# Sum multiples of 5 (but don't double count the multiples of 3 *and* 5!):
sum_5s = 0
for i in range(5, 1000, 5):
    if i % 3:
        sum_5s += i

# Add up the results and print the answer:
print('The sum of all the multiples of 3 or 5 below 1000 is:')
print(sum_3s + sum_5s)
