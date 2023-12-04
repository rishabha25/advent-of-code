import re

j=0

original_l = []
winning_l = []
my_l = []

cu_sum_card_power = 0 

# Part 1
with open("2023/Day4/input.txt") as file:
    for line in file:    
        winning_l.append(re.split(r":|\|",line.rstrip())[1].strip().split() )
        my_l.append(re.split(r":|\|",line.rstrip())[2].strip().split() )

        card_match = 0
        for my_num in my_l[j]:
            if my_num in winning_l[j]:
                card_match += 1
        if card_match > 0:
            card_power = 2**(card_match-1)
        else:
            card_power = 0
        
        cu_sum_card_power += card_power
    

        j +=1

print (my_l[0])
print(f"The total sum of card pile scores is: {cu_sum_card_power}")

# Part 2
# Use Recursion
# Dict to keep track of numbers of copies

dict_count_cards = dict([(i+1, 1) for i in range(len(winning_l))])

def process_card(card):
    card_match = 0
    for my_num in my_l[card-1]:
        if my_num in winning_l[card-1]:
            card_match += 1
    
    for i in range(card_match):
        dict_count_cards[card+i+1] = dict_count_cards[card+i+1]+1
        process_card(card+i+1)

    return

for i in range(len(my_l)):
    process_card(i+1)
                

print(sum(dict_count_cards.values()))