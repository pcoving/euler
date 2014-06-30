import numpy as np

array = []
with open('p11.dat') as fd:
    for line in fd:
        array.append(map(int, line.split()))
array = np.asarray(array)
N = array.shape[0]

largest = -1
for idx in range(N):
    for jdx in range(N-3):
        largest = max(largest, array[idx,jdx]*array[idx,jdx+1]*array[idx,jdx+2]*array[idx,jdx+3])
        largest = max(largest, array[jdx,idx]*array[jdx+1,idx]*array[jdx+2,idx]*array[jdx+3,idx])

for idx in range(N-3):
    for jdx in range(N-3):
        largest = max(largest, array[idx,jdx]*array[idx+1,jdx+1]*array[idx+2,jdx+2]*array[idx+3,jdx+3])
        largest = max(largest, array[N-1-idx,jdx]*array[N-2-idx,jdx+1]*array[N-idx-3,jdx+2]*array[N-idx-4,jdx+3])
        
print largest
