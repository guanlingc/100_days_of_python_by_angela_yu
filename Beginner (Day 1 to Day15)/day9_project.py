# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import resource.gavel_art as art
import os
print(art.logo)
print(f'Welcome to the secret auction program.')

# Creates empty dict outside the loop to save the information while looping
bidding_list = {}
# Condition statement for a while loop
continue_bid = True
# Loop while condition is true
while continue_bid:
    #ask for name, bid and other bidders
    name = input('What is your name?: ')
    bid = int(input('What is your bid?: $ '))
    other_bidders = input('Are there any other bidders? Type "yes" or "no \n').lower()
    bidding_list[name] = bid
    # print(bidding_list)

    if other_bidders == "no":
        continue_bid = False
    else:
        # print('\n'* 20)
        os.system('clear')

# input phase ends
os.system('clear')
winning_bid = 0
winner = ""
for key in bidding_list:
    if bidding_list[key] > winning_bid:
        winning_bid = bidding_list[key]
        winner = key

# instructor solution
# print(max(bidding_list))

print(f'The winner is {winner} with a winning bid of ${winning_bid}')
