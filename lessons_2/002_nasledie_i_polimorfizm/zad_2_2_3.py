class OneClass:
    pass


class TwoClass(OneClass):
    pass


class ThreeClass:
    pass


class FourClass(ThreeClass):
    pass


class FiveClass(TwoClass, FourClass):
    pass


def main():
    print(OneClass.mro())
    print(TwoClass.mro())
    print(ThreeClass.mro())
    print(FourClass.mro())
    print(FiveClass.mro())


if __name__ == '__main__':
    main()


'''
Наримере класса "FiveClass" можно увидеть линеаризацию данных
в таком порядке FiveClass(класс-потомок) -> TwoClass(второй класс-потомок)
-> OneClass (родительский класс), FourClass -> ThreeClass -> и родительский класс object
'''