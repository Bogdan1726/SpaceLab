class City:

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __new__(cls, name, population):
        instance = super(City, cls).__new__(cls)
        if population > 1500:
            return instance
        else:
            return 'Your city is too small'

    def __str__(self):
        return f'City {self.name} - {self.population} people'


people = City('Dnipro', 1000)
print(people)
