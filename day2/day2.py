import copy
inputlist = []
sum_of_invalid = 0

def readfile():
    read_str = ""
    with open("./day2/data.txt") as f:
       read_str = f.read()
       read_str = read_str.split(",")
       for val in read_str:
           val_list = []
           low = int(val.split("-")[0])
           high = int(val.split("-")[1])
           for i in range(low,high+1):
               val_list.append(i)
           inputlist.append(val_list)

readfile()

for val_range in inputlist:
    for val in val_range:
        val = str(val)
        invalid_id = True
        if (len(val) % 2) == 0:
            for i in range(int(len(val)/2)):
                if val[i] != val[int(len(val)/2+i)]:
                    invalid_id = False
        else:
            invalid_id = False
        if invalid_id:
            sum_of_invalid += int(val)

#print(sum_of_invalid)
sum_of_invalid_v2 = 0
for val_range in inputlist:
    for val in val_range:
        val = str(val)
        invalid_id = False
        print(f"Value: {val}")
        for count in range(1,int(len(val)/2)+1):
            alltrue = True
            snipped = copy.deepcopy(val[0:count])
            if len(val) % len(snipped) != 0:
                continue
            for i in range(int(len(val) / count)):    
                if val[i*count:(i*count)+count] == snipped:
                    pass
                    #print(f"snipped: {snipped} match: {val[i*count:(count+(i*count))]}")
                if val[i*count:(i*count)+count] != snipped:
                    alltrue = False
                    #print(f"i * count={i*count} count+(i*count)= {count+(i*count)}")
                    #print(f"snipped: {snipped} mismatch: {val[i*count:(count+(i*count))]}")
            if alltrue == True:
                #print(snipped)
                invalid_id = True
        if invalid_id:
            print(val)
            sum_of_invalid_v2 += int(val)
print(sum_of_invalid_v2)
            

