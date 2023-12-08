import sys

data = open(sys.argv[1]).read().splitlines()
instr = data[0]
nodes = {}

for item in data[2:]:
    key, value = item.split(' = ')
    value = value.strip('()')
    l, r = value.split(', ')
    nodes[key] = (l, r)

cur = 'AAA'
steps = 0

while True:
    for dir in instr:
        if dir == 'L':
            cur = nodes[cur][0]
        else:
            cur = nodes[cur][1]
        steps += 1

        if cur == 'ZZZ':
            print(steps)
            exit(0)
