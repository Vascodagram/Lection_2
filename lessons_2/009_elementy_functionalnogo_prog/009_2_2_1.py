list_numbers = [1, 2, 4, 6, 7, 24, 121, 3524, 23, 352, 34]
ls_number = filter(lambda x: x % 2 != 0, list_numbers)
ls_squares = map(lambda x: x ** 2, ls_number)
print(list(ls_squares))
