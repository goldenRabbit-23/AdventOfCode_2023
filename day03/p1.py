import sys

grid = list(map(str.strip, open(sys.argv[1]).readlines()))
num_str = ""
flag = False
res = 0

for i in range(len(grid)):
    for j in range(len(grid[i]) + 1):
        if j == len(grid[i]):
            if num_str != "" and flag:
                res += int(num_str)
                flag = False
            num_str = ""
        elif num_str == "" and not grid[i][j].isnumeric():
            continue
        elif num_str != "" and not grid[i][j].isnumeric():
            if flag:
                res += int(num_str)
                flag = False
            num_str = ""
        else:
            num_str += grid[i][j]
            for dx, dy in [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]:
                if i + dx < 0 or i + dx >= len(grid) or j + dy < 0 or j + dy >= len(grid[i]):
                    continue
                if not grid[i + dx][j + dy].isnumeric() and grid[i + dx][j + dy] != '.':
                    flag = True
                    break

print(res)
