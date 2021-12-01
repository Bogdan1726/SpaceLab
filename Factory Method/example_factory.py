from abc import ABC, abstractmethod


class Product(ABC):
    """
    Абстрактный клас продукта
    """

    @abstractmethod
    def release_product(self):
        pass


class Table(Product):
    """
    Конкретный продукт стол
    """

    def release_product(self):
        print('Release new table')


class Chair(Product):
    """
    Конкретный продукт стул
    """

    def release_product(self):
        print('Release new chair')


class Factory(ABC):
    """
    Абстрактный клас фабрики
    """

    @abstractmethod
    def create(self, type_furniture):
        pass


class FurnitureFactory(Factory):

    def create(self, type_furniture):
        if type_furniture == 'Table':
            return Table()
        if type_furniture == 'Chair':
            return Chair()


if __name__ == '__main__':
    create = FurnitureFactory()
    product = create.create('Table')
    product.release_product()

# class TableFactory(Factory):
#
#     def create(self):
#         return Table()
#
#
# class ChairFactory(Factory):
#
#     def create(self):
#         return Chair()
#
#
# if __name__ == '__main__':
#     creator = TableFactory()
#     table = creator.create()
#
#     creator = ChairFactory()
#     chair = creator.create()
#
#     print(table.release_product())
#     print(chair.release_product())
