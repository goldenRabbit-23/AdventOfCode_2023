import sys


def main():
    grid = open(sys.argv[1]).read().splitlines()
    R, C = len(grid), len(grid[0])

    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'S':
                sr, sc = r, c
                break
        else:
            continue
        break

    current_plots = {(sr, sc)}

    for _ in range(64):
        next_plots = set()
        for r, c in current_plots:
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < R and 0 <= nc < C:
                    if grid[nr][nc] != '#':
                        next_plots.add((nr, nc))

        current_plots = next_plots

    print(len(current_plots))


if __name__ == "__main__":
    main()
