def main():
    content = [int(i) for i in open("day2.txt").read().split(",")]
    noun = 0
    verb = 0
    while True:
        content[1] = noun
        content[2] = verb
        this_content, err = int_code(content)
        if this_content[0] == 19690720 and not err:
            print(noun*100+verb)
            break
        elif verb != 99:
            verb += 1
        else:
            verb = 0
            noun += 1


def int_code(content):
    err = False
    virtual_content = list(content)
    place = 0
    while place < len(virtual_content):
        if virtual_content[place] == 1:
            virtual_content[virtual_content[place+3]] = virtual_content[virtual_content[place+1]] + virtual_content[virtual_content[place+2]]
            place += 4
        elif virtual_content[place] == 2:
            virtual_content[virtual_content[place+3]] = virtual_content[virtual_content[place+1]] * virtual_content[virtual_content[place+2]]
            place += 4
        elif virtual_content[place] == 99:
            break
        else:
            err = True
            break
    return virtual_content, err


if __name__ == '__main__':
    main()
