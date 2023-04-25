from card import Card
from deck import Deck
from hand import Hand


class Person:
    def __init__(self, name, player):
        self.name = name
        self.player = player
        self.hand = Hand()

    def show_hand(self):
        print("*******", self.name, "*******")
        for card in self.hand.cards:
            card.display()


