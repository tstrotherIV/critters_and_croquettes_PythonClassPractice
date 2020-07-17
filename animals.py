from datetime import date
# {Petting Area: sheep, goats, rabbits, ponies, alpacas} {Glass Tank: python, lizard, frog, cricket, salamander } {Pond: gold fish, watersnake, crawdad, catfish}

# {Petting Area: sheep, goats, rabbits, ponies, alpacas}


class Sheep:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = "petting area"
        self.walking = True,
        self.shift = shift
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"


Sheepy = Sheep("Sheepness", "sheep", "morning", "Sheep Chow")
print(Sheepy.name)
print(Sheepy)

print(Sheepy.feed())


class Goats:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = "petting area"
        self.walking = True,
        self.shift = shift
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"


Goatsy = Goats("John", "goat", "midday", "goolosh")
print(Goatsy.name)
print(Goatsy)
print(Goatsy.feed())


class Rabbit:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = "petting area"
        self.walking = True,
        self.shift = shift
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"


Rabbity = Rabbit("Cotton", "rabbit", "afternoon", "Rabit pellets")
print(Rabbity.name)
print(Rabbity)
print(Rabbity.feed())


class Ponies:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = "petting area"
        self.walking = True,
        self.shift = shift
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"


Ponytail = Ponies("Fred", "horse", "midday", "hay")
print(Ponytail.name)
print(Ponytail)
print(Ponytail.feed())


class Alpaca:
    def __init__(self, name, species, shift, food):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = "petting area"
        self.walking = True,
        self.shift = shift
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"


AlpacaMan = Alpaca("Sire", "alpaca", "morning", "alpacasauce")
print(AlpacaMan.name)
roberto = Alpaca("Roberto", "alpaca", "midday", "alpacasauce")
print(f'{roberto.name} the {roberto.species} is available to pet during the {roberto.shift} shift.')
# prints Roberto the alpaca is available to pet during the midday shift.
print(AlpacaMan.feed())
print(AlpacaMan)

# {Glass Tank: python, lizard, frog, cricket, salamander }


class Python:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = "Glass Tank"
        self.slithering = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"


Pythoness = Python("Slitherness", "snake", "crickets")
print(Pythoness.name)
print(Pythoness)
print(Pythoness.feed())


class Lizard:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = "Glass Tank"
        self.shift = shift
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"


Lizardy = Lizard("Split", "reptile", "midday", "crickets")
print(Lizardy.name)
print(Lizardy)
print(Lizardy.feed())


class Frog:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = "Glass Tank"
        self.hopping = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"


FrogNer = Frog("Hoppy", "frog", "crickets")
print(FrogNer.name)
print(FrogNer)
print(FrogNer.feed())


class Cricket:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = "Glass Tank"
        self.hopping = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"


JimminyCricket = Cricket("Jimminy", "cricket", "ants")
print(JimminyCricket.name)
print(JimminyCricket)
print(JimminyCricket.feed())


class Salamander:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = "Glass Tank"
        self.walking = True
        self.shift = shift
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"


YellowSalamander = Salamander(
    "Wiggle", "salamander", "afternoon", "cricket")
print(YellowSalamander.name)
print(YellowSalamander)
print(YellowSalamander.feed())

# {Pond: goldfish, watersnake, crawdad, catfish, leech}


class Goldfish:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = "Pond"
        self.swimming = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"


Goldy = Goldfish("Goldy", "fish", "fish pellets")
print(Goldy.name)
print(Goldy)
print(Goldy.feed())


class Watersnake:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = "Pond"
        self.swimming = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"


SSSS = Watersnake("Slimey", "snake", "rat")
print(SSSS.name)
print(SSSS)
print(SSSS.feed())


class Crawdad:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = "Pond"
        self.swimming = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"


PinchyPinchy = Crawdad("Pinchy", "crustaceans", "fish")
print(PinchyPinchy.name)
print(PinchyPinchy)
print(PinchyPinchy.feed())


class Catfish:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = "Pond"
        self.swimming = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"


MrSucker = Catfish("Whiskers", "fish", "fish pellets")
print(MrSucker.name)
print(MrSucker)
print(MrSucker.feed())


class Leech:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = "Pond"
        self.swimming = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"


BlackLeech = Leech("Sucker", "gross", "scum")
print(BlackLeech.name)
print(BlackLeech)
print(BlackLeech.feed())


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
