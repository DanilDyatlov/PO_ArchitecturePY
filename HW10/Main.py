class Product: 
    # Класс продукта у которого есть id, название и цена
    def __init__(self,id,name,prise):
        self.id = id
        self.name = name
        self.prise = prise

class ProductDAO:
    # Содержит методы для добавления, удаления и получения продуктов из базы данных (или списка).
    # Для этого создаем список продуктов
    # Методы отвечают за определенные методы
    def __init__(self): 
        self.products = []
    
    def add_product(self,product):
        self.products.append(product)
        
    def remove_product(self,product):
        self.products.remove(product)
    
    def get_all_product(self):
        return self.products
    
class ProductRepository:
    # Служит репозиторием для продуктов. Он должен использовать DAO для доступа к данным.
    # Репозиторий должен иметь методы для добавления, удаления и получения продуктов. 
    def __init__(self,dao):
        self.dao = dao

    def add_product(self,product):
        self.dao.products.append(product)
        
    def remove_product(self,product):
        self.dao.products.remove(product)
    
    def get_all_product(self):
        return self.dao.products
    
class ProductService:
    # использовать репозиторий для выполнения операций с продуктами.
    # Добавили бизнес-логику в сервисе (например, проверку цены продукта).
    def __init__(self,repository):
        self.repository = repository

    def add_product(self,product):
        if product.prise > 100:
            print("!")
        self.repository.products.append(product)
class UnitOfWork:
    # Может группировать операции с продуктами в рамках транзакции.
    # Т.е. мы собираем сначала в группы (wait), а после потверждаем (commit).
    def __init__(self):
        self.new_product = []
        self.delete_product = []

    # Создаем списоки и добавляем туда продукты: 
    def wait_new_product(self,product):
        self.new_product.append(product)
    
    def wait_remove_product(self,product):
        self.delete_product.append(product)
    
    def commit(self,product):
        # Процесс сохранения и удаления продуктов
        for product in self.new_product:
            print("Продукты сохранены: ", product.name)
        for product in self.delete_product:
            print("Продукты удалены: ", product.name)

        self.new_product = []
        self.delete_product = []

def main():
    dao = ProductDAO()
    repository = ProductRepository(dao)
    service = ProductService(repository)
    uow = UnitOfWork()

    # Создание продукта 
    product = Product(1, "Rice", 20)

    # Добавление продукта в список
    uow.wait_new_product(product)

    # Проверка бизнес логики в сервисе 
    service.add_product(product)

    # Сохраняем изменения 
    uow.commit()

    # Удаляем продукт 
    uow.delete_product(product)

    # Сохраняем изменения 
    uow.commit()

    # Выводим все продукты 
    products = repository.get_all_product()
    for product in products:
        print(product.id, product.name, product.prise)

if __name__ == "__main__":
    main()