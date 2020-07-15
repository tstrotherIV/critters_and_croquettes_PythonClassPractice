from datetime import date
# {Petting Area: sheep, goats, rabbits, ponies, alpacas} {Glass Tank: python, lizard, frog, cricket, salamander } {Pond: gold fish, watersnake, crawdad, catfish}

# {Petting Area: sheep, goats, rabbits, ponies, alpacas}


class Sheep:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = "petting area"
        self.walking = True,
        self.shift = shift


Sheepy = Sheep("Sheepness", "sheep", "morning'")
print(Sheepy.name)


class Goats:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = "petting area"
        self.walking = True,
        self.shift = shift


Goatsy = Goats("John", "goat", "midday")
print(Goatsy.name)


class Rabbit:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = "petting area"
        self.walking = True,
        self.shift = shift


Rabbity = Rabbit("Cotton", "rabbit", "afternoon")
print(Rabbity.name)


class Ponies:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = "petting area"
        self.walking = True,
        self.shift = shift


Ponytail = Ponies("Fred", "horse", "midday")
print(Ponytail.name)


class Alpaca:
    def __init__(self, name, species, shift):

        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = "petting area"
        self.walking = True,
        self.shift = shift


AlpacaMan = Alpaca("Sire", "alpaca", "morning")
print(AlpacaMan.name)
roberto = Alpaca("Roberto", "alpaca", "midday")
print(f'{roberto.name} the {roberto.species} is available to pet during the {roberto.shift} shift.')
# prints Roberto the alpaca is available to pet during the midday shift.

# {Glass Tank: python, lizard, frog, cricket, salamander }


class Python:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = "Glass Tank"
        self.slithering = True


Pythoness = Python("Slitherness", "snake")
print(Pythoness.name)


class Lizard:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = "Glass Tank"
        self.shift = shift


Lizardy = Lizard("Split", "reptile", "midday")
print(Lizardy.name)


class Frog:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = "Glass Tank"
        self.hopping = True


FrogNer = Frog("Hoppy", "frog")
print(FrogNer.name)


class Cricket:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = "Glass Tank"
        self.hopping = True


JimminyCricket = Cricket("Jimminy", "cricket")
print(JimminyCricket.name)


class Salamander:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = "Glass Tank"
        self.walking = True
        self.shift = shift


YellowSalamander = Salamander(
    "Wiggle", "salamander", "afternoon")
print(YellowSalamander.name)

# {Pond: goldfish, watersnake, crawdad, catfish, leech}


class Goldfish:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = "Pond"
        self.swimming = True


Goldy = Goldfish("Goldy", "fish")
print(Goldy.name)


class Watersnake:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = "Pond"
        self.swimming = True


SSSS = Watersnake("Slimey", "snake")
print(SSSS.name)


class Crawdad:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = "Pond"
        self.swimming = True


PinchyPinchy = Crawdad("Pinchy", "crustaceans")
print(PinchyPinchy.name)


class Catfish:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = "Pond"
        self.swimming = True


MrSucker = Catfish("Whiskers", "fish")
print(MrSucker.name)


class Leech:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = "Pond"
        self.swimming = True


BlackLeech = Leech("Sucker", "gross")
print(BlackLeech.name)
