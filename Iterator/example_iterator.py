from collections.abc import Iterable, Iterator
import random


class Car:
    cars_brand = ['Subaru', 'Ford', 'Kia', 'Hyundai', 'Mercedes']
    color_cars = ['red', 'green', 'blue', 'grey', 'yellow']

    def __init__(self):
        self.color = random.choice(self.color_cars)
        self.brand = random.choice(self.cars_brand)
        self.price = random.randint(10000, 100000)

    def __repr__(self):
        return f'Brand: {self.brand}, color: {self.color}, price: {self.price}$'


class CarIterable(Iterable):
    """
    Class Iterable
    """
    def __init__(self):
        self.collection = [Car() for _ in range(101)]

    def __iter__(self):
        return CarIterator(self.collection)


class CarIterator(Iterator):
    """
    Iterator class
    """
    def __init__(self, collection: [CarIterable]):
        self.collection = collection
        self.limit = 50000
        self.index = 0

    def __next__(self):
        result = ''
        try:
            value = self.collection[self.index]
            self.index += 1
            if value.price <= self.limit:
                result = value
        except IndexError:
            raise StopIteration()
        return result


if __name__ == '__main__':
    car = Car()
    magazine = CarIterable()
    for item in magazine:
        print(item)




















