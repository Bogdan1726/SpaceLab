class Num:

    def __init__(self, num):
        self.num = num

    def __eq__(self, other):
        return self.num == other.num

    def __ne__(self, other):
        return self.num != other.num

    def __gt__(self, other):
        return self.num > other.num

    def __lt__(self, other):
        return self.num < other.num

    def __ge__(self, other):
        return self.num >= other.num

    def __le__(self, other):
        return self.num <= other.num


num1 = Num(10)
num2 = Num(11)
print(num1 <= num2)



