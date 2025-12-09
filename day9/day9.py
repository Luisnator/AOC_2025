import copy
import itertools
inputlist = []
combolist = []
def readfile():
    with open("./day9/data.txt") as f:
       for line in f:
        vals = line.strip().split(",")
        inputlist.append((int(vals[0]),int(vals[1])))
    for combo in itertools.combinations(inputlist,2):
       combolist.append(combo)

readfile()
maxvolume = 0
listvolumes = []
for combo in combolist:
   x = abs(combo[0][0]-combo[1][0])+1
   y = abs(combo[0][1]-combo[1][1])+1
   listvolumes.append((x*y,combo))
   if ((x) * (y)) > maxvolume:
      maxvolume = x* y

listvolumes.sort(key=lambda val: val[0])
print(listvolumes)
listvolumes.reverse()

maxvol = 0
first = True

#inputlist.append((94525,48322))
#inputlist.append((94525,50422))

inputlist.append((20000,49322))
inputlist.append((50000,49422))
inputlist.append((70000,49422))
inputlist.append((40000,49422))
for vol in listvolumes:

   point1 = vol[1][0]
   point2 = vol[1][1]
   small_x = 0
   big_x = 0
   small_y = 0
   big_y = 0
   if point1[0] < point2[0]:
      small_x = point1[0]
      big_x = point2[0]
   else:
      small_x = point2[0]
      big_x = point1[0]
   if point1[1] < point2[1]:
      small_y = point1[1]
      big_y = point2[1]
   else:
      small_y = point2[1]
      big_y = point1[1]
   feasable = True
   if first:
      print(vol)
      first = False
      print(vol[1][0])
      print(vol[1][1])
      print(f"sx: {small_x}, bx: {big_x}, sy: {small_y}, by: {big_y}")
   for input in inputlist:
      if ((input[0] > small_x) and (input[0] < big_x)) and ((input[1] > small_y) and (input[1] < big_y)):
         if (input != point1) and (input != point2):
            feasable = False
   if feasable:
      maxvol = vol[0]
      break


print(maxvolume)
print(maxvol)