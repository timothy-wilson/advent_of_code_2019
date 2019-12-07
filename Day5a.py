def main():
    content = [int(i) for i in open("day5.txt").read().split(",")]
    int_code(content)


def int_code(content):
    place = 0
    while place < len(content):
        if content[place] == 99:
            break
        elif int(str(content[place])[-2:]) == 1:
            if content[place] == 1:
                content[content[place+3]] = content[content[place+1]] + content[content[place+2]]
            elif len(str(content[place])) == 3:
                content[content[place+3]] = content[place+1] + content[content[place+2]]
            elif int(str(content[place])[-3]) == 0:
                content[content[place + 3]] = content[content[place + 1]] + content[place + 2]
            else:
                content[content[place + 3]] = content[place + 1] + content[place + 2]
            place += 4
        elif int(str(content[place])[-2:]) == 2:
            if content[place] == 2:
                content[content[place + 3]] = content[content[place + 1]] * content[content[place + 2]]
            elif len(str(content[place])) == 3:
                content[content[place + 3]] = content[place + 1] * content[content[place + 2]]
            elif int(str(content[place])[-3]) == 0:
                content[content[place + 3]] = content[content[place + 1]] * content[place + 2]
            else:
                content[content[place + 3]] = content[place + 1] * content[place + 2]
            place += 4
        elif content[place] == 3:
            content[content[place+1]] = int(input(">>> "))
            place += 2
        elif int(str(content[place])[-2:]) == 4:
            if content[place] == 4:
                print(content[content[place+1]])
            else:
                print(content[place+1])
            place += 2
        else:
            exit("an error occurred")


if __name__ == '__main__':
    main()
