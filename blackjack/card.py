""" This class represents a single playing card from a French Deck (the type
most Americans are familiar with).  It will know what valid values and suits
are, and be able to calculate how many points it is worth.  If there's time,
it may have a validator that confirms you're not trying to make a Duke of
Donuts card. """

class CardValueError(Exception):
    """ this is what gets thrown when you give me the wrong value """

class CardSuitError(Exception):
    """ this is what gets thrown when you give me the wrong suit """

class Card:
    values = [str(i) for i in range(2, 11)]
    values.extend('JQKA')
    suits = ['hearts', 'clubs', 'spades', 'diamonds']
    point_values = {'J': 10, 'Q': 10, 'K': 10, 'A': (1, 11)}

    def __init__(self, value, suit):
        self.value = value # always a string
        self.suit = suit
        self._validate()

    def __repr__(self):
        return f"Card('{self.value}', '{self.suit}')"

    def __str__(self):
        return f'{self.value} of {self.suit}'

    def points(self):
        try:
            return int(self.value)
        except ValueError:
            return self.point_values[self.value]

    def _validate(self):
        """ check to make sure that the card is valid """
        if self.value not in self.values:
            raise CardValueError(f'Card value "{self.value}" is not valid')
        if self.suit not in self.suits:
            raise CardSuitError(f'Card suit "{self.suit}" is not valid; choose from {self.suits}')
