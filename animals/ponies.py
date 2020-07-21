from .animals import Animal
from movements import Walking


class Ponies(Animal, Walking):
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.location = "petting area"
        self.shift = shift

    def run(self):
        print(f'{self} and canters')

    def __str__(self):
        return f"{self.name} is a {self.species}"


# Ponytail = Ponies("Fred", "horse", "midday", "hay", 4)
# print(Ponytail.name)
# print(Ponytail)
# Ponytail.feed()
