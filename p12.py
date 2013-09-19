import sys
from itertools import chain, combinations

def make_primes(n):
    primes = set(range(2,n))
    for i in range(2,n):
        if i in primes:
            m = i
            while m < n:
                m += i
                primes.discard(m)
    return primes

def find_factors(n, primes):
    factors = []
    for p in primes:
        if p >= n:
            break
        m = int(float(n)/p)
        if m == float(n)/p:
            factors += [p, m] + find_factors(m, primes)
    return factors 

if __name__ == "__main__":
    primes = make_primes(10000)
    for m in range(1,100000):
        ndivisors = len(set(find_factors(m*(m+1)/2, primes))) + 2
        print m*(m+1)/2, ndivisors
        if ndivisors > 500:
            break;
    
