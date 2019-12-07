def main():
    content = {}
    for i in open("day6.txt").readlines():
        content[i.split(")")[1].strip()] = i.split(")")[0]
    for i in content:
        if i == "YOU":
            you = find_orbits(content, i, [])
        elif i == "SAN":
            santa = find_orbits(content, i, [])
    shortest_orbit = set(you).intersection(set(santa))
    distances = []
    for i in shortest_orbit:
        my_distance = len(find_orbits(content, "YOU", [], i))
        santa_distance = len(find_orbits(content, "SAN", [], i))
        distances.append(my_distance + santa_distance)
    print(sorted(distances)[0])


def find_orbits(content, outer_orbit,  orbits, destination="COM"):
    if outer_orbit != destination and content[outer_orbit] != destination:
        orbits.append(content[outer_orbit])
        return find_orbits(content, content[outer_orbit], orbits, destination)
    else:
        return orbits


if __name__ == '__main__':
    main()
