class Singleton:

    __instances = None

    def __new__(cls, *args, **kwargs):
        if cls.__instances is None:
            cls.__instances = super(Singleton, cls).__new__(cls)
        return cls.__instances


class Test(Singleton):
    pass


if __name__ == '__main__':
    one = Test()
    two = Test()
    print(one is two)


class SingletonMeta(type):
    """
    Meta class
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    pass


if __name__ == "__main__":

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
