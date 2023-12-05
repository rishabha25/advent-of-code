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
