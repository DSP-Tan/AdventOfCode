import sys
Lines = [ line.strip('\n') for line in open(sys.argv[1], 'r').readlines() ]

class Card:
    def __init__(self, id, winners, myNums, wins, count):
        self.id = id
        self.winners = winners
        self.myNums = myNums
        self.wins = wins
        self.count = count

def collect_cards(Lines):
    Cards=[]
    for i, line in enumerate(Lines):
        wins=0
        numbers = line.split(":")[1].split("|")
        winners = numbers[0].split()
        myNums  = numbers[1].split()
        wins    = sum(1 for num in myNums if num in winners)

        Cards.append( Card(i+1, winners, myNums, wins, 1) )
    return Cards

# Part 1
Cards=collect_cards(Lines)
scores=[]
for card in Cards:
    score = 0
    for num in card.myNums:
        if num in card.winners:
            score = 1 if (score == 0) else score*2
    scores.append(score)
print(sum(scores))

# Part 2
for i, card in enumerate(Cards):
    if i== len(Cards)-1:
        continue
    for j in range(card.wins):
        print(i,i+j+1)
        Cards[i+j+1].count +=card.count
print(sum([i.count for i in Cards]) )
