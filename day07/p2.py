import sys
from collections import Counter


def classify(card):
    count = Counter(card)

    if len(count) == 1:  # five of a kind
        return 6
    elif len(count) == 2:
        if count.most_common()[0][1] == 4:  # four of a kind
            return 5
        else:  # full house
            return 4
    elif len(count) == 3:
        if count.most_common()[0][1] == 3:  # three of a kind
            return 3
        else:  # two pair
            return 2
    elif len(count) == 4:  # one pair
        return 1
    else:  # high card
        return 0


data = list(map(str.split, open(sys.argv[1]).read().splitlines()))
data = [[item[0], int(item[1])] for item in data]

five_kind = []
four_kind = []
full_house = []
three_kind = []
two_pair = []
one_pair = []
high_card = []

for line in data:
    other_symbols = list(dict.fromkeys(line[0]))
    other_symbols = [c for c in other_symbols if c != 'J']
    max_hand = 0

    if 'J' in line[0] and line[0] != 'JJJJJ':
        for c in other_symbols:
            new_card = line[0].replace('J', c)
            max_hand = max(max_hand, classify(new_card))
    else:
        max_hand = classify(line[0])

    if max_hand == 6:  # five of a kind
        five_kind.append(line)
    elif max_hand == 5:  # four of a kind
        four_kind.append(line)
    elif max_hand == 4:  # full house
        full_house.append(line)
    elif max_hand == 3:  # three of a kind
        three_kind.append(line)
    elif max_hand == 2:  # two pair
        two_pair.append(line)
    elif max_hand == 1:  # one pair
        one_pair.append(line)
    else:  # high card
        high_card.append(line)

card_order = 'AKQT98765432J'

five_kind.sort(key=lambda e: [card_order.index(c) for c in e[0]])
four_kind.sort(key=lambda e: [card_order.index(c) for c in e[0]])
full_house.sort(key=lambda e: [card_order.index(c) for c in e[0]])
three_kind.sort(key=lambda e: [card_order.index(c) for c in e[0]])
two_pair.sort(key=lambda e: [card_order.index(c) for c in e[0]])
one_pair.sort(key=lambda e: [card_order.index(c) for c in e[0]])
high_card.sort(key=lambda e: [card_order.index(c) for c in e[0]])

cur_rank = len(data)
winnings = 0

for card in five_kind + four_kind + full_house + three_kind + two_pair + one_pair + high_card:
    winnings += cur_rank * card[1]
    cur_rank -= 1

print(winnings)
