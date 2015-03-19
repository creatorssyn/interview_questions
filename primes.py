#!/usr/bin/python
import math

"""
Write a program to find the number of primes up to and including a given number.
For example, given 5, the program should return 3 (2, 3 and 5 are prime).

@author Brandon Telle <btelle@creators.com>
"""

def is_prime(i):
    k=2
    while k <= math.sqrt(i):
        if i%k == 0:
            return False
        k += 1
    return True
    
def find_primes(limit):
    count = 0
    for i in range(2, limit+1):
        if is_prime(i):
            count += 1
    return count

limit = int(input("Enter limit: "))
print(find_primes(limit))