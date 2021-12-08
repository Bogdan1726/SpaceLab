# Паттерн посредник
from abc import ABC, abstractmethod


class WindowBase(ABC):
    """
    Abstract class window
    """
    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def hide(self):
        pass


class MainWindow(WindowBase):
    """
    Class main window
    """
    def show(self):
        print('Show MainWindow')

    def hide(self):
        print('Hide MainWindow')


class SettingWindow(WindowBase):
    """
    Class setting window
    """
    def show(self):
        print('Show SettingWindow')

    def hide(self):
        print('Hide SettingWindow')


class HelpWindow(WindowBase):
    """
    Class help window
    """
    def show(self):
        print('Show HelpWindow')

    def hide(self):
        print('Hide HelpWindow')


class WindowMediator(object):
    """
    Class mediator
    """
    def __init__(self):
        self.windows = dict.fromkeys(['main', 'setting', 'help'])

    def show(self, win):
        for window in self.windows.values():
            if window is not win:
                window.hide()
        win.show()

    def set_main(self, win):
        self.windows['main'] = win

    def set_setting(self, win):
        self.windows['setting'] = win

    def set_help(self, win):
        self.windows['help'] = win


main_win = MainWindow()
setting_win = SettingWindow()
help_win = HelpWindow()

med = WindowMediator()
med.set_main(main_win)
med.set_setting(setting_win)
med.set_help(help_win)


med.show(setting_win)

