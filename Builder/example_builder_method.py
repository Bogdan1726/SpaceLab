from abc import ABC, abstractmethod


class Computer:

    def __init__(self, type_pc):
        self.type_pc = type_pc
        self.cpu = None
        self.ram = None
        self.hard_disk = None
        self.power_unit = None
        self.motherboard = None
        self.graphics_card = None
        self.case = None

    def __str__(self):
        return f"Configuration Computer {self.type_pc}:\n" \
               f"Case - {self.case}\n" \
               f"Motherboard - {self.motherboard}\n" \
               f"CPU - {self.cpu}\n" \
               f"Hard disk - {self.hard_disk}\n" \
               f"RAM - {self.ram}\n" \
               f"Power unit - {self.power_unit}\n" \
               f"Graphics card - {self.graphics_card}\n"


class PickerPC(ABC):
    """
    Абстрактный клас строитель
    """

    @abstractmethod
    def installation_motherboard(self):
        pass

    @abstractmethod
    def installation_cpu(self):
        pass

    @abstractmethod
    def installation_ram(self):
        pass

    @abstractmethod
    def installation_hard_disk(self):
        pass

    @abstractmethod
    def installation_power_unit(self):
        pass

    @abstractmethod
    def installation_graphics_card(self):
        pass

    @abstractmethod
    def installation_case(self):
        pass

    @abstractmethod
    def get_computer(self):
        pass


class GamingPC(PickerPC):

    def __init__(self):
        self.type_pc = Computer('Gaming')

    def installation_motherboard(self):
        self.type_pc.motherboard = 'MSI'

    def installation_cpu(self):
        self.type_pc.cpu = 'Intel i9'

    def installation_ram(self):
        self.type_pc.ram = 'Kingston 32gb'

    def installation_hard_disk(self):
        self.type_pc.hard_disk = 'Kingston 1Tb'

    def installation_power_unit(self):
        self.type_pc.power_unit = 'Chieftec 1000W '

    def installation_graphics_card(self):
        self.type_pc.graphics_card = 'Nvidia GeForse RTX 3070 Ti'

    def installation_case(self):
        self.type_pc.case = 'Artline Overlord'

    def get_computer(self):
        return self.type_pc


class BudgetPC(PickerPC):

    def __init__(self):
        self.type_pc = Computer('Budget')

    def installation_motherboard(self):
        self.type_pc.motherboard = 'AMD'

    def installation_cpu(self):
        self.type_pc.cpu = 'AMD FX 4300'

    def installation_ram(self):
        self.type_pc.ram = 'Kingston 8gb'

    def installation_hard_disk(self):
        self.type_pc.hard_disk = 'Kingston 500Gb'

    def installation_power_unit(self):
        self.type_pc.power_unit = 'Chieftec 600W'

    def installation_graphics_card(self):
        self.type_pc.graphics_card = 'Nvidia GeForse RTX 1060 Ti'

    def installation_case(self):
        self.type_pc.case = 'BaseCase'

    def get_computer(self):
        return self.type_pc


class Director:

    def __init__(self):
        self.builder = None

    def set_builder(self, builder: PickerPC):
        self.builder = builder

    def worker(self):
        self.builder.installation_motherboard()
        self.builder.installation_cpu()
        self.builder.installation_ram()
        self.builder.installation_hard_disk()
        self.builder.installation_cpu()
        self.builder.installation_power_unit()
        self.builder.installation_graphics_card()
        self.builder.installation_case()


if __name__ == '__main__':
    director = Director()
    for item in (GamingPC, BudgetPC):
        builder = item()
        director.set_builder(builder)
        director.worker()
        computer = builder.get_computer()
        print(computer)



