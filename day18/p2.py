import sys


def main():
    plan = open(sys.argv[1]).read().splitlines()
    points = [(0, 0)]
    perimeter = 0

    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    cr, cc = 0, 0

    for line in plan:
        hex_code = line.split('#')[1].rstrip(')')
        dist_hex = hex_code[:5]
        length = int(dist_hex, 16)
        direction = int(hex_code[5])

        dr, dc = directions[direction]
        cr += dr * length
        cc += dc * length
        perimeter += length
        points.append((cr, cc))

    # Calculate Area using Shoelace Formula
    area = 0

    for i in range(len(points) - 1):
        r1, c1 = points[i]
        r2, c2 = points[i + 1]
        area += c1 * r2 - c2 * r1

    area = abs(area) // 2

    # Pick's Theorem
    print(area + (perimeter // 2) + 1)


if __name__ == "__main__":
    main()
