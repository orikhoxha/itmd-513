'''
    Name: Orik Hoxha
    Class: ITMD 513
    Description: This file creates a class Ship for creating ship objects.
'''

# Field validator for validating the Employee object attributes.
import FieldValidatorType


class Ship(object):

    '''
        fn: __init__(name, yearBuilt)
        Constructor for creation of object. While creating the object, checks for the paramenters
        passed, for validation purpose.

        Parameters
        ----------
        name : string
            Ship name.

        yearBuilt : integer
            Year built.

        Returns
        ---------
        Object
            returns self from constructor.
    '''

    def __init__(self, name, yearBuilt):
        self.__validateSetFields(name, yearBuilt)
        self.__name = name
        self.__yearBuilt = yearBuilt

    '''
        fn: __validateSetFields(name, yearBuilt)
        Private method which calls the set methods for name and number for validation purpose.
        Parameters
        ----------
        name : string
            Ship name.

        yearBuilt : integer
            Year built.

        Returns
        ---------
        void
    '''

    def __validateSetFields(self, name, yearBuilt):
        self.setName(name)
        self.setYearBuilt(yearBuilt)

    '''
        The following setter/getter methods are the mutators/accessor methods of the Ship object attributes.
        It uses the decorators(@) for validating the attributes.

    '''

    @FieldValidatorType.validateString
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @FieldValidatorType.validateInteger
    @FieldValidatorType.validateNegativeVal
    def setYearBuilt(self, yearBuilt):
        self.__yearBuilt = yearBuilt

    def getYearBuilt(self):
        return self.__yearBuilt

    '''
        fn: __eq__(self, other)
        Inherited method for checking equality between two objects by comparing the name and year built.

        Parameters
        ----------
        self : Ship/CargoShip/CruiseShip
            First Ship-subclass object.

        other : Employee
            Second Ship-subclass object.

        Returns
        ---------
        boolean
            True if two objects are the same. False otherwise.
    '''

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.getName() == other.getName() and self.getYearBuilt() == other.getYearBuilt()
        return False

    '''
        fn: __hash__(self)
        Creating the hash for the object based on the name and yearBuilt attributes.

        Parameters
        ----------
        self : Employee
            The Employee.

        Returns
        ---------
        integer
            A hash value for the object
    '''

    def __hash__(self):
        hashVal = 7
        hashVal = 31 * hashVal + self.__yearBuilt
        hashVal = 31 * hashVal + hash(self.__name)
        return hashVal

    '''
        fn: __str__(self)
        Creating string representation of the object.

        Parameters
        ----------
        self : Ship
            The Ship object.

        Returns
        ---------
        string
            String value of the object.
    '''

    def __str__(self):
        return "Ship name:%s, Year built:%s" % (self.getName(), self.getYearBuilt())

