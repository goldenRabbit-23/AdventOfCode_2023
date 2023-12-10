import sys


def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                return (i, j)


grid = open(sys.argv[1]).read().splitlines()
start = find_start(grid)

x = start[0]
y = start[1]
loop_length = 1
# enter_dir: [0, 1, 2, 3] == ['N', 'E', 'S', 'W']

if grid[x - 1][y] in ['7', '|', 'F']:
    x = x - 1
    enter_dir = 2
elif grid[x][y + 1] in ['J', '-', '7']:
    y = y + 1
    enter_dir = 3
elif grid[x + 1][y] in ['J', '|', 'L']:
    x = x + 1
    enter_dir = 0
elif grid[x][y - 1] in ['L', '-', 'F']:
    y = y - 1
    enter_dir = 1

while (x, y) != start:
    loop_length += 1

    if grid[x][y] == '-':
        if enter_dir == 1:
            y = y - 1
        elif enter_dir == 3:
            y = y + 1
    elif grid[x][y] == '|':
        if enter_dir == 0:
            x = x + 1
        elif enter_dir == 2:
            x = x - 1
    elif grid[x][y] == 'J':
        if enter_dir == 0:
            y = y - 1
            enter_dir = 1
        elif enter_dir == 3:
            x = x - 1
            enter_dir = 2
    elif grid[x][y] == 'L':
        if enter_dir == 0:
            y = y + 1
            enter_dir = 3
        elif enter_dir == 1:
            x = x - 1
            enter_dir = 2
    elif grid[x][y] == '7':
        if enter_dir == 2:
            y = y - 1
            enter_dir = 1
        elif enter_dir == 3:
            x = x + 1
            enter_dir = 0
    elif grid[x][y] == 'F':
        if enter_dir == 1:
            x = x + 1
            enter_dir = 0
        elif enter_dir == 2:
            y = y + 1
            enter_dir = 3

print(loop_length // 2)
