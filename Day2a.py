def main():
    content = [int(i) for i in open("day2.txt").read().split(",")]
    content[1] = 12
    content[2] = 2
    int_code(content)
    print(content[0])


def int_code(content):
    place = 0
    while place < len(content):
        if content[place] == 1:
            content[content[place+3]] = content[content[place+1]] + content[content[place+2]]
            place += 4
        elif content[place] == 2:
            content[content[place+3]] = content[content[place+1]] * content[content[place+2]]
            place += 4
        elif content[place] == 99:
            break
        else:
            exit("an error occurred")


if __name__ == '__main__':
    main()
