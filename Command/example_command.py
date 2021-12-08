from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self):
        pass


class OnLight(Command):

    def __init__(self, on):
        self.on = on

    def execute(self):
        self.on.turn_on_the_light()


class OffLight(Command):

    def __init__(self, off):
        self.off = off

    def execute(self):
        self.off.turn_off_the_lights()


class On:

    def turn_on_the_light(self):
        print("Свет включён")


class Off:

    def turn_off_the_lights(self):
        print("Свет выключен")


class LightSwitch:
    def __init__(self, command):
        self.command = command

    def invoke(self):
        self.command.execute()


if __name__ == '__main__':
    on = On()
    command_on = OnLight(on)
    off = Off()
    command_off = OffLight(off)
    light_switch = LightSwitch(command_on)
    light_switch.invoke()
    light_switch = LightSwitch(command_off)
    light_switch.invoke()
