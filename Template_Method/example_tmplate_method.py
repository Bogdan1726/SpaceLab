from abc import ABC, abstractmethod


class BaseTemplate(ABC):
    def template_method(self):
        self.block_navbar()
        self.block_content()
        self.block_footer()

    @abstractmethod
    def block_navbar(self):
        pass

    @abstractmethod
    def block_content(self):
        pass

    @abstractmethod
    def block_footer(self):
        pass


class HomeTemplates(BaseTemplate):
    def block_navbar(self):
        print('Navbar')

    def block_content(self):
        print('Content')

    def block_footer(self):
        print('Footer')


base = HomeTemplates()
base.template_method()
