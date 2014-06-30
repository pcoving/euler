length_dict = {1: 1}
max_length = 0
max_start = -1

def calc_length(val, memoized):
    if val%2 == 0:
        val /= 2
    else:
        val = 3*val + 1
    
    if val in memoized:
        return memoized[val] + 1
    else:
        return calc_length(val, memoized) + 1

for start in range(2, 1000000):
    length = calc_length(start, length_dict)
    length_dict[start] = length
    if length > max_length:
        max_length = length
        max_start = start
    
