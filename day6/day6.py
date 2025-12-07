
import copy
inputlist = []

def readfile():
    with open("./day6/data.txt") as f:
        init = False
        for i, line in enumerate(f):
            if not init:
                for columns in line.split():
                    #print(columns)
                    inputlist.append([])
                #print(f"init: {len(inputlist)}")
                init = True
            for j, entry in enumerate(line.split()):
                #print(len(line.split()))
                inputlist[j].append(entry.strip())

inputcolumns = []
def readfile2():
    with open("./day6/data.txt") as f:
        init = False
        for i, line in enumerate(f):
            inputcolumns.append(line)

readfile()
readfile2()
super_result = 0
for data in inputlist:
    result = 0
    if data[-1] is "*":
        result = 1
        for num in data[:-1]:
            result *= int(num)
        super_result += result
    else:
        for num in data[:-1]:
            result += int(num)
        super_result += result

print(super_result)

parsedinput = []
for i, list in enumerate(inputlist):
    parsedinput.append([])
    maxlen = 0
    for data in list[:-1]:
        if len(data) > maxlen:
            maxlen = len(data)
    for j in range(maxlen):
        parsedinput[i].append("")
    for data in list[:-1]:
        for j, char in enumerate(data):
            parsedinput[i][j] += char
    parsedinput[i].append(list[-1])
print(parsedinput)

newinput = []
templist = []
skip = False
for i in range(len(inputcolumns[0])):
    if skip:
        skip = False
        continue
    inputproto = ""
    for j in range(len(inputcolumns)):
        if inputcolumns[j][len(inputcolumns[0])-i-1] in ["*","+"]:
            templist.append(inputproto)
            templist.append(inputcolumns[j][len(inputcolumns[0])-i-1])
            skip = True
            continue
        if inputcolumns[j][len(inputcolumns[0])-i-1] not in [" ","\n"]:
            inputproto += inputcolumns[j][len(inputcolumns[0])-i-1]
    if not skip:
        if inputproto != "":
            templist.append(inputproto)
    else:
        newinput.append(copy.deepcopy(templist))
        templist = []

super_result = 0
for data in newinput:
    result = 0
    if data[-1] is "*":
        result = 1
        for num in data[:-1]:
            result *= int(num)
        super_result += result
    else:
        for num in data[:-1]:
            result += int(num)
        super_result += result

print(super_result)

            
    
        



