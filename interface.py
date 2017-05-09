from basicbits import *

# Player must be object adam
adam = player("Adam", "male", (plaza, 0, 0))

class interface(object):

    def __init__(self):
        self.isQuit = False

    # adam methods

    def walkNorth():
        print("You walk north.")
        adam.walk(-1,0)

    def walkSouth():
        print("You walk south.")
        adam.walk(1,0)

    def walkEast():
        print("You walk east.")
        adam.walk(0,-1)

    def walkWest():
        print("You walk west.")
        adam.walk(0,1)

    def set_isQuit(self):
        self.isQuit = True

    def displayInv():

        count = 0

        for item in adam.getInv():
            print(str(count) + ": " + item.name)

    def wield():

        displayInv()

        number = input("Which item would you like to wield? ")
        number = int(number)

        weapon = adam.getInv()[number]

        if (adam.setWeapon(weapon) == True):
            print("You brandish the " + weapon.name)
        
        else:
            print("That didn't work.")

    def equipArmor():

        displayInv()

        number = input("Which item would you like to equip? ")

        armor = adam.getInv[number]

        if (adam.setArmor(armor) == True):
            print("You equip the " + armor.name)

        else:
            print("That didn't work.")

    def attack():
        direction = input("In which direction would you like to attack? ")
        attackLocation = adam.getLocation()

        def attackLocation(x, y):
            attackLocation = adam.getLocation()
            attackLocation = (attackLocation[0], attackLocation[1] + x, attackLocation[2] + y)
            print(attackLocation)
            return attackLocation

        if (direction == "w"):
            attackLocation = attackLocation(-1, 0)

        if (direction == "s"):
            attackLocation = attackLocation(1,0)

        if (direction == "a"):
            attackLocation = attackLocation(0,-1)

        if (direction == "d"):
            attackLocation = attackLocation(0,1)

        print(attackLocation)

        if (attackLocation != None):
            adam.attack(attackLocation)

        else:
            print("You can't attack nothing!")
 
    # enemy methods

    def enemyWalkNorth(enemy):
        enemy.walk(-1,0)

    def enemyWalkSouth(enemy):
        enemy.walk(1,0)

    def enemyWalkEast(enemy):
        enemy.walk(0,-1)

    def enemyWalkWest(enemy):
        enemy.walk(0,1)

    #not working- seems to be true up to 2 tiles away
    def checkProximity(thingOne, thingTwo):
        if (1 >= (thingOne.getLocation()[1] - thingTwo.getLocation()[1]) >= -1):
            if (1 >= (thingOne.getLocation()[2] - thingTwo.getLocation()[2]) >= -1):
                return True
        else:
            return False

    def enemyWalkToAdam(enemy):

        # switch 

        if (adam.getLocation()[1] < enemy.getLocation()[1]):
            interface.enemyWalkNorth(enemy)
            return None

        elif (adam.getLocation()[1] > enemy.getLocation()[1]):
            interface.enemyWalkSouth(enemy)
            return None

        elif (adam.getLocation()[2] < enemy.getLocation()[2]):
            interface.enemyWalkEast(enemy)
            return None

        elif (adam.getLocation()[2] > enemy.getLocation()[2]):
            interface.enemyWalkWest(enemy)
            return None

    def enemyAttack(enemy):
        if (interface.checkProximity(adam, enemy)):
            enemy.attack(adam.getLocation())
            print("The " + enemy.name + " attacks you for " + str(enemy.baseDamage) + " damage!")
            return

    def enemyTurn():

        enemyList = list(creatureLocations.values())
        eve = man("Eve", "female", (plaza, 1, 1))
        print(enemyList)
        count = 0

        for enemy in enemyList:
            # exists and is not adam
            if ((enemy != None) and (enemy != adam)):
                # and is on adam's map
                if (enemy.getLocation()[0] == adam.getLocation()[0]):

                    interface.enemyAttack(enemy)
                    interface.enemyWalkToAdam(enemy)
                    print(enemy.name)
                    print(count)
                    count += 1

    def interface(self):

        def setCommands():

            number = input("Choose commandlist: \n 0: basicCommands \n 1: inventoryCommands")
            number = int(number)
            
            basicCommands = {
                "w" : interface.walkNorth, 
                "s" : interface.walkSouth,
                "a" : interface.walkEast,
                "d" : interface.walkWest,
                "attack" : interface.attack,
                "quit" : self.set_isQuit,
                "i" : setCommands
                }

            inventoryCommands = {
                "w" : interface.wield,
                "i" : setCommands
                }
            
            commandList = [basicCommands, inventoryCommands]
            commands = commandList[number]

            return commands

        commands = setCommands()

        while not (self.isQuit):
            try:
                adam.getLocation()[0].printMap()
                givenCommand = input("Enter a command: ")
                commands[givenCommand]()
                interface.enemyTurn()
                # print(givenCommand)

            except KeyError:
                print("That command is not recognized.")

        print("Thank you for playing!")