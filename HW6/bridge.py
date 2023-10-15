from __future__ import annotations
from abc import ABC, abstractmethod


class Abstraction:
    """
    Абстракция устанавливает интерфейс для «управляющей» части двух иерархий
    классов. Она содержит ссылку на объект из иерархии Реализации и делегирует
    ему всю настоящую работу.
    """

    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        self.implementation.operation_implementation()

class Implementation(ABC):
    """
    Реализация устанавливает интерфейс для всех классов реализации. Он не должен
    соответствовать интерфейсу Абстракции. На практике оба интерфейса могут быть
    совершенно разными. Как правило, интерфейс Реализации предоставляет только
    примитивные операции, в то время как Абстракция определяет операции более
    высокого уровня, основанные на этих примитивах.
    """

    @abstractmethod
    def operation_implementation(self) -> str:
        pass


"""
Каждая Конкретная Реализация соответствует определённой платформе и реализует
интерфейс Реализации с использованием API этой платформы.
"""

class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        print("Выполнение операции с использованием реализации A")


class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        print("Выполнение операции с использованием реализации B")

if __name__ == "__main__":
    """
    Клиентский код должен работать с любой предварительно сконфигурированной
    комбинацией абстракции и реализации.
    """

implementation_a = ConcreteImplementationA()
implementation_b = ConcreteImplementationB()
abstraction = Abstraction(implementation_a)
abstraction.operation()
abstraction.implementation = implementation_b
abstraction.operation()

#Пример 
class AbstractFigure():
    """Общая реализация Фигуры"""
    def __init__(self, ImplementColoRClass):
        self.bridge_color = ImplementColoRClass

class Circle(AbstractFigure):
    """Реализация круга"""
    def draw(self):
        print(f"Нарисовать  Круг цветом {self.bridge_color.color}")

class Square(AbstractFigure):
    """Реализация квадрата"""
    def draw(self):
        print(f"Нарисовать  Квадрат цветом {self.bridge_color.color}")

class AbstractLine():
    """ Вынесенные в отдельный класс манипуляции с цветом для разгрузки основного  класса AbstractFigure
        для упрощения и более гибкой работы. В данном контексте является мостом для работы с цветом у класса AbstractFigure.
    """
    def __init__(self):
        self.color = "White"

    def info_color(self):
        print(f"My color {self.color}")

class BlueLine(AbstractLine):
    """ Реализация  Голубого цвета """
    def __init__(self):
        super().__init__()
        self.color = "Blue"

class RedLine(AbstractLine):
    """ Реализация  Красного цвета """
    def __init__(self):
        super().__init__()
        self.color = "Red"

class GreenLine(AbstractLine):
    def __init__(self):
        super().__init__()
        self.color = "Green"

if __name__ == '__main__':
    red_squar=Square(RedLine())
    red_squar.draw()
    blue_squar = Square(BlueLine())
    blue_squar.draw()
    red_circle=Circle(RedLine())
    red_circle.draw()