from abc import ABC, abstractmethod


class Engine(ABC):
    """
    Абстрактный класс двигателя
    """
    @abstractmethod
    def release_engine(self):
        pass


class JapanEngine(Engine):
    def release_engine(self):
        print('Japanese engine')


class ChineEngine(Engine):
    def release_engine(self):
        print('Chinese engine')


class Car(ABC):
    """
    Абстрактный класс авто
    """
    @abstractmethod
    def release_car(self, engine: Engine):
        pass


class JapanCar(Car):

    def release_car(self, engine: Engine):
        print('Release Japanese Car', end=" - ")
        engine.release_engine()


class ChineCar(Car):

    def release_car(self, engine: Engine):
        print('Release Chine Car', end=" - ")
        engine.release_engine()


class Factory(ABC):
    """
    Абстрактный класс фабрики
    """

    @abstractmethod
    def create_engine(self):
        pass

    @abstractmethod
    def create_car(self):
        pass


class JapanFactory(Factory):

    def create_engine(self):
        return JapanEngine()

    def create_car(self):
        return JapanCar()


class ChineFactory(Factory):

    def create_engine(self):
        return ChineEngine()

    def create_car(self):
        return ChineCar()


class FactoryProducer:
    """
    Класс завода производителя
    """

    def get_factory(self, type_of_factory):
        if type_of_factory == 'Japan':
            return JapanFactory()
        if type_of_factory == 'Chine':
            return ChineFactory()


if __name__ == '__main__':
    dealer = FactoryProducer()
    customer = dealer.get_factory('Japan')
    engine = customer.create_engine()
    car = customer.create_car()
    car.release_car(engine)













































