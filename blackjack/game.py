""" this is the actual blackjack game """

from deck import Deck
from card import Card

def main():
    dealer_deck = Deck()
    dealer_deck.fill(7)
    dealer_deck.shuffle()

    dealer_hand = Deck()
    dealer_hand.cards = dealer_deck.deal(2)

    player_hand = Deck()
    player_hand.cards = dealer_deck.deal(2)

    print(f'The dealer is showing a {dealer_hand[0]}')
    print('You have the following cards:')
    for card in player_hand.cards:
        print(card)

if __name__ == '__main__':
    main()
