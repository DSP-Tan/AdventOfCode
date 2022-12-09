Sacks = [i.strip("\n") for i in open('input.txt', 'r').readlines()]

# Part 1
def priority(c):
  return ord(c)-96 if ord(c) > 90 else ord(c)-38

tot=0
for bag in Sacks:
  half=int(len(bag)/2)
  for i in set(bag[:half]):
    if i in set(bag[half:]):
      tot += priority(i)
print(tot)

# Part 2
i=tot=0
for i in range(0,len(Sacks),3):
  for j in set(Sacks[i]):
    if j in set(Sacks[i+1]) and j in set(Sacks[i+2]):
      tot+=priority(j)
print(tot)
