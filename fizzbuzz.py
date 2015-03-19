#!/usr/bin/python

"""
Write a program that prints the numbers from 1 to 100. But for multiples of
three print "Fizz" instead of the number and for the multiples of five print
"Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

@author Brandon Telle<btelle@creators.com>
"""
    
for i in range(1, 101):
    str = ''
    if i%3 == 0:
        str += 'Fizz'
    if i%5 == 0:
        str += 'Buzz'
    if i%3 != 0 and i%5 != 0:
        str = i
    print(str)
