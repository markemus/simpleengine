from items import *

class creature(object):

    location = (loader, 0, 0)
    character = "Q"
    weapon = None
    armor = None

    def __init__(self, name, startingLocation = (loader, 0, 0)):
        self.name = name
        self.setLocation(startingLocation)

    def getLocation(self):
        return self.location

    def setLocation(self, newLocation):
        oldLocation = self.getLocation()

        setCreatureLocations(oldLocation, None)
        setCreatureLocations(newLocation, self)

        oldLocation[0].setMap(oldLocation[1], oldLocation[2], "X")
        newLocation[0].setMap(newLocation[1], newLocation[2], self.character)
        
        self.location = newLocation

    def walk(self, x = 0, y = 0):

        newLocation = self.getLocation()
        newLocation = (newLocation[0], newLocation[1] + x, newLocation[2] + y)
                
        if (getCreatureLocations(newLocation) == None):

            self.setLocation(newLocation)
            print(self.getLocation())

    def attack(self, attackLocation):
        attackCreature = getCreatureLocations(attackLocation)

        print(attackCreature.hitpoints)
        
        if (self.weapon != None):
            attackCreature.hitpoints -= self.weapon.damage

        else:
            attackCreature.hitpoints -= self.baseDamage

        print(attackCreature.hitpoints)

class tiger(creature):

    character = "T"
    hitpoint = 120
    baseDamage = 30

    def __init__(self, startingLocation = (loader, 0, 0)):
        creature.__init__(self, "tiger", startingLocation)

class man (creature):

    # attributes
    character = "M"
    hitpoints = 100
    baseDamage = 1

    # limbs
    leftArm = True
    rightArm = True
    leftLeg = True
    rightLeg = True
    rightEye = True
    leftEye = True
    heart = True

    def __init__(self, name, gender, startingLocation = (loader, 0, 0)):
        creature.__init__(self, name, startingLocation)
        self.gender = gender
        self.inventory = []

    def getInv(self):
        return self.inventory

    def searchInv(self, term):
        
        for invItem in self.inventory:
            
            if (invItem == term):
                return True
        
        return False

    def addInv(self, term):

        self.inventory.append(term)

    def setWeapon(self, weapon):

        if (self.searchInv(weapon) == True):
            self.weapon = weapon
            return True

        else:
            return False

    def getWeapon(self):
        return self.weapon

    def setArmor(self, armor):

        if (self.searchInv(armor) == True):
            self.armor = armor
            return True

        else:
            return False

    def getArmor(self):
        return self.armor

class player(man):
    character = "C"

    def __init__(self, name, gender, startingLocation = (loader, 0, 0)):
        man.__init__(self, name, gender, startingLocation)

    def walk(self, x = 0, y = 0):

        newLocation = self.getLocation()
        newLocation = (newLocation[0], newLocation[1] + x, newLocation[2] + y)
        
        try:
            if (getCreatureLocations(newLocation) == None):

                self.setLocation(newLocation)
                print(self.getLocation())

            else:
                print("Someone else is already standing there (or perhaps there is furniture or something).")

        except KeyError:
            print("You bump into the wall.")    