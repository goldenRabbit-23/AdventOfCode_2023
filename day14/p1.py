import sys

grid = open(sys.argv[1]).read().splitlines()
row, col = len(grid), len(grid[0])
res = 0

for c in range(col):
  rock_row = -1
  for r in range(row):
    if grid[r][c] == '.':
      pass
    elif grid[r][c] == 'O':
      rock_row += 1
      res += row - rock_row
    elif grid[r][c] == '#':
      rock_row = r

print(res)