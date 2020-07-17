from animals import Sheepy
from animals import Goatsy
from animals import Rabbity
from animals import Ponytail
from animals import AlpacaMan
from animals import Pythoness
from animals import Lizardy
from animals import FrogNer
from animals import JimminyCricket
from animals import YellowSalamander
from animals import Goldy
from animals import SSSS
from animals import PinchyPinchy
from animals import MrSucker
from animals import BlackLeech


# Creating Attracions in the business
class PettingZoo:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animals):
        self.animals.extend(animals)


class SnakePit:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animals):
        self.animals.extend(animals)


class Wetlands:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animals):
        self.animals.extend(animals)


PetPet = PettingZoo("PettingZoo", "area to pet animals")
Slitherland = SnakePit("Slitherland", "area to get bit")
WaterWorld = Wetlands(
    "WaterWorld", "explore the creatures that live in the wet world")

PetPet.add_animal([Sheepy, Goatsy, Rabbity, Ponytail, AlpacaMan])

Slitherland.add_animal([Pythoness, SSSS])

WaterWorld.add_animal([Lizardy, FrogNer, JimminyCricket,
                       YellowSalamander, Goldy, PinchyPinchy, MrSucker, BlackLeech])
