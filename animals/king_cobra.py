from .animal import Animal
from movements import Slithering

class King_Cobra(Animal, Slithering): 
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)