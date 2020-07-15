from datetime import date

class Lama: 
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()

rosco = Lama("Rosco", "Lama", "Morning")
print(f'{rosco.name} the {rosco.species} is available for face-spitting during the {rosco.shift} shift.')

class Donkey: 
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()

frosty = Donkey("Frosty", "Donkey", "Midday")
print(f'{frosty.name} the {frosty.species} is available for pictures during the {frosty.shift} shift.')

class Goat: 
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()

bella = Goat("Bella", "Goat", "Evening")

class Monkey: 
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()

bill = Monkey("Bill", "Monkey", "Morning")

class Lion: 
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()

nasty = Lion("Nasty", "Lion", "Midday")

class Copperhead: 
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

rusty = Copperhead("Rusty", "Copperhead")
class Rat_Snake: 
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

ratty = Rat_Snake("Ratty", "Rat_Snake")

class Anaconda: 
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

tiny = Anaconda("Tiny", "Anaconda")

class Python: 
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

hugs = Python("Hugs", "Python")

class King_Cobra: 
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

nebuchadnezzar = King_Cobra("Nebuchadnezzar", "King Cobra")

class Catfish: 
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

tricks = Catfish("Tricks", "Catfish")

class Frog: 
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

froggy = Frog("Froggy", "Frog")

class Mallard: 
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

daffy = Mallard("Daffy", "Mallard")

class Goldfish: 
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

willy = Goldfish("Willy", "Goldfish")

class Alligator: 
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

cuddles = Alligator("Cuddles", "Alligator")