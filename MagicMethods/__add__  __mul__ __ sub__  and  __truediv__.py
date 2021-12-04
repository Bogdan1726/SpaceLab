class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        print('__add__')
        print(self.balance + other)

    def __mul__(self, other):
        print('__mul__')
        print(self.balance * other)

    def __sub__(self, other):
        print('__sub__')
        print(self.balance - other)

    def __truediv__(self, other):
        print('__truediv__')
        print(self.balance / other)


ivan = BankAccount('Ivan', 2000)
ivan + 2000
ivan * 3
ivan - 500
ivan / 2
