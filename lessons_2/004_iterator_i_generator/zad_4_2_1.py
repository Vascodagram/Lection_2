class Reverse:
    def __init__(self, my_list):
        self.my_list = my_list
        self.index_my_list = len(my_list) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index_my_list < 0:
            raise StopIteration
        result = self.my_list[self.index_my_list]
        self.index_my_list -= 1
        return result


def main():
    my_list = [32, 4, 35, 657, 545, 42]
    for i in Reverse(my_list):
        print(i)


if __name__ == "__main__":
    main()