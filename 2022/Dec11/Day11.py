Lines=[i.strip('\n') for i in open("input.txt").readlines()]
n_monk=len("".join(Lines).split("Monkey")) -1
counts=[0]*n_monk
items=[ [int(i) for i in mon.replace(",","").split()[2:] ] for mon in Lines if "item" in mon]
ops=  [mon.split(":")[1]       for mon in Lines if "Oper"  in mon]
tests=[int(mon.split("by")[1]) for mon in Lines if "Test"  in mon]
tossT=[int(mon[-1])            for mon in Lines if "true"  in mon]
tossF=[int(mon[-1])            for mon in Lines if "false" in mon]


for round in range(20):
    for i in range(n_monk):
        counts[i] += len(items[i])
        # monkey gets item
        for _ in range(len(items[i])):
            old = items[i].pop(0)
            # monkey operates on item
            new = eval(ops[i].split("=")[1])
            # relief lowers items worry.
            new //=3
            # monkey tests and tosses item.
            if new % tests[i] == 0:
                items[tossT[i]].append(new)
            else:
                items[tossF[i]].append(new)
print(sorted(counts,reverse=True)[0]*sorted(counts,reverse=True)[1])

# reset items and counts
counts=[0]*n_monk
items=[ [int(i) for i in mon.replace(",","").split()[2:] ] for mon in Lines if "item" in mon]

big=1
for i in tests:
    big *=i

for round in range(10000):
    for i in range(n_monk):
        counts[i] += len(items[i])
        # monkey gets item
        for _ in range(len(items[i])):
            old = items[i].pop(0)
            # monkey operates on item
            new = eval(ops[i].split("=")[1])
            # relief lowers items worry.
            if new >=big:
                new = new%big
            # monkey tests and tosses item.
            if new % tests[i] == 0:
                items[tossT[i]].append(new)
            else:
                items[tossF[i]].append(new)


print(sorted(counts,reverse=True)[0]*sorted(counts,reverse=True)[1])
