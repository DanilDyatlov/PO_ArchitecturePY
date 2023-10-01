# Принцип разделения интерфейса (Interface Segregation Principle – ISP) гласит, что клиенты не должны зависеть от интерфейсов, которые они не используют. 
# Вместо создания общих интерфейсов следует создавать специфические интерфейсы для конкретных клиентов.

from abc import ABC, abstractmethod

# Базовые абстрактные классы, описывающие методы работы с документами.
# Эти классы определенные интерфейсы с одной ответственностью каждый 
class Printer(ABC):
    @abstractmethod
    def print(self):
        pass

class Fax(ABC):
    @abstractmethod
    def fax(self):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self):
        pass


# Класс OldPrinter наследуется от Printer и использует его методы, так как другие методы ему использовать не нужно/он не может их использовать
class OldPrinter(Printer):
    def print(self):
        print(f"Printing...")

# Класс NewPrinter наследуется сразу от 3х абстрактных классов и использует их методы. 
class NewPrinter(Printer, Fax, Scanner):
    def print(self):
        print(f"Printing ...")

    def fax(self):
        print(f"Faxing ...")

    def scan(self):
        print(f"Scanning ...")

# Вызов метода
if __name__ == '__main__':
    old = OldPrinter()
    new = NewPrinter()

    old.print()

    new.print()
    new.fax()
    new.scan()