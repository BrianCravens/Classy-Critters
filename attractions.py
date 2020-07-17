class PettingZoo: 
    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and fuzzy critters to cuddle."
        self.animals = []
    def add_animal(self, animal):
        self.animals.append(animal)
        print(f'You have added {animal.name} the {animal.species} to {self.attraction_name}')
    def __str__(self):
        return f'{self.attraction_name} is full of {self.description}'
    @property
    def last_critter_added(self):
        return (f'Our newest animal in {self.attraction_name} is {self.animals[-1].name} the {self.animals[-1].species}.')

class SnakePit:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "slimy friends that want to squeeze you."
        self.animals = []
    def add_animal(self, animal):
        self.animals.append(animal)
        print(f'You have added {animal.name} the {animal.species} to {self.attraction_name}')
    def __str__(self):
        return f'{self.attraction_name} is full of {self.description}'
    @property
    def last_critter_added(self):
        return (f'Our newest animal in {self.attraction_name} is {self.animals[-1].name} the {self.animals[-1].species}.')
class Wetlands:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "slippery water lovers to play polo with."
        self.animals = []
    def add_animal(self, animal):
        self.animals.append(animal)
        print(f'You have added {animal.name} the {animal.species} to {self.attraction_name}')
    def __str__(self):
        return f'{self.attraction_name} is full of {self.description}'
    @property
    def last_critter_added(self):
        return (f'Our newest animal in {self.attraction_name} is {self.animals[-1].name} the {self.animals[-1].species}.')


def attraction_report (*attractions):
    for attraction in attractions:
        print(f'******CURRENT ANIMALS IN {attraction.attraction_name}******'.upper())
        for animal in attraction.animals:
            print(f'{animal.name} the {animal.species}')



