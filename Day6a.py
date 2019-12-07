def main():
    content = {}
    for i in open("day6.txt").readlines():
        content[i.split(")")[1].strip()] = i.split(")")[0]
    all_orbits = []
    for i in content:
        all_orbits.append(find_indirect_orbits(content, i))
    print(len(content) + sum(all_orbits))


def find_indirect_orbits(content, inner_orbit, orbits=0):
    if inner_orbit != "COM" and content[inner_orbit] != "COM":
        orbits += 1
        return find_indirect_orbits(content, content[inner_orbit], orbits)
    else:
        return orbits


if __name__ == '__main__':
    main()
