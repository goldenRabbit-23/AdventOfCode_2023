import sys

grid = open(sys.argv[1]).read().splitlines()
row, col = len(grid), len(grid[0])

grid = [[c for c in row] for row in grid]
cache = {}

# rotate grid 90 degrees clockwise
def rotate():
  global grid

  grid = [list(row) for row in zip(*grid)]
  grid = [row[::-1] for row in grid]

# tilt grid north
def tilt():
  global grid

  for c in range(col):
    rock_row = -1
    for r in range(row):
      if grid[r][c] == '.':
        pass
      elif grid[r][c] == 'O':
        rock_row += 1
        grid[rock_row][c] = 'O'
        # if the rock (O) actually moved
        if rock_row != r:
          grid[r][c] = '.'
      elif grid[r][c] == '#':
        rock_row = r

def do_cycle():
  for _ in range(4):
    tilt()
    rotate()

def find_interval_start(grid_str):
  global cache

  for cyc, str in cache.items():
    if grid_str == str:
      return cyc

def load(grid):
  row_n = len(grid)
  res = 0
  
  for r, row in enumerate(grid):
    for ch in row:
      res += (row_n - r) * (1 if ch == 'O' else 0)
  
  return res

# evaluate distinct grid combinations
cycle = 0

while True:
  do_cycle()
  cycle += 1
  grid_str = '\n'.join([''.join(row) for row in grid])
  if grid_str in cache.values():
    break
  cache[cycle] = grid_str

# distinct grids
distinct_grids = len(cache)

# find start of the interval
# grid_str is currently in a next cycle after the last cycle in cache
grid_str = '\n'.join([''.join(row) for row in grid])
start = find_interval_start(grid_str)

length = distinct_grids - start + 1
index = (10 ** 9 - start) % length + start

print(load(cache[index].split('\n')))