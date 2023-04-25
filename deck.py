import random
from card import Card


class Deck:
    def __init__(self):
        self.cards = []
        self.deck()
    
    def deck(self):
        for suit in ["Clubs", "Spades", "Hearts", "Diamonds"]:
            for char in range(1, 14):
                self.cards.append(Card(suit, char))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()