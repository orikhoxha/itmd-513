'''
    Name: Orik Hoxha
    Class: ITMD 513
    Description: This file creates a class Employee for creating employee objects.
'''

# Field validator for validating the Employee object attributes.
import FieldValidatorType


class Employee:

    '''
        fn: __init__(name, number)
        Constructor for creation of object. While creating the object, checks for the paramenters
        passed, for validation purpose.

        Parameters
        ----------
        name : string
            Employee name.

        number : integer
            Employee number.

        Returns
        ---------
        Object
            returns self from constructor.
    '''

    def __init__(self, name, number):
        self.__validateSetFields(name, number)
        self.__name = name
        self.__number = number

    '''
        fn: __validateSetFields(name, number)
        Private method which calls the set methods for name and number for validation purpose.
        Parameters
        ----------
        name : string
            Employee name.

        number : integer
            Employee number.

        Returns
        ---------
        void
    '''

    def __validateSetFields(self, name, number):
        self.setName(name)
        self.setNumber(number)

    '''
        The following setter/getter methods are the mutators/accessor methods of the Employee object attributes.
        It uses the decorators(@) for validating the attributes.
    
    '''

    @FieldValidatorType.validateString
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @FieldValidatorType.validateInteger
    @FieldValidatorType.validateNegativeVal
    def setNumber(self, number):
        self.__number = number

    def getNumber(self):
        return self.__number

    '''
        fn: __eq__(self, other)
        Inherited method for checking equality between two objects by comparing the number and name attributes.
        
        Parameters
        ----------
        self : Employee
            First Employee.

        other : Employee
            Second number.

        Returns
        ---------
        boolean
            True if two objects are the same. False otherwise.
    '''

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.getNumber() == other.getNumber() and self.getName() == other.getName()
        return False

    '''
        fn: __hash__(self)
        Creating the hash for the object based on the number and name attributes.

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
        hashVal = 31 * hashVal + self.__number
        hashVal = 31 * hashVal + hash(self.__name)
        return hashVal

    '''
        fn: __str__(self)
        Creating string representation of the object.

        Parameters
        ----------
        self : Employee
            The Employee.

        Returns
        ---------
        string
            String value of the object.
    '''

    def __str__(self):
        return "Number: %s, Name:%s" % (self.getNumber(), self.getName())
