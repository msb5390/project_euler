# Filename: p6.py
# Author: Michael Bell
# Date Created: 09/25/2022
# Date Last Modified: 09/25/2022
# Email: msb5390@gmail.com

# From ProjectEuler.net
# Sum square difference
# Problem 6
#
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385.
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025.
# Hence the difference between the sum of the squares of the first
# ten natural numbers and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.

# Try brute force. Note: There's a simple formula for the sum of the
# first n digits, but since we're only going up to 100, I don't think
# I need to use that here. (It won't take long.)
sum_n = sum(i for i in range(101))
sum_sqs_n = sum(i**2 for i in range(101))

print('The sum of squares of the first 100 natural numbers minus')
print('the square of the sum is:', abs(sum_sqs_n - sum_n**2))
