'''
    Name: Orik Hoxha
    Class: ITMD 513
    Description: This file creates a class CruiseShip for creating CruiseShip objects. The CruiseShip
    is a Ship, therefore it's a subclass of the Ship class.
'''

from ship import Ship
import FieldValidatorType


class CruiseShip(Ship):

    '''
        fn: __init__(name, yearBuilt, capacityNumPassengers)
        Constructor for creation of object. While creating the object, calls the super class constructor,
        checks for the parameters passed, for validation purpose.

        Parameters
        ----------
        name : string
            Ship name.

        number : integer
            Year built.

        capacityNumPassengers : integer
            Capacity number.

        Returns
        ---------
        Object
            returns self from constructor.
    '''

    def __init__(self, name, yearBuilt, capacityNumPassengers):
        super().__init__(name, yearBuilt)
        self.__validateSetFields(capacityNumPassengers)

    '''
        fn: __validateSetFields(capacityNumPassengers)
        Private method which calls the set methods for name and number for validation purpose.
        Parameters
        ----------
        capacityNumPassengers : integer
            Employee shift number.

        Returns
        ---------
        void
    '''

    def __validateSetFields(self, capacityNumPassengers):
        self.setCapacityNumPassengers(capacityNumPassengers)

    '''
        The following setter/getter methods are the mutators/accessor methods of the Ship object attributes.
        It uses the decorators(@) for validating the attributes.

    '''

    @FieldValidatorType.validateInteger
    @FieldValidatorType.validateNegativeVal
    def setCapacityNumPassengers(self, capacityNumPassengers):
        self.__capacityNumPassengers = capacityNumPassengers

    def getCapacityNumPassengers(self):
        return self.__capacityNumPassengers

    '''
        fn: __str__(self)
        Creating string representation of the object.

        Parameters
        ----------
        self : CruiseShip
            The CruiseShip object.

        Returns
        ---------
        string
            String value of the object.
    '''

    def __str__(self):
        return "Ship name:%s, Maximum number of passengers:%s " % (self.getName(), self.getCapacityNumPassengers())
