# Filename: p3.py
# Author: Michael Bell
# Date Created: 09/24/2022
# Date Last Modified: 09/25/2022
# Email: msb5390@gmail.com

# From ProjectEuler.net
# Largest prime factor
# Problem 3
#
# The prime factors of 13195 are 5, 7, 13, and 29.
#
# What is the largest prime factor of the number 600851475143?

from math import sqrt

n = 600851475143

# Keep a list of currently-known primes to make code more efficient.
# Start with the smallest prime number:
prime_list = [2]

def isPrime(n):
    if n in prime_list:
        return True
    for prime in prime_list:
        if not n % prime:
            return False
    return True

# Search for the next prime number. The Fundamental Theorem of Arithmetic
# states that every number can be broken down into a product of
# primes. If no prime factors can be found, then the number itself
# must be another prime. Once we find one, add it to the list.
def getNextPrime(n):
    n += 1 if n == 2 else 2
    while not isPrime(n):
        n += 2
    prime_list.append(n)
    return n

# Here's where we do the main work. Keep dividing our original number
# by known primes, until we're left with 1. Because we're dividing by
# primes in ascending order, the last division we do, which results in
# a 1 means we have found the largest prime factor. Print it out.
# (For fun, we also print out *all* prime factors.)
prime_factors = []
factor = 2                      # Start with first prime number.
largestPrime = 0                # Stores the largest prime factor.
while n > 1:
    while not n % factor:       # Keep dividing by current prime until we can't.
        n //= factor
        largestPrime = factor   # This is currently the largest prime factor.
        prime_factors.append(factor)
    factor = getNextPrime(factor)

print('Largest prime factor:', largestPrime)
print('All prime factors:', prime_factors)
