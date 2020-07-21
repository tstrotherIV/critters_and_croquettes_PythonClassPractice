from .animals import Animal
from movements import Walking


class Goats(Animal, Walking):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.location = "petting area"
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}"


# Goatsy = Goats("John", "goat", "midday", "goolosh", 2)
# print(Goatsy.name)
# print(Goatsy)
# Goatsy.feed()
