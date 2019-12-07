def main():
    content = [int(i) for i in open('day1.txt').readlines()]
    numbers = [gas_calc(i) for i in content]
    print(sum(numbers))


def gas_calc(weight, total=0):
    if weight//3-2 > 0:
        total += weight//3-2
        return gas_calc(weight//3-2, total)
    else:
        return total


if __name__ == '__main__':
    main()
