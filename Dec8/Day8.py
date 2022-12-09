import numpy as np
Lines=open("input.txt","r").read().split()
matrix = np.array( [ [int(i) for i in j ] for j in [ list(i) for i in Lines ]] )
N=matrix.shape[0]

def trees(i,j):
    up    = np.flip(matrix[0:i,j] < matrix[i,j])
    down  = matrix[i+1:N,j]       < matrix[i,j]
    left  = np.flip(matrix[i,0:j] < matrix[i,j])
    right = matrix[i,j+1:N]       < matrix[i,j]
    return (up,down,left,right)

count= 4*N-4 # Edge trees are all visible
for i in range(1,N-1):
    for j in range(1,N-1):
        up, down, left, right = trees(i,j)
        count += all(up) or all(down) or all(left) or all(right)
print(count)

def scenic(i,j, direction):
    up, down, left, right = trees(i,j)
    dir={"up":up,"down":down,"left":left,"right":right}
    count=0
    for tree in dir[direction]:
        if tree:
            count +=1
        else:
            count +=1
            return count
    return count

scenes=np.zeros((N,N))
for i in range(1,N-1):
    for j in range(1,N-1):
        counts = [ scenic(i,j,direc) for direc in ["up","down","left","right"] ]
        scenes[i,j] = counts[0]*counts[1]*counts[2]*counts[3]
print(scenes.max())
