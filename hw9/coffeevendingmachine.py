'''
    Name: Orik Hoxha
    Class: ITMD 513
    Description: This file creates a class CoffeeVendingMachine for creating Vending machinges,
'''

# Field validator for creation of the object CoffeeVendingMaching
import FieldValidator


class CoffeeVendingMachine:

    '''
        fn: __init__(quantity, pricePerCoffee)
        Constructor for creation of object. While creating the object, checks for the paramenters
        of passed, for validation purpose.

        Parameters
        ----------
        quantity : int
            quantity of the vending machines.

        pricePerCoffee : float
            price per coffee.

        Returns
        ---------
        Object
            returns self from constructor.
    '''

    def __init__(self, quantity, pricePerCoffee):
        self.__validateSetFields(quantity, pricePerCoffee)
        self.__cupsAvailable = self.__quantity
        self.__amountInserted = 0

    '''
        fn: __validateSetFields(quantity, pricePerCoffee)
        Private method which calls the set methods for quantity and pricePerCoffe for validation purpose.
        Parameters
        ----------
        quantity : int
            quantity of the vending machines.

        pricePerCoffee : float
            price per coffee.

        Returns
        ---------
        void
    '''

    def __validateSetFields(self, quantity, pricePerCoffee):
        self.setQuantity(quantity)
        self.setPricePerCoffee(pricePerCoffee)

    '''
        fn: menu()
        Print the menu with the vending machine information.
        ----------

        Returns
        ---------
        void
    '''

    def menu(self):
        print("Quantity: %s, Price of coffee: $%s " % (self.__quantity, self.__pricePerCoffee))

    '''
        fn: insert(quarters, dimes, nickles)
        Inserts the quarters, dimes, and nickles. Converts it to amount accordingly.
        Parameters
        ----------
        quarters : int
            the quarters.
        dimes : int
            the dimes.

        nickles : float
            the nickles.

        Returns
        ---------
        void
    '''

    def insert(self, quarters, dimes, nickles):
        self.__amountInserted = (quarters * 0.25 + dimes * 0.10 + nickles * 0.05)
        print("Amount inserted:  $%s" % self.__amountInserted)

    '''
        fn: select()
        Disposes the coffee for user. If amount incorrect/no coffee available refunds the money.
        Returns
        ---------
        void
    '''

    def select(self):
        if self.__amountInserted != self.__pricePerCoffee:
            print("Please put exact amount of money.")
            self.refund()
        elif self.getQuantity() < 1:
            print("No more coffee is available.")
            self.refund()
        else:
            self.setQuantity(self.getQuantity() - 1)
            self.__amountInserted = 0
            print("Enjoy your coffee")

    '''
        fn: refund()
        Refund the money to the user. Sets the amountInserted to 0.
    
        Returns
        ---------
        void
    '''

    def refund(self):
        print("Money refunded: $%s" % self.__amountInserted)
        self.__amountInserted = 0

    '''
        fn: setQuantity(quantity)
        Sets the quantity. Uses the decorators for validating the value.
        Parameters
        ----------
        quantity : int
            the quantity of coffee.

        Returns
        ---------
        void
    '''


    @FieldValidator.validateInteger
    @FieldValidator.validateNegativeVal
    def setQuantity(self, quantity):
        self.__quantity = quantity

    '''
        fn: getQuantity()
        Gets the quantity of the coffees per vending machine.
        Parameters
        ----------
    
        Returns
        ---------
        int
            quantity of the coffees.
    '''

    def getQuantity(self):
        return self.__quantity

    '''
        fn: setPricePerCoffee(pricePerCoffee)
        Sets the price per coffee. Uses the decorators for validating the value.
        Parameters
        ----------
        pricePerCoffee : float
            the price per the coffee.

        Returns
        ---------
        void
    '''

    @FieldValidator.validateNegativeVal
    @FieldValidator.validatePriceSet
    def setPricePerCoffee(self, pricePerCoffee):
        self.__pricePerCoffee = pricePerCoffee

    '''
            fn: getPricePerCoffee()
            Gets the price of the coffees per vending machine.
            Parameters
            ----------
            Returns
            ---------
            int
                price of the coffee.
        '''

    def getPricePerCoffee(self):
        return self.__pricePerCoffee



