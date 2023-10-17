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

def blackjack(shoe):
    while len(shoe) != 0:
        player_hand = []
        dealer_hand = []

        


while True:
    try:
        player_input = int(input("How many Decks Would you like to play with? \n"))
        break
    except ValueError:
        print("That is not a valid entry Please Try Again! \n")

counter = 0
shoe =  []

while counter <= player_input:
    cards = build_deck()
    for x in cards:
        shoe.append(x)
    shuffle(shoe)
    counter += 1

for x in shoe:
    print (x)

