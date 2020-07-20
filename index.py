from attractions import *
from animals import *

## Create Animals ##
## Varmint Village ##
frosty = Donkey("Frosty", "Donkey", "Midday", "Hay", 19378387)
rosco = Lama("Rosco", "Lama", "Morning", "Lama Chow", 123456)
bella = Goat("Bella", "Goat", "Evening", "GoatMeal", 101893843)
bill = Monkey("Bill", "Monkey", "Morning", "Nuts", 1924747)
nasty = Lion("Nasty", "Lion", "Midday", "Chicken", 129305854)

## Snake Pit ##
rusty = Copperhead("Rusty", "Copperhead", "Mice", 1212)
ratty = Rat_Snake("Ratty", "Rat Snake", "Rat", 1112222)
tiny = Anaconda("Tiny", "Anaconda", "Rabbit", 1917324784)
hugs = Python("Hugs", "Python", "Rabbit", 12298766)
nebuchadnezzar = King_Cobra("Nebuchadnezzar", "King Cobra", "Mice", 121233333)

## Wetlands ##
tricks = Catfish("Tricks", "Catfish", "Catfood", 323232323)
froggy = Frog("Froggy", "Frog", "Frog Legs", 9987766)
daffy = Mallard("Daffy", "Mallard", "Bread", 8767565422)
willy = Goldfish("Willy", "Goldfish", "Fish Flakes", 876756545)
cuddles = Alligator("Cuddles", "Alligator", "Chicken", 98765665)

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
rusty.feed()

##Print Attraction Report##
attraction_report(varmint_village, snake_pit, wetlands)

##Test for Getter and Setter##
rosco.chip_num = 4444444
print(rosco.chip_num)

##Newest Animals##
print(varmint_village.last_critter_added)
print(snake_pit.last_critter_added)
print(wetlands.last_critter_added)



