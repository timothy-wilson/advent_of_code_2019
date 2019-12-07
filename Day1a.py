def main():
    content = [int(i) for i in open("day1.txt").readlines()]
    numbers = [gas_calc(i) for i in content]
    print(sum(numbers))


def gas_calc(weight):
    return weight//3-2


if __name__ == '__main__':
    main()
