from .animals import Animal
from movements import Hopping


class Rabbit(Animal, Hopping):
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Hopping.__init__(self)
        self.location = "petting area"
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}"


# Rabbity = Rabbit("Cotton", "rabbit", "afternoon", "Rabit pellets", 3)
# print(Rabbity.name)
# print(Rabbity)
# Rabbity.feed()
