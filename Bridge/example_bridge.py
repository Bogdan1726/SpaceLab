from abc import ABC, abstractmethod


class TVBase(ABC):
    """
    Абстрактный класс TV
    """

    @abstractmethod
    def model_tv(self):
        pass

    @abstractmethod
    def show_channel(self, channel):
        pass


class LG(TVBase):
    """
    TV LG
    """

    def model_tv(self):
        print('TV - LG-55"')

    def show_channel(self, channel):
        print(f'Show channel {channel}')


class Samsung(TVBase):
    """
    TV Samsung
    """

    def model_tv(self):
        print('TV - Samsung-50"')

    def show_channel(self, channel):
        print(f'Show channel: {channel}')


class RemoteControlBase(ABC):
    """
    Абстрактный класс пульта управления
    """

    @abstractmethod
    def show_channel(self, channel):
        pass

    @abstractmethod
    def power_tv(self):
        pass


class RemoteControl(RemoteControlBase):
    """
    Пульт управления
    """

    def __init__(self, tv: TVBase):
        self.tv = tv

    def show_channel(self, channel):
        self.tv.show_channel(channel)

    def power_tv(self):
        self.tv.model_tv()


lg = LG()
remote_control = RemoteControl(lg)
remote_control.power_tv()
remote_control.show_channel('History')

