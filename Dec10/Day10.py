Lines=[i.strip("\n").split() for i in open("input.txt").readlines()]
cycle=1
X=1
cycles=[(cycle,X)]
for i in Lines:
    if i[0]=="noop":
        cycle +=1
        cycles.append((cycle,X))
    else:
        for _ in range(1):
            cycle +=1
            cycles.append((cycle,X))
        cycle+=1
        X +=int(i[1])
        cycles.append((cycle,X))

sum=0
for i in cycles:
    if (i[0]-20)%40 == 0:
        sum+= i[0]*i[1]
print(sum)

for i in cycles:
    if i[1]-1<=(i[0]-1)%40<=i[1]+1:
        print("#",end="")
    else:
        print('.',end="")
    if i[0]%40 ==0:
        print("\n",end="")
