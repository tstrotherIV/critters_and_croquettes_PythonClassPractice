from datetime import date
# {Petting Area: sheep, goats, rabbits, ponies, alpacas} {Glass Tank: python, lizard, frog, cricket, salamander } {Pond: gold fish, watersnake, crawdad, catfish}

# {Petting Area: sheep, goats, rabbits, ponies, alpacas}


class Sheep:
    def __init__(self, name, species, date_added, location, walking):
        self.name = name
        self.species = species
        self.date_added = date_added
        self.location = location
        self.walking = walking


Sheepy = Sheep("Sheepness", "sheep", date.today(), "petting area", True)
print(Sheepy.name)


class Goats:
    def __init__(self, name, species, date_added, location, walking):
        self.name = name
        self.species = species
        self.date_added = date_added
        self.location = location
        self.walking = walking


Goatsy = Goats("John", "goat", date.today(), "petting area", True)
print(Goatsy.name)


class Rabbit:
    def __init__(self, name, species, date_added, location, walking):
        self.name = name
        self.species = species
        self.date_added = date_added
        self.location = location
        self.walking = walking


Rabbity = Rabbit("Cotton", "rabbit", date.today(), "petting area", True)
print(Rabbity.name)


class Ponies:
    def __init__(self, name, species, date_added, location, walking):
        self.name = name
        self.species = species
        self.date_added = date_added
        self.location = location
        self.walking = walking


Ponytail = Ponies("Fred", "horse", date.today(), "petting area", True)
print(Ponytail.name)


class Alpaca:
    def __init__(self, name, species, date_added, location, walking):

        self.name = name
        self.species = species
        self.date_added = date_added
        self.location = location
        self.walking = walking


AlpacaMan = Alpaca("Sire", "alpaca", date.today(), "petting area", True)
print(AlpacaMan.name)


# {Glass Tank: python, lizard, frog, cricket, salamander }


class Python:
    def __init__(self, name, species, date_added, location, slithering):
        self.name = name
        self.species = species
        self.date_added = date_added
        self.location = location
        self.slithering = slithering


Pythoness = Python("Slitherness", "snake", date.today(), "glass tank", True)
print(Pythoness.name)


class Lizard:
    def __init__(self, name, species, date_added, location, walking):
        self.name = name
        self.species = species
        self.date_added = date_added
        self.location = location
        self.walking = walking


Lizardy = Lizard("Split", "reptile", date.today(), "glass tank", True)
print(Lizardy.name)


class Frog:
    def __init__(self, name, species, date_added, location, walking):
        self.name = name
        self.species = species
        self.date_added = date_added
        self.location = location
        self.walking = walking


FrogNer = Frog("Hoppy", "frog", date.today(), "glass tank", True)
print(FrogNer.name)


class Cricket:
    def __init__(self, name, species, date_added, location, walking):
        self.name = name
        self.species = species
        self.date_added = date_added
        self.location = location
        self.walking = walking


JimminyCricket = Cricket("Jimminy", "cricket",
                         date.today(), "glass tank", True)
print(JimminyCricket.name)


class Salamander:
    def __init__(self, name, species, date_added, location, walking):
        self.name = name
        self.species = species
        self.date_added = date_added
        self.location = location
        self.walking = walking


YellowSalamander = Salamander("Wiggle", "salamander",
                              date.today(), "glass tank", True)
print(YellowSalamander.name)

# {Pond: goldfish, watersnake, crawdad, catfish, leech}


class Goldfish:
    def __init__(self, name, species, date_added, location, swimming):
        self.name = name
        self.species = species
        self.date_added = date_added
        self.location = location
        self.swimming = swimming


Goldy = Goldfish("Goldy", "fish", date.today(), "pond", True)
print(Goldy.name)


class Watersnake:
    def __init__(self, name, species, date_added, location, swimming):
        self.name = name
        self.species = species
        self.date_added = date_added
        self.location = location
        self.swimming = swimming


SSSS = Watersnake("Slimey", "snake", date.today(), "pond", True)
print(SSSS.name)


class Crawdad:
    def __init__(self, name, species, date_added, location, swimming):
        self.name = name
        self.species = species
        self.date_added = date_added
        self.location = location
        self.swimming = swimming


PinchyPinchy = Crawdad("Pinchy", "crustaceans", date.today(), "pond", True)
print(PinchyPinchy.name)


class Catfish:
    def __init__(self, name, species, date_added, location, swimming):
        self.name = name
        self.species = species
        self.date_added = date_added
        self.location = location
        self.swimming = swimming


MrSucker = Catfish("Whiskers", "fish", date.today(), "pond", True)
print(MrSucker.name)


class Leech:
    def __init__(self, name, species, date_added, location, swimming):
        self.name = name
        self.species = species
        self.date_added = date_added
        self.location = location
        self.swimming = swimming


BlackLeech = Leech("Sucker", "gross", date.today(), "pond", True)
print(BlackLeech.name)
