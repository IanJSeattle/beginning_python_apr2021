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

    return dealer_deck, dealer_hand, player_hands

def dealer_final_deal(hand, deck, points):
    """ manage the dealer's draw after everyone else has gone """
    show_dealer_cards(hand)
    while points <= 16:
        hit(deck, hand)
        print('Dealer hits')
        show_dealer_cards(hand)
        points = get_hand_points(hand)
        print(f'Dealer has {points} points')
        if points > 16:
            break
    else:
        print(f'Dealer has {points} points')
    if points > 21:
        print('Dealer busts!')
    return points

def main():
    number_of_players = 2
    dealer_deck, dealer_hand, player_hands = setup_cards(number_of_players)

    print(f'The dealer is showing a {dealer_hand[0]}')
    dealer_points = get_hand_points(dealer_hand)
    player_points = []

    for i in range(number_of_players):
        player_points.append(get_player_input(i + 1,
                                              player_hands[i],
                                              dealer_deck))
    bust_count = 0
    for score in player_points:
        if score > 21:
            bust_count += 1
    if bust_count == number_of_players:
        print('BUST! The game ends.')
        return

    # now deal with the dealer's hand
    dealer_points = dealer_final_deal(dealer_hand, dealer_deck, dealer_points)

    # at this point we know:
    # * the players have not *all* busted out
    # * the dealer has at least 16 points, but may have busted
    # logic for winning:
    # * dealer's 21 is stronger than player's 21
    # * if all players bust, dealer doesn't check their cards
    # * one player's 21 doesn't affect another player's 21
    # * if dealer points == player points, it's a push, no money lost

    # this section would probably be better as its own standalone function
    for i in range(number_of_players):
        if dealer_points < 21:
            if player_points[i] > dealer_points:
                print(f'Player {i}: you win, with {player_points[i]} points!')
            elif player_points[i] == 21:
                print(f'Player {i} wins with blackjack!')
            elif dealer_points > player_points[i]:
                print(f'Player {i}: you lose, dealer beats you with {dealer_points} points')
            elif dealer_points == player_points[i]:
                print(f'Player {i} pushes, with {dealer_points}')
        elif dealer_points == 21:
            if player_points[i] <= 21:
                print(f'Player {i}: you lose, dealer beats you with {dealer_points} points')
        elif dealer_points > 21:
            if player_points[i] <= 21:
                print(f'Player {i}: dealer busts, and you win with {player_points[i]} points!')


if __name__ == '__main__':
    main()
