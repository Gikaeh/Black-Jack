import unittest
from person import Person
from card import Card
from deck import Deck
from hand import Hand
import game


class TestGameFunctions(unittest.TestCase):
    def setUp(self):
        self.player = Person("Ethan", True)
        self.dealer = Person("Dealer", False)
        self.deck = Deck()

        self.blackjack_hand = Hand([Card("Hearts", 13), Card("Hearts", 1)])
        self.losing_hand = Hand([Card("Hearts", 2), Card("Hearts", 3)])
        self.winning_hand = Hand([Card("Hearts", 13), Card("Hearts", 12)])
        self.bust_hand = Hand([Card("Hearts", 13), Card("Hearts", 12), Card("Hearts", 11)])
        self.above_17 = Hand([Card("Hearts", 13), Card("Hearts", 7)])
        self.below_17 = Hand([Card("Hearts", 13), Card("Hearts", 2)])

    def test_if_hand_is_bust(self):
        self.player.hand = self.bust_hand
        self.assertFalse(self.player.hand.total_count() < 21)

        self.player.hand = self.blackjack_hand
        self.assertTrue(self.player.hand.total_count() <= 21)

    def test_player_wins(self):
        self.player.hand = self.winning_hand
        self.dealer.hand = self.losing_hand
        self.assertEqual(self.player.name, game.check_winner(self.player, self.dealer))

    def test_dealer_wins(self):
        self.player.hand = self.losing_hand
        self.dealer.hand = self.winning_hand
        self.assertEqual(self.dealer.name, game.check_winner(self.player, self.dealer))

    def test_tie(self):
        self.player.hand = self.blackjack_hand
        self.dealer.hand = self.blackjack_hand
        self.assertEqual(self.dealer.name, game.check_winner(self.player, self.dealer))

    def test_bank_17_rule(self):
        self.dealer.hand = self.below_17
        self.player.hand = self.above_17
        self.assertEqual("hit", game.check_dealer_17(self.player, self.dealer, self.deck))

        self.dealer.hand = self.above_17
        self.player.hand = self.above_17
        self.assertEqual("stand", game.check_dealer_17(self.player, self.dealer, self.deck))

if __name__ == '__main__':
    unittest.main()
