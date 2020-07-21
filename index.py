from animals import Alpaca
from animals import Catfish
from animals import Crawdad
from animals import Cricket
from animals import Frog
from animals import Goats
from animals import Goldfish
from animals import Leech
from animals import Lizard
from animals import Ponies
from animals import Python
from animals import Rabbit
from animals import Salamander
from animals import Sheep
from animals import Watersnake
from animals import Goose
from attractions import PettingZoo
from attractions import Wetlands
from attractions import SnakePit
from attractions import attractions


AlpacaMan = Alpaca("Sire", "alpaca", "morning", "alpacasauce", 5)
AlpacaMan.run()

MrSucker = Catfish("Whiskers", "fish", "fish pellets", 14)
MrSucker.swim()

PinchyPinchy = Crawdad("Pinchy", "crustaceans", "fish", 13)
PinchyPinchy.swim()

JimminyCricket = Cricket("Jimminy", "cricket", "ants", 9)
JimminyCricket.hop()

FrogNer = Frog("Hoppy", "frog", "crickets", 8)
FrogNer.hop()

Goatsy = Goats("John", "goat", "midday", "goolosh", 2)
Goatsy.run()

Goldy = Goldfish("Goldy", "fish", "fish pellets", 11)
Goldy.swim()

BlackLeech = Leech("Sucker", "gross", "...you know", 15)
BlackLeech.swim()

Lizardy = Lizard("Split", "reptile", "midday", "crickets", 7)
Lizardy.run()

Ponytail = Ponies("Fred", "horse", "midday", "hay", 4)
Ponytail.run()

Pythoness = Python("Slitherness", "snake", "crickets", 6)
Pythoness.slither()

Rabbity = Rabbit("Cotton", "rabbit", "afternoon", "Rabit pellets", 3)
Rabbity.hop()

YellowSalamander = Salamander(
    "Wiggle", "salamander", "afternoon", "cricket", 10)
YellowSalamander.run()

Sheepy = Sheep("Sheepness", "sheep", "morning", "Sheep Chow", 1)
Sheepy.run()

SSSS = Watersnake("Slimey", "snake", "rat", 12)
SSSS.swim()

bob = Goose("Bob", "Canada goose", "watercress sandwiches", 16)
bob.run()


# building areas
varmint_village = PettingZoo(
    "Varmint Village", "critters that like to dig and scurry")
varmint_village.add_animal([bob, Sheepy])

for animal in varmint_village.animals:
    print(animal)

PetPet = PettingZoo("PettingZoo", "area to pet animals")
PetPet.add_animal([Sheepy, Goatsy, Rabbity, Ponytail, AlpacaMan])

Slitherland = SnakePit("Slitherland", "area to get bit")
Slitherland.add_animal([Pythoness, SSSS])

WaterWorld = Wetlands(
    "WaterWorld", "explore the creatures that live in the wet world")
WaterWorld.add_animal([Lizardy, FrogNer, JimminyCricket,
                       YellowSalamander, Goldy, PinchyPinchy, MrSucker, BlackLeech])
