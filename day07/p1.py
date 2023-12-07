import sys
from collections import Counter

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
    count = Counter(line[0])

    if len(count) == 1:  # five of a kind
        five_kind.append(line)
    elif len(count) == 2:
        if count.most_common()[0][1] == 4:  # four of a kind
            four_kind.append(line)
        else:  # full house
            full_house.append(line)
    elif len(count) == 3:
        if count.most_common()[0][1] == 3:  # three of a kind
            three_kind.append(line)
        else:  # two pair
            two_pair.append(line)
    elif len(count) == 4:  # one pair
        one_pair.append(line)
    else:  # high card
        high_card.append(line)

card_order = 'AKQJT98765432'

five_kind = sorted(five_kind, key=lambda e: [
                   card_order.index(c) for c in e[0]])
four_kind = sorted(four_kind, key=lambda e: [
                   card_order.index(c) for c in e[0]])
full_house = sorted(full_house, key=lambda e: [
                    card_order.index(c) for c in e[0]])
three_kind = sorted(three_kind, key=lambda e: [
                    card_order.index(c) for c in e[0]])
two_pair = sorted(two_pair, key=lambda e: [card_order.index(c) for c in e[0]])
one_pair = sorted(one_pair, key=lambda e: [card_order.index(c) for c in e[0]])
high_card = sorted(high_card, key=lambda e: [
                   card_order.index(c) for c in e[0]])

cur_rank = len(data)
winnings = 0

for card in five_kind + four_kind + full_house + three_kind + two_pair + one_pair + high_card:
    winnings += cur_rank * card[1]
    cur_rank -= 1

print(winnings)
