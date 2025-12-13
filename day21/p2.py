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

    total_steps = 26501365
    remainder = total_steps % R
    target_checkpoints = [remainder, remainder + R, remainder + 2 * R]

    current_plots = {(sr, sc)}
    results = []
    max_steps = target_checkpoints[-1]

    for step in range(1, max_steps + 1):
        next_plots = set()
        for r, c in current_plots:
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                if grid[nr % R][nc % C] != '#':
                    next_plots.add((nr, nc))

        current_plots = next_plots

        if step in target_checkpoints:
            results.append(len(current_plots))

            if len(results) == 3:
                break

    y0, y1, y2 = results
    n = (total_steps - remainder) // R

    a = (y2 - 2 * y1 + y0) // 2
    b = y1 - y0 - a
    c = y0

    print(a * n**2 + b * n + c)


if __name__ == "__main__":
    main()
