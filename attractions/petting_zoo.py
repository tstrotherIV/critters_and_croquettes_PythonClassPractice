from .attractions import Attraction


class PettingZoo(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)

    def add_animal(self, animals):
        try:
            if animals.walk_speed > -1:
                self.animals.append(animals)
        except AttributeError as ex:
            print(
                f'{animal} doesn\'t like to be petted, so please do not put it in the {self.name} attraction.')

    @property
    def last_critter_added(self):
        return f'{self.animals[-1]}'
