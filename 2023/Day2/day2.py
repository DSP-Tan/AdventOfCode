file1 = open('input.txt', 'r')
Lines = [ line.strip('\n') for line in file1.readlines() ]

# Part 1
def part_1(Games):
    impossibles = []
    possibles=[]
    maxB= 14
    maxG= 13
    maxR= 12
    for game in Games:
        impossible = False
        gameId=int(game.split(":")[0].split("Game")[1].strip() )
        draws =game.split(":")[1].split(';')
        for draw in draws:
            red = blue = green = 0
            #print(draw)
            for colour in draw.split(","):
                if 'blue' in colour:
                    blue = int(colour.split('blue')[0].strip())
                    if blue > maxB: impossible = True
                if 'red' in colour:
                    red = int(colour.split('red')[0].strip())
                    if red > maxR: impossible = True
                if 'green' in colour:
                    green = int(colour.split('green')[0].strip())
                    if green > maxG: impossible = True
        if impossible: impossibles.append(gameId)
        else: possibles.append(gameId)
    return sum(possibles)

print(part_1(Lines))



def part_2(Games):
    maxes = []
    sum=0
    for game in Games:
        maxG=maxB=maxR=0
        gameId=int(game.split(":")[0].split("Game")[1].strip() )
        draws =game.split(":")[1].split(';')
        for draw in draws:
            reds = blues = greens = 0
            for colour in draw.split(","):
                if 'blue' in colour:
                    blues = int(colour.split('blue')[0].strip())
                    if blues > maxB: maxB = blues
                if 'red' in colour:
                    reds = int(colour.split('red')[0].strip())
                    if reds > maxR: maxR=reds
                if 'green' in colour:
                    greens = int(colour.split('green')[0].strip())
                    if greens > maxG: maxG=greens
        maxes.append((gameId,maxR,maxG,maxB))
        sum+= maxR*maxG*maxB
    return sum

print(part_2(Lines))
