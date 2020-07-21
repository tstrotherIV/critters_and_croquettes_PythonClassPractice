from .animals import Animal
from movements import Swimming


class Goldfish(Animal, Swimming):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        self.location = "Pond"

    def __str__(self):
        return f"{self.name} is a {self.species}"


# Goldy = Goldfish("Goldy", "fish", "fish pellets", 11)
# print(Goldy.name)
# print(Goldy)
# Goldy.feed()
