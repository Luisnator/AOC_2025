from enum import Enum

matrix = []

def readfile():
    with open("./day4/data.txt") as f:
        for i, line in enumerate(f):
            line = line.strip()
            matrix.append([])
            for j, char in enumerate(line):
                matrix[i].append(char)

readfile()


class Direction(Enum):
   N = 0
   NE = 1
   E = 2
   SE = 3
   S = 4
   SW = 5
   W = 6
   NW = 7

def printMatrix():
    print("-----------")
    for line in matrix:
        print(line)
    print("-----------")
    print("")


def checkDirection(direction, x , y,symbol):
    try:
        match direction:
            case Direction.N:
                if not checkCoordinates(x,y-1):
                    return False
                return symbol == matrix[y-1][x]
            case Direction.NE:
                if not checkCoordinates(x+1,y-1):
                    return False
                return symbol == matrix[y-1][x+1]
            case Direction.E:
                if not checkCoordinates(x+1,y):
                    return False
                return symbol == matrix[y][x+1]
            case Direction.SE:
                if not checkCoordinates(x+1,y+1):
                    return False
                return symbol == matrix[y+1][x+1]
            case Direction.S:
                if not checkCoordinates(x,y+1):
                    return False
                return symbol == matrix[y+1][x]
            case Direction.SW:
                if not checkCoordinates(x-1,y+1):
                    return False
                return symbol == matrix[y+1][x-1]
            case Direction.W:
                if not checkCoordinates(x-1,y):
                    return False
                return symbol == matrix[y][x-1]
            case Direction.NW:
                if not checkCoordinates(x-1,y-1):
                    return False
                return symbol == matrix[y-1][x-1]
    except:
            return False
    
def checkCoordinates(x,y):
    if (x < 0) or (y < 0):
        return False
    if x > (len(matrix[0])-1):
        return False
    if y > (len(matrix)-1):
        return False
    return True


def checkAllDirections(x,y,symbol):
    count = 0
    if checkDirection(Direction.N,x,y,symbol): count +=1
    if checkDirection(Direction.NE,x,y,symbol): count +=1
    if checkDirection(Direction.E,x,y,symbol): count += 1
    if checkDirection(Direction.SE,x,y,symbol): count += 1
    if checkDirection(Direction.S,x,y,symbol): count += 1
    if checkDirection(Direction.SW,x,y,symbol): count += 1
    if checkDirection(Direction.W,x,y,symbol): count += 1
    if checkDirection(Direction.NW,x,y,symbol): count += 1
    return count


day1count = 0
change = True 
while(change):
    change = False
    for y, line in enumerate(matrix):
        for x, element in enumerate(line):
            if element == '@':
                rolls = checkAllDirections(x,y,'@')
                if rolls < 4:
                    day1count += 1
                    matrix[y][x] = '.'
                    change = True


print(day1count)

