from .attractions import Attraction


class Wetlands(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)

    # def add_animal(self, animals):
    #     self.animals.extend(animals)
