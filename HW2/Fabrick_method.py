"""
Фабричный метод — это порождающий паттерн проектирования, 
который определяет общий интерфейс для создания объектов в суперклассе, 
позволяя подклассам изменять тип создаваемых объектов.
Создание объектов наиболее частая задача, которую решает Фабричный метод (Factory Method).

abc.ABC – базовый класс для создания абстрактных классов. 
Абстрактный класс содержит один или несколько абстрактных методов, то есть методов без определения (пустых, без кода). 
Эти методы необходимо переопределить в подклассах.

abc.abstractmethod – декоратор, который указывает, что метод является абстрактным. 
Этот декоратор применяется к методу внутри абстрактного класса. 
Класс, который наследует свойства и методы от абстрактного класса, 
должен реализовать все абстрактные методы, иначе он также будет считаться абстрактным.
"""
from abc import ABC, abstractmethod

class Creator(ABC):
    """
    Это абстрактный класс создателя. Нужен для создания абстрактных классов.
    Он содержит несколько абстрактных методов (пустых без кода). Они переопределяются в подклассах.
    Этот класс объявляет фабричный метод.  
    У этого класса есть несколько методов. def factory_method должен реализоваться в создателе. 
    def some_operation, который использует factory_method для создания продукта и выполняет некоторых операции. 
    """
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        """
        Также заметьте, что, несмотря на название, основная обязанность
        Создателя не заключается в создании продуктов. Обычно он содержит
        некоторую базовую бизнес-логику, которая основана на объектах Продуктов,
        возвращаемых фабричным методом. Подклассы могут косвенно изменять эту
        бизнес-логику, переопределяя фабричный метод и возвращая из него другой
        тип продукта.
        """
        # Вызываем фабричный метод, чтобы получить объект-продукт.
        product = self.factory_method()
        # Далее, работаем с этим продуктом.
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result
    


"""
-----------------------------------------------------------------
Часть 2 
Затем определяются конкретные создатели. Они наследуются от класса Creator и реализуют абстрактный метод factory_method.
Каждый создатель создает свой собственный продукт. 
"""
class ConcreteCreator1(Creator):
    
    """
    Используется абстрактный тип продукта, хотя фактически из метода возвращается конкретный
    продукт. Таким образом, Создатель может оставаться независимым от конкретных
    классов продуктов.
    """

    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()
    



"""
-----------------------------------------------------------------
Часть 3
Определяется абстрактный класс Product. У него есть абстрактный метод operation, 
который реализуется в каждом конкретном продукте.
Затем определяем два продукта. Они наследуются от класса Product и реализуют его метод.
"""

class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

"""
Конкретные Продукты предоставляют различные реализации интерфейса Продукта.
"""
class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"
    

"""
-----------------------------------------------------------------
Часть 4 
Клиентский код работает с экземпляром конкретного создателя, хотя и через
его базовый интерфейс. Пока клиент продолжает работать с создателем через
базовый интерфейс, вы можете передать ему любой подкласс создателя.
"""
def client_code(creator: Creator) -> None:


    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")
    


    
"""
-----------------------------------------------------------------
Часть 5 
В Python есть специальный прием, который позволяет указать, что какой-то код не должен выполняться при импорте: 
все строки, которые находятся в блоке if __name__ == '__main__' не выполняются при импорте.
Переменная __name__ - это специальная переменная, которая будет равна "__main__", 
только если файл запускается как основная программа, и выставляется равной имени модуля при импорте модуля. 
То есть, условие if __name__ == '__main__' проверяет, был ли файл запущен напрямую.
Как правило, в блок if __name__ == '__main__' заносят все вызовы функций и 
вывод информации на стандартный поток вывода. 

В этом блоке создается объект ConcreteCreator затем вызывается его метод some_operation
который создает продукт ConcreteProduct
Весь код построен на созданиии продуктов, действующий фабричным методом, который определяется в абстрактном методе Creator.
"""

if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())


"""
-----------------------------------------------------------------
Часть 6 Пример кода 

Пример № 1 

# Это базовый класс для всех наших фигур
import abc
class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calculate_area(self):
        pass

    @abc.abstractmethod
    def calculate_perimeter(self):
        pass
        
# Несколько более конкретных форм:

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width 

    def calculate_perimeter(self):
        return 2 * (self.height + self.width) 

class Square(Shape):
    def __init__(self, width):
        self.width = width

    def calculate_area(self):
        return self.width ** 2

    def calculate_perimeter(self):
        return 4 * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

# Создав Фабрику фигур , которая будет использоваться для создания конкретных классов фигур на основе входных данных клиента:

class ShapeFactory:
    def create_shape(self, name):
        if name == 'circle':
            radius = input("Enter the radius of the circle: ")
            return Circle(float(radius))

        elif name == 'rectangle':
            height = input("Enter the height of the rectangle: ")
            width = input("Enter the width of the rectangle: ")
            return Rectangle(int(height), int(width))

        elif name == 'square':
            width = input("Enter the width of the square: ")
            return Square(int(width))

# Наша ShapeFactory работает, получая информацию о форме, такую как имя и необходимые размеры. 
# Затем наш фабричный метод create_shape() будет использоваться для создания и возврата готовых объектов нужной формы.

def shapes_client():
    shape_factory = ShapeFactory()
    shape_name = input("Enter the name of the shape: ")

    shape = shape_factory.create_shape(shape_name)

    print(f"The type of object created: {type(shape)}")
    print(f"The area of the {shape_name} is: {shape.calculate_area()}")
    print(f"The perimeter of the {shape_name} is: {shape.calculate_perimeter()}")

"""

"""
-----------------------------------------------------------------
Пример № 2 

from enum import Enum

class PizzaType(Enum):
    # Перечисление текущих рецептов пицц в пиццерии, которые можно приготовить
    MARGARITA = 0,
    MEXICO = 1,
    STELLA = 2

class Pizza:
    #Базовый класс для пицц, которые можно приготовить в пиццерии

    def __init__(self, price: float):
        self.__price = price # цена пиццы

    def get_price(self) -> float:
        return self.__price

class PizzaMargarita(Pizza):
    def __init__(self):
        super().__init__(3.5)

class PizzaMexico(Pizza):
    def __init__(self):
        super().__init__(17.5)

class PizzaStella(Pizza):
    def __init__(self):
        super().__init__(5.5)

def create_pizza(pizza_type: PizzaType) -> Pizza
    # Factory Method
    factory_dict = {
        PizzaType.MARGARITA: PizzaMargarita,
        PizzaType.MEXICO: PizzaMexico,
        PizzaType.STELLA: PizzaStella
    }
    return factory_dict[pizza_type]()

if __name__ == '__main__':
    for pizza in PizzaType:
        my_pizza = create_pizza(pizza)
        print(f'Pizza type: {pizza}, price: {my_pizza.get_price()}')

"""