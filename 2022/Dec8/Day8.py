import numpy as np
Lines=open("input.txt","r").read().split()
matrix = np.array( [ [int(i) for i in j ] for j in [ list(i) for i in Lines ]] )
N=matrix.shape[0]

def scenic(look):
    negs = [ i for i, val in enumerate(look) if val==False ]
    return look[:negs[0]].sum() +1 if negs else look.sum()

scenes=np.zeros((N,N))
visible = 4*N-4 # Edge trees are all visible
for i in range(1,N-1):
    for j in range(1,N-1):
        up    = np.flip(matrix[0:i,j] < matrix[i,j])
        down  = matrix[i+1:N,j]       < matrix[i,j]
        left  = np.flip(matrix[i,0:j] < matrix[i,j])
        right = matrix[i,j+1:N]       < matrix[i,j]

        visible += all(up) or all(down) or all(left) or all(right)
        views    = [ scenic(dir) for dir in [up,down,left,right] ]
        scenes[i,j] = views[0]*views[1]*views[2]*views[3]
print(f"Part 1: {visible}")
print(f"Part 2: {scenes.max()}")
