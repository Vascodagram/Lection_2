def arithmetics(*number):
    return sum(number) / len(number)


def main():
    print(arithmetics(100, 348))
    print(arithmetics(*range(16)))


if __name__ == '__main__':
    main()