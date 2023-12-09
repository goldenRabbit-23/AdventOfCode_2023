import sys

data = open(sys.argv[1]).read().splitlines()
res = 0

for line in data:
    history = list(map(int, line.split()))
    last_value = history[-1]

    while not all(h == 0 for h in history):
        diff = []
        for i in range(len(history) - 1):
            diff.append(history[i + 1] - history[i])
        last_value += diff[-1]
        history = diff

    res += last_value

print(res)
