from abc import ABC, abstractmethod


class Strategy(ABC):

    @abstractmethod
    def do_algorithm(self, name, language):
        pass


class English(Strategy):

    def do_algorithm(self, name, language):
        print(f'Hello, {name}')


class Russian(Strategy):

    def do_algorithm(self, name, language):
        print(f'Здравствуйте, {name}')


class Ukrainian(Strategy):

    def do_algorithm(self, name, language):
        print(f'Вітаю, {name}')


class Operator:

    def __init__(self, name, language):
        self.name = name
        self.language = language

    def language_choice(self):
        if self.language == 1:
            English().do_algorithm(self.name, self.language)
        elif self.language == 2:
            Russian().do_algorithm(self.name, self.language)
        elif self.language == 3:
            Ukrainian().do_algorithm(self.name, self.language)
        else:
            print('wrong command')


ivan = Operator('Ivan', 3)
ivan.language_choice()
gon = Operator('Gon', 1)
gon.language_choice()
egor = Operator('Egor', 2)
egor.language_choice()




