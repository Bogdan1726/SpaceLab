class Example:
    name = 'Bogdan'
    DEFAULT_AGE = 0

    def __getattr__(self, item):
        if item == 'age':
            return self.DEFAULT_AGE
        else:
            raise AttributeError


example = Example()
print(example.name)
print(example.age)


class Example2:
    def __setattr__(self, attr, value):
        if attr == 'age':
            self.__dict__[attr] = value
        else:
            raise AttributeError


example2 = Example2()
example2.age = 40
print(example2.age)
print(example2.__dict__)
