import math

inputlist = []

def readfile():
    with open("./day8/testdata.txt") as f:
        for line in f:
            split = line.strip().split(",")
            intsplit = [int(x) for x in split]
            inputtuble = (intsplit[0],intsplit[1],intsplit[2])
            inputlist.append(inputtuble)


def distance(point1, point2):
    return math.dist(point1,point2)

readfile()

setdic = {}

min_distance = 0
for i in range(10):
    shortest = 999999999
    curset = []
    for j,item in enumerate(inputlist):
        for l,item2 in enumerate(inputlist):
            d = distance(inputlist[j],inputlist[l])
            if (d < shortest) and (d > min_distance):
                shortest = d
                curset.clear()
                curset.append(inputlist[j])
                curset.append(inputlist[l])
    foundset = False
    justone = None
    for c in curset:
        #print(c)
        s = setdic.get(c)
        if s:
            foundset = True
            if justone == None:
                justone = s
            else:
                justone == None
    if not foundset:
        newset = set(())
        newset.add(curset[0])
        newset.add(curset[1])
        setdic[curset[0]] = newset
        setdic[curset[1]] = newset
    if justone:
        justone.add(curset[0])
        justone.add(curset[1])
        setdic[curset[0]] = justone
        setdic[curset[1]] = justone
    unionset = None
    if setdic.get(curset[0]) and setdic.get(curset[1]):
        unionset = setdic[curset[0]].union(setdic[curset[1]])
    if unionset:
        print("Union")
        print(setdic.get(curset[0]))
        print(setdic.get(curset[1]))
        for x in setdic.get(curset[0]):
            #print(x)
            setdic[x] = unionset
        #print("---")
        for x in setdic.get(curset[1]):
            #print(x)
            setdic[x] = unionset
    min_distance = shortest
print(setdic)

uniquelist = []
for key, val in setdic.items():
    if val not in uniquelist:
        uniquelist.append(val)

uniquelist.sort(key=len)
print(uniquelist)
for un in uniquelist:
    print(len(un))