import re

f = open("2023/Day3/input.txt", "r")
# lines = f.readlines()

in_array = [ [ch for ch in line.strip()] for line in f.readlines()]

in_lines = [ "".join(line) for line in in_array]

# print(in_lines[1])
# print(in_array[0][138])



# print(re.findall(r"[^\d\.]", in_lines[1]))


# all_numbers = list()

# for line in in_lines:
#     all_numbers.extend(re.findall(r"[\d]+", line) )

# print(max([len(num) for num in all_numbers]))

def check_adj(match, j, dig_l, dig_r):
    for h, v in adj:
        for ind in [dig_l, dig_r]:
            try:
                print("Adjacent ch -"+ in_array[j+v][ind+h])
                if re.findall(r"[^\d\.]", in_array[j+v][ind+h]):
                    print(match.group())
                    return int(match.group())
            except:
                pass
    return 0


adj = [(0,1),(-1,1), (-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1)]
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

# for i in len(in_array):
#     dig_index_l = 0
#     for j in len(in_array):
#         if in_array[i][j].isdigit():
#             dig_index_l = j
#             dig_index_r = j
#             while(in_array[i][dig_index_r].isdigit()):
#                 dig_index_r += 1