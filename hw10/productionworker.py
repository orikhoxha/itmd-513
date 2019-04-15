'''
    Name: Orik Hoxha
    Class: ITMD 513
    Description: This file creates a class ProductionWorker for creating ProductionWorker objects. The ProductionWorker
    is an Employee, therefore it's a subclass of the Employee object.
'''

from employee import Employee
import productionworkerfieldvalidator
import FieldValidatorType


class ProductionWorker(Employee):

    '''
        fn: __init__(name, number, shiftNr, hourlyPayRate)
        Constructor for creation of object. While creating the object, calls the super class constructor,
        checks for the parameters passed, for validation purpose.

        Parameters
        ----------
        name : string
            Employee name.

        number : integer
            Employee number.

        shiftNr : integer
            Shift number.

        hourlyPayRate : number
            Hourly pay rate.

        Returns
        ---------
        Object
            returns self from constructor.
    '''

    def __init__(self, name, number, shiftNr, hourlyPayRate):
        super().__init__(name, number)
        self.__validateSetFields(shiftNr, hourlyPayRate)
        self.__shiftNr = shiftNr
        self.__hourlyPayRate = hourlyPayRate

    '''
        fn: __validateSetFields(shiftNr, hourlyPayRate)
        Private method which calls the set methods for name and number for validation purpose.
        Parameters
        ----------
        shiftNr : integer
            Employee shift number.

        hourlyPayRate : number
            Employee hourly pay rate.

        Returns
        ---------
        void
    '''
    def __validateSetFields(self, shiftNr, hourlyPayRate):
        self.setShiftNr(shiftNr)
        self.setHourlyPayRate(hourlyPayRate)

    '''
        The following setter/getter methods are the mutators/accessor methods of the ProductionWorker object attributes.
        It uses the decorators(@) for validating the attributes.

    '''

    @productionworkerfieldvalidator.validateShift
    def setShiftNr(self, shiftNr):
        self.__shiftNr = shiftNr

    def getShiftNr(self):
        return self.__shiftNr

    @FieldValidatorType.validateNumber
    @FieldValidatorType.validateNegativeVal
    def setHourlyPayRate(self, hourlyPayRate):
        self.__hourlyPayRate = hourlyPayRate

    def getHourlyPayRate(self):
        return self.__hourlyPayRate

    '''
        fn: __str__(self)
        Calls the string representation of the super class. Creates string representation of the object and concats
        with the super class string.

        Parameters
        ----------
        self : ProductionWorker
            The ProductionWorker.

        Returns
        ---------
        string
            String value of the object.
    '''

    def __str__(self):
        return super().__str__() + ", shiftNr:%s, Hourly Pay Rate:%s  " % (self.getShiftNr(), self.getHourlyPayRate())
