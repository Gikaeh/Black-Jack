def check_if_hit_or_stand(player, dealer, deck):
    choice = input("Would you like to hit or stand: ")
    print("==========================================")
    while choice.lower() == "hit":
        player.hand.add_card(deck.draw_card())
        player.show_hand()
        print("*******", dealer.name, "*******")
        dealer.hand.cards[0].display()
        if player.hand.total_count() > 21:
            print("You have lost by going over 21.")
            break
        choice = input("Would you like to hit or stand: ")
        print("==========================================")

    if choice.lower() == "stand":
        player.show_hand()
        dealer.show_hand()
        print("==========================================")
        check_dealer_17(player, dealer, deck)


def check_dealer_17(player, dealer, deck):
    if dealer.hand.total_count() < 17:
        while dealer.hand.total_count() < 17:
            dealer.hand.add_card(deck.draw_card())
            player.show_hand()
            dealer.show_hand()
            check_winner(player, dealer)
        action = "hit"
        return action
    check_winner(player, dealer)
    action = "stand"
    return action


def check_winner(player, dealer):
    if player.hand.total_count() > 21:
        print("You have lost by going over 21.")
        return player.name
    if dealer.hand.total_count() > 21:
        print(player.name, "you win, dealer went over 21.")
        return player.name
    elif player.hand.total_count() > dealer.hand.total_count():
        print(player.name, "you win, dealer had", dealer.hand.total_count(), "vs your", player.hand.total_count())
        return player.name
    elif dealer.hand.total_count() == player.hand.total_count():
        print(player.name, "you tied with the dealer with", player.hand.total_count(), ". Dealer wins")
        return dealer.name
    else:
        print(player.name, "you lose, dealer had", dealer.hand.total_count(), "vs your", player.hand.total_count())
        return dealer.name
