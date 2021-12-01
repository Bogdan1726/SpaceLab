from abc import ABC, abstractmethod
from enum import Enum


class MenuType(Enum):
    VEGAN = 1
    CLASSIC = 2


class Menu(ABC):
    """
    Абстрактный класс меню
    """
    @abstractmethod
    def get_name(self):
        pass


class Vegan(Menu):

    def get_name(self):
        return 'Вегетарианское меню'


class Classic(Menu):

    def get_name(self):
        return 'Классическое меню'


class Client(ABC):

    @abstractmethod
    def request_menu(self, menu: Menu):
        pass

    @abstractmethod
    def form_order(self):
        pass

    @abstractmethod
    def get_name(self):
        pass


class Kitchen:
    """
    Класс кухня
    """

    def prepare_food(self):
        print('Еда готовится')

    def call_waiter(self):
        print('Выдача еды официанту')

    def get_name(self):
        return 'Number 1'


class Waiter:
    """
    Класс официант
    """
    def take_order(self, client: Client):
        print(f'Официант принял заказ посетителя {client.get_name()}')

    def send_to_kitchen(self, kitchen: Kitchen):
        print(f'Официант передал заказ на кухню {kitchen.get_name()}')

    def serve_client(self, client: Client):
        print(f'Заказ готов, отдаём клиенту {client.get_name()}')


class RestaurantFacade:
    """
    Класс ресторан на основе паттерна Фасад
    """
    def __init__(self):
        self.kitchen = Kitchen()
        self.waiter = Waiter()
        self.menu = {MenuType.VEGAN: Vegan,
                     MenuType.CLASSIC: Classic}

    def get_name(self, type_menu: MenuType):
        return self.menu[type_menu]()

    def take_order(self, client: Client):
        self.waiter.take_order(client)
        self.waiter.send_to_kitchen(self.kitchen)
        self.kitchen.prepare_food()
        self.kitchen.call_waiter()
        self.waiter.serve_client(client)


class ClientRestaurant(Client):

    def __init__(self, name):
        self.name = name

    def request_menu(self, menu: Menu):
        print(f'Посетитель {self.name} ознакомился с {menu.get_name()}')

    def form_order(self):
        print(f'Посетитель {self.name} делает заказ')

    def get_name(self):
        return self.name


if __name__ == '__main__':
    restaurant = RestaurantFacade()
    client = ClientRestaurant('Robert')
    client.request_menu(restaurant.get_name(MenuType.VEGAN))
    client.form_order()
    restaurant.take_order(client)
    print('-- // --')
    client2 = ClientRestaurant('Gon')
    client2.request_menu(restaurant.get_name(MenuType.CLASSIC))
    client2.form_order()
    restaurant.take_order(client2)





