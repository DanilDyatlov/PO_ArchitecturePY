# SRP (Single Responsibility): Принцип единственной ответственности
# В соответствии с принципом единой ответственности каждая из этих задач должна быть разделена на отдельный файл или компонент.
# Принцип единой ответственности гласит: у класса должна быть только одна причина для изменения.


# Класс Animal отвечает лишь за имя животного
class Animal:
    def __init__(self, name):
        self.name = name

# Классы Flyable, Walkable, Swimming отвечают за возможности/действия
class Flyable:
    def fly(self):
        pass

class Walkable:
    def walk(self):
        pass

class Swimming:
    def swim(self):
        pass

# Общий класс. в котором реализован класс Утки. Он найследуется от других классов(Animal) и выполняет описаные там деуствия(Flyable, Walkable, Swimming)
class Duck(Animal, Flyable, Walkable, Swimming):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        print(f"{self.name} is flying")

    def walk(self):
        print(f"{self.name} is walking")

    def swim(self):
        print(f"{self.name} is swimming")

# Вызываем наш метод
def main():
    duck = Duck("Donald")
    duck.fly()
    duck.walk()
    duck.talk()

# Специальный прием, для вызова кода
if __name__ == "__main__":
    main()