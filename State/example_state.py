from abc import ABC, abstractmethod


class ComputerStateBase(ABC):
    """
    Abstract class state computer
    """

    @abstractmethod
    def get_state(self):
        pass


class ComputerOffState(ComputerStateBase):
    def get_state(self):
        return 'Computer Off'


class ComputerOnState(ComputerStateBase):
    def get_state(self):
        return 'Computer On'


class ComputerSleepState(ComputerStateBase):
    def get_state(self):
        return 'Computer Sleep'


class Computer(object):
    def __init__(self):
        self.current_state = None
        self.states = self.get_states()

    @staticmethod
    def get_states():
        return [ComputerOffState(), ComputerOnState(), ComputerSleepState()]

    def next_state(self):
        if self.current_state is None:
            self.current_state = self.states[0]
        else:
            index = self.states.index(self.current_state)
            if index < len(self.states) - 1:
                index += 1
            else:
                index = 0
            self.current_state = self.states[index]
        return self.current_state

    def set_state(self):
        state = self.next_state()
        print(state.get_state())


comp = Computer()
comp.set_state()
comp.set_state()
comp.set_state()
comp.set_state()


