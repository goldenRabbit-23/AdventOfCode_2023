import sys

data = open(sys.argv[1]).read().splitlines()
res = 0


def extrapolate(history):
    if all(h == 0 for h in history):
        return 0

    diff = []
    for i in range(len(history) - 1):
        diff.append(history[i] - history[i + 1])
    return history[-1] - extrapolate(diff)


for line in data:
    history = list(map(int, line.split()))
    res += extrapolate(history[::-1])

print(res)
