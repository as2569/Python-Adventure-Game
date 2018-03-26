import sys
import random

def GetPosition():
    print("Current location {0} {1}".format(player.position.x, player.position.y))
    return player.position

def TakeInput():
    in_str = input("Enter Command \n")
    in_str.lstrip()
    if in_str == "exit":
        print("Goodbye")
        sys.exit()
    else:
        print("Invalid command")

class Player():
    position = None

    def NewPlayer(self):
        self.position = planetMap.GetRandomPlanet()
                
class Planet():
    def __init__(self, x, y):
        self.x = x
        self.y = y
            
class Map():
    matrix = {}
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def NewMap(self):
        for x in range(0, self.width):
            for y in range(0, self.height):
                self.matrix[(x, y)] = Planet(x, y)

    def GetPlanetAt(self, x, y):
        return self.matrix[(x, y)]
    
    def GetRandomPlanet(self):
        x = random.randrange(0, self.width - 1)
        y = random.randrange(0, self.height - 1)
        return self.matrix[(x, y)]
        
planetMap = Map(10, 10)
planetMap.NewMap()

player = Player()
player.NewPlayer()

while True:
    GetPosition()
    TakeInput()

    
