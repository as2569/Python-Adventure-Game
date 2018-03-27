import sys
import random

def GetPosition():
    print("Current location {0} {1}".format(player.position.x, player.position.y))
    return player.position


class InputManager():
    def TakeInput(self):
        inString = input("Enter Command \n")
        inString.lstrip()
        inString.lower()
        inList = inString.split()
        if len(inList) > 2:
            print("Too many inputs")
            return
        if len(inList) == 0:
            print("No input")
            return
        
        if inList[0] == "exit":
            print("Goodbye")
            sys.exit()
        elif inList[0] == "move":
            if(len(inList) < 2):
                print("Move command requires a direction")
                return
            self.Move(inList[1])
        else:
            print("Invalid command")

    def Move(self, direction):
        if direction == "north":
            if(player.position.y - 1 >= 0):
                print("Moving north!")
                player.MoveNorth()
                return
        elif direction == "south":
            if(player.position.y + 1 < planetMap.height):
                print("Moving south!")
                player.MoveSouth()
                return
        
        print("Nothing but void that way!")
        return

class Player():
    position = None

    def NewPlayer(self):
        self.position = planetMap.GetRandomPlanet()

    def MoveNorth(self):
        self.position = planetMap.GetPlanetAt(self.position.x, self.position.y - 1)

    def MoveSouth(self):
        self.position = planetMap.GetPlanetAt(self.position.x, self.position.y + 1)

    def MoveEast(self):
        self.position = planetMap.GetPlanetAt(self.position.x + 1, self.position.y)

    def MoveWest(self):
        self.position = planetMap.GetPlanetAt(self.position.x - 1, self.position.y)
        
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

manager = InputManager()
planetMap = Map(10, 10)
planetMap.NewMap()

player = Player()
player.NewPlayer()

while True:
    GetPosition()
    manager.TakeInput()

    
