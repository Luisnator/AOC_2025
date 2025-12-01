start = 50
cur = start
hits = 0
inputlist = []

def readfile():
    with open("./day1/data.txt") as f:
        for line in f:
            if line[0] == "L":
                inputlist.append(-int(line[1:]))
            else:
                inputlist.append(int(line[1:]))


readfile()
print(inputlist)

for input in inputlist:
   print(f"Cur Pos: {cur}")
   if (cur is 0) and (input < 0):
       print("zero start pos subtracting hit")
       hits = hits - 1
   cur = cur + input
   dontcheck = False
   print(f"Cur Input: {input}")
   while cur < 0:
       cur = cur + 100
       hits = hits + 1
       print(f"underflow hit")
   while cur > 99:
       cur = cur - 100
       hits = hits + 1
       dontcheck = True
       print(f"overflow hit")
   if (cur is 0) and (dontcheck is False):
       hits = hits + 1
       print(f"perfect hit")
   print(f"Cur hits : {hits}") 
print(cur)
print(hits)


