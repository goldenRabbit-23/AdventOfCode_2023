import sys


def det(a, b, c, d):
    return a * d - b * c

def main():
    data = open(sys.argv[1]).read().splitlines()
    hailstones = []

    MIN = 200000000000000
    MAX = 400000000000000

    for line in data:
        coords, velocity = line.split(' @ ')
        px, py, pz = map(int, coords.split(', '))
        vx, vy, vz = map(int, velocity.split(', '))
        hailstones.append(((px, py, pz), (vx, vy, vz)))

    n = len(hailstones)
    total_collisions = 0

    for i in range(n):
        (px1, py1, _), (vx1, vy1, _) = hailstones[i]
        for j in range(i + 1, n):
            (px2, py2, _), (vx2, vy2, _) = hailstones[j]

            D1 = det(px2 - px1, vx2, py2 - py1, vy2)
            D2 = det(vx1, vx2, vy1, vy2)

            if D2 == 0:
                continue

            t1 = D1 / D2
            x_intersect = px1 + vx1 * t1
            y_intersect = py1 + vy1 * t1
            t2 = (x_intersect - px2) / vx2 if vx2 != 0 else (y_intersect - py2) / vy2

            if (MIN <= x_intersect <= MAX and MIN <= y_intersect <= MAX) and (t1 > 0 and t2 > 0):
                total_collisions += 1

    print(total_collisions)


if __name__ == "__main__":
    main()
