joltlist = []

def readfile():
    with open("./day3/data.txt") as f:
        for line in f:
            global joltlist
            joltlist.append([int(x) for x in line[:-1]])

readfile()
output = 0
for battery in joltlist:
    indexleft = 0
    maxleft = 0
    maxright = 0
    for i in range(len(battery)-1):
        if maxleft < battery[i]:
            maxleft = battery[i]
            indexleft = i
    for i in range(len(battery)-1,indexleft,-1):
        if maxright < battery[i]:
            maxright = battery[i]
    output += int(str(maxleft)+str(maxright))


output2 = 0
for battery in joltlist:
    indexleft = 0
    maxleft = 0
    active_list = []
    for j in range(12):
        maxleft=0
        for i in range(indexleft,len(battery)-11+j):
            if maxleft < battery[i]:
                maxleft = battery[i]
                indexleft = i+1
        active_list.append(str(maxleft))
    print(f"{active_list}")
    output2 += int(str("".join(active_list)))
print(output2)