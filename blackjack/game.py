""" this is the actual blackjack game """

from deck import Deck
from card import Card

def show_cards(hand):
    for card in hand.cards:
        print(card)
    value = get_hand_points(hand)
    print(f'Worth {value} points')


def show_player_cards(player_hand):
    """ tell the player what cards they have """
    print('You have the following cards:')
    show_cards(player_hand)


def show_dealer_cards(dealer_hand):
    """ tell the player what cards they have """
    print('The dealer has the following cards:')
    show_cards(dealer_hand)


def get_hand_points(hand):
    """ add up the points in a hand, assuming that we don't want
    to break 21 if possible (when deciding whether an A is worth 1
    or 11) """
    total = 0
    aces = 0
    for card in hand.cards:
        if card.value == 'A':
            aces += 1
        else:
            total += card.points()

    for _ in range(aces):
        if total + 11 > 21:
            total += 1
        else:
            total += 11
    return total


def hit(dealer_deck, hand):
    hand.cards.extend(dealer_deck.deal(1))


def main():
    dealer_deck = Deck()
    dealer_deck.fill(7)
    dealer_deck.shuffle()

    dealer_hand = Deck()
    dealer_hand.cards = dealer_deck.deal(2)

    player_hand = Deck()
    player_hand.cards = dealer_deck.deal(2)

    print(f'The dealer is showing a {dealer_hand[0]}')
    show_player_cards(player_hand)
    player_points = get_hand_points(player_hand)
    dealer_points = get_hand_points(dealer_hand)

    while player_points <= 21:
        answer = input('Hit (h) or stay (s)? ')
        if answer == 'h':
            hit(dealer_deck, player_hand)
            player_points = get_hand_points(player_hand)
            show_player_cards(player_hand)
        else:
            break

    if player_points > 21:
        print('BUST!')
        return

    # now deal with the dealer's hand

    while dealer_points <= 16:
        print('Dealer hits')
        hit(dealer_deck, dealer_hand)
        show_dealer_cards(dealer_hand)
        dealer_points = get_hand_points(dealer_hand)

    if dealer_points > 21:
        print('Dealer busts, you win!')
    elif player_points > dealer_points:
        print(f'Dealer has {dealer_points} vs your {player_points}, you win!')
    else:
        print(f'Dealer has {dealer_points} vs your {player_points}, you lose.')

if __name__ == '__main__':
    main()
