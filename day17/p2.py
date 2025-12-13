import sys
import heapq


def main():
    grid = open(sys.argv[1]).read().splitlines()
    grid = [list(map(int, row)) for row in grid]
    R, C = len(grid), len(grid[0])

    pq = [(0, 0, 0, 0, 0, 0)]
    visited = set()

    while pq:
        hl, r, c, dr, dc, steps = heapq.heappop(pq)

        if r == R - 1 and c == C - 1 and steps >= 4:
            print(hl)
            return

        if (r, c, dr, dc, steps) in visited:
            continue
        visited.add((r, c, dr, dc, steps))

        for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (ndr, ndc) == (-dr, -dc):
                continue

            if (ndr, ndc) == (dr, dc):
                if steps < 10:
                    nsteps = steps + 1
                else:
                    continue
            else:
                if steps >= 4 or (dr == 0 and dc == 0):
                    nsteps = 1
                else:
                    continue

            nr, nc = r + ndr, c + ndc

            if 0 <= nr < R and 0 <= nc < C:
                nhl = hl + grid[nr][nc]
                heapq.heappush(pq, (nhl, nr, nc, ndr, ndc, nsteps))


if __name__ == "__main__":
    main()
