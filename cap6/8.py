import random

colors = ['red', 'green', 'blue', 'white', 'black', 'magenta']

names = [ 
    "Tyrell", "Vito" , "Vorian",
     "Winter" , "Zalga", "Zhora", "Zoe", "Zorg"
]

aliens = []

for i in range(100):
    aliens.append(
        {
            "color": random.choice(colors),
            "name":  random.choice(names),
            "rayos-x": random.choice([True, False])
        }
    )


## Show aliens that have x-rays
#for alien in aliens:
#    if alien['rayos-x'] == True:
#        print(f"Nombre {alien['name']} - Color {alien['color']} - Rayos-x {alien['rayos-x']}")


# Create a dictionary that holds the information of
#   how many aliens per color exist
# e.g: { "red": 10, "green": 5, }
# Then print a message displaying how many aliens are of each color