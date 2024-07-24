import sys

init_seq = open(sys.argv[1]).read().split(',')
boxes = {b: [] for b in range(256)}
label_pos = {}

def modify_focal_length(boxes, box_n, label, new_foc):
  for i, (lbl, foc) in enumerate(boxes[box_n]):
    if lbl == label:
      boxes[box_n][i] = (lbl, new_foc)
      return

for seq in init_seq:
  box_n = 0

  # assign lens to the box
  if '=' in seq:
    label, focal = seq.split('=')
    for ch in label:
      box_n += ord(ch)
      box_n *= 17
      box_n %= 256
    if label in label_pos:
      modify_focal_length(boxes, box_n, label, focal)
    else:
      label_pos[label] = box_n
      boxes[box_n].append((label, focal))
  
  # remove lens from the box (if exists)
  elif '-' in seq:
    label = seq.split('-')[0]
    if label in label_pos:
      box_n = label_pos[label]
      del label_pos[label]
      boxes[box_n] = list(filter(lambda p: p[0] != label, boxes[box_n]))

focusing_power = 0

for box, lenses in boxes.items():
  for i, (label, focal) in enumerate(lenses):
    focusing_power += (box + 1) * (i + 1) * int(focal)

print(focusing_power)