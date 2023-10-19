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

deck = build_deck()
shuffle(deck)

player_hand = deal(deck)
dealer_hand = deal(deck)

for x in player_hand:
    print(x)

for x in dealer_hand:
    print(x)

change_value(player_hand)
change_value(dealer_hand)

win_condition(player_hand, dealer_hand)
