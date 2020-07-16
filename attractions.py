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



