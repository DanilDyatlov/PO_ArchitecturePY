# Принцип подстановки Лисков
# Принцип гласит, что: подтипы должны быть взаимозаменяемыми для своих базовых типов.

from abc import ABC, abstractmethod

# Абстрактный базовый класс с методом расчета 
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

# Два класса которые наследуют от основного. Имеют разные параметры, но общее решение по подсчету.
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2
    
# Функция вычисляет общую площадь. Расчитывая площадь, совершенно не важно какие используются фигуры
def get_total_area(shapes):
    return sum(shape.calculate_area() for shape in shapes)

get_total_area([Rectangle(10, 5), Square(5)])

#-------------------------------------------------------

from abc import ABC, abstractmethod

# Базовый абстрктный класс с общими методами старта и остановки 
class Car(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Два класса наследника. Они реализуют свою логику для методов станрта и сотановки.
class RegularCar(Car):

    def start(self):
        return f"RegularCar: {self.name} - started"
    
    def stop(self):
        return f"RegularCar: {self.name} - stopped"
    
class SportsCar(Car):

    def start(self):
        return f"SportsCar: {self.name} - started"
    
    def stop(self):
        return f"SportsCar: {self.name} - stopped"

# Функция принимает в качестве аргумента класс Car и вызывает его методы. В этот метод передаем подклассы класса Car и они выполнятся, так как у них такие же методы 
def drive(car):
    print(car.start())
    print(car.stop())

# Даем название наших машин и предаем их в класс
regularCar = RegularCar("LADA")
sportsCar = SportsCar("BMW")

# Вызываем методы 
drive(regularCar)
drive(sportsCar)