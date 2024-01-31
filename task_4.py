# Задание No4
# 📌 Создайте класс Сотрудник.
# 📌 Воспользуйтесь классом человека из прошлого задания.
# 📌 У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
from sem_10.task_3 import Human


class Employee(Human):
    __id_list = []
    __SEP = 7
    __ID_START = 100000

    def __init__(self, name: str, surname: str, patronymic: str, age: int):
        super().__init__(name, surname, patronymic, age)
        if not self.__id_list:
            self.__id = self.__ID_START
            self.__id_list.append(self.__id)
        else:
            self.__id = self.__id_list[-1] + 1
            self.__id_list.append(self.__id)
        self.__access = self.__id % self.__SEP

    def get_id(self):
        return self.__id

    def get_access(self):
        return self.__access


if __name__ == '__main__':
    staff_1 = Employee('Paul', 'Jonthon', 'Junior', 45)
    staff_2 = Employee('David', 'Bush', 'Senior', 66)
    print(f"{staff_1.full_name()=  }")
    print(f'{staff_1.get_id()=  }')
    print(f"{staff_1.get_access()=  }")
    print(staff_2.full_name())
    print(staff_2.get_id())
    print(staff_2.get_access())
    print(staff_2.get_age())
    staff_2.birthday()
    print(staff_2.get_age())
