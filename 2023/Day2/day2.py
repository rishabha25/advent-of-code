import re

f = open("2023/Day2/input.txt", "r")
calibration_l = []
lines = f.readlines()

# Parse data to make dictionary of list of dictonaries

games_dict = {}

def parse(game):
    colours = ('red', 'blue', 'green')
    temp_dict = dict()

    for colour in colours:
        exp = r"(\d+) " + colour
        balls = re.findall(exp, game)
        if balls:
            temp_dict[colour] = int(balls[0])
        else:
            temp_dict[colour] = 0

    return temp_dict

i = 1
output_sum = 0
for line in lines:
    games = line.split(';')
    draws = []
    print(games)
    print(re.findall(r"Game (\d+)", games[0])[0])
    
    draws = [ parse(game) for game in games]

    games_dict[re.findall(r"Game (\d+)", games[0])[0]] = draws

    max_balls = dict()

    colours = ('red', 'blue', 'green')
    ball_capacity = {'red': 12, 'green':13, 'blue':14}
    for colour in colours:
        max_balls[colour] = max([ draw[colour] for draw in draws])

    print(max_balls)

    # Check for 12 red cubes, 13 green cubes, and 14 blue
    if (max_balls['red'] <= 12) and (max_balls['green'] <= 13) and (max_balls['blue'] <= 14):
        output_sum += i
    
    i += 1

    print(f"Sum of IDs {output_sum}")




    
    
