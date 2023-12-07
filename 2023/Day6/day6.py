from math import sqrt, ceil, floor
Lines = [ line.strip('\n') for line in open("input.txt", 'r').readlines() ]

times= [int(i) for i in Lines[0].split()[1:] ]
dists= [int(i) for i in Lines[1].split()[1:] ]
print(times)
print(dists)

ways=1
for T, D in zip(times,dists):
    print(T,D)
    determinant = sqrt(T**2-4*D)
    r1=(T-determinant)/2
    r2=(T+determinant)/2
    nums=len(range(floor(r1)+1,ceil(r2) ) )
    print(nums)
    ways = ways*nums

print(f"part1: {ways}")
T=7; D=9
print(f"T={T}; D={D}")
determinant = sqrt(T**2-4*D)
r1=(T-determinant)/2
r2=(T+determinant)/2
print(f"r1:{r1},r2:{r2}")
print(len(range(int(r1),int(r2) ) ) )

for t in range(7):
    d=(T-t)*t
    print(f"t:{t}, d:{d}")

T=71530
D=940200

T=49979494
D=263153213781851

print(f"T={T}; D={D}")
determinant = sqrt(T**2-4*D)
r1=(T-determinant)/2
r2=(T+determinant)/2
nums=len(range(floor(r1)+1,ceil(r2) ) )
print(f"r1:{r1},r2:{r2}")
print(nums)
