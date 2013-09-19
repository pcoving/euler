'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

from p12 import make_primes

def find_factors(n, primes):
    factors = []
    for p in primes:
        if p >= n:
            break
        m = int(float(n)/p)
        if m == float(n)/p:
            factors += [p] + find_factors(m, primes)
    return factors 

primes = make_primes(int(1e7))
print max(find_factors(600851475143, primes))
