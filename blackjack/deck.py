""" This class represents a deck of Card objects.  It will have methods to fill
itself with a traditional 52 card set, deal cards, and shuffle itself. """

import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []

    def __str__(self):
        return f'Deck object containing {len(self.cards)} cards'

    def __getitem__(self, index):
        return self.cards[index]

    def fill(self, number):
        for i in range(number):
            for suit in Card.suits:
                for value in Card.values:
                    self.cards.append(Card(value, suit))

    def deal(self, number):
        cards = []
        for i in range(number):
            cards.append(self.cards[0])
            del self.cards[0]
        return cards

    def shuffle(self):
        random.shuffle(self.cards)
