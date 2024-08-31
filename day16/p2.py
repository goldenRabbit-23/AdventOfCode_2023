import sys
from collections import deque
from enum import Enum

class Dir(Enum):
  NORTH = 0
  EAST  = 1
  SOUTH = 2
  WEST  = 3

def main():
  # NORTH -> (r-1, c)
  # EAST  -> (r, c+1)
  # SOUTH -> (r+1, c)
  # WEST  -> (r, c-1)
  delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

  grid = open(sys.argv[1]).read().splitlines()
  row, col = len(grid), len(grid[0])
  
  def simulate(sr, sc, sdir):
    energized = set()
    visited = []
    q = deque()

    def in_bound(r, c):
      return 0 <= r < row and 0 <= c < col

    q.append((sr, sc, sdir))
    while q:
      r, c, dir = q.popleft()
      
      # skip out-of-bounds cell
      if not in_bound(r, c):
        continue

      # skip already visited cell in certain direction
      if (r, c, dir) in visited:
        continue

      # add in-bound cell
      energized.add((r, c))
      # current cell is visited in certain direction
      visited.append((r, c, dir))

      tile = grid[r][c]
      if tile == '.':
        # keep previous direction
        q.append((r + delta[dir.value][0], c + delta[dir.value][1], dir))
      elif tile == '/':
        # 0 -> 1, 1 -> 0, 2 -> 3, 3 -> 2
        ndir = Dir(dir.value ^ 1)
        q.append((r + delta[ndir.value][0], c + delta[ndir.value][1], ndir))
      elif tile == '\\':
        # 0 -> 3, 1 -> 2, 2 -> 1, 3 -> 0
        ndir = Dir(3 - dir.value)
        q.append((r + delta[ndir.value][0], c + delta[ndir.value][1], ndir))
      elif tile == '|':
        # pointy end
        if dir == Dir.NORTH or dir == Dir.SOUTH:
          # keep previous direction
          q.append((r + delta[dir.value][0], c + delta[dir.value][1], dir))
        # flat end
        else:
          # split into two beams
          q.append((r + delta[Dir.NORTH.value][0], c + delta[Dir.NORTH.value][1], Dir.NORTH))
          q.append((r + delta[Dir.SOUTH.value][0], c + delta[Dir.SOUTH.value][1], Dir.SOUTH))
      elif tile == '-':
        # pointy end
        if dir == Dir.EAST or dir == Dir.WEST:
          # keep previous direction
          q.append((r + delta[dir.value][0], c + delta[dir.value][1], dir))
        # flat end
        else:
          # split into two beams
          q.append((r + delta[Dir.EAST.value][0], c + delta[Dir.EAST.value][1], Dir.EAST))
          q.append((r + delta[Dir.WEST.value][0], c + delta[Dir.WEST.value][1], Dir.WEST))
    
    return len(energized)
  
  res = 0

  # top & bottom row
  for c in range(col):
    res = max(res, simulate(0, c, Dir.SOUTH))
    res = max(res, simulate(row - 1, c, Dir.NORTH))
  # leftmost & rightmost column
  for r in range(row):
    res = max(res, simulate(r, 0, Dir.EAST))
    res = max(res, simulate(r, col - 1, Dir.WEST))
  
  print(res)

if __name__ == '__main__':
  main()
