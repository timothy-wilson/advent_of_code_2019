def main():
    range_start = 246540
    range_end = 787419
    print(len(passwords(range_start, range_end+1)))


def passwords(range_start, range_end):
    passwords = []
    for i in range(range_start, range_end):
        list_i = [int(j) for j in str(i)]
        if list_i == sorted(list_i):
            for j in range(len(list_i) - 1):
                if list_i[j] == list_i[j+1]:
                    if j+2 < len(list_i):
                        if list_i[j + 2] != list_i[j] and list_i[j-1] != list_i[j]:
                            passwords.append(i)
                            break
                    elif list_i[j-1] != list_i[j]:
                        passwords.append(i)
                        break
    return passwords


if __name__ == '__main__':
    main()
