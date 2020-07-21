from .animals import Animal
from movements import Swimming


class Leech(Animal, Swimming):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num,)
        Swimming.__init__(self)
        self.location = "Pond"

    def feed(self):
        print(
            f'On {self.date_added}, {self.name} crawled on a unsuspecting hippo and ate {self.food}')

    def __str__(self):
        return f"{self.name} is a {self.species}"


# BlackLeech = Leech("Sucker", "gross", "...you know", 15)
# print(BlackLeech.name)
# print(BlackLeech)
# BlackLeech.feed()
