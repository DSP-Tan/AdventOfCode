input="input.txt"
with open(input,'r') as f:
    Lines = f.readlines()
lists=  [i.strip("\n").split() for i in Lines ]

listA, listB = list(zip(*lists))

diff=[abs(int(i)-int(j)) for i,j in zip(sorted(listA),sorted(listB) ) ]
print(sum(diff))

similarity = [listB.count(i)*int(i) for i in listA]
print(sum(similarity))
