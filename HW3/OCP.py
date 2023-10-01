# Принцип открытого-закрытого (Open/Closed Principle – OCP) заключается в том, что программные сущности, такие как классы, модули и функции, 
# должны быть открыты для расширения, но закрыты для модификации.

from abc import ABC, abstractmethod

# Абстрактный метод, который определяет метод calculate_area.
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

# Два класса наследника. Они реализуются метод у абстрактного класса. Метод по расчету площади.
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

# Метод отвечает принципу OCP, так как он открыт для расширения, но при этом не изменяет свой. 
# Т.е. мы можем добавлять новые фигуры, при этом основной код будет работать без измененией.
class AreaCalculator:
    def calculate_total_area(self, shapes):
        total_area = 0
        for shape in shapes:
            total_area += shape.calculate_area()
        return total_area
    
    # Метод Main для работоспособности кода. В него мы добавляет параментры фигур и запускаем просчет общий площади.
    def main():
        rectangle = Rectangle(5, 10)
        circle = Circle(7)

        calculator = AreaCalculator()
        shapes = [rectangle, circle]
        # Расчет общий площади состоит из класса (calculator = AreaCalculator()) в который подается метод (calculate_area) по расчету с параметрами shapes = [rectangle, circle].
        total_area = calculator.calculate_area(shapes)
        print(f"Total area: {total_area}")
    
    # Для вызова в одном коде
    if __name__ == "__main__":
        main()
