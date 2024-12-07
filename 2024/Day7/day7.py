from itertools import product
lines = [i.strip("\n") for i in open("example.txt").readlines()]

resOperands= [[j.strip(":") for j in i.split()] for i in lines]
tests = [int(i[0]) for i in resOperands]
Operands = [i[1:] for i in resOperands]


def calculate(nums: list, ops: list):
    num1 = nums[0]
    for i in range(len(nums)-1):
        num2 = nums[i+1]
        exp = num1+ops[i]+num2
        res= int(num1+num2) if ops[i]=='|' else eval(exp)
        num1=str(res)
    return res

def solve(tests, Operands, possOps):
    sum=0
    for i, test in enumerate(tests):
        nums = Operands[i]
        opList = product(possOps, repeat=len(nums)-1)
        for ops in opList:
            result = calculate(nums,ops)
            if(result==test):
                sum +=test
                break
    return sum

print(solve(tests, Operands, ["+","*"]))
print(solve(tests, Operands, ["+","*","|"]))
