'''
    Name: Orik Hoxha
    Class: ITMD 513
    Description: This file creates a class CargoShip for creating CargoShip objects. The CargoShip
    is a Ship, therefore it's a subclass of the Ship class.
'''

from ship import Ship
import FieldValidatorType


class CargoShip(Ship):

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

        cargoCapacity : number
            Cargo capacity.

        Returns
        ---------
        Object
            returns self from constructor.
    '''

    def __init__(self, name, yearBuilt, cargoCapacity):
        super().__init__(name, yearBuilt)
        self.__validateSetFields(cargoCapacity)

    '''
        fn: __validateSetFields(cargoCapacity)
        Private method which calls the set methods for name and number for validation purpose.
        Parameters
        ----------
        cargoCapacity : number
            Ship cargo capacity

        Returns
        ---------
        void
    '''

    def __validateSetFields(self, cargoCapacity):
        self.setCargoCapacity(cargoCapacity)

    '''
        The following setter/getter methods are the mutators/accessor methods of the Ship object attributes.
        It uses the decorators(@) for validating the attributes.

    '''

    @FieldValidatorType.validateNumber
    @FieldValidatorType.validateNegativeVal
    def setCargoCapacity(self, cargoCapacity):
        self.__cargoCapacity = cargoCapacity

    def getCargoCapacity(self):
        return self.__cargoCapacity

    '''
        fn: __str__(self)
        Creating string representation of the object.

        Parameters
        ----------
        self : CargoShip
            The CargoShip object.

        Returns
        ---------
        string
            String value of the object.
    '''

    def __str__(self):
        return "Ship name:%s, Maximum number of passengers:%s " % (self.getName(), self.getCargoCapacity())
