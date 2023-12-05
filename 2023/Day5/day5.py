import sys
Lines = [ line.strip('\n') for line in open(sys.argv[1], 'r').readlines() ]

class Transfer:
    def __init__(self, name):
        self.name   = name
        self.read   = False
        self.dicto  = {}

trans=["seed-to-soil","soil-to-fert","fertilizer-to-water",
       "water-to-light","light-to-temp","temperature-to-humid",
       "humidity-to-location"]

transfers = [Transfer(i) for i in trans]
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
            dst, src, rng = [int(i) for i in line.split()]
            source= range(src, src + rng )
            dest=   range(dst, dst + rng )
            for j, k in zip(source, dest):
                trans.dicto[j]=k


print(seeds)
for i in transfers:
    print(i.name)
    #print(i.ranges)

entities=[seeds]
old = new =seeds
for i, trans in enumerate(transfers):
    old = new
    new = [ trans.dicto[j] if j in trans.dicto else j for j in old ]

for i in new:
    print(i)

print("\n\n")
print(min(new))
#print(min(entities[-1]))

#print(soils)
#soils=[]
#for i in seeds:
#    if i in dicto:
#        soils.append(dicto[i])
#    else:
#        soils.append(i)
