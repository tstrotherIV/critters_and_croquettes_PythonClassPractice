from datetime import date
# {Petting Area: sheep, goats, rabbits, ponies, alpacas} {Glass Tank: python, lizard, frog, cricket, salamander } {Pond: gold fish, watersnake, crawdad, catfish}


class Animal:
    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.food = food
        self.__chip_number = chip_num
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    @property
    def chip_number(self):
        return self.__chip_number

    @chip_number.setter
    def chip_number(self, num):
        pass


# {Petting Area: sheep, goats, rabbits, ponies, alpacas}

class Sheep(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.location = "petting area"
        self.walking = True,
        self.shift = shift

    def feed(self):
        print(f'On {date.today().strftime("%m/%d/%Y")}, {self.name} had "Rockytop" sung to it so it would eat its {self.food}')

    def __str__(self):
        return f"{self.name} is a {self.species}"


Sheepy = Sheep("Sheepness", "sheep", "morning", "Sheep Chow", 1)
print(Sheepy.name)
print(Sheepy)
# print(Sheepy.chip_number)

Sheepy.feed()


class Goats(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.location = "petting area"
        self.walking = True,
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}"


Goatsy = Goats("John", "goat", "midday", "goolosh", 2)
print(Goatsy.name)
print(Goatsy)
Goatsy.feed()


class Rabbit(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.location = "petting area"
        self.walking = True,
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}"


Rabbity = Rabbit("Cotton", "rabbit", "afternoon", "Rabit pellets", 3)
print(Rabbity.name)
print(Rabbity)
Rabbity.feed()


class Ponies(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.location = "petting area"
        self.walking = True,
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}"


Ponytail = Ponies("Fred", "horse", "midday", "hay", 4)
print(Ponytail.name)
print(Ponytail)
Ponytail.feed()


class Alpaca(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.location = "petting area"
        self.walking = True,
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}"


AlpacaMan = Alpaca("Sire", "alpaca", "morning", "alpacasauce", 5)
print(AlpacaMan.name)
roberto = Alpaca("Roberto", "alpaca", "midday", "alpacasauce", 5)
print(f'{roberto.name} the {roberto.species} is available to pet during the {roberto.shift} shift.')
# prints Roberto the alpaca is available to pet during the midday shift.
AlpacaMan.feed()
print(AlpacaMan)

# {Glass Tank: python, lizard, frog, cricket, salamander }


class Python(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.location = "Glass Tank"
        self.slithering = True

    def __str__(self):
        return f"{self.name} is a {self.species}"


Pythoness = Python("Slitherness", "snake", "crickets", 6)
print(Pythoness.name)
print(Pythoness)
Pythoness.feed()


class Lizard(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.location = "Glass Tank"
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}"


Lizardy = Lizard("Split", "reptile", "midday", "crickets", 7)
print(Lizardy.name)
print(Lizardy)
print(Lizardy.feed())


class Frog(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.location = "Glass Tank"
        self.hopping = True

    def __str__(self):
        return f"{self.name} is a {self.species}"


FrogNer = Frog("Hoppy", "frog", "crickets", 8)
print(FrogNer.name)
print(FrogNer)
FrogNer.feed()


class Cricket(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.location = "Glass Tank"
        self.hopping = True

    def __str__(self):
        return f"{self.name} is a {self.species}"


JimminyCricket = Cricket("Jimminy", "cricket", "ants", 9)
print(JimminyCricket.name)
print(JimminyCricket)
JimminyCricket.feed()


class Salamander(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.location = "Glass Tank"
        self.walking = True
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}"


YellowSalamander = Salamander(
    "Wiggle", "salamander", "afternoon", "cricket", 10)
print(YellowSalamander.name)
print(YellowSalamander)
YellowSalamander.feed()

# {Pond: goldfish, watersnake, crawdad, catfish, leech}


class Goldfish(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.location = "Pond"
        self.swimming = True

    def __str__(self):
        return f"{self.name} is a {self.species}"


Goldy = Goldfish("Goldy", "fish", "fish pellets", 11)
print(Goldy.name)
print(Goldy)
Goldy.feed()


class Watersnake(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.location = "Pond"
        self.swimming = True

    def __str__(self):
        return f"{self.name} is a {self.species}"


SSSS = Watersnake("Slimey", "snake", "rat", 12)
print(SSSS.name)
print(SSSS)
SSSS.feed()


class Crawdad(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.location = "Pond"
        self.swimming = True

    def feed(self):
        print(
            f"{self.name} sat on a rock underwater listening to Lynyrd Skynyrd and ate {self.food}.")

    def __str__(self):
        return f"{self.name} is a {self.species}"


PinchyPinchy = Crawdad("Pinchy", "crustaceans", "fish", 13)
print(PinchyPinchy.name)
print(PinchyPinchy)
PinchyPinchy.feed()


class Catfish(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.location = "Pond"
        self.swimming = True

    def __str__(self):
        return f"{self.name} is a {self.species}"


MrSucker = Catfish("Whiskers", "fish", "fish pellets", 14)
print(MrSucker.name)
print(MrSucker)
MrSucker.feed()


class Leech(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.location = "Pond"
        self.swimming = True

    def feed(self):
        print(f'On {date.today().strftime("%m/%d/%Y")}, {self.name} crawled on a unsuspecting hippo and ate {self.food}')

    def __str__(self):
        return f"{self.name} is a {self.species}"


BlackLeech = Leech("Sucker", "gross", "...you know", 15)
print(BlackLeech.name)
print(BlackLeech)
BlackLeech.feed()


# # Creating Attracions in the business
# class PettingZoo:

#     def __init__(self, name, description):
#         self.attraction_name = name
#         self.description = description
#         self.animals = list()

#     def add_animal(self, animals):
#         self.animals.extend(animals)


# class SnakePit:

#     def __init__(self, name, description):
#         self.attraction_name = name
#         self.description = description
#         self.animals = list()

#     def add_animal(self, animals):
#         self.animals.extend(animals)


# class Wetlands:

#     def __init__(self, name, description):
#         self.attraction_name = name
#         self.description = description
#         self.animals = list()

#     def add_animal(self, animals):
#         self.animals.extend(animals)


# PetPet = PettingZoo("PettingZoo", "area to pet animals")
# Slitherland = SnakePit("Slitherland", "area to get bit")
# WaterWorld = Wetlands(
#     "WaterWorld", "explore the creatures that live in the wet world")

# PetPet.add_animal([Sheepy, Goatsy, Rabbity, Ponytail, AlpacaMan])


# def PetPetstr():
#     print(f"PetPet is where you'll find all the wonderful things you can run away from: like:")
#     for animal in PetPet.animals:
#         print(f"  * {animal.name} the {animal.species}")


# PetPetstr()

# Slitherland.add_animal([Pythoness, SSSS])


# def Slitherlandstr():
#     print(f"Slitherland is where you'll find all the wonderful things you can pet: like:")
#     for animal in Slitherland.animals:
#         print(f"  * {animal.name} the {animal.species}")


# Slitherlandstr()

# WaterWorld.add_animal([Lizardy, FrogNer, JimminyCricket,
#                        YellowSalamander, Goldy, PinchyPinchy, MrSucker, BlackLeech])


# def WaterWorldstr():
#     print(f"WaterWorld is where you'll find all the wonderful things that will slime you: like:")
#     for animal in WaterWorld.animals:
#         print(f"  * {animal.name} the {animal.species}")


# WaterWorldstr()
