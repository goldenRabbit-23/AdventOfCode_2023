import sys
from collections import defaultdict

grid = list(map(str.strip, open(sys.argv[1]).readlines()))
gears = defaultdict(list)
num_str = ""
found = False
res = 0

for i in range(len(grid)):
  for j in range(len(grid[i])):
    if grid[i][j] == '*':
      gears[(i, j)]

for i in range(len(grid)):
  for j in range(len(grid[i]) + 1):
    if j == len(grid[i]):
      if num_str != "" and found:
        gears[(x, y)].append(int(num_str))
        found = False
      num_str = ""
      x, y = 0, 0
    elif num_str == "" and not grid[i][j].isnumeric():
      continue
    elif num_str != "" and not grid[i][j].isnumeric():
      if found:
        gears[(x, y)].append(int(num_str))
        found = False
      num_str = ""
      x, y = 0, 0
    else:
      num_str += grid[i][j]
      for dx, dy in [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]:
        if i + dx < 0 or i + dx >= len(grid) or j + dy < 0 or j + dy >= len(grid[i]):
          continue
        if grid[i + dx][j + dy] == '*':
          found = True
          x, y = i + dx, j + dy
          break

for parts in gears.values():
  if len(parts) == 2:
    res += parts[0] * parts[1]

print(res)
