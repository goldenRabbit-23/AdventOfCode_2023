import sys
from collections import deque


def main():
    plan = open(sys.argv[1]).read().splitlines()

    directions = {
        'R': (0, 1),
        'D': (-1, 0),
        'L': (0, -1),
        'U': (1, 0),
    }

    # 1. Precomputation
    instructions = []
    cr, cc = 0, 0
    min_r, max_r = 0, 0
    min_c, max_c = 0, 0

    for line in plan:
        parts = line.split()
        direction, length = parts[0], int(parts[1])
        instructions.append((direction, length))

        dr, dc = directions[direction]
        cr += dr * length
        cc += dc * length

        min_r = min(min_r, cr)
        max_r = max(max_r, cr)
        min_c = min(min_c, cc)
        max_c = max(max_c, cc)

    # 2. Grid Simulation
    H = max_r - min_r + 3
    W = max_c - min_c + 3

    grid = [['.' for _ in range(W)] for _ in range(H)]

    off_r = -min_r + 1
    off_c = -min_c + 1

    cr, cc = off_r, off_c
    grid[cr][cc] = '#'

    for direction, length in instructions:
        dr, dc = directions[direction]

        for _ in range(length):
            cr += dr
            cc += dc
            grid[cr][cc] = '#'

    # 3. Flood Fill "Outside"
    q = deque([(0, 0)])
    grid[0][0] = 'O'

    while q:
        r, c = q.popleft()

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < H and 0 <= nc < W:
                if grid[nr][nc] == '.':
                    grid[nr][nc] = 'O'
                    q.append((nr, nc))

    # 4. Count Enclosed Area
    print(sum(1 if grid[r][c] != 'O' else 0 for r in range(H) for c in range(W)))


if __name__ == "__main__":
    main()
