hand1 = [{'value': 2, 'suit': 'hearts'},
           {'value': 5, 'suit': 'spades'},
           {'value': 7, 'suit': 'diamonds'}]

hand2 = [{'value': 2, 'suit': 'hearts'},
           {'value': 5, 'suit': 'spades'},
           {'value': 7, 'suit': 'diamonds'}]

hand3 = [{'value': 2, 'suit': 'hearts'},
           {'value': 5, 'suit': 'spades'},
           {'value': 7, 'suit': 'diamonds'}]

hands_list = [hand1, hand2, hand3]

def count_hand(hand):
    output('Starting a count')
    total_value = 0
    for card in hand:
        value = card['value']
        suit = card['suit']
        output(f'{value} of {suit}')
        total_value += value
    output(f'This hand is worth {total_value} points')

def output(text):
    print(text)

def main():
    for hand in hands_list:
        count_hand(hand)

if __name__ == '__main__':
    main()
