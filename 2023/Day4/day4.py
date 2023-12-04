Lines = [ line.strip('\n') for line in open("input.txt", 'r').readlines() ]

class Card:
    def __init__(self, wins, count): self.wins, self.count = wins, count

Cards=[]
for i, line in enumerate(Lines):
    numbers = line.split(":")[1].split("|")
    winners = numbers[0].split()
    myNums  = numbers[1].split()
    wins    = sum(1 for num in myNums if num in winners)
    Cards.append( Card( wins, 1) )

# Part 1
print(sum( 2**(card.wins-1)  for card in Cards if card.wins ) )

# Part 2
for i, card in enumerate(Cards):
    for j in range(card.wins):
        Cards[i+j+1].count +=card.count
print(sum(card.count for card in Cards) )
