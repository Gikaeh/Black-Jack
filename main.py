from person import Person
from deck import Deck
import game


def main():
    play = "yes"
    name = input("--------Hello welcome to blackjack-------- \nWhat is your name? \n")
    
    while play.lower() == "yes":
        player = Person(name, True)
        dealer = Person("Dealer", False)
        deck = Deck()
        
        for i in range(2):
            player.hand.add_card(deck.draw_card())
            dealer.hand.add_card(deck.draw_card())
        player.show_hand()
        print("*******", dealer.name, "*******")
        dealer.hand.cards[0].display()
        game.check_if_hit_or_stand(player, dealer, deck)
        play = input("Would you like to continue playing; Yes or No: ")
        print("==========================================")


if __name__ == "__main__":
    main()
