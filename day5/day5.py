
ingredient_ranges = []
ingredient_list = []
ingredient_list_fresh = []
def readfile():
    with open("./day5/data.txt") as f:
        il = False
        for line in f:
            if not il:
                if line == "\n":
                    il = True
                else:
                    splitted = line.strip().split("-")
                    ingredient_ranges.append((int(splitted[0]),int(splitted[1])))
            else:
                ingredient_list.append(int(line.strip()))
    

readfile()
#print(ingredient_ranges)
#print(ingredient_list)

for i_range in ingredient_ranges:
    change = False
    toremove = []
    for ingredient in ingredient_list:
        change = True
        if (ingredient >= i_range[0]) and (ingredient <= i_range[1]):
            ingredient_list_fresh.append(ingredient)
            toremove.append(ingredient)
    for tr in toremove:
        ingredient_list.remove(tr)
    if not change:
        break

print(f"Fresh Count: {len(ingredient_list_fresh)}")

merged_ranges = []
ignore_index = []
for i, i_range in enumerate(ingredient_ranges):
    if i in ignore_index:
        #print("ingored")
        continue
    lowest = i_range[0]
    highest = i_range[1]
    if i != len(ingredient_ranges) -1:
        change = True
        while change:
            change = False
            for j in range(i+1,len(ingredient_ranges)):
                #print(f"cur: {i_range} to {ingredient_ranges[j]}")
                if (ingredient_ranges[j][0] < lowest) and (ingredient_ranges[j][1] > highest):
                    lowest = ingredient_ranges[j][0]
                    highest = ingredient_ranges[j][1]
                    ignore_index.append(j)
                    change = True
                elif (ingredient_ranges[j][0] < lowest) and (ingredient_ranges[j][1] >= lowest):
                    lowest = ingredient_ranges[j][0]
                    ignore_index.append(j)
                    change = True
                elif (ingredient_ranges[j][0] <= highest) and (ingredient_ranges[j][1] > highest): 
                    highest = ingredient_ranges[j][1]
                    ignore_index.append(j)
                    change = True
                elif (ingredient_ranges[j][0] >= lowest) and (ingredient_ranges[j][1] <= highest):
                    ignore_index.append(j)
                    
        merged_ranges.append((lowest,highest))
    else:
        merged_ranges.append(i_range)

count = 0
for m_range in merged_ranges:
    count += m_range[1]-m_range[0] + 1
    print(m_range)
print(f"Fresh Indexes: {count}")
