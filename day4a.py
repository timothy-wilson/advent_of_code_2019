def main():
    range_start = 246540
    range_end = 787419
    print(len(passwords(range_start, range_end+1)))


def passwords(range_start, range_end):
    passwords = []
    for i in range(range_start, range_end):
        list_i = [int(j) for j in str(i)]
        if list_i == sorted(list_i):
            if len(list_i) != len(set(list_i)):
                passwords.append(i)
    return passwords


if __name__ == '__main__':
    main()
