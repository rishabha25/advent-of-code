import re

f = open("2023/Day3/input.txt", "r")

in_array = [ [ch for ch in line.strip()] for line in f.readlines()]

in_lines = [ "".join(line) for line in in_array]


def check_adj(match, j, dig_l, dig_r):
    for h, v in adj:
        for ind in [dig_l, dig_r]:
            try:
                # print("Adjacent ch -"+ in_array[j+v][ind+h])
                if re.findall(r"[^\d\.]", in_array[j+v][ind+h]):
                    print(match.group())
                    return int(match.group())
            except:
                pass
    return 0


adj = [(0,1),(-1,1), (-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1)]

# Part  1 solution
# Search adjacent to the start and end of each number found using regex.
# If valid symbol in neighbourhood add it to cumulative sum
j= 0
cu_sum = 0
for line in in_lines:
    for match in re.finditer(r'\d+', line):
        print("match", match.group(), "start index", match.start(), "End index", match.end())
        dig_l = match.start()
        dig_r = match.end() - 1

        cu_sum += check_adj(match,j,dig_l, dig_r)
            
    j +=1

print(f"The engine code is {cu_sum}")

# part 2 - gear ratio
# Idea is to make a dict of all the gears around each number, then reverse the keys and values 

digit_gear_dict = {}

def check_gear(digit_gear_dict,match,j,dig_l, dig_r):
    gear_loc = []
    for h, v in adj:
        for ind in [dig_l, dig_r]:
            try:
                # print("Adjacent ch -"+ in_array[j+v][ind+h])
                if re.findall(r"\*", in_array[j+v][ind+h]):
                    # print(re.findall(r"\*", in_array[j+v][ind+h]))
                    gear_loc.append(str(j+v) + "_"+ str(ind+h))
            except:
                pass
    digit_gear_dict[match.group() + "_"+str(j)+ "_" + str(dig_l)] = set(gear_loc)

j= 0
for line in in_lines:
    for match in re.finditer(r'\d+', line):
        print("match", match.group(), "start index", match.start(), "End index", match.end())
        dig_l = match.start()
        dig_r = match.end() - 1

        check_gear(digit_gear_dict,match,j,dig_l, dig_r)
            
    j +=1


dict_gear_ratio = {}

for dig, gears in digit_gear_dict.items():
    for gear in gears:
        if gear in dict_gear_ratio.keys():
            dict_gear_ratio[gear].append(dig.split("_")[0])
        else:
            dict_gear_ratio[gear] = [dig.split("_")[0]]
    pass

gear_ratio_cu_sum = 0
for vals in dict_gear_ratio.values():
    if len(vals) == 2:
        gear_ratio = int(vals[0]) * int(vals[1])
    elif len (vals) == 1:
        gear_ratio = 0
    else:
        print(f"The adjacent to gears are {len(vals)} numbers")
    
    gear_ratio_cu_sum += gear_ratio

print(gear_ratio_cu_sum)

