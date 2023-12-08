import math
import re

with open("2023/Day8/input.txt") as file:
    lines = file.readlines()

dir = lines[0].strip()

steps = 0

dir_mapping = {'L':0, 'R':1}

mapping = {}

for line in lines[2:]:
    s, dest = line.split("=")[0].strip(), tuple(line.split("=")[1].strip().strip('(').strip(')').split(", "))
    mapping[s] = dest

source = 'AAA'
print(mapping)
while 1:
    for direction in dir:
        source = mapping[source][dir_mapping[direction]]
        print(f"Locaton {source}")
        steps += 1
        if source == 'ZZZ':
            break
    if source == 'ZZZ':
        break

print(f"Total steps taken {steps}")


# Part 2 take LCM of all the individual steps

# math.lcm()


origin = [ x for x in list(mapping.keys()) if re.findall(r"..A", x)]

# store steps for reaching dest for each source
step_list = []
for s in origin:
    steps = 0
    while 1:
        for direction in dir:
            s = mapping[s][dir_mapping[direction]]
            print(f"Location {s}")
            steps += 1
            if re.findall(r"..Z", s):
                break
        if re.findall(r"..Z", s):
            step_list.append(steps)
            break    

print(f'The steps for 6 origins are {step_list}\n')
print(math.lcm(*step_list))

