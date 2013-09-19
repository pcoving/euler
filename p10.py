'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''


from p12 import make_primes

primes = make_primes(int(2e6))

print sum(primes)
