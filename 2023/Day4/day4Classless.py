Cards=[]
for line in ( line.strip('\n') for line in open("input.txt", 'r').readlines() ):
    numbers = line.split(":")[1].split("|")
    winners, myNums = ( numbers[0].split(), numbers[1].split() )
    wins    = sum(1 for num in myNums if num in winners)
    Cards.append( [ wins, 1] )

# Part 1
print(sum( 2**(card[0]-1)  for card in Cards if card[0] ) )

# Part 2
for i, card in enumerate(Cards):
    for j in range(card[0]):
        Cards[i+j+1][1] +=card[1]
print(sum(i[1] for i in Cards) )
