def delve(left,right):
    print(f"left:  {left}\nright: {right}")

    # Two lists, code for size diffs.
    if isinstance(left,list) and isinstance(right,list):
        # One list empty:
        if not left and right:
            print("Left is empty and right is not: 1")
            return 1
        if not right and left:
            print("Right is empty and left is not: -1")
            return -1
        # Both lists empty
        if not left and not right:
            return 0

        # Double dwarves delve deep
        print("Iterating over two lists:")
        sl=len(left)
        sr=len(right)
        print(f"sl: {sl}\nsr: {sr}")
        i=0
        while( i < min([sl,sr]) ):
            greed=delve(left[i],right[i])
            if greed !=0:
                return greed
            i +=1
        if sl<sr:
            print("Left ran out of elements.")
        if sl>sr:
            print("Right ran out of elements.")
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


Lines= [eval(i.strip('\n')) for i in open("input.txt").readlines() if i !="\n"]
orders=[]
for i in range(0,len(Lines),2):
    print(f"-------------------------------------------------------------------")
    print(f"Pair: {i}")
    left=Lines[i]
    right=Lines[i+1]
    greed=delve(left,right)
    orders.append(greed)
    print(f"\nGreed: {greed}")
print(len(orders))
print(sum([i+1 for i,val in enumerate(orders) if val==1]))

for i in Lines:
    print(i)
