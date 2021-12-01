from abc import ABC, abstractmethod
from datetime import datetime
from babel.dates import format_datetime


class Server(ABC):
    """
    Исходний Абстрактный класс USA сервера
    """

    @abstractmethod
    def get_temperature(self):
        pass

    @abstractmethod
    def get_date_time(self):
        pass


class ClassicServer(ABC):
    """
    Абстрактный класс сервера для Украины
    """
    @abstractmethod
    def get_celsius_temperature(self):
        pass

    @abstractmethod
    def get_format_datetime(self):
        pass


class Cisco(Server):
    """
    класс сервера для USA
    """
    DATA_TIME = datetime.now()
    FAHRENHEIT = 122

    def get_temperature(self):
        return self.FAHRENHEIT

    def get_date_time(self):
        return self.DATA_TIME

    def __str__(self):
        return f'Temperature: {self.get_temperature()}-F\n' \
               f'Data and time: {self.get_date_time()}'


class Dell(ClassicServer):
    """
    Адаптер(Сервер которий адптирует USA формат дати время и температурі в UA формат
    """

    def __init__(self, server: Server):
        self.server = server

    def get_celsius_temperature(self):
        return (self.server.get_temperature() - 32) * 5 / 9

    def get_format_datetime(self):
        return format_datetime(self.server.get_date_time(), "EEEE  d MMMM Y року H:mm", locale='uk_UA')

    def __str__(self):
        return f'Температура повітря: {self.get_celsius_temperature()}-C\n' \
               f'Дата та час: {self.get_format_datetime()}'


if __name__ == '__main__':
    cisco = Cisco()
    dell = Dell(cisco)
    print(f'{cisco}\n{dell}')
