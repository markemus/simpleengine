creatureLocations = {}

class location(object):

    def __init__(self, x, y):
        self.localMap = [["X" for a in range(x)] for b in range(y)]

        rowIndex, colIndex = 0,0

        for col in self.localMap:

            rowIndex = 0
            
            for row in col:
                creatureLocations[(self, rowIndex, colIndex)] = None
                rowIndex += 1

            colIndex += 1

    def getMap(self):
        return self.localMap

    def setMap(self, x, y, character):
        self.localMap[x][y] = character

    def printMap(self):
        mLocalMap = self.getMap()

        print("")
        
        for col in mLocalMap:
            rowAppearance = ""
        
            for row in col:
                rowAppearance = rowAppearance + row

            print(rowAppearance)

        print("")

# unclassed scripts

def getCreatureLocations(location):
    return creatureLocations[location]

def setCreatureLocations(location, creature):
    creatureLocations[location] = creature

# main

loader = location(1,1)
plaza = location(7,7)