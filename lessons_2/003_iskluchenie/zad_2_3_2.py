class Operation:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number
    try:
        def add(self):
            return self.first_number + self.second_number

        def mull(self):
            return self.first_number * self.second_number

        def pow(self):
            return self.first_number ** self.second_number

        def sub(self):
            return self.first_number - self.second_number

        def truediv(self):
            try:
                return self.first_number / self.second_number
            except ZeroDivisionError:
                print('Error деление на ноль!')
    except (NameError, ValueError) as error:
        print('error', error)


def input_operation():
    operator = input('Введите +, -, /, *, ^ или exit для выхода: ')
    if operator == 'exit':
        exit('Завершение работы.')
    else:
        first_number = float(input("A = "))
        second_number = float(input("B = "))
        test_res = Operation(first_number, second_number)

        if operator == '+':
            return test_res.add()
        elif operator == '/':
            return test_res.truediv()
        elif operator == '-':
            return test_res.sub()
        elif operator == '*':
            return test_res.mull()
        elif operator == '^':
            return test_res.pow()
        else:
            raise NotImplementedError('В строке "Введите +, -, /, *, ^ или exit для выхода:" введено неверное значение')


def main():
    while True:
        try:
            result = input_operation()
            print(result)
        except (ValueError, ArithmeticError, NotImplementedError) as error:
            print('Возникла ошибка:', error)
            print()


if __name__ == '__main__':
    main()