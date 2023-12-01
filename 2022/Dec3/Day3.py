Sacks = [i.strip("\n") for i in open('input.txt', 'r').readlines()]

# Part 1
def priority(c):
  return ord(c)-96 if ord(c) > 90 else ord(c)-38

tot=0
for i in Sacks:
  half=len(i)//2
  for j in set(i[:half]).intersection(set(i[half:])):
    tot += priority(j)
print(tot)

# Part 2
i=tot=0
for i in range(0,len(Sacks),3):
  for j in set(Sacks[i]).intersection(Sacks[i+1],Sacks[i+2]):
    tot+=priority(j)
print(tot)
