from .attractions import Attraction


class PettingZoo(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)

    # def add_animal(self, animals):
    #     self.animals.extend(animals)

    @property
    def last_critter_added(self):
        return f'{self.animals[-1]}'
