import sys
from z3 import Int, Ints, Solver, sat


def main():
    data = open(sys.argv[1]).read().splitlines()
    hailstones = []

    for line in data:
        coords, velocity = line.split(' @ ')
        px, py, pz = map(int, coords.split(', '))
        vx, vy, vz = map(int, velocity.split(', '))
        hailstones.append(((px, py, pz), (vx, vy, vz)))

    rx, ry, rz = Ints('rx ry rz')
    rvx, rvy, rvz = Ints('rvx rvy rvz')
    solver = Solver()

    for i, h in enumerate(hailstones[:3]):
        t = Int(f't{i}')
        solver.add(t >= 0)

        solver.add(rx + t * rvx == h[0][0] + t * h[1][0])
        solver.add(ry + t * rvy == h[0][1] + t * h[1][1])
        solver.add(rz + t * rvz == h[0][2] + t * h[1][2])

    if solver.check() == sat:
        model = solver.model()
        print(model.evaluate(rx + ry + rz))


if __name__ == "__main__":
    main()
