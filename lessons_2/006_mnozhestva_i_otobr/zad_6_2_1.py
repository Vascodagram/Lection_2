"""
Задание 1
Даны две строки. Выведите на экран символы, которые есть в обоих строках.
Задание 2
"""

set_one = set(input('String one: '))
set_two = set(input('String two: '))
result = ' '.join(set_two & set_one)
print(result)