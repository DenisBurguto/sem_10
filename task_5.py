# Задание No5
# 📌 Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# 📌 У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# 📌 Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

class Animal:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def birthday(self):
        self.__age += 1


class Cat(Animal):
    def __init__(self, name: str, age: int, run_speed: int, voice: str = None):
        super().__init__(name, age)
        self.__run_speed = run_speed
        self.__voice = voice

    def get_run(self):
        return self.__run_speed

    def get_voice(self):
        return self.__voice


class Bird(Animal):
    def __init__(self, name: str, age: int, fly_speed: int, max_fly_height: int, singing: str = None):
        super().__init__(name, age)
        self.__fly_speed = fly_speed
        self.__max_fly_height = max_fly_height
        self.__singing = singing

    def get_fly(self):
        return f"fly speed ={self.__fly_speed} and max flight height = {self.__max_fly_height}"

    def sing(self):
        return self.__singing


class Fish(Animal):
    def __init__(self, name: str, age: int, swim_speed: int, max_swim_depth: int):
        super().__init__(name, age)
        self.swim_speed = swim_speed
        self.max_swim_depth = max_swim_depth

    def get_swim(self):
        return f"swim speed ={self.swim_speed} and max swim depth = {self.max_swim_depth}"


if __name__ == '__main__':
    cat_1 = Cat('Bars', 3, 9, 'Myaaaau')
    cat_2 = Cat('Pups', 4, 8)
    bird_1 = Bird('Arra Ku', 5, 10, 20)
    fish_1 = Fish('Salmon Sam', 6, 11, 21)
    print(cat_1.get_name())
    print(cat_1.get_age())
    cat_1.birthday()
    print(cat_1.get_age())
    print(cat_1.get_run())
    print(cat_1.get_voice())
    print(cat_2.get_name())
    print(cat_2.get_age())
    print(cat_2.get_run())
    print(cat_2.get_voice())
    print(f"{bird_1.get_fly()=}")
    print(f"{fish_1.get_swim()=}")
