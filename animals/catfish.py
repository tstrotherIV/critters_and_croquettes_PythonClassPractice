from .animals import Animal
from movements import Swimming


class Catfish(Animal, Swimming):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        self.location = "Pond"

    def __str__(self):
        return f"{self.name} is a {self.species}"


# MrSucker = Catfish("Whiskers", "fish", "fish pellets", 14)
# print(MrSucker.name)
# print(MrSucker)
# MrSucker.feed()
