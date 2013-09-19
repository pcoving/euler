'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

N = 20
n = N
done = False
while not done:
    done = True
    for m in range(2,N+1):
        if n/m != float(n)/m:
            done = False
    
    if not done:
        n += N

print n
