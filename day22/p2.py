import sys
from collections import defaultdict, deque


def main():
    data = open(sys.argv[1]).read().splitlines()
    bricks = []

    for line in data:
        start, end = line.split('~')
        x1, y1, z1 = map(int, start.split(','))
        x2, y2, z2 = map(int, end.split(','))
        bricks.append([x1, y1, z1, x2, y2, z2])

    bricks.sort(key=lambda b: b[2])

    height_map = {}
    k_supports_v = defaultdict(set)
    k_supported_by_v = defaultdict(set)

    for idx, b in enumerate(bricks):
        x1, y1, z1, x2, y2, z2 = b
        footprint = []

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                footprint.append((x, y))

        base_z = 0
        for x, y in footprint:
            if (x, y) in height_map:
                base_z = max(base_z, height_map[(x, y)][0])

        dist_fall = z1 - (base_z + 1)
        new_z1, new_z2 = z1 - dist_fall, z2 - dist_fall
        bricks[idx][2] = new_z1
        bricks[idx][5] = new_z2

        for x, y in footprint:
            if (x, y) in height_map:
                top_z, support_id = height_map[(x, y)]
                if top_z == base_z:
                    k_supported_by_v[idx].add(support_id)
                    k_supports_v[support_id].add(idx)

        for x, y in footprint:
            height_map[(x, y)] = (new_z2, idx)

    total_chain_reaction = 0

    for i in range(len(bricks)):
        q = deque([i])
        falling = {i}

        while q:
            current = q.popleft()

            for beneficiary in k_supports_v[current]:
                if beneficiary not in falling:
                    if k_supported_by_v[beneficiary].issubset(falling):
                        falling.add(beneficiary)
                        q.append(beneficiary)

        total_chain_reaction += len(falling) - 1

    print(total_chain_reaction)


if __name__ == "__main__":
    main()
