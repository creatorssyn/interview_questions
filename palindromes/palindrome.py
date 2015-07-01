#/usr/bin/python

"""
Find and print the longest palindrome in a given string.

@author Brandon Telle <btelle@creators.com>
"""

def is_palindrome(str):
    return len(str) > 1 and str == str[::-1]
    
# read the string
f = open('string.txt')
str = f.read()
f.close()

# this definitely isn't the best way to do this.
pal = ''
for i in range(0, len(str)):
    for j in range(i, len(str)-i):
        if is_palindrome(str[i:j]) and len(str[i:j]) > len(pal):
            pal = str[i:j]
          
# print our palindrome          
print(pal)