### Fake black jack for fun. Not much here sadly

#begin source code

from random import shuffle


class Card:
    def __init__(self, value, color ):
        self.value = value
        self.color = color

    def __str__(self):
        return f"{self.value} of {self.color}"

def build_deck(): 
    colors = ['hearts', 'diamonds', 'spades', 'clubs']
    values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
    deck = [Card(value, color) for value in values for color in colors]
    return deck

def check_win(player_hand, dealer_hand, bet):
    if sum(player_hand) == 21 and sum(dealer_hand) != 21:
        print("You have a Blackjack and have won %s!" %(bet * (3/2)))
    elif sum(dealer_hand) == 21 and sum(player_hand) != 21:
        print("The dealear has a Blackjack. Unfortunatly you have Lost.")

def game(shoe):
    while len(shoe) != 0:
        try:
            bet = int(input("Place your bet now: "))
            if bet < 25 or bet > 1000:
                print("I am sorry but the minimum at this table is 25 and the max is 1000!\n")
                break
        except ValueError:
            print("That is not a vaild bet. Try Agian! \n")
        player_hand = []
        dealer_hand = []

        for x in range(2):
            player_hand.append(shoe[0])
            shoe.pop(0)
            dealer_hand.append(shoe[0])
            shoe.pop(0)



