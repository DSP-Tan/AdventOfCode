from math import ceil
from time import sleep
pageLists = [[int(j) for j in i.strip("\n").split(",")] for i in open("input_pages.txt","r").readlines()]
rules     = [[int(j) for j in i.strip("\n").split("|")] for i in open("input_orders.txt").readlines() ]

def filterRules(pages, rules):
    return [(rule1,rule2) for rule1,rule2 in rules if (rule1 in pages and rule2 in pages)]

def checkRules(i_page,pages,paired_pages,before_or_after):
    """
    i_page is the index of the page whose position we will check against the rules.
    pages is the full list of pages.
    paired_pages is either all the pages that s hould be before this one, or all
    the pages which should be after, depending on the variable before_or_after.
    """
    bads=[]
    start= before_or_after*i_page
    end  = len(pages)-(not before_or_after)*(len(pages)-i_page)
    for page in paired_pages:
        try:
            pages.index(page,start,end)
        except:
            res = (pages[i_page],page) if before_or_after else (page,pages[i_page])
            bads.append(res)
    return bads

def getBrokenRules(pageList, filtered_rules):
    bads=[]
    for i,page in enumerate(pageList):
        befores = [j[0] for j in filtered_rules if j[1]==page]
        afters  = [j[1] for j in filtered_rules if j[0]==page]
        bads   += checkRules(i, pageList,befores, 0) + checkRules(i, pageList,afters, 1 )
    return list(set(bads))



def applyRules(pageList,bads):
    for badTup in list(set(bads)):
        pageList[pageList.index(badTup[0])] = badTup[1]
        pageList[pageList.index(badTup[1])] = badTup[0]
        print(f"Applying rule {badTup}")
        print(pageList)
    return pageList


print(f"All pageLists:\n{pageLists}")
print(f"All rules:\n{rules}")

numBads = 0
sumMids=0
sumMidBads=0

for pageList in pageLists:
    filtered_rules=filterRules(pageList, rules)

    bads = getBrokenRules(pageList, filtered_rules)
    print(f"{pageList} is good. Mid is {pageList[ceil(len(pageList)/2)]}") if not bads else print(f"{pageList} is bad")

    if not bads:
        sumMids += pageList[ceil(len(pageList)/2)-1]
    else:
        print("--"*40)
        print("--"*40)
        while( bads ):
            print(pageList)
            print("Recalculate broken rules")
            bads = getBrokenRules(pageList, filtered_rules)
            print(bads )
            applyRules(pageList,bads )

        print(pageList)
        print(f"{pageList} is now good. Mid is {pageList[ceil(len(pageList)/2)-1]}")
        sumMidBads += pageList[ceil(len(pageList)/2)-1]
        print("--"*40)
        print("--"*40)



    numBads  += int(bool(bads))
print(f"{numBads} of these lists are bad.")
print(f"{len(pageLists)-numBads} of these lists are good.")
print(f"{sumMids} is the sum of the midpoints of goods.")
print(f"{sumMidBads} is the sum of the midpoints of Bads.")
