from datetime import date
from .animal import Animal
from movements import Walking

class Lama(Animal, Walking): 
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)

    def feed(self):
        print(f'{self.name} was fed {self.food}, and given their antibiotic on {date.today().strftime("%m/%d/%Y")}')