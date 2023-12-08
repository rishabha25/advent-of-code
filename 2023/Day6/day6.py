import re
import math

with open("2023/Day6/input.txt") as file:
    lines = file.readlines()

times = lines[0].split()[1:]
times = [int(x) for x in times]

dist = lines[1].split()[1:]
dist = [int(x) for x in dist]
winning_ways = []


record_beat = 1
for i in range(len(times)):
    race_win = 0
    for x in range(1,times[i]):
        print(x)
        if (times[i]*x - x*x) > dist[i]:
            race_win += 1
    record_beat *= race_win
    # break

print(f"Record beat {record_beat}")

# Part 2
# Equation is x*x - Tx  + D
#  a = 1, b=-T, c=D
time_act = int("".join(lines[0].split()[1:]))
dest_act = int("".join(lines[1].split()[1:]))

# print(f"Sqrt {time_act*time_act - (4*1*dest_act)}")

root1 = math.floor( (time_act+ math.sqrt(time_act*time_act - (4*1*dest_act)))/2)

root2 = math.ceil( (time_act - math.sqrt(time_act*time_act - (4*1*dest_act)))/2)

print(f"Part 2: {root1 - root2 + 1}")