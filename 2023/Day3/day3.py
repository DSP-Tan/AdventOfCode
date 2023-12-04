def get_numbers(Lines):
    numbers=[]
    for i, line in enumerate(Lines):
        num=""
        indices=[]
        start = False
        for j, letter in enumerate(line):
            if letter.isdigit():
                if start == False:
                    start= True
                num +=letter
                indices.append((i,j))
                if j== len(line)-1:
                    numbers.append( (int(num),indices) )
            else:
                if start == True:
                    numbers.append( (int(num),indices) )
                    start=False
                    num=""
                    indices=[]
    return numbers

def get_stars(Lines):
    stars=[]
    for i, line in enumerate(Lines):
        for j, letter in enumerate(line):
            if letter=="*":
                stars.append((i,j))
    return stars

def look_around_stars(star_locs, parts):
    partVals = []
    count =0
    i,j = star_locs
    for part in parts:
        partVal = part[0]
        loc = part[1]
        found = False
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                if dx == dy == 0 or found:
                    continue
                if (i+dx,j+dy) in loc:
                    count +=1
                    #print(f"star {(i,j)} touches part {(i+dx,j+dy)}; count={count}")
                    partVals.append(partVal)
                    found=True
    return (count,partVals)

def look_around(i, j, Lines):
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if dx == dy == 0:
                continue
            if i+dx< len(Lines) and j+dy < len(Lines[0]) :
                neigh = Lines[i+dx][j+dy]
                if not neigh.isdigit() and neigh != ".":
                    return True
    return False

import sys
if __name__=='__main__':
    Lines = [ line.strip('\n') for line in open(sys.argv[1], 'r').readlines() ]
    for i in Lines:
        print(i)
    numbers=get_numbers(Lines)
    stars=get_stars(Lines)

    parts=[]
    part_indices=[]
    for number, indices in numbers:
        for i,j in indices:
            if look_around(i,j,Lines):
                parts.append( (number,indices) )
                part_indices.append(indices)
                break

    gears = []
    sum=0
    for star in stars:
        #print(f"star: {star}")
        answer =look_around_stars(star, parts)
        if look_around_stars(star, parts)[0]==2:
            print(f"gear at {star}, parts {answer[1]}")
            sum += answer[1][0]*answer[1][1]
    print(sum)
