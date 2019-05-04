'''
    Name: Orik Hoxha
    Class: ITMD 513
    Homework: 13
    Description: This file creates a class ChangeCounter for creating Change counter object.
'''


class ChangeCounter:

    '''
        fn: __init__(quarters=0, dimes=0, nickles=0, pennies=0, halfDollar=0, dollar=0)
        Constructor for creation of object. Default values to 0.

        Parameters
        ----------
        quarters : int

        dimes : int

        nickles : int

        pennies : int

        halfDollar : int

        dollar : int

        Returns
        ---------
        Object
            returns self from constructor.
    '''

    def __init__(self, quarters=0, dimes=0, nickles=0, pennies=0, halfDollar=0, dollar=0):
        self.__quarters = quarters
        self.__dimes = dimes
        self.__nickles = nickles
        self.__pennies = pennies
        self.__halfDollar = halfDollar
        self.__dollar = dollar

    '''
        setter/getters for the object.
    '''

    def setQuarters(self, quarters):
        self.__quarters = quarters

    def getQuarters(self):
        return self.__quarters

    def setDimes(self, dimes):
        self.__dimes = dimes

    def getDimes(self):
        return self.__dimes

    def setNickles(self, nickles):
        self.__nickles = nickles

    def getNickles(self):
        return self.__nickles

    def setPennies(self, pennies):
        self.__pennies = pennies

    def getPennies(self):
        return self.__pennies

    def setHalfDollar(self, halfDollar):
        self.__halfDollar = halfDollar

    def getHalfDollar(self):
        return self.__halfDollar

    def setDollar(self, dollar):
        self.__dollar = dollar

    def getDollar(self):
        return self.__dollar


    '''
        calculation of the coins
    '''

    def calculateQuarters(self):
        return self.formatNumber(self.getQuarters() * .25)

    def calculateDimes(self):
        return self.formatNumber(self.getDimes() * 0.1)

    def calculateNickles(self):
        return self.formatNumber(self.getNickles() * 0.05)

    def calculatePennies(self):
        return self.formatNumber(self.getPennies() * 0.01)

    def calculateHalfDollars(self):
        return self.formatNumber(self.getHalfDollar() * 0.5)

    # total amount of the calculation of coins.
    def calculateChangeCounter(self):
        total = self.getDollar() + self.calculateHalfDollars() + self.calculateQuarters() + \
                                            self.calculateDimes() + self.calculateNickles() + self.calculatePennies()

        return self.formatNumber(total)

    '''
        fn: formatNumber(number)
        Number to format.

        Parameters
        ----------
        number : int|float

        Returns
        ---------
        int|float
            Returns int if the number mod 1 = 0, otherwise returns the float format.
    '''

    def formatNumber(self, number):
        if number % 1 == 0:
            return int(number)
        return round(number, 2)




