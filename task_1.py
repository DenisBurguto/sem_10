# Задание No1
# 📌 Создайте класс окружность.
# 📌 Класс должен принимать радиус окружности при создании
# экземпляра.
# 📌 У класса должно быть два метода, возвращающие длину окружности и её площадь.
import math


class Circumference:

    def __init__(self, radius):
        self.radius = radius

    def get_length(self):
        return 2 * math.pi * self.radius

    def get_square(self):
        return math.pi * self.radius ** 2


if __name__ == '__main__':
    first = Circumference(10)
    second = Circumference(34)
    print(first.get_square())
    print(first.get_length())
    print(second.get_square())
    print(second.get_length())

