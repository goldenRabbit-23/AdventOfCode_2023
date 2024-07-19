import sys

lines = open(sys.argv[1]).read().splitlines()
groups = []
new_groups = []
cur_str = ''
arrangement = 0
res = 0

def generate_perms(str, idx, len):
  global cur_str, arrangement

  if idx == len:
    arrangement += validate()
    return

  if str[idx] == '?':
    for ch in '.#':
      cur_str += ch
      generate_perms(str, idx + 1, len)
      cur_str = cur_str[:-1]
  else:
    cur_str += str[idx]
    generate_perms(str, idx + 1, len)
    cur_str = cur_str[:-1]

def validate():
  global cur_str, groups, new_groups

  new_groups = []
  cnt = 0

  for ch in cur_str:
    if ch == '#':
      cnt += 1
    elif cnt > 0:
      new_groups.append(cnt)
      cnt = 0
  
  if cnt > 0:
    new_groups.append(cnt)

  return 1 if groups == new_groups else 0

for line in lines:
  pattern, record = line.split()
  groups = list(map(int, record.split(',')))
  arrangement = 0

  generate_perms(pattern, 0, len(pattern))

  res += arrangement

print(res)