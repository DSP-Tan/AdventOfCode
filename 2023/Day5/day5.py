import sys
Lines = [ line.strip('\n') for line in open(sys.argv[1], 'r').readlines() ]

class Transfer:
    def __init__(self, name):
        self.name   = name
        self.read   = False
        self.ranges = []

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
            trans.ranges.append([int(i) for i in line.split()])


print(seeds)
for i in transfers:
    print(i.name)
    #print(i.ranges)

print(seeds)
olds= seeds
for transfer in transfers:
    news=[]
    for old in olds:
        new = old
        for range in transfer.ranges:
            dst, src, rng = range
            if src<= old < src +rng:
                differ = dst -src
                new = old+differ
                break
        news.append(new)

    olds=news
print(min(news))
