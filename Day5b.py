def main():
    content = [int(i) for i in open("day5.txt").read().split(",")]
    int_code(content)


def int_code(content):
    place = 0
    while place < len(content):
        #print(content[place])
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
        elif int(str(content[place])[-2:]) == 5:
            if content[place] == 5:
                if content[content[place+1]] != 0:
                    place = content[content[place+2]]
                else:
                    place += 3
            elif len(str(content[place])) == 3:
                if content[place+1] != 0:
                    place = content[content[place+2]]
                else:
                    place += 3
            elif int(str(content[place])[-3]) == 0:
                if content[content[place+1]] != 0:
                    place = content[place+2]
                else:
                    place += 3
            else:
                if content[place+1] != 0:
                    place = content[place+2]
                else:
                    place += 3
        elif int(str(content[place])[-2:]) == 6:
            if content[place] == 5:
                if content[content[place+1]] == 0:
                    place = content[content[place+2]]
                else:
                    place += 3
            elif len(str(content[place])) == 3:
                if content[place+1] == 0:
                    place = content[content[place+2]]
                else:
                    place += 3
            elif int(str(content[place])[-3]) == 0:
                if content[content[place+1]] == 0:
                    place = content[place+2]
                else:
                    place += 3
            else:
                if content[place+1] == 0:
                    place = content[place+2]
                else:
                    place += 3
        elif int(str(content[place])[-2:]) == 7:
            if content[place] == 7:
                if content[content[place+1]] < content[content[place+2]]:
                    content[content[place+3]] = 1
                else:
                    content[content[place+3]] = 0
            elif len(str(content[place])) == 3:
                if content[place+1] < content[content[place+2]]:
                    content[content[place + 3]] = 1
                else:
                    content[content[place + 3]] = 0
            elif int(str(content[place])[-3]) == 0:
                if content[content[place+1]] < content[place+2]:
                    content[content[place + 3]] = 1
                else:
                    content[content[place + 3]] = 0
            else:
                if content[place+1] < content[place+2]:
                    content[content[place + 3]] = 1
                else:
                    content[content[place + 3]] = 0
            place += 4
        elif int(str(content[place])[-2:]) == 8:
            if content[place] == 8:
                if content[content[place+1]] == content[content[place+2]]:
                    content[content[place+3]] = 1
                else:
                    content[content[place+3]] = 0
            elif len(str(content[place])) == 3:
                if content[place+1] == content[content[place+2]]:
                    content[content[place + 3]] = 1
                else:
                    content[content[place + 3]] = 0
            elif int(str(content[place])[-3]) == 0:
                if content[content[place+1]] == content[place+2]:
                    content[content[place + 3]] = 1
                else:
                    content[content[place + 3]] = 0
            else:
                if content[place+1] == content[place+2]:
                    content[content[place + 3]] = 1
                else:
                    content[content[place + 3]] = 0
            place += 4
        else:
            exit("an error occurred")


if __name__ == '__main__':
    main()
