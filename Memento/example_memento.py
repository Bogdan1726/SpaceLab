from abc import ABC, abstractmethod


class StateWindows:
    """
    Class state of windows
    """
    def __init__(self):
        self.state = 'Windows 10'

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def save_state(self):
        return Memento(self.state)

    def restore_state(self, memento):
        self.state = memento.get_state()


class IMemento(ABC):
    """
    Abstract class memento
    """
    @abstractmethod
    def get_state(self):
        pass


class Memento(IMemento):
    """
    Class save memento
    """
    def __init__(self, state):
        self.state = state

    def get_state(self):
        return self.state


class Caretaker:
    """
    Опекун
    """
    def __init__(self, state_windows: StateWindows):
        self.memento = None
        self.state_windows = state_windows

    def backup(self):
        self.memento = self.state_windows.save_state()

    def get_memento(self):
        return self.memento


windows = StateWindows()
caretaker = Caretaker(windows)
caretaker.backup()
print(windows.get_state())
windows.set_state('Windows 11')
print(windows.get_state())
windows.restore_state(caretaker.get_memento())
print(windows.get_state())
