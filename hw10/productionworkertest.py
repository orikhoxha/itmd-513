'''
    Name: Orik Hoxha
    Class: ITMD 513
    Description: This file creates test cases for the object creating from Employee/ProductionWorker class.
'''


# Remove the traceback logs. Only show the error message.
import sys
sys.tracebacklimit = 0

from productionworker import ProductionWorker
from employee import Employee


# Test case for creating the ProductionWorker object.
def testCase1():
    print("--- Test Case 1 Start ---")
    name = "Orik"
    number = 1
    shiftNr = 1
    hourlyPayRate = 40

    productionWorker = ProductionWorker(name, number, shiftNr, hourlyPayRate)

    print(productionWorker)

    print("--- Test Case 1 End---")


# Test case for creating the Employee object
def testCase2():
    print("--- Test Case 2 Start ---")
    name = "Oket"
    number = 2
    employee = Employee(name, number)
    print(employee)

    print("--- Test Case 2 End---")


# Using mutators to change values of objects after creation.
def testCase3():
    print("--- Test Case 3 Start ---")
    name = "Orik"
    number = 1
    shiftNr = 1
    hourlyPayRate = 40

    productionWorker = ProductionWorker(name, number, shiftNr, hourlyPayRate)

    productionWorker.setNumber()
    productionWorker.setHourlyPayRate(50)
    productionWorker.setShiftNr(2)
    productionWorker.setName("Oket")

    print(productionWorker)
    print("---Test Case 3 End---")


# Validating the shiftNr attribute when creating the ProductionWorker object.
def testCase4():
    print("--- Test Case 4 Start ---")
    name = "Orik"
    number = 1
    shiftNr = 3
    hourlyPayRate = 40
    productionWorker = ProductionWorker(name, number, shiftNr, hourlyPayRate)
    print(productionWorker)
    print("--- Test Case 4 End---")

# Validating the number attribute when creating the ProductionWorker object.
def testCase5():
    print("--- Test Case 5 Start ---")
    name = "Orik"
    number = -1
    shiftNr = 2
    hourlyPayRate = 40
    productionWorker = ProductionWorker(name, number, shiftNr, hourlyPayRate)
    print(productionWorker)
    print("--- Test Case 5 End---")


# Validating the hourlyPayRate attribute when creating the ProductionWorker object.
def testCase6():
    print("--- Test Case 6 Start ---")
    name = "Orik"
    number = 1
    shiftNr = 1
    hourlyPayRate = "string"
    productionWorker = ProductionWorker(name, number, shiftNr, hourlyPayRate)
    print(productionWorker)
    print("--- Test Case 6 End ---")


# Validating the number attribute when creating the ProductionWorker object.
def testCase7():
    print("--- Test Case 7 Start ---")
    name = "Orik"
    number = 1.5
    shiftNr = 1
    hourlyPayRate = 50
    productionWorker = ProductionWorker(name, number, shiftNr, hourlyPayRate)
    print(productionWorker)
    print("--- Test Case 7 End ---")


# Checks if two objects are equal.
def testCase8():
    print("--- Test Case 8 Start ---")
    name = "Orik"
    number = 1
    shiftNr = 1
    hourlyPayRate = 50
    productionWorker = ProductionWorker(name, number, shiftNr, hourlyPayRate)

    print("productionWorker: %s  " % productionWorker)

    shiftNr = 1
    hourlyPayRate = 40

    productionWorker2 = ProductionWorker(name, number, shiftNr, hourlyPayRate)

    print("productionWorker2: %s " % productionWorker2)
    print("productinWorker == productionWorker2 is %s " % (productionWorker == productionWorker2))

    print("--- Test Case 8 End ---")


# Checks if set will take two same objects. Print the objects from the set.
def testCase9():
    print("--- Test Case 9 Start ---")

    productionWorkerSet = set()

    name = "Orik"
    number = 1
    shiftNr = 1
    hourlyPayRate = 50
    productionWorker = ProductionWorker(name, number, shiftNr, hourlyPayRate)


    name2 = "Orik"
    number2 = 1
    shiftNr2 = 2
    hourlyPayRate2 = 50
    productionWorker2 = ProductionWorker(name2, number2, shiftNr2, hourlyPayRate2)

    name3 = "Oket"
    number3 = 2
    shiftNr3 = 1
    hourlyPayRate3 = 40
    productionWorker3 = ProductionWorker(name3, number3, shiftNr3, hourlyPayRate3)

    productionWorkerSet.add(productionWorker)
    productionWorkerSet.add(productionWorker2)
    productionWorkerSet.add(productionWorker3)

    for productionWork in productionWorkerSet:
        print(productionWork)


# Checks if two objects have the same hash.
def testCase10():
    print("--- Test Case 9 Start ---")

    name = "Orik"
    number = 1
    shiftNr = 1
    hourlyPayRate = 50
    productionWorker = ProductionWorker(name, number, shiftNr, hourlyPayRate)


    name2 = "Orik"
    number2 = 1
    shiftNr2 = 2
    hourlyPayRate2 = 50
    productionWorker2 = ProductionWorker(name2, number2, shiftNr2, hourlyPayRate2)

    print("productionWorker hash == productionWorker2 hash: %s" % (productionWorker.__hash__() == productionWorker2.__hash__()))


def main():
    #testCase1()
    #testCase2()
    #testCase3()
    #testCase4()
    #testCase5()
    #testCase6()
    #testCase7()
    #testCase8()
    testCase9()
    #testCase10()


if __name__ == '__main__':
    main()