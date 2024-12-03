def checkMonotonic(diffs):
  incOrDec = [i>0 for i in diffs]
  return all(incOrDec) or ( not any(incOrDec) )

def checkSpaces(diffs):
    return not [i for i in diffs if abs(i)<1 or abs(i)>3]

def problemDampner(nums):
    for i in range(len(nums)):
        newNums= [val for j,val in enumerate(nums) if j!=i]
        newDiffs = [newNums[i+1] - newNums[i] for i in range(len(newNums)-1) ]
        if checkMonotonic(newDiffs) and checkSpaces(newDiffs):
            return True
    return False


Lines = open("input.txt").readlines()
Lists = [ [int(i) for i in line.split()] for line in Lines]

safe=0
dampedSafe=0
for nums in Lists:
    diffs = [nums[i+1] - nums[i] for i in range(len(nums)-1) ]
    good = checkMonotonic(diffs) and checkSpaces(diffs)

    safe = safe + good
    if not (good):
        good = problemDampner(nums)
    dampedSafe = dampedSafe + (good)

print(safe)
print(dampedSafe)
