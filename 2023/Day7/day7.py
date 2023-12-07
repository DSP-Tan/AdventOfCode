Lines = [i.strip('\n') for i in open("example.txt",'r').readlines() ]
order= ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2" ]

def stronger(a,b):
    A=order.index(a)
    B=order.index(b)
    return A if A < B else B

def get_matches(cards):
    matches=[]
    for i,card1 in enumerate(cards):
        count=1
        for card2 in cards[i+1:]:
            if card2==card1:
                count +=1
        if count>1: matches.append(count)
    return matches

def get_hand(matches):
    fiveOkind  =  len(matches)==1 and matches[0]==5
    fourOkind  =  len(matches)==1 and matches[0]==4
    fullHouse  =  len(matches)==2 and (matches[0]==3 or matches[1]==3 )
    threeOkind =  len(matches)==1 and matches[0]==3
    twoPair    =  len(matches)==2 and (matches[0]==2 and matches[1]==2 )
    pair       =  len(matches)==1 and matches[0]==2
    high       =  len(matches)==0
    hand=[fiveOkind,fourOkind,fullHouse,threeOkind,twoPair,pair,high]
    return hand

print(Lines)
