from abc import ABC, abstractmethod
from datetime import datetime


class StateWindows:
    """
    Class state of windows
    """
    system = 'Windows 10 version 16.07'

    def __init__(self):
        self.state = self.system

    def set_state(self, state):
        self.state = state
        print(f'Установлена новая версия: {self.state}')

    def save_state(self):
        return Memento(self.state)

    def get_state(self):
        return self.state

    def restore_state(self, memento):
        self.state = memento.get_state()
        print(f'Система восстановила состояния : {self.state}')


class IMemento(ABC):
    """
    Abstract class memento
    """
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_date(self):
        pass

    @abstractmethod
    def get_state(self):
        pass


class Memento(IMemento):
    """
    Class save memento
    """
    def __init__(self, state):
        self.state = state
        self.date = str(datetime.now())

    def get_state(self):
        return self.state

    def get_name(self):
        return f'{self.date}: {self.state}'

    def get_date(self):
        return self.date


class Caretaker:
    """
    Опекун
    """
    def __init__(self, state_windows: StateWindows):
        self.mementos = []
        self.state_windows = state_windows

    def backup(self):
        self.mementos.append(self.state_windows.save_state())

    def undo(self):
        if not len(self.mementos):
            print('Нет больше точек восстановления')
            return
        memento = self.mementos.pop()
        print(f'Восстановление состояния до: {memento.get_name()}')
        try:
            self.state_windows.restore_state(memento)
        except Exception:
            self.undo()

    # def undo(self, index):
    #     try:
    #         memento = self.mementos[index]
    #         print(f'Восстановление состояния до: {memento.get_name()}')
    #         self.state_windows.restore_state(memento)
    #     except IndexError:
    #         print('Нет точки восстановления с таким номером!')

    def show_history(self):
        print('Доступные точки восстановления')
        for memento in self.mementos:
            print(memento.get_name())


windows = StateWindows()
caretaker = Caretaker(windows)
caretaker.backup()
windows.set_state('Windows 10 version 18.10')
caretaker.backup()
windows.set_state('Windows 10 version 19.04')
print()
caretaker.show_history()
print()

caretaker.undo()
caretaker.undo()
caretaker.undo()

# caretaker.undo(1)
# caretaker.undo(0)
# caretaker.undo(1)
# caretaker.undo(2)

print(windows.get_state())
