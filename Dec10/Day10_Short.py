Lines=[i.strip("\n").split() for i in open("input.txt").readlines()]
cycle=1
X=1
cycles=[(cycle,X)]

for i in Lines:
    if i[0]=="noop":
        cycle +=1
    else:
        cycles.append((cycle+1,X))
        cycle+=2
        X +=int(i[1])
    cycles.append((cycle,X))

# Part 1
print(sum( [i[0]*i[1] for i in cycles if (i[0]-20)%40 == 0]))

# Part 2
for i in cycles:
    print("#",end="") if i[1]-1<= (i[0]-1)%40 <= i[1]+1 else print('.',end="")
    if i[0]%40 ==0: print("\n",end="")
