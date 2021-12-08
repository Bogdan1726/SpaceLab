# Паттерн наблюдатель
from abc import ABC, abstractmethod

class FireFightingSystem:
    """
    Класс системы пожаротушения
    """
    def __init__(self):
        self.server = []

    def add(self, sensor):
        self.server.append(sensor)

    def notify(self):
        for item in self.server:
            item.activate_sensor()


class AbstractSensor(ABC):
    """
    Abstract class sensor
    """
    @abstractmethod
    def activate_sensor(self):
        pass


class FireSensor(AbstractSensor):
    """
    Class fire sensor
    """

    def __init__(self, name):
        self.name = name

    def activate_sensor(self):
        print(f'Активирован противопожарный датчик №{self.name}')


sensor1 = FireSensor('1')
sensor2 = FireSensor('2')
sensor3 = FireSensor('3')
system = FireFightingSystem()
system.add(sensor1)
system.add(sensor2)
system.add(sensor3)
system.notify()
