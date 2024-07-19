import sys

cards = list(map(str.strip, open(sys.argv[1]).readlines()))
wins = []
card_count = [1 for _ in range(len(cards))]

for card in cards:
  card = card.split(': ')[1]
  win_num, my_num = card.split(' | ')
  win_num = win_num.split()
  my_num = my_num.split()

  win_cnt = 0
  for num in my_num:
    if num in win_num:
      win_cnt += 1

  wins.append(win_cnt)

for i in range(len(cards)):
  for j in range(i+1, i+1+wins[i]):
    card_count[j] += card_count[i]

print(sum(card_count))
