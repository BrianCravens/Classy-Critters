from datetime import date

class Lama: 
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

rosco = Lama("Rosco", "Lama", "Morning", "Lama Chow")
print(f'{rosco.name} the {rosco.species} is available for face-spitting during the {rosco.shift} shift.')

print(rosco)


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


frosty = Donkey("Frosty", "Donkey", "Midday", "Hay")

print(f'{frosty.name} the {frosty.species} is available for pictures during the {frosty.shift} shift.')

print(frosty.feed())

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

bella = Goat("Bella", "Goat", "Evening", "GoatMeal")

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

bill = Monkey("Bill", "Monkey", "Morning", "Nuts")

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

nasty = Lion("Nasty", "Lion", "Midday", "Chicken")

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

rusty = Copperhead("Rusty", "Copperhead", "Mice")

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

ratty = Rat_Snake("Ratty", "Rat_Snake", "Rat")

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

tiny = Anaconda("Tiny", "Anaconda", "Rabbit")

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

hugs = Python("Hugs", "Python", "Rabbit")

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

nebuchadnezzar = King_Cobra("Nebuchadnezzar", "King Cobra", "Mice")

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

tricks = Catfish("Tricks", "Catfish", "Catfood")

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

froggy = Frog("Froggy", "Frog", "Frog Legs")

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

daffy = Mallard("Daffy", "Mallard", "Bread")

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

willy = Goldfish("Willy", "Goldfish", "Fish Flakes")
print(willy.feed())

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

cuddles = Alligator("Cuddles", "Alligator", "Chicken")
print(cuddles.feed())

