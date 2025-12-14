import sys


def main():
    grid = open(sys.argv[1]).read().splitlines()
    R, C = len(grid), len(grid[0])

    start = (0, grid[0].index('.'))
    end = (R - 1, grid[-1].index('.'))

    points = [start, end]

    for r in range(R):
        for c in range(C):
            if grid[r][c] == '#':
                continue

            neighbors = 0
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#':
                    neighbors += 1

            if neighbors > 2:
                points.append((r, c))

    points_set = set(points)
    graph = {pt: {} for pt in points}

    for sr, sc in points:
        stack = [(sr, sc, 0)]
        visited = {(sr, sc)}

        while stack:
            r, c, dist = stack.pop()

            if dist > 0 and (r, c) in points_set:
                graph[(sr, sc)][(r, c)] = dist
                continue

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#':
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        stack.append((nr, nc, dist + 1))

    max_steps = 0
    visited_nodes = set()

    def dfs(current, steps):
        nonlocal max_steps

        if current == end:
            max_steps = max(max_steps, steps)
            return

        visited_nodes.add(current)

        for neighbor, dist in graph[current].items():
            if neighbor not in visited_nodes:
                dfs(neighbor, steps + dist)

        visited_nodes.remove(current)

    dfs(start, 0)
    print(max_steps)


if __name__ == "__main__":
    main()
