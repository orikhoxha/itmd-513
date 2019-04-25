'''
    Name: Orik Hoxha
    Class: ITMD 513
    Description: This file creates test cases for the object creating from CoffeeVendingMachine class.
'''


# Remove the traceback logs. Only show the error message.
import sys
sys.tracebacklimit = 0

from ship import Ship
from cargoship import CargoShip
from cruiseship import CruiseShip


# Iterate and print the ship list
def printShipList(shipList):
    for ship in shipList:
        print("Ship type:%s, %s " % (getShipType(ship), ship))

# Get the ship type based on the instace of the object.
def getShipType(ship):
    if isinstance(ship, CargoShip):
        return "CargoShip"
    elif isinstance(ship, CruiseShip):
        return "CruiseShip"
    elif isinstance(ship, Ship):
        return "Ship"
    else:
        return "Undefined"


# Test cases for creating 3 different ships and printing them.
def testCase1():
    print("--- Test Case 1 Start ---")
    name = "Aurelia"
    yearBuilt = 1992
    ship = Ship(name, yearBuilt)

    name = "Corona"
    yearBuilt = 1990
    cargoCapacity = 12040
    cargoShip = CargoShip(name, yearBuilt, cargoCapacity)

    name = "Odisea"
    yearBuilt = 1988
    capacityNumPassengers = 1000
    cruiseShip = CruiseShip(name, yearBuilt, capacityNumPassengers)

    shipList = []

    shipList.append(ship)
    shipList.append(cargoShip)
    shipList.append(cruiseShip)

    printShipList(shipList)
    print("--- Test Case 1 End---")


# Testing the attribute yearBuilt validation.
def testCase2():
    print("--- Test Case 2 Start ---")
    name = "Corona"
    yearBuilt = -1990
    cargoCapacity = 12040
    ship = CargoShip(name, yearBuilt, cargoCapacity)
    print(ship)
    print("--- Test Case 2 End---")


# Testing the attribute name validation.
def testCase3():
    print("--- Test Case 3 Start ---")
    name = 321
    yearBuilt = 1990
    cargoCapacity = 12040
    ship = CargoShip(name, yearBuilt, cargoCapacity)
    print(ship)

    print("--- Test Case 3 End---")


# Testing the attribute capacityNumPassengers validation.
def testCase4():
    print("--- Test Case 4 Start ---")
    name = "Julia"
    yearBuilt = 1990
    capacityNumPassengers = -1200
    ship = CruiseShip(name, yearBuilt, capacityNumPassengers)
    print(ship)

    print("--- Test Case 4 End---")


# Testing the equality of two same ships. Inserting them into a set and print the set list.
def testCase5():
    print("--- Test Case 5 Start ---")

    name = "Odisea"
    yearBuilt = 1998
    cargoCapacity = 10000
    cargoShip1 = CargoShip(name, yearBuilt, cargoCapacity)

    name = "Odisea"
    yearBuilt = 1998
    cargoCapacity = 1000
    cargoShip2 = CargoShip(name, yearBuilt, cargoCapacity)

    cargoShipSet = {cargoShip1, cargoShip2}

    printShipList(cargoShipSet)

    print("--- Test Case 5 End---")


# Testing mutators of an object.
def testCase6():
    print("--- Test Case 6 Start ---")
    name = "Odisea"
    yearBuilt = 1998
    cargoCapacity = 10000
    cargoShip = CargoShip(name, yearBuilt, cargoCapacity)

    print(cargoShip)

    cargoShip.setYearBuilt(2000)
    cargoShip.setCargoCapacity(1000)
    cargoShip.setName("Aurelia")

    print(cargoShip)

    print("--- Test Case 6 End---")


'''
    fn: main()
    Calls test cases. The uncommented test cases will run. 

    Returns
    ---------
    void
'''


def main():
    testCase1()
    #testCase2()
    #testCase3()
    #testCase4()
    #testCase5()
    #testCase6()


if __name__ == '__main__':
    main()