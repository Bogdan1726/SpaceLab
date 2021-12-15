from abc import ABC, abstractmethod


class Visitor(ABC):
    """
    Abstract class visitor
    """
    @abstractmethod
    def visit(self, item):
        pass


class Component(ABC):
    """
    Abstract class component
    """
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass


class Cinema(Component):

    def accept(self, visitor: Visitor):
        visitor.visit(self)

    def __str__(self):
        return "Cinema - 'Rodina'"


class Theatre(Component):

    def accept(self, visitor: Visitor):
        visitor.visit(self)

    def __str__(self):
        return "Theatre - 'National'"


class Circus(Component):

    def accept(self, visitor: Visitor):
        visitor.visit(self)

    def __str__(self):
        return "Circus - 'Du Soleil'"


class ConcreteVisitor(Visitor):

    def __init__(self, name):
        self.name = name
        self.value = ''

    def visit(self, item):
        if isinstance(item, Cinema):
            self.value = f'Visitor {self.name} visits the {item}'
        elif isinstance(item, Theatre):
            self.value = f'Visitor {self.name} visits the {item}'
        elif isinstance(item, Circus):
            self.value = f'Visitor {self.name} visits the {item}'


if __name__ == '__main__':

    places = [Cinema(), Theatre(), Circus()]

    for place in places:
        visitor = ConcreteVisitor('Ivan')
        place.accept(visitor)
        print(visitor.value)

