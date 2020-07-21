from .animals import Animal
from movements import Slithering


class Python(Animal, Slithering):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)
        self.location = "Glass Tank"

    def __str__(self):
        return f"{self.name} is a {self.species}"


# Pythoness = Python("Slitherness", "snake", "crickets", 6)
# print(Pythoness.name)
# print(Pythoness)
# Pythoness.feed()
