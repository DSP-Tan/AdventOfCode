#input="example.txt"
input="input.txt"
lists=  [i.strip("\n").split() for i in open(input,"r").readlines() ]

list1 = sorted([int(i[0]) for i in lists])
list2 = sorted([int(i[1]) for i in lists])

diff=[abs(list2[i]-list1[i]) for i in range(len(list1))]
print(sum(diff))

similarity = [list2.count(i)*i for i in list1]
print(sum(similarity))
