import sys

init_seq = open(sys.argv[1]).read().split(',')
res = 0

for seq in init_seq:
  val = 0
  for ch in seq:
    val += ord(ch)
    val *= 17
    val %= 256
  res += val

print(res)