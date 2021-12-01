from abc import ABC, abstractmethod


class IProduct(ABC):
    """
    Абстрактный класс продукта
    """
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def get_name(self):
        pass


class Product(IProduct):
    """
    Класс продукта
    """
    def __init__(self, name, cost):
        self._cost = cost
        self._name = name

    def cost(self):
        return self._cost

    def get_name(self):
        return self._name


class ComponentProduct(IProduct):
    """
    Класс компонуемых продуктов
    """
    def __init__(self, name):
        self._name = name
        self.products = []

    def cost(self):
        cost = 0
        for it in self.products:
            cost += it.cost()
        return cost

    def get_name(self):
        return self._name

    def add_product(self, product: IProduct):
        self.products.append(product)

    def remove_product(self, product: IProduct):
        self.products.remove(product)

    def clear_product(self):
        self.products = []


class Pizza(ComponentProduct):
    """
    Класс пицы
    """
    def __init__(self, name):
        super(Pizza, self).__init__(name)

    def cost(self):
        cost = 0
        for it in self.products:
            cost_it = it.cost()
            print(f'Стоимость {it.get_name()} = {cost_it}$')
            cost += cost_it
        print(f'Стоимость пицы {self.get_name()} = {cost}$')
        return cost


if __name__ == '__main__':
    base = ComponentProduct('Основа для пицы')
    base.add_product(Product('мука', 5))
    base.add_product(Product('яйцо', 3))
    base.add_product(Product('соль', 1))
    base.add_product(Product('сахар', 2))

    topping = ComponentProduct('Топпинг')
    topping.add_product(Product('Дор блю', 10))
    topping.add_product(Product('Пармезан', 8))
    topping.add_product(Product('Моцарелла', 9))
    topping.add_product(Product('Маасдам', 7))
    pizza = Pizza('4 сыра')
    pizza.add_product(base)
    pizza.add_product(topping)
    print(pizza.cost())

