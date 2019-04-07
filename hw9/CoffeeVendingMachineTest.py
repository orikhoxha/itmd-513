'''
    Name: Orik Hoxha
    Class: ITMD 513
    Description: This file creates test cases for the object creationg from CoffeeVendingMachine class.
'''


# Remove the traceback logs. Only show the error message.
import sys
sys.tracebacklimit = 0

from coffeevendingmachine import CoffeeVendingMachine


# Test cases for creating the object.
def testCase1():
    print("--- Test Case 1 Start ---")
    coffeeVendingMaching = CoffeeVendingMachine(3, 1)
    coffeeVendingMaching.menu()
    coffeeVendingMaching.insert(4, 0, 0)
    coffeeVendingMaching.select()
    coffeeVendingMaching.menu()
    print("--- Test Case 1 End---")


def testCase2():
    print("--- Test Case 2 Start ---")
    coffeeVendingMaching = CoffeeVendingMachine(4, 0.75)
    coffeeVendingMaching.menu()
    coffeeVendingMaching.insert(2, 1, 3)
    coffeeVendingMaching.select()
    coffeeVendingMaching.menu()
    coffeeVendingMaching.insert(2, 2, 1)
    coffeeVendingMaching.select()
    coffeeVendingMaching.menu()
    print("--- Test Case 2 End---")


def testCase3():
    print("--- Test Case 3 Start ---")
    coffeeVendingMaching = CoffeeVendingMachine(1, 0.5)
    coffeeVendingMaching.menu()
    coffeeVendingMaching.insert(1, 2, 1)
    coffeeVendingMaching.select()
    coffeeVendingMaching.menu()
    coffeeVendingMaching.insert(2, 0, 0)
    coffeeVendingMaching.select()
    coffeeVendingMaching.menu()
    print("--- Test Case 3 End---")


def testCase4():
    print("--- Test Case 4 Start ---")
    coffeeVendingMaching = CoffeeVendingMachine(1, 0.5)
    coffeeVendingMaching.menu()
    coffeeVendingMaching.select()
    coffeeVendingMaching.menu()
    print("--- Test Case 4 End---")


def testCase5():
    print("--- Test Case 5 Start ---")
    coffeeVendingMaching = CoffeeVendingMachine(1, 0.5)
    coffeeVendingMaching.menu()
    coffeeVendingMaching.insert(2, 1, 1)
    coffeeVendingMaching.select()
    coffeeVendingMaching.menu()
    print("--- Test Case 5 End---")


def testCase6():
    print("--- Test Case 6 Start ---")
    coffeeVendingMaching = CoffeeVendingMachine(1, 0.5)
    coffeeVendingMaching.menu()
    coffeeVendingMaching.insert(2, 1, 1)
    coffeeVendingMaching.refund()
    coffeeVendingMaching.menu()
    print("--- Test Case 6 End---")


def testCase7():
    print("--- Test Case 7 Start ---")
    coffeeVendingMaching = CoffeeVendingMachine(3, 0.5)
    coffeeVendingMaching.menu()
    coffeeVendingMaching.setPricePerCoffee(0.75)
    coffeeVendingMaching.menu()
    coffeeVendingMaching.insert(2, 2, 1)
    coffeeVendingMaching.select()
    coffeeVendingMaching.menu()
    print("--- Test Case 7 End---")


def testCase8():
    print("--- Test Case 8 Start ---")
    coffeeVendingMaching = CoffeeVendingMachine(1, 0.5)
    coffeeVendingMaching.menu()
    coffeeVendingMaching.setPricePerCoffee(0.75)
    coffeeVendingMaching.menu()
    coffeeVendingMaching.insert(2, 2, 1)
    coffeeVendingMaching.select()
    coffeeVendingMaching.menu()
    coffeeVendingMaching.setQuantity(3)
    coffeeVendingMaching.menu()
    print("--- Test Case 8 End---")


def testCase9():
    print("--- Test Case 9 Start ---")
    quantity = -1
    price = 0.75

    print("Vending machine quantity: %s, price %s" % (quantity, price))
    coffeeVendingMaching = CoffeeVendingMachine(quantity, price)


def testCase10():
    print("--- Test Case 10 Start ---")
    quantity = 1
    price = -2

    print("Vending machine quantity: %s, price %s" % (quantity, price))
    coffeeVendingMaching = CoffeeVendingMachine(quantity, price)


def testCase11():
    print("--- Test Case 11 Start ---")
    quantity = 1.4
    price = 0.75

    print("Vending machine quantity: %s, price %s" % (quantity, price))
    coffeeVendingMaching = CoffeeVendingMachine(quantity, price)


def testCase12():
    print("--- Test Case 12 Start ---")
    quantity = 2
    price = 0.74
    print("Vending machine quantity: %s, price %s" % (quantity, price))
    coffeeVendingMaching = CoffeeVendingMachine(quantity, price)


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
    #testCase7()
    #testCase8()
    #testCase9()
    #testCase10()
    #testCase11()
    #testCase12()


if __name__ == '__main__':
    main()