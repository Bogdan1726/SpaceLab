from abc import ABC, abstractmethod


class Iterator(ABC):
    """
    Abstract class Iterator
    """
    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def has_next(self):
        pass


class ColorCarIterator(Iterator):
    """
    Iterator class
    """
    def __init__(self, color):
        self.color = color
        self.index = 0

    def next(self):
        color_item = self.color[self.index]
        self.index += 1
        return f'Color car: {color_item}'

    def has_next(self):
        return False if self.index >= len(self.color) else True


class CarMagazine:
    """
    Class Iterable
    """
    def __init__(self):
        self.color_cars = ['red', 'green', 'blue', 'green', 'yellow']

    def iterator(self):
        return ColorCarIterator(self.color_cars)


if __name__ == '__main__':
    car_magazine = CarMagazine()
    iterator = car_magazine.iterator()
    print(iterator.next())
    print(iterator.next())
    print(iterator.next())
    print(iterator.next())











