import sys

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
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = {(0, 0): Planet}
        
    def MakeEmpty(self):
        for x in range(0, self.width):
            for y in range(0, self.height):
                self.matrix[(x, y)] = Planet(x, y)
        return self.matrix
    
planetMapObj = PlanetMap(10, 10)
grid = planetMapObj.MakeEmpty()

while True:
    TakeInput()

    
