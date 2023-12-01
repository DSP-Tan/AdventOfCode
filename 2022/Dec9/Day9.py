import numpy as np
moves = [i.strip('\n').split() for i in open("input.txt").readlines()]

def react(head,tail):
    diff = head-tail
    dx = diff[0]/abs(diff[0]) if diff[0] !=0 else 0
    dy = diff[1]/abs(diff[1]) if diff[1] !=0 else 0
    if np.linalg.norm(np.absolute(diff)) > pow(2,1/2):
       return tail + np.array([dx, dy ])
    return tail

grid1 = np.zeros((1000,1000),dtype=int)
head=np.array([0,0])
tail=np.array([0,0])
grid1[tuple(tail)] = 1

grid2 = np.zeros((1000,1000),dtype=int)
rope  = [np.array([0,0])]*10
grid2[tuple(rope[9])] = 1

mov_dict={"R":(0,1), "L":(0,-1), "U":(-1,0), "D":(1,0)}
for move in moves:
    for i in range(int(move[1])):
        head += mov_dict[move[0]]
        tail = react(head,tail).astype(int)
        grid1[tuple(tail)] = 1

        rope[0] += mov_dict[move[0]]
        for i, knot in enumerate(rope[1:]):
            rope[i+1] = react(rope[i],rope[i+1]).astype(int)
        grid2[tuple(rope[9])] = 1
print(grid1.sum())
print(grid2.sum())
