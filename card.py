class Card:
    def __init__(self, suit, char):
        self.suit = suit
        self.char = char

    def display(self):
        if self.char == 1:
            print("A of", self.suit)
        elif self.char == 11:
            print("J of", self.suit)
        elif self.char == 12:
            print("Q of", self.suit)
        elif self.char == 13:
            print("K of", self.suit)
        else:
            print(self.char, "of", self.suit)

    def show_char(self):
        return self.char