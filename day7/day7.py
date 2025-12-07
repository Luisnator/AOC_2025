
inputlist = []
start = ()
def readfile():
    with open("./day7/data.txt") as f:
        for i, line in enumerate(f):
            inputlist.append([])
            for j, symbol in enumerate(line.strip()):
                inputlist[i].append(symbol)
                if symbol == "S":
                    global start
                    start = (i,j)

readfile()

def checkCoordinates(x,y):
    if (x < 0) or (y < 0):
        return False
    if x > (len(inputlist[0])-1):
        return False
    if y > (len(inputlist)-1):
        return False
    return True

def printGrid(grid):
    print("--------")
    for line in grid:
        print(str(line))
    print("--------")


posmap = {}

count = 0
secondcount = 0

def tachion(pos):
    global posmap
    if posmap.get((pos[0],pos[1])) != None:
        #posmap[(pos[0],pos[1])] += 1
        return posmap[(pos[0],pos[1])]
    if not checkCoordinates(pos[1],pos[0]):
        global secondcount
        secondcount += 1
        posmap[(pos[0],pos[1])] = 1
        return posmap[(pos[0],pos[1])]
    posmap[(pos[0],pos[1])] = 0
    if inputlist[pos[0]][pos[1]] == "^":
        if checkCoordinates(pos[1]+1,pos[0]):
            posmap[(pos[0],pos[1])] += tachion((pos[0],pos[1]+1)) 
        if checkCoordinates(pos[1]-1,pos[0]):
            posmap[(pos[0],pos[1])] += tachion((pos[0],pos[1]-1))
        return posmap.get((pos[0],pos[1]))
    else:
        posmap[(pos[0],pos[1])] = tachion((pos[0]+1,pos[1]))
        return tachion((pos[0]+1,pos[1]))

tachion(start)
print(count)
print(secondcount)
print(posmap[start])
#print(posmap)
