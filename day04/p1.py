import sys

cards = list(map(str.strip, open(sys.argv[1]).readlines()))
res = 0

for card in cards:
    card = card.split(': ')[1]
    win_num, my_num = card.split(' | ')
    win_num = win_num.split()
    my_num = my_num.split()

    win_cnt = 0
    for num in my_num:
        if num in win_num:
            win_cnt += 1

    if win_cnt > 0:
        res += 2 ** (win_cnt - 1)

print(res)
