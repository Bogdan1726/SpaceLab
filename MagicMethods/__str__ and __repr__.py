class Lion:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name}'


lion1 = Lion('Gon')
lion2 = Lion('Jek')
animals = [lion1, lion2]

print(animals)
