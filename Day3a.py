def main():
    first_wire, second_wire = [], []
    [first_wire.append((i[0], int(i[1:]))) for i in open("day3.txt").readlines()[0].split(",")]
    [second_wire.append((i[0], int(i[1:]))) for i in open("day3.txt").readlines()[1].split(",")]
    points_a = construct(first_wire)
    print("done wire one")
    points_b = construct(second_wire)
    print("done wire two")
    intercepts = compare_points(points_a, points_b)
    print("done comparing points")
    best = sorted(intercepts, key=lambda p: abs(p[0])+abs(p[1]))[0]
    print(abs(best[0])+abs(best[1]))


def construct(wire):
    points, x, y = [], 0, 0
    for i in wire:
        direction, distance = i
        if direction == "U":
            while distance > 0:
                points.append((x, y+1))
                distance -= 1
                y += 1
        if direction == "D":
            while distance > 0:
                points.append((x, y-1))
                y -= 1
                distance -= 1
        if direction == "L":
            while distance > 0:
                points.append((x-1, y))
                x -= 1
                distance -= 1
        if direction == "R":
            while distance > 0:
                points.append((x+1, y))
                x += 1
                distance -= 1
    return points


def compare_points(points_a, points_b):
    set_a = set(points_a)
    set_b = set(points_b)
    return set_a & set_b


if __name__ == '__main__':
    main()
