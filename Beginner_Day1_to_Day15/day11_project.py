import resource.blackjack
import random

# create a list of cards in a deck
deck_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King",
             "Ace"]
score_replacement = {"Jack": 10,
                     "Queen": 10,
                     "King": 10,
                     "Ace": 11}

# function to add a card into a hand of choice
def deal_card(hand:list):
    """This function adds a card into a player's hand"""
    hand.append(random.choice(deck_list))

def convert_hand(hand:list):
    """This function changes all the picture cards into their respective scoring
    Jack, Queen, King will count as 10"""
    #loop through the hand list
    for i in range(len(hand)):
        if hand[i] in score_replacement:
            hand[i] = score_replacement[hand[i]]


def make_decision(player_hand:list, dealer_hand:list):
    """This function checks compares the sum of both hands
    If both exceed 21 = draw
    If one hand exceed 21 while the other is within = hand with < 21 wins
    If both within 21 = higher hand wins
    """
    if sum(player_hand) > 21 and sum(dealer_hand) > 21:
        print(f"Both players exceeded 21, it's a draw.")
    elif sum(player_hand) > 21:
        print(f"You exceeded 21, You lose :(")
    elif sum(dealer_hand) > 21:
        print(f"Computer exceeded 21. You win!!")
    elif sum(player_hand) > sum(dealer_hand):
        print(f'You win!')
    else:
        print(f'You lose :(')

def play_black_jack():
    # question to initiate the game
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ")
    if start_game == 'y':
        game_loop = True
        print(resource.blackjack.logo)

    # create starting hands
    player_hand = []
    dealer_hand = []
    # deal 2 cards into player and dealer hand
    for card in range(2):
        deal_card(player_hand)
        deal_card(dealer_hand)

    continue_game = True
    while continue_game:
        # displays current hand and dealer's first card
        print(f'Your cards: {player_hand}')
        print(f"Dealer's first card: {dealer_hand[0]}")
        # check with player if they want to draw
        draw_another_card = input(f"Type 'y' to get another card or 'n' to see who wins ")
        # if user selects no
        if draw_another_card == 'n':
            print('\n') # to separate the phases of the game
            # converts both hands to numbers
            convert_hand(dealer_hand)
            convert_hand(player_hand)
            # dealer has to draw one more card if the score is less than 17
            while sum(dealer_hand) < 17:
                deal_card(dealer_hand)
                convert_hand(dealer_hand)

            print(f'Your cards: {player_hand}. Total score is {sum(player_hand)}.')
            print(f"Dealer's first card: {dealer_hand}. Total score is {sum(dealer_hand)}.")
            make_decision(player_hand, dealer_hand)
            continue_game = False
            play_black_jack() #calls the function again to restart
            print('\n' * 20)
        else:
            print('\n')
            deal_card(player_hand)

# starts the game for the 1st time, recursion is built into the function
play_black_jack()
