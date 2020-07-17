from attractions import WaterWorld
from attractions import Slitherland
from attractions import PetPet


def WaterWorldstr():
    print(f"WaterWorld is where you'll find all the wonderful things that will slime you: like:")
    for animal in WaterWorld.animals:
        print(f"  * {animal.name} the {animal.species}")


WaterWorldstr()


def Slitherlandstr():
    print(f"Slitherland is where you'll find all the wonderful things you can pet: like:")
    for animal in Slitherland.animals:
        print(f"  * {animal.name} the {animal.species}")


Slitherlandstr()


def PetPetstr():
    print(f"PetPet is where you'll find all the wonderful things you can run away from: like:")
    for animal in PetPet.animals:
        print(f"  * {animal.name} the {animal.species}")


PetPetstr()
