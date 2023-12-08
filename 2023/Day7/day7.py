import re
from collections import Counter
import numpy as np


with open("2023/Day7/input.txt") as file:
    lines = file.readlines()

val_map_1 = {'2':'02' , '3':'03', '4':'04', '5':'05', 
               '6':'06', '7':'07', '8':'08', '9':'09', 'T':'10', 
               'J':'11', 'Q':'12', 'K':'13', 'A':'14'}

def check_card_type(card_dict):
    
    card_sets = sorted(list(card_dict.values()),  reverse=True)

    if card_sets == [1,1,1,1,1]:
        card_dict['Type'] = '1'
        print('High Card')
    elif card_sets == [2,1,1,1]:
        card_dict['Type'] = '2'
        print('One Pair')
    elif card_sets == [2,2,1]:
        card_dict['Type'] = '3'
        print('Two Pair')
    elif card_sets == [3,1,1]:
        card_dict['Type'] = '4'
        print('Three of a kind')
    elif card_sets == [3,2]:
        card_dict['Type'] = '5'
        print('Full House')
    elif card_sets == [4,1]:
        card_dict['Type'] = '6'
        print('Four of a kind')
    elif card_sets == [5]:
        card_dict['Type'] = '7'
        print('Five of a kind')
    else:
        print('None')
    return card_dict

def parser(check_card_type, val_map):
    hand_strength = []
    bids = []

    for line in lines:
        print((line.split()[0]))
        temp_dict = Counter(line.split()[0])
        temp_dict = check_card_type(temp_dict)
        temp_dict['Cards'] = line.split()[0].strip()
        temp_dict['Bid'] = int(line.split()[1].strip())

        val_str = temp_dict['Type']

        for card in temp_dict['Cards']:
            # print(val_map[card])
            val_str += val_map[card]
        
        # print(f"Value of string is" +  val_str)
        hand_strength.append(int(val_str))
        bids.append(temp_dict['Bid'])
        # print(temp_dict)
        # break
    # argsort
    print(f"Hand Strength {hand_strength} \n")

    sorted_index = np.argsort(hand_strength)

    print(f"Hand Strength Sorted index {sorted_index} \n")

    cu_sum = 0
    for rank in range(len(sorted_index)):
        rank + 1
        print(f"Rank is {rank+1} and bid is {bids[sorted_index[rank]]}")
        cu_sum += (rank+1) * bids[sorted_index[rank]]
        # print(cu_sum)
    print(f"Cumulative Sum is {cu_sum}")
    return cu_sum

print(f"Part 1 answer {parser(check_card_type, val_map_1)} \n\n")



# Part 2

val_map_2 = {'2':'02' , '3':'03', '4':'04', '5':'05', 
               '6':'06', '7':'07', '8':'08', '9':'09', 'T':'10', 
               'J':'01', 'Q':'12', 'K':'13', 'A':'14'}

def check_card_type_2(card_dict):
    
    card_sets = sorted(list(card_dict.values()),  reverse=True)

    if card_dict.get('J', 0) and (card_dict.get('J', 0) != 5) :
        count_j = card_dict['J']
        del card_dict['J']
        card_sets.remove(count_j)
        card_sets[0] = card_sets[0] + count_j

    if card_sets == [1,1,1,1,1]:
        card_dict['Type'] = '1'
        print('High Card')
    elif card_sets == [2,1,1,1]:
        card_dict['Type'] = '2'
        print('One Pair')
    elif card_sets == [2,2,1]:
        card_dict['Type'] = '3'
        print('Two Pair')
    elif card_sets == [3,1,1]:
        card_dict['Type'] = '4'
        print('Three of a kind')
    elif card_sets == [3,2]:
        card_dict['Type'] = '5'
        print('Full House')
    elif card_sets == [4,1]:
        card_dict['Type'] = '6'
        print('Four of a kind')
    elif card_sets == [5]:
        card_dict['Type'] = '7'
        print('Five of a kind')
    else:
        print('None')
    return card_dict

print(f"Part 2 answer {parser(check_card_type_2, val_map_2  )}")