# from animals import Sheepy
# from animals import Goatsy
# from animals import Rabbity
# from animals import Ponytail
# from animals import AlpacaMan
# from animals import Pythoness
# from animals import Lizardy
# from animals import FrogNer
# from animals import JimminyCricket
# from animals import YellowSalamander
# from animals import Goldy
# from animals import SSSS
# from animals import PinchyPinchy
# from animals import MrSucker
# from animals import BlackLeech


class Attraction:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def __str__(self):
        return f'{self.name} ({len(self)} animals)'

    def __len__(self):
        return len(self.animals)

#


# PetPet = PettingZoo("PettingZoo", "area to pet animals")
# Slitherland = SnakePit("Slitherland", "area to get bit")
# WaterWorld = Wetlands(
#     "WaterWorld", "explore the creatures that live in the wet world")

# PetPet.add_animal([Sheepy, Goatsy, Rabbity, Ponytail, AlpacaMan])

# Slitherland.add_animal([Pythoness, SSSS])

# WaterWorld.add_animal([Lizardy, FrogNer, JimminyCricket,
#                        YellowSalamander, Goldy, PinchyPinchy, MrSucker, BlackLeech])

# print(PetPet.last_critter_added)
