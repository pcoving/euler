'''
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
'''
import numpy as np
array = []
with open('p13.dat') as fd:
    for line in fd:
        array.append(map(int,list(line.strip())))

array = np.asarray(array)

digits = []

for idx in range(array.shape[1]):
    colsum = sum(array[:,idx])
    for jdx, digit in enumerate(str(colsum)[::-1]):
        if idx+jdx >= len(digits):
            digits.append(0)            
        digits[idx+jdx] += int(digit)
        if digits[idx+jdx] > 9:
            if idx+jdx+1 >= len(digits):
                digits.append(0)
            digits[idx+jdx+1] += int(digits[idx+jdx]/10.)
            digits[idx+jdx] = digits[idx+jdx]%10

digits = digits[::-1]

print ''.join(map(str,digits[:10]))



