import re
import os

# print(os.getcwd())


f = open("2023/Day1/input.txt", "r")

calibration_l = []

lines = f.readlines()

# lines = ['gsdf1fasoneightsdasm4', 'asfasf3nnv4f']

num_mapping = {'one':1,
              'two':2,
              'three':3,
              'four':4,
              'five':5,
              'six':6,
              'seven':7,
              'eight':8,
              'nine':9}

i=0
cu_sum = 0
for line in lines:

    calibration_l.append(re.findall( r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line))
    left = calibration_l[i][0] if calibration_l[i][0].isdigit() else num_mapping[calibration_l[i][0]]

    right = calibration_l[i][-1] if calibration_l[i][-1].isdigit() else num_mapping[calibration_l[i][-1]]


    cu_sum += int(left)*10 + int(right)

    i += 1
    
print(f"Cumulativve sum is {cu_sum}")


