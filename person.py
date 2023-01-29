from card import Card
from deck import Deck

class Person:
    def __init__(self, name, player):
        self.name = name
        self.player = player
        self.hand = []
        self.total = 0
    
    def add_card(self, card):
        self.hand.append(card)
        self.total_count()

    def show_hand(self):
        print("This is", self.name, "hand:")
        for card in self.hand:
            card.display()            

    def total_count(self):
        total_hold = 0
        for A in self.hand:
            if A.char == 1:
                self.hand.append(self.hand.pop(self.hand.index(1)))
            else:
                break
        for card in self.hand:
            if card.char == 11 or card.char == 12 or card.char == 13:
                total_hold += 10
            elif card.char == 1:
                if total_hold < 11:
                    total_hold += 11
                else:
                    total_hold += 1
            else:
                total_hold += card.char
        
        self.total = total_hold
        return self.total