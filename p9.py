'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

from math import sqrt

N = 1000
count = 0
for a in range(1,N):
    for b in range(a,N-a):
        c = N-a-b
        #print a, b, c, a+b+c
        if sqrt(a**2 + b**2) == c:
            print a,b,c,a*b*c
        count += 1
