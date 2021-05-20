suits = ['hearts', 'spades', 'clubs', 'diamonds']

my_hand = []

for suit in suits:
    for i in range(9):
        my_hand.append({'value': i+2, 'suit': suit})

print(my_hand)
