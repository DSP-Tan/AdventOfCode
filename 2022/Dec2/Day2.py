# Part 1
Moves = [i.strip("\n").split() for i in open('input.txt', 'r').readlines()]
score  = {"X":1, "Y":2, "Z":3,
          "AX":3, "AY":6, "AZ":0,
          "BX":0, "BY":3, "BZ":6,
          "CX":6, "CY":0, "CZ":3}
print(sum([score[ i[1] ] + score[ i[0]+i[1] ] for i in Moves]))

# Part 2
move_needed={"AX":"C", "AY":"A", "AZ":"B",
             "BX":"A", "BY":"B", "BZ":"C",
             "CX":"B", "CY":"C", "CZ":"A"}
Moves2 = [i+[ move_needed[ i[0]+i[1]] ] for i in Moves]
score2 = {"A":1, "B":2, "C":3, "X":0, "Y":3, "Z":6}
print(sum([score2[i[1]]+score2[i[2]] for i in Moves2]))

# Version 2 using ord
Movs= [  i.strip('\n').split()  for i in open('input.txt', 'r').readlines()]
Moves=[ (ord(i[0])-64, ord(i[1])-87) for i in Movs  ]

def score(A,B):
    return (A-B+1)*3

tot=0
for B,A in Moves:
    if abs(A-B)<2:
        tot += A + score(A,B)
    elif(A<B):
        tot += A + score(A+3,B)
    else:
        tot += A + score(A,B+3)
print(tot)


# Smaller
Moves = [ (ord(i.strip('\n').split()[0])-64, ord(i.strip('\n').split()[1])-87) for i in open('input.txt', 'r').readlines()]
score=0
for B,A in Moves:
    score += A + (A-B+1)*3 if abs(A-B) <2 else ( A + (A+4-B)*3 if A<B else A+ (A-2-B)*3 )
print(score)

# One line
sum( [ A + (A-B+1)*3 if abs(A-B) <2 else ( A + (A+4-B)*3 if A<B else A+ (A-2-B)*3 ) for B,A in [(ord(i.strip('\n').split()[0])-64,ord(i.strip('\n').split()[1])-87) for i in open('input.txt', 'r').readlines()] ]  )
