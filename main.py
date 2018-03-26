import sys
import random

class Player():
    position = None
                
class Planet():
    def __init__(self, x, y):
        self.x = x
        self.y = y
            
def TakeInput():
    in_str = input("Enter Command \n")
    in_str.lstrip()
    if in_str == "exit":
        print("Goodbye")
        sys.exit()
    else:
        print("Invalid command")


class PlanetMap():
    matrix = {}
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def MakeEmpty(self):
        for x in range(0, self.width):
            for y in range(0, self.height):
                self.matrix[(x, y)] = Planet(x, y)

    def GetPlanetAt(self, x, y):
        return self.matrix[(x, y)]
    
    def GetRandomPlanet(self):
        x = random.randint(0, self.width)
        y = random.randint(0, self.height)
        return self.GetPlanetAt(x, y)
        
planetMap = PlanetMap(10, 10)
planetMap.MakeEmpty()
currentPlanet = planetMap.GetRandomPlanet()

while True:
    TakeInput()

    
