"""
Задание 3
Используя ссылки в конце данного урока, ознакомьтесь с таким средством инкапсуляции как свойства.
Ознакомьтесь с декоратором property в Python. Создайте класс, описывающий температуру и
позволяющий задавать и получать температуру по шкале Цельсия и Фаренгейта, причём данные могут
быть заданы в одной шкале, а получены в другой.
"""


class Temperature:
    def __init__(self, celsius=0):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) / (9 / 5)

    def __str__(self):
        return f"Celsius: {self.celsius}\nFahrenheit: {self.fahrenheit}\n"


t = Temperature(13)
print(t)
t.celsius = 5
print(t)
t.fahrenheit = 15
print(t)
