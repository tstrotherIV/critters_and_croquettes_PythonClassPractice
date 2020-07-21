from .animals import Animal
from movements import Hopping


class Frog(Animal, Hopping):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Hopping.__init__(self)
        self.location = "Glass Tank"

    def __str__(self):
        return f"{self.name} is a {self.species}"


# FrogNer = Frog("Hoppy", "frog", "crickets", 8)
# print(FrogNer.name)
# print(FrogNer)
# FrogNer.feed()
