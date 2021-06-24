""" this is the actual blackjack game """

from deck import Deck
from card import Card

def show_cards(hand):
    for card in hand.cards:
        print(card)
    value = get_hand_points(hand)
    print(f'Worth {value} points')


def show_player_cards(number, player_hand):
    """ tell the player1 what cards they have """
    print(f'Player {number}, You have the following cards:')
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


def get_player_input(number, hand, dealer_deck):
    """ figure out how the player wants to deal with their hand """
    show_player_cards(number, hand)
    player_points = get_hand_points(hand)

    while player_points <= 21:
        answer = input(f'Player {number}, Would you like to Hit (h) or stay (s)? ')
        if answer == 'h':
            hit(dealer_deck, hand)
            player_points = get_hand_points(hand)
            show_player_cards(number, hand)
        else:
            break

    if player_points > 21:
        print(f'Player {number} BUSTS!')

    return player_points


def deal_cards(deck, count):
    """ deal cards out to a deck, which is returned """
    new_hand = Deck()
    new_hand.cards = deck.deal(count)
    return new_hand

def setup_cards(number):
    """ create the dealer's deck, and deal cards out to players """
    dealer_deck = Deck()
    dealer_deck.fill(7)
    dealer_deck.shuffle()

    dealer_hand = deal_cards(dealer_deck, 2)
    player_hands = []
    for num in range(number):
        player_hands.append(deal_cards(dealer_deck, 2))

    return dealer_hand, player_hands

def main():
    number_of_players = 2
    dealer_hand, player_hands = setup_cards(number_of_players)

    print(f'The dealer is showing a {dealer_hand[0]}')
    dealer_points = get_hand_points(dealer_hand)

    player1_points = get_player_input(1, player1_hand, dealer_deck)

    show_player_cards(2, player2_hand)
    player2_points = get_hand_points(player2_hand)

    while player2_points <= 21:
        answer = input('Player 2, Would you like to Hit (h) or stay (s)? ')
        if answer == 'h':
            hit(dealer_deck, player2_hand)
            player2_points = get_hand_points(player2_hand)
            show_player_cards(2, player2_hand)
        else:
            break

    if player2_points > 21 and player1_points > 21:
        print('BUST! The game ends.')
        return
    elif player2_points > 21:
        print ('Player 2 BUSTS!')

        

    # now deal with the dealer's hand

    while dealer_points <= 16:
        print('Dealer hits')
        hit(dealer_deck, dealer_hand)
        show_dealer_cards(dealer_hand)
        dealer_points = get_hand_points(dealer_hand)
        

    if dealer_points > 21 and player1_points <= 21 and player2_points <= 21:
        print('Dealer busts! Player 1 and 2 win!')
    elif player1_points > dealer_points and player2_points > dealer_points:
        print(f'Dealer has {dealer_points}, Player 1 has {player1_points} points, and Player 2 has {player2_points}. Player 1 and 2 win!')
    elif player1_points > dealer_points and player2_points < dealer_points:
        print(f'Dealer has {dealer_points}, Player 1 has {player1_points} points, and Player 2 has {player2_points}. Player 1 wins! Player 2 loses.')
    elif player1_points < dealer_points and player2_points > dealer_points:    
        print(f'Dealer has {dealer_points}, Player 1 has {player1_points} points, and Player 2 has {player2_points}. Player 2 wins! Player 1 loses.')
    else:
        print(f'Dealer has {dealer_points}, Player 1 has {player1_points} points, and Player 2 has {player2_points}. Players 1 and 2 lose.')

if __name__ == '__main__':
    main()
