from abc import ABC, abstractmethod


class Configuration(ABC):
    """
    Абстрактный класс декорируемого объекта
    """

    @abstractmethod
    def cost(self):
        pass


class BaseConfiguration(Configuration):
    """
    Класс декорируемого объекта
    """
    PRICE = 20000

    def cost(self):
        return self.PRICE


class Decorator(Configuration):
    """
    Абстрактный класс объекта
    """
    @abstractmethod
    def options(self):
        pass


class StandardConfiguration(Decorator):

    PRICE_OPTION_PACKAGE = 2000

    def __init__(self, base: BaseConfiguration):
        self.base = base

    def cost(self):
        return f"Стоимость данной комплектации - {self.PRICE_OPTION_PACKAGE+self.base.cost()}$"

    def options(self):
        return f"Комплектация стандарт включает пакет опций таких как: " \
               f"полный электропакет, усилитель руля, легкосплавные диски г16"


class LuxConfiguration(Decorator):

    PRICE_OPTION_PACKAGE = 5000

    def __init__(self, base: BaseConfiguration):
        self.base = base

    def cost(self):
        return f"Стоимость данной комплектации - {self.PRICE_OPTION_PACKAGE+self.base.cost()}$"

    def options(self):
        return f"Комплектация люкс включает пакет опций таких как: " \
               f"полный электропакет, усилитель руля, легкосплавные диски г17," \
               f"кожаный салон, подогрев руля, адаптивная оптика"


if __name__ == "__main__":
    base = BaseConfiguration()
    standard = StandardConfiguration(base)
    print(standard.options())
    print(standard.cost())
    print('-- // --')
    lux = LuxConfiguration(base)
    print(lux.options())
    print(lux.cost())

