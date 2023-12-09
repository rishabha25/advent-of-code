with open("2023/Day9/input.txt") as file:
    lines = file.readlines()

next_vals = []
first_vals = []

def inner(p_list):
    inner_list = []
    for i in range(len(p_list) - 1):
        inner_list.append( (p_list[i+1] - p_list[i]) )
    
    end_cond = not(any(inner_list)) or (len(inner_list) <= 1)
    return (inner_list, end_cond)

for line in lines:
    temp_list = []
    print(line.split())
    temp_list.append( [int(x) for x in line.split()] )
    
    end_cond = False
    i = 0
    
    while not end_cond:
    # for i in range(len(temp_list[0]) -1):
        inner_list, end_cond = inner(temp_list[i])
    
        temp_list.append(inner_list)
        i += 1
    print(f"Temp list is {temp_list} \n")
    
    temp_n_val = 0
    
    # Part A
    for lis in temp_list:
        temp_n_val += lis[-1]
    next_vals.append(temp_n_val)

    # Part B
    temp_f_val = 0
    count = 0
    for lis in temp_list:
        temp_f_val += (lis[0] * (-1)**count)
        count += 1
    first_vals.append(temp_f_val)


print(f"The next values are {next_vals} and their sum is {sum(next_vals)}")

print(f"The first values are {first_vals} and their sum is {sum(first_vals)}")