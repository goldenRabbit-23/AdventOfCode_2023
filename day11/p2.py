import sys
from itertools import combinations

grid = open(sys.argv[1]).read().splitlines()

row = len(grid)
col = len(grid[0])

galaxies = []
empty_rows = []
empty_cols = []

for r in range(row):
  for c in range(col):
    if grid[r][c] == '#':
      galaxies.append((r, c))

for r in range(row):
  for c in range(col):
    if grid[r][c] == '#':
      break
  else:
    empty_rows.append(r)

for c in range(col):
  for r in range(row):
    if grid[r][c] == '#':
      break
  else:
    empty_cols.append(c)

pairs = list(combinations(galaxies, 2))
res = 0

for (x1, y1), (x2, y2) in pairs:
  dist = abs(x1 - x2) + abs(y1 - y2)
  for row in empty_rows:
    dist += 999999 if min(x1, x2) < row < max(x1, x2) else 0
  for col in empty_cols:
    dist += 999999 if min(y1, y2) < col < max(y1, y2) else 0
  res += dist

print(res)
