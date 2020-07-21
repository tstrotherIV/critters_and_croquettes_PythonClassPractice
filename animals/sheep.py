from .animals import Animal
from movements import Walking


class Sheep(Animal, Walking):
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.location = "petting area"
        self.shift = shift

    def feed(self):
        print(
            f'On {self.date_added}, {self.name} had "Rockytop" sung to it so it would eat its {self.food}')

    def __str__(self):
        return f"{self.name} is a {self.species}"


# Sheepy = Sheep("Sheepness", "sheep", "morning", "Sheep Chow", 1)
# print(Sheepy.name)
# print(Sheepy)
# # print(Sheepy.chip_number)

# Sheepy.feed()
