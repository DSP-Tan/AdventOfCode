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

# part 1
print(seeds)
olds= seeds
for transfer in transfers:
    news=[]
    for old in olds:
        new = old
        for rang in transfer.ranges:
            dst, src, rng = rang
            if src<= old < src +rng:
                differ = dst -src
                new = old+differ
                break
        news.append(new)

    olds=news
print(min(news))


def get_ranges(seeds):
    seedRs = []
    count=0
    for i in range(int(len(seeds)/2)):
        fart= seeds[count]
        part= seeds[count+1]
        seedRs.append(range(fart, fart + part))
        count+=2
    return seedRs

# part 2
print(seeds)
new_seeds=[]
print(get_ranges(seeds))
for r in get_ranges(seeds):
    for i in r:
        new_seeds.append(i)
print(new_seeds)

olds= new_seeds
for transfer in transfers:
    print(transfer.name)
    news=[]
    for old in olds:
        new = old
        for rang in transfer.ranges:
            dst, src, rng = rang
            if src<= old < src +rng:
                differ = dst -src
                new = old+differ
                break
        news.append(new)

    olds=news
print(min(news))
#olds= seeds
#import ipdb
#for transfer in transfers:
#    ipdb.set_trace()
#    print(transfer.name)
#    print(olds)
#    news=[]
#    Rs = get_ranges(olds)
#    print(Rs)
#    for r in Rs:
#        print(r)
#        for old in r:
#            new = old
#            for rang in transfer.ranges:
#                dst, src, rng = rang
#                if src<= old < src +rng:
#                    differ = dst -src
#                    new = old+differ
#                    break
#            news.append(new)
#    olds=news
#print(min(news))

def solve_two(fart):
    input = open(fart, 'r').readlines()
    inputs = input.split('\n\n')
    seeds = [int(i) for i in inputs[0].split(': ')[1].split(' ')]
    maps = [i.split('\n')[1:] for i in inputs[1:]]

    ranges = []   # Initial ranges of seeds
    for i in range(0, len(seeds), 2):
        ranges.append((seeds[i], seeds[i]+seeds[i+1]-1))

    def mapping(ranges, map):
        new = []   # To be ranges
        for range in ranges:
            start = range[0]
            end = range[1]
            initial_new_length = len(new)
            for m in map:
                # Destination, source, range length
                d, s, r = m.split(' ')
                # Start is beyond the range or end is before
                if start >= (int(s) + int(r)) or end < int(s):
                    continue
                # Start is within the range
                if start >= int(s):
                    new_start = start - int(s) + int(d)
                    # End is also within the range, so move all
                    if end < (int(s) + int(r)):
                        new_end = end - int(s) + int(d)
                        new.append([new_start, new_end])
                    # End is beyond the range, so move part, and rest goes in
                    # the initial range to be assessed against the other moves
                    else:
                        new_end = int(d) + int(r) - 1
                        new.append([new_start, new_end])
                        ranges.append([int(s) + int(r), end])
                    continue
                # Start is before the range, and end within, so move part and rest goes in
                # the initial range to be assessed against the other moves
                if end < (int(s) + int(r)):
                    new_start = int(d)
                    new_end = end - int(s) + int(d)
                    new.append([new_start, new_end])
                    ranges.append([start, int(s)-1])
                # Start is before the range and end beyond, so move only the
                # range within
                else:
                    new_start = int(d)
                    new_end = int(d) + int(r) - 1
                    new.append([new_start, new_end])
                continue
            # If we didn't make any moves during this iteration, let's just
            # keep the initial range
            if initial_new_length == len(new):
                new.append(range)
        return new

    dest = ranges
    for map in maps:  # Do all the migrations
        dest = mapping(dest, map)
    result = min(d[0] for d in dest)

    return result
solve_two("example.txt")


# Ok, so the way to solve this is to never store what you don't need to store.
# so if you have 1-5, you do not store [1,2,3,4,5] but one and five. And if you
# have the numbers in this range being transformed, you transform them into
# more ranges, not more numbers.

# As we are looking for only the minimum, this can be calculated on the fly as
# we look at the numbers. And there may even be a way to cheat by using the
# ranges of the transformations and looking at only the edge numbers.
