'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

N = 1000000
primes = set(range(2,N))

for i in range(2,N):
    m = i
    while m < N:
        m += i
        primes.discard(m)
        
primes = list(primes)
print primes[10000]
