import sys
from math import sqrt, ceil

times, dists = open(sys.argv[1]).read().splitlines()
times = list(map(int, times.split()[1:]))
dists = list(map(int, dists.split()[1:]))
res = 1

for time, dist in zip(times, dists):
    small_root = (time - sqrt(time ** 2 - 4 * dist)) / 2
    if small_root.is_integer():
        min_time = int(small_root + 1)
    else:
        min_time = ceil(small_root)

    center = time / 2
    if center.is_integer():
        res *= 2 * int(center - min_time) + 1
    else:
        res *= 2 * (ceil(center) - min_time)

print(res)
