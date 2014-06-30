N = 20

num_routes = {(0,0): 1}

for i in range(N+1):
    for j in range(N+1):
        if (i,j) != (0,0):
            total = 0;
            if i > 0:
                total += num_routes[(i-1,j)] 
            if j > 0:
                total += num_routes[(i,j-1)] 
        
            num_routes[(i,j)] = total

