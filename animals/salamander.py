from .animals import Animal
from movements import Walking


class Salamander(Animal, Walking):
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.location = "Glass Tank"
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}"


# YellowSalamander = Salamander(
#     "Wiggle", "salamander", "afternoon", "cricket", 10)
# print(YellowSalamander.name)
# print(YellowSalamander)
# YellowSalamander.feed()
