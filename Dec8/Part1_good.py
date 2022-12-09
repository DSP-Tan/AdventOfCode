import numpy as np
Lines=open("input.txt","r").read().split()
matrix = np.array( [ [int(i) for i in j ] for j in [ list(i) for i in Lines ]] )
N=matrix.shape[0]

count= 4*N-4 # Edge trees are all visible
for i in range(1,N-1):
    for j in range(1,N-1):
        up    = all(matrix[0:i,j]   < matrix[i,j])
        down  = all(matrix[i+1:N,j] < matrix[i,j])
        left  = all(matrix[i,0:j]   < matrix[i,j])
        right = all(matrix[i,j+1:N] < matrix[i,j])
        count += up or down or left or right
print(count)
