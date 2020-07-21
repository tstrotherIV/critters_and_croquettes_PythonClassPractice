from .animals import Animal
from movements import Walking


class Goose(Animal, Walking):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.location = "petting area"

    def run(self):
        print(f'{self} and waddles')

    def __str__(self):
        return f"{self.name} is a {self.species}"
