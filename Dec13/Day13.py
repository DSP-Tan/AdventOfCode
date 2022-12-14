def delve(left,right):
    # Two lists, code for size diffs.
    if isinstance(left,list) and isinstance(right,list):
        # One list empty:
        if not left and right:
            return 1
        if not right and left:
            return -1
        # Both lists empty
        if not left and not right:
            return 0

        # Dirty dwarves delve doubly deep
        sl=len(left)
        sr=len(right)
        i=0
        while( i < min([sl,sr]) ):
            greed=delve(left[i],right[i])
            if greed !=0:
                return greed
            i +=1
        return 0 if sl==sr else int( (sr-sl)/abs(sr-sl) )

    # One a list, other not.
    if isinstance(left,list) and isinstance(right,int):
        return delve(left,[right])
    if isinstance(left,int) and isinstance(right,list):
        return delve([left],right)

    # Integer bedrock
    if isinstance(left,int) and isinstance(right,int):
        if left!=right:
            return int( (right-left)/abs(left-right) )
        elif(left==right):
            return 0

# Part 1
Lines= [eval(i.strip('\n')) for i in open("input.txt").readlines() if i !="\n"]
orders = [delve(Lines[i],Lines[i+1]) for i in range(0,len(Lines),2)]
print(sum([i+1 for i,val in enumerate(orders) if val==1]))

# Part 2
Lines.append([[2]])
Lines.append([[6]])
swaps=1
while(swaps !=0):
    swaps=0
    for i in range(0,len(Lines)-1):
        left=Lines[i]
        right=Lines[i+1]
        greed=delve(left,right)
        if greed == -1:
            Lines[i+1]=left
            Lines[i]=right
            swaps +=1
print( (Lines.index([[2]])+1)*(Lines.index([[6]])+1)   )
