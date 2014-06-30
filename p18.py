triangle = []

with open('p67.txt', 'r') as fd:
    for line in fd:
        triangle.append([int(s) for s in line.split(' ')])

paths = [triangle[0][0]]

for row in range(1,len(triangle)):
    # lengthen by one
    new_paths = [0]*(row+1)

    # each end automatically gets what's coming to it
    new_paths[0] = paths[0] + triangle[row][0]
    new_paths[-1] = paths[-1] + triangle[row][-1]

    for col in range(1,row):
        new_paths[col] = max(paths[col-1], paths[col]) + triangle[row][col]
        
    paths = new_paths


print max(paths)
    
    
    
    
    


