import sys

grids = open(sys.argv[1]).read().split('\n\n')
res = 0

def check_mirrored(grid, row):
  left = row
  right = row + 1
  max_bound = len(grid) - 1
  
  while left >= 0 and right <= max_bound:
    if grid[left] != grid[right]:
      return False
    
    left -= 1
    right += 1
  
  return True

for grid in grids:
  grid = grid.split('\n')
  row = len(grid)
  found = False

  # original grid -> check rows first
  for r in range(0, row - 1):
    if check_mirrored(grid, r):
      res += (r + 1) * 100
      found = True
      break
  
  # if row is found, skip to next grid
  if found:
    continue

  # transpose
  grid = list(zip(*grid))
  row = len(grid)

  # transposed grid -> check rows second
  for r in range(0, row - 1):
    if check_mirrored(grid, r):
      res += r + 1
      break

print(res)