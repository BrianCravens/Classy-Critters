from attractions import *
from animals import *

## Create Animals ##
## Varmint Village ##
frosty = Donkey("Frosty", "Donkey", "Midday", "Hay")
rosco = Lama("Rosco", "Lama", "Morning", "Lama Chow", 123456)
bella = Goat("Bella", "Goat", "Evening", "GoatMeal")
bill = Monkey("Bill", "Monkey", "Morning", "Nuts")
nasty = Lion("Nasty", "Lion", "Midday", "Chicken")

## Snake Pit ##
rusty = Copperhead("Rusty", "Copperhead", "Mice")
ratty = Rat_Snake("Ratty", "Rat Snake", "Rat")
tiny = Anaconda("Tiny", "Anaconda", "Rabbit")
hugs = Python("Hugs", "Python", "Rabbit")
nebuchadnezzar = King_Cobra("Nebuchadnezzar", "King Cobra", "Mice")

## Wetlands ##
tricks = Catfish("Tricks", "Catfish", "Catfood")
froggy = Frog("Froggy", "Frog", "Frog Legs")
daffy = Mallard("Daffy", "Mallard", "Bread")
willy = Goldfish("Willy", "Goldfish", "Fish Flakes")
cuddles = Alligator("Cuddles", "Alligator", "Chicken")

## Create Attractions ##
varmint_village = PettingZoo("Varmint Village")
snake_pit = SnakePit("The Snake Pit")
wetlands = Wetlands("The Wetlands")

## Add Animals to Attractions ##
## Add Varmints ##
varmint_village.add_animal(frosty)
varmint_village.add_animal(rosco)
varmint_village.add_animal(bella)
varmint_village.add_animal(bill)
varmint_village.add_animal(nasty)

## Add Snakes ##
snake_pit.add_animal(rusty)
snake_pit.add_animal(ratty)
snake_pit.add_animal(tiny)
snake_pit.add_animal(hugs)
snake_pit.add_animal(nebuchadnezzar)

## Add Wet Ones ##
wetlands.add_animal(tricks)
wetlands.add_animal(froggy)
wetlands.add_animal(daffy)
wetlands.add_animal(willy)
wetlands.add_animal(cuddles)

## Feed ##
rosco.feed()
frosty.feed()
bella.feed()

##Print Attraction Report##
attraction_report(varmint_village, snake_pit, wetlands)

##Test for Getter and Setter##
rosco.chip_number = 444444
print(rosco.chip_number)

##Newest Animals##
print(varmint_village.last_critter_added)
print(snake_pit.last_critter_added)
print(wetlands.last_critter_added)



