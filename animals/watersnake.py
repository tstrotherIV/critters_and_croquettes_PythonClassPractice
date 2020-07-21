from .animals import Animal
from movements import Swimming


class Watersnake(Animal, Swimming):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        self.location = "Pond"

    def __str__(self):
        return f"{self.name} is a {self.species}"


# SSSS = Watersnake("Slimey", "snake", "rat", 12)
# print(SSSS.name)
# print(SSSS)
# SSSS.feed()
