from random import shuffle
from main import Card
from main import build_deck

values = ['Jack', 'Queen', 'King']

def change_value(deck):
    for x in deck:
        if x.value == "Ace":
            x.value = 11
        elif x.value == "Jack":
            x.value = 10
        elif x.value == "Queen":
            x.value = 10
        elif x.value == "King":
            x.value = 10

def win_condition(player_hand, dealer_hand):
    player_hand_value = []
    dealer_hand_value = []

    for x in player_hand:
        player_hand_value.append(x.value)
    for x in dealer_hand:
        dealer_hand_value.append(x.value)
    
    if sum(player_hand_value) <= 21 and sum(dealer_hand_value) != 21:
        print("You have won")
    else:
        print("You have lost!")

def deal(deck):
    hand = []
    for x in range(2):
        hand.append(deck[0])
        deck.pop(0)
    return hand

def hit (hand,shoe):
    hand.append(shoe[0])
    shoe.pop(0)
    hand_value = []
    for x in hand:
        hand_value.append(x.value)
    while sum(hand_value) < 21:
        player_input = input("Your current total is %s. Would you like to hit (h) or stay (s)?\n"% sum(hand_value)) 
        if player_input.lower() == "h":
            hand.append(shoe[0])
            hand_value.append(hand[len(hand) - 1])
            shoe.pop(0)
        elif player_input.lower() ==  "s":
            break


deck = build_deck()
shuffle(deck)

player_hand = deal(deck)
dealer_hand = deal(deck)

change_value(player_hand)
change_value(dealer_hand)

hand_value = []
for x in player_hand:
    hand_value.append(x.value)

player_input = input("Your current hand is %s, Would you like to Hit (h)? \n" %sum(hand_value))

if player_input.lower() == "h":
    hit(player_hand, deck)
    win_condition(player_hand, dealer_hand)
else:
    win_condition(player_hand, dealer_hand)
