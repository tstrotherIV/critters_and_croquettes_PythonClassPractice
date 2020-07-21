from .animals import Animal
from movements import Swimming


class Crawdad(Animal, Swimming):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        self.location = "Pond"

    def feed(self):
        print(
            f"{self.name} sat on a rock underwater listening to Lynyrd Skynyrd and ate {self.food}.")

    def __str__(self):
        return f"{self.name} is a {self.species}"


# PinchyPinchy = Crawdad("Pinchy", "crustaceans", "fish", 13)
# print(PinchyPinchy.name)
# print(PinchyPinchy)
# PinchyPinchy.feed()
