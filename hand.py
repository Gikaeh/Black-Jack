from card import Card
from deck import Deck


class Hand:
    def __init__(self, cards=None):
        if cards:
            self.cards = cards
        else:
            self.cards = []
        self.total = 0

    def total_count(self):
        total_hold = 0
        try:
            ace_index = self.cards.index(1)
        except ValueError:
            ace_index = -1
        if ace_index != -1:
            self.cards.append(self.cards.pop(self.cards.index(1)))
        for card in self.cards:
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

    def add_card(self, card):
        self.cards.append(card)
        self.total_count()
