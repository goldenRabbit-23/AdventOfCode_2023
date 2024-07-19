import sys
from collections import deque


def find_start(grid):
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j] == 'S':
        return (i, j)


def check_bound(r, c):
  global length, width
  return 0 <= r < length and 0 <= c < width


def flood_fill(sr, sc):
  global visited, points_in_same_domain, path_points

  visited[sr][sc] = 1
  points_in_same_domain.append((sr, sc))

  dq = deque()
  dq.append((sr, sc))

  while len(dq) > 0:
    front = dq.popleft()
    r = front[0]
    c = front[1]

    for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
      nr = r + dr
      nc = c + dc
      if check_bound(nr, nc):
        if visited[nr][nc] == 0 and (nr, nc) not in path_points:
          dq.append((nr, nc))
          visited[nr][nc] = 1
          points_in_same_domain.append((nr, nc))


grid = open(sys.argv[1]).read().splitlines()
start = find_start(grid)
length = len(grid)
width = len(grid[0])

r = start[0]
c = start[1]
# enter_dir: [0, 1, 2, 3] == ['N', 'E', 'S', 'W']

path_points = [start]
path_right_points = set()

if grid[r - 1][c] in ['7', '|', 'F']:
  r = r - 1
  enter_dir = 2
elif grid[r][c + 1] in ['J', '-', '7']:
  c = c + 1
  enter_dir = 3
elif grid[r + 1][c] in ['J', '|', 'L']:
  r = r + 1
  enter_dir = 0
elif grid[r][c - 1] in ['L', '-', 'F']:
  c = c - 1
  enter_dir = 1

while (r, c) != start:
  path_points.append((r, c))

  if grid[r][c] == '-':
    if enter_dir == 1:
      if check_bound(r - 1, c):
        path_right_points.add((r - 1, c))
      c = c - 1
    elif enter_dir == 3:
      if check_bound(r + 1, c):
        path_right_points.add((r + 1, c))
      c = c + 1
  elif grid[r][c] == '|':
    if enter_dir == 0:
      if check_bound(r, c - 1):
          path_right_points.add((r, c - 1))
      r = r + 1
    elif enter_dir == 2:
      if check_bound(r, c + 1):
          path_right_points.add((r, c + 1))
      r = r - 1
  elif grid[r][c] == 'J':
    if enter_dir == 0:
      c = c - 1
      enter_dir = 1
    elif enter_dir == 3:
      if check_bound(r + 1, c):
        path_right_points.add((r + 1, c))
      if check_bound(r, c + 1):
        path_right_points.add((r, c + 1))
      r = r - 1
      enter_dir = 2
  elif grid[r][c] == 'L':
    if enter_dir == 0:
      if check_bound(r, c - 1):
        path_right_points.add((r, c - 1))
      if check_bound(r + 1, c):
        path_right_points.add((r + 1, c))
      c = c + 1
      enter_dir = 3
    elif enter_dir == 1:
      r = r - 1
      enter_dir = 2
  elif grid[r][c] == '7':
    if enter_dir == 2:
      if check_bound(r, c + 1):
        path_right_points.add((r, c + 1))
      if check_bound(r - 1, c):
        path_right_points.add((r - 1, c))
      c = c - 1
      enter_dir = 1
    elif enter_dir == 3:
      r = r + 1
      enter_dir = 0
  elif grid[r][c] == 'F':
    if enter_dir == 1:
      if check_bound(r - 1, c):
        path_right_points.add((r - 1, c))
      if check_bound(r, c - 1):
        path_right_points.add((r, c - 1))
      r = r + 1
      enter_dir = 0
    elif enter_dir == 2:
      c = c + 1
      enter_dir = 3

# (r, c) is now back to start
if all(p in path_points for p in [(r, c - 1), (r - 1, c)]) and enter_dir == 3:
  if check_bound(r + 1, c):
    path_right_points.add((r + 1, c))
  if check_bound(r, c + 1):
    path_right_points.add((r, c + 1))
elif all(p in path_points for p in [(r, c + 1), (r - 1, c)]) and enter_dir == 0:
  if check_bound(r, c - 1):
    path_right_points.add((r, c - 1))
  if check_bound(r + 1, c):
    path_right_points.add((r + 1, c))
elif all(p in path_points for p in [(r, c - 1), (r + 1, c)]) and enter_dir == 2:
  if check_bound(r, c + 1):
    path_right_points.add((r, c + 1))
  if check_bound(r - 1, c):
    path_right_points.add((r - 1, c))
elif all(p in path_points for p in [(r, c + 1), (r + 1, c)]) and enter_dir == 1:
  if check_bound(r - 1, c):
    path_right_points.add((r - 1, c))
  if check_bound(r, c - 1):
    path_right_points.add((r, c - 1))
elif all(p in path_points for p in [(r, c - 1), (r, c + 1)]):
  if enter_dir == 1 and check_bound(r - 1, c):
    path_right_points.add((r - 1, c))
  elif enter_dir == 3 and check_bound(r + 1, c):
    path_right_points.add((r + 1, c))
elif all(p in path_points for p in [(r - 1, c), (r + 1, c)]):
  if enter_dir == 0 and check_bound(r, c - 1):
    path_right_points.add((r, c - 1))
  elif enter_dir == 2 and check_bound(r, c + 1):
    path_right_points.add((r, c + 1))


path_right_points = list(path_right_points)
path_right_points = [p for p in path_right_points if p not in path_points]

visited = [[0 for _ in range(width)] for _ in range(length)]
points_in_same_domain = []

for r, c in path_right_points:
  if visited[r][c] == 0:
    flood_fill(r, c)

# one of two numbers is the answer
print(len(points_in_same_domain))  # path right
print(length * width - len(path_points) -
      len(points_in_same_domain))  # path left
