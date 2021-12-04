import random
import uuid


class Dot:
    colors = ['red', 'yellow']
    widths = [10, 15, 20]
    height = [10, 15, 20]

    def __init__(self):
        self.width = random.choice(self.widths)
        self.height = random.choice(self.height)
        self.color = random.choice(self.colors)

    def __repr__(self):
        return f'{[self.width, self.height, self.color]}'


class DotUnique:

    def __init__(self, unique_state, flyweight: Dot):
        self.unique_state = unique_state
        self.flyweight = flyweight

    def __repr__(self):
        return f'Unique state - {self.unique_state}\n' \
               f'Shared state - {self.flyweight}'


class FlyWeightFactory:

    def __init__(self):
        self.flyweights = []

    def get_flyweight(self, shared_state):
        flyweights = list(filter(lambda x: x.shared_state == shared_state,
                                 self.flyweights))

        if flyweights:
            return flyweights[0]
        else:
            flyweight = Dot()
            self.flyweights.append(flyweight)
            return flyweight


class DotMaker:

    def __init__(self, flyweight_factory: FlyWeightFactory):
        self.flyweight_factory = flyweight_factory
        self.context = []

    def maker(self, shared_state, unique_state=uuid.uuid4()):
        flyweight = self.flyweight_factory.get_flyweight(shared_state)
        context = DotUnique(unique_state=unique_state, flyweight=flyweight)
        self.context.append(context)
        return context


if __name__ == '__main__':
    flyweight_factory = FlyWeightFactory()
    maker = DotMaker(flyweight_factory)
    maker.maker(Dot())
    print(maker.context)







