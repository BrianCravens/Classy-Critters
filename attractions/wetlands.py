from attractions.attraction import Attraction

class Wetlands(Attraction):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.attraction_name = name
        self.description = description
    
    @property
    def last_critter_added(self):
        return (f'Our newest animal in {self.attraction_name} is {self.animals[-1].name} the {self.animals[-1].species}.')