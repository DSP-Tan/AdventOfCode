Lines = [ line.strip('\n') for line in open("example.txt", 'r').readlines() ]

seeds=[]
class Transfer:
    def __init__(self, name):
        self.name   = name
        self.ranges = []
        self.read   = False
        self.dicto  = {}

trans=["seed-to-soil","soil-to-fert","fertilizer-to-water",
       "water-to-light","light-to-temp","temperature-to-humid",
       "humidity-to-location"]

transfers = [Transfer(i) for i in trans]
s2s=[]
seed_to_soil=False
for line in Lines:
    if "seeds:" in line:
        seeds = [int(i) for i in line.split("seeds:")[1].split()]
    for trans in transfers:
        if trans.name in line:
            trans.read=True
            break
        if not bool(line.strip() ) and trans.read:
            trans.read=False
            break
        if trans.read:
            #trans.ranges.append([int(i) for i in line.split()])
            dst, src, rng = [int(i) for i in line.split()]
            source= range(src, src + rng )
            dest=   range(dst, dst + rng )
            for j, k in zip(source, dest):
                trans.dicto[j]=k

        #s2s.append([int(i) for i in line.split()])

print(seeds)
#for i in transfers:
#    print(i.name)
#    print(i.ranges)

s2s= transfers[0]
#print(s2s.ranges)

dicto={}
for i in s2s.ranges:
    source= range(i[1],i[1]+i[2] )
    dest=   range(i[0],i[0]+i[2] )
    for j,k in zip(source, dest):
        dicto[j]=k
#print(dicto)
soils=[]
for i in seeds:
    if i in dicto:
        soils.append(dicto[i])
    else:
        soils.append(i)
print(soils)
print(dicto)
print(transfers[0].dicto==dicto)
