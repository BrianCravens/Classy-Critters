from datetime import date

class Lama: 
    def __init__(self, name, species, shift, food, chip_num):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()
        self.food = food
        self.__chip_number = chip_num
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f'{self.name} is a {self.species}'

    @property
    def chip_number(self):
        return self.__chip_number
    @chip_number.setter
    def chip_number(self, num):
        pass

class Donkey: 
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f'{self.name} is a {self.species}'

class Goat: 
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f'{self.name} is a {self.species}'

class Monkey: 
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f'{self.name} is a {self.species}'

class Lion: 
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f'{self.name} is a {self.species}'

class Copperhead: 
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f'{self.name} is a {self.species}'

class Rat_Snake: 
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f'{self.name} is a {self.species}'

class Anaconda: 
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f'{self.name} is a {self.species}'

class Python: 
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f'{self.name} is a {self.species}'

class King_Cobra: 
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f'{self.name} is a {self.species}'

class Catfish: 
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f'{self.name} is a {self.species}'

class Frog: 
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f'{self.name} is a {self.species}'

class Mallard: 
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f'{self.name} is a {self.species}'

class Goldfish: 
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f'{self.name} is a {self.species}'

class Alligator: 
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f'{self.name} is a {self.species}'