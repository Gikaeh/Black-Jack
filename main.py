from person import Person
from deck import Deck
from card import Card

def main():
    play = "yes"
    name = input("Hello welcome to blackjack. What is your name?\n")
    
    while play.lower() == "yes":
        player = Person(name, True)
        dealer = Person("Dealer", False)
        deck = Deck()
        
        for i in range(2):
            player.add_card(deck.draw_card())
            dealer.add_card(deck.draw_card())
        player.show_hand()
        print("This is", dealer.name, "hand:")
        dealer.hand[0].display()
        choice = input("Would you like to hit or stand: ")
        
        while choice.lower() == "hit":
            player.add_card(deck.draw_card())
            player.show_hand()
            print("This is", dealer.name, "hand:")
            dealer.hand[0].display()
            if player.total_count() > 21:
                print("You have lost by going over 21.")
                break
            choice = input("Would you like to hit or stand: ")
        
        if choice.lower() == "stand":
            player.show_hand()
            dealer.show_hand()
            while dealer.total_count() < 17:
                dealer.add_card(deck.draw_card())
                player.show_hand()
                dealer.show_hand()
            if dealer.total_count() > 21:
                print(player.name, "you win, dealer went over 21.")
            elif dealer.total_count() < player.total_count():
                print(player.name, "you win, dealer had", dealer.total_count(), "vs your", player.total_count())
            elif dealer.total_count() == player.total_count():
                print(player.name, "you tied with the dealer with", player.total_count())
            else:
                print(player.name, "you lose, dealer had", dealer.total_count(), "vs your", player.total_count())
        play = input("Would you like to continue playing; Yes or No: ")

if __name__=="__main__":
    main()