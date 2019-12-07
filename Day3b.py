def main():
    first_wire = [(i[0], int(i[1:])) for i in open("day3.txt").readlines()[0].split(",")]
    second_wire = [(i[0], int(i[1:])) for i in open("day3.txt").readlines()[1].split(",")]
    points_a = construct(first_wire)
    points_b = construct(second_wire)
    steps = compare_points(points_a, points_b)
    print(sorted(steps)[0])


def construct(wire):
    points, x, y, count = {}, 0, 0, 1
    for i in wire:
        direction, distance = i
        if direction == "U":
            while distance > 0:
                points[(x, y+1)] = count
                distance -= 1
                y += 1
                count += 1
        elif direction == "D":
            while distance > 0:
                points[(x, y-1)] = count
                y -= 1
                distance -= 1
                count += 1
        elif direction == "L":
            while distance > 0:
                points[(x-1, y)] = count
                x -= 1
                distance -= 1
                count += 1
        elif direction == "R":
            while distance > 0:
                points[(x+1, y)] = count
                x += 1
                distance -= 1
                count += 1
    return points


def compare_points(points_a, points_b):
    set_a = points_a.keys()
    set_b = points_b.keys()
    steps = [points_a[i] + points_b[i] for i in set_a & set_b]
    return steps


if __name__ == '__main__':
    main()
