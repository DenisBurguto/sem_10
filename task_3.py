# Задание No3
# 📌 Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# 📌 У класса должны быть методы birthday для увеличения возраста
# на год, full_name для вывода полного ФИО и т.п. на ваш выбор.
# 📌 Убедитесь, что свойство возраст недоступно для прямого изменения,
# но есть возможность получить текущий возраст.

class Human:
    def __init__(self, name: str, surname: str, patronymic: str, age: int):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.__age = age

    def birthday(self):
        self.__age += 1

    def get_age(self):
        return self.__age

    def full_name(self):
        return f'{self.name} {self.patronymic} {self.surname}'


if __name__ == '__main__':
    ivanov = Human('Иван', 'Иванов', 'Иванович', 24)
    print(ivanov.get_age())
    print(ivanov.full_name())
    ivanov.birthday()
    print(ivanov.get_age())

