from .animals import Animal
from movements import Walking


class Lizard(Animal, Walking):
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.location = "Glass Tank"
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}"


# Lizardy = Lizard("Split", "reptile", "midday", "crickets", 7)
# print(Lizardy.name)
# print(Lizardy)
# print(Lizardy.feed())
