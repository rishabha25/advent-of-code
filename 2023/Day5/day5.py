import re

with open("2023/Day5/input.txt") as file:
    input = file.readlines()

input_joined = "".join(line for line in input)

mappings = []

for split in input_joined.split("\n\n"):
    mappings.append(split.split(":")[1].strip())

# C1 column 1 name and c2 column 2 name
def check_mapping(maps, input_source):

    # Process one line mapping at a time
    for line in maps.split("\n"):
        dest, source, r =  line.strip().split(" ")

        dest = int(dest)
        source = int(source)
        r = int(r)

        if input_source in range(source, source+r,1):
            destin = dest+input_source-source
            return destin
    return input_source


# Make dataframe for all the mappings
low_loc = 1852510996
for seed in mappings[0].strip().split(" "):
    print(f"Seed is - {seed}")
    print(f"Number of seeps is {len(mappings[0].strip().split(' '))}")

    out_1 = check_mapping(mappings[1], int(seed))
    out_2 = check_mapping(mappings[2], out_1)
    out_3 = check_mapping(mappings[3], out_2)
    out_4 = check_mapping(mappings[4], out_3)
    out_5 = check_mapping(mappings[5], out_4)
    out_6 = check_mapping(mappings[6], out_5)
    out_7 = check_mapping(mappings[7], out_6)
    print(f"For seed {seed}, type is {type(seed)} the location is {out_7}")

    low_loc = min(low_loc, out_7)

# print(f"Lowest location is {low_loc}")

# out_1 = check_mapping(mappings[1], 2041142901)
# out_2 = check_mapping(mappings[2], out_1)
# out_3 = check_mapping(mappings[3], out_2)
# out_4 = check_mapping(mappings[4], out_3)
# out_5 = check_mapping(mappings[5], out_4)
# out_6 = check_mapping(mappings[6], out_5)
# out_7 = check_mapping(mappings[7], out_6)

print(low_loc)


# Part 2
# Need to treate inputs as set. mappings are linear increasing. So just need to check the minimum of intersection of location
# Range of humidity inputs, do intersection of each with humidity mapping range and take minimum

# Hypothesis lowest location has to be at the edges of input - wrong
# Find all the deicision points of intervals and make sets of those

# Seeds

for line in mappings[7].split("\n"):
    dest, source, r =  line.strip().split(" ")
    source


def intersection(input_range, mapping_range,interval_ranges):

    comm_l, comm_r = max(input_range[0], mapping_range[0]), min(input_range[1], mapping_range[1])

    if comm_l <= comm_r:
        # Remove older interval range
        interval_ranges.remove(input_range)
        # case 1 input is left to the mapping range
        if comm_l > input_range[0]:
            interval_ranges.append((input_range[0], comm_l))
            interval_ranges.append((comm_l, comm_r))



seeds = mappings[0].strip().split(" ")
seeds = list(map(int, seeds))
print(f"Lenght : {len(seeds)}")

interval_ranges = []

low_loc = 1852510996421424
for i in range(int(len(seeds)/2)):
    #upper and lower end of interval
    int_low, int_high = seeds[2*i] , seeds[2*i] + seeds[2*i+1] - 1
    print(f"Lower bound: {int_low}, Higher bound: {int_high}")
    int_ranges.append((int_low, int_high))
    for seed in [int_low, int_high]:
        pass
        # out_1 = check_mapping(mappings[1], int(seed))
        # out_2 = check_mapping(mappings[2], out_1)
        # out_3 = check_mapping(mappings[3], out_2)
        # out_4 = check_mapping(mappings[4], out_3)
        # out_5 = check_mapping(mappings[5], out_4)
        # out_6 = check_mapping(mappings[6], out_5)
        # out_7 = check_mapping(mappings[7], out_6)
        # print(f"For seed {seed}, type is {type(seed)} the location is {out_7}")

        # low_loc = min(low_loc, out_7)
print(f"Seed ranges {int_ranges}")