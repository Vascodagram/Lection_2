def reverse(my_list):
    len_list = len(my_list) - 1
    while len_list >= 0:
        yield my_list[len_list]
        len_list -= 1


def main():
    my_list = [32, 4, 35, 657, 545, 42]
    for i in reverse(my_list):
        print(i)


if __name__ == '__main__':              
    main()