import numpy as np
Lines=open("input.txt","r").read().split()
matrix = np.array( [ [int(i) for i in j ] for j in [ list(i) for i in Lines ]] )
N=matrix.shape[0]
visible=np.zeros((N,N))
visible[0,:] = visible [:,0] = visible[N-1,:] = visible [:,N-1] = 1

def trees(i,j):
    up    = np.flip(matrix[0:i,j] < matrix[i,j])
    down  = matrix[i+1:N,j] < matrix[i,j]
    left  = np.flip(matrix[i,0:j] < matrix[i,j])
    right = matrix[i,j+1:N] < matrix[i,j]
    return (up,down,left,right)

def viz(i,j):
    up, down, left, right = trees(i,j)
    return all(up) or all(down) or all(left) or all(right)

for i in range(1,N-1):
    for j in range(1,N-1):
        visible[i,j] = viz(i,j)

print(visible.sum())


def scenic(i,j, direction):
    up, down, left, right = trees(i,j)
    dir={"above":up,"below":down,"left":left,"right":right}
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
        counts = [ scenic(i,j,direc) for direc in ["above","below","left","right"] ]
        scenes[i,j] = counts[0]*counts[1]*counts[2]*counts[3]
print(scenes.max())
