'''
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91x90

Find the largest palindrome made from the product of two 3-digit numbers.
'''

from itertools import combinations

def check_palindrome(n):
    div = 1
    digits = []
    while div <= n:
        digits.append(n/div%10)
        div *= 10
    return digits == digits[::-1]
    

max_palindrome = 0
for pair in combinations(range(100, 1000), 2):
    candidate = pair[0]*pair[1]
    if check_palindrome(candidate) and candidate > max_palindrome:
        max_palindrome = candidate
        print max_palindrome





