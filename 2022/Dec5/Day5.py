Lines = open('input.txt', 'r').readlines()
# Get bottom layer of stacks to read indices
for i, line in enumerate(Lines):
    if '1' in line:
        bottom_layer_of_stacks=i-1
        break
# Get index of instruction start
for i, line in enumerate(Lines):
    if 'move' in line:
        instruct_start=i
        break

# Read indices.
indices = []
n_stack = 0
for i, val in enumerate(Lines[bottom_layer_of_stacks]):
    if val!=' ' and val !='\n' and val !='[' and val!=']':
        indices.append(i)


# Read stacks
stacks=[]
stacks2=[]
for i in range(len(indices)):
    stacks.append([])
    stacks2.append([])
for line in Lines[:bottom_layer_of_stacks+1]:
    for i, val in enumerate(indices):
        if line[val] !=' ':
            stacks[i].append(line[val])
            stacks2[i].append(line[val])

# Block moving part 1
for instruction in Lines[instruct_start:]:
    N   = int(instruction.split()[1])
    fro = int(instruction.split()[3])-1
    tow = int(instruction.split()[5])-1
    letters=[]
    for i in range(N):
        letter = stacks[fro][i]
        letters.append(letter)
    for i in letters:
        stacks[tow].insert(0,i)
        stacks[fro].remove(i)

for i in stacks:
    print(i[0],end="")
print('\n')

# Block moving part 2
for instruction in Lines[instruct_start:]:
    N   = int(instruction.split()[1])
    fro = int(instruction.split()[3])-1
    tow = int(instruction.split()[5])-1
    letters=[]
    for i in range(N):
        letter = stacks2[fro][i]
        letters.append(letter)
    for i in reversed(letters):
        stacks2[tow].insert(0,i)
        stacks2[fro].remove(i)

for i in stacks2:
    print(i[0],end="")
