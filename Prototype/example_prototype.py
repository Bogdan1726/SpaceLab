import copy


class OperationSystem:
    def __init__(self, operation_system, version):
        self.operation_system = operation_system
        self.version = version

    def __str__(self):
        return f'{self.operation_system}'


class Robot:

    def __init__(self, name, power, type_operation_system):
        self.name = name
        self.power = power
        self.type_operation_system = type_operation_system

    def __str__(self):
        return f'I am Robot\n' \
               f'My name is - {self.name}\n' \
               f'My power is - {self.power} and me operation_system - {self.type_operation_system}'


if __name__ == '__main__':
    system = OperationSystem('Android', '1.0')
    alisa = Robot('Alisa', '2000w', system)
    print(alisa)
    siri = copy.deepcopy(alisa)
    print("-- // --")
    siri.name = 'Siri'
    siri.type_operation_system = 'iOS'
    print(alisa)
    print("-- // --")
    print(siri)
