""" this file tests the game functions to see if they work correctly """

import unittest
import game
import game_2
from deck import Deck
from card import Card

class TestBasicGame(unittest.TestCase):

    def test_point_counting(self):
        my_hand = Deck()
        my_hand.cards = [Card('2', 'hearts'), Card('3', 'hearts')]
        total = game.get_hand_points(my_hand)
        self.assertEqual(total, 5)

    def test_A_point_counting(self):
        my_hand = Deck()
        my_hand.cards = [Card('A', 'hearts'), Card('3', 'hearts')]
        total = game.get_hand_points(my_hand)
        self.assertEqual(total, 14)

    def test_double_A_point_counting(self):
        my_hand = Deck()
        my_hand.cards = [Card('A', 'diamonds'),
                         Card('A', 'hearts'),
                         Card('3', 'hearts')]
        total = game.get_hand_points(my_hand)
        self.assertEqual(total, 15)

    def test_A_over_21_counting(self):
        my_hand = Deck()
        my_hand.cards = [Card('A', 'diamonds'),
                         Card('10', 'spades'),
                         Card('A', 'hearts'),
                         Card('3', 'hearts')]
        total = game.get_hand_points(my_hand)
        self.assertEqual(total, 15)

    def test_A_at_21_counting(self):
        my_hand = Deck()
        my_hand.cards = [Card('A', 'diamonds'),
                         Card('9', 'spades'),
                         Card('A', 'hearts')]
        total = game.get_hand_points(my_hand)
        self.assertEqual(total, 21)

class TestPlayerInteraction(unittest.TestCase):

    """
    testing the following things:
    * if player 1 busts, player 2 goes next
    * player 1 interaction happens before player 2
    * scoring at the end makes sense
    """

    def test_setup_cards(self):
        number = 2
        dealer, players = game_2.setup_cards(number)
        self.assertIsInstance(dealer, Deck)
        self.assertIsInstance(players, list)
        self.assertIsInstance(players[0], Deck)



if __name__ == '__main__':
    unittest.main()
