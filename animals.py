from datetime import date

class Animal:
    def __init__(self, name, species, food, chip_num ):
        self.name = name
        self.species = species
        self.food = food
        self.__chip_num = chip_num
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f'{self.name} is a {self.species}'

    @property
    def chip_num(self):
        return self.__chip_num
    @chip_num.setter
    def chip_num(self, chip_num):
        pass

class Lama(Animal): 
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True

    def feed(self):
        print(f'{self.name} was fed {self.food}, and given their antibiotic on {date.today().strftime("%m/%d/%Y")}')
    

class Donkey(Animal): 
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True

    def feed(self):
        print(f'{self.name} was fed {self.food}, and given their antibiotic on {date.today().strftime("%m/%d/%Y")}')

class Goat(Animal): 
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True
    
    def feed(self):
        print(f'{self.name} was fed {self.food}, and given their antibiotic on {date.today().strftime("%m/%d/%Y")}')

class Monkey(Animal): 
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True

    def feed(self):
        print(f'{self.name} was fed {self.food}, and given their antibiotic on {date.today().strftime("%m/%d/%Y")}')

class Lion(Animal): 
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True

    def feed(self):
        print(f'{self.name} was fed {self.food}, and given their antibiotic on {date.today().strftime("%m/%d/%Y")}')

class Copperhead(Animal): 
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

class Rat_Snake(Animal): 
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

class Anaconda(Animal): 
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

class Python(Animal): 
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

class King_Cobra(Animal): 
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

class Catfish(Animal): 
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

class Frog(Animal): 
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

class Mallard(Animal): 
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

class Goldfish(Animal): 
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

class Alligator(Animal): 
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True