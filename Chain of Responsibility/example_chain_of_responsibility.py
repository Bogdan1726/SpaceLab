from abc import ABC, abstractmethod


class Handler:
    """
    Abstract class handler
    """
    @abstractmethod
    def handler(self, request):
        pass


class BadRoom(Handler):

    def handler(self, request):
        if request == 'Bed':
            return 'Установить в спальне'


class Kitchen(Handler):

    def handler(self, request):
        if request == 'Microwave':
            return 'Установить на кухне'


class Bathroom(Handler):

    def handler(self, request):
        if request == 'Washing machine':
            return 'Установить в ванной комнате'


class House:

    def __init__(self):
        self.rooms = [BadRoom(), Kitchen(), Bathroom()]

    def response(self, request):
        for room in self.rooms:
            msg = room.handler(request)
            if msg:
                print(msg)
                break
        else:
            print('Нет места для этого предмета')


house = House()
house.response('Microwave')



