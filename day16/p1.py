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

  energized = set()
  q = deque()

  def in_bound(r, c):
    return 0 <= r < row and 0 <= c < col

  q.append((0, 0, Dir.EAST))
  while q:
    r, c, dir = q.popleft()
    
    # skip out-of-bounds case
    if not in_bound(r, c):
      continue

    # add in-bound cell
    energized.add((r, c))

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

    print(len(energized))

if __name__ == '__main__':
  main()

# Part 1: 6855

# real    1m32.397s
# user    0m32.791s
# sys     0m59.581s