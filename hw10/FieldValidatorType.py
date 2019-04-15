'''
    Name: Orik Hoxha
    Class: ITMD 513
    Description: This script defines the functions for validating fields from Employee/ProductionWorker class.
                 They are used as decorators/extensions of the setter functions in the up-mentioned classes.
'''


# Python built-in function to get the name of the original function called on a chain of function calls.
from functools import wraps


'''
    fn: validateNegativeVal(func)
    Checks if a field is negative value. If yes, raises an error. Otherwise returns the main function.
    

    Parameters
    ----------
    func : function(object)
        the main function to check for.

    Returns
    ---------
    function or error
        the main function if pass validation. Error otherwise.
'''


def validateNegativeVal(func):

    @wraps(func)
    def negativeValFn(obj, val):
        if val < 0:
            raise ValueError("The attribute:%s cannot be negative" % getAttributeName(func))
        res = func(obj, val)
        return res
    return negativeValFn


'''
    fn: validateInteger(func)
    Checks if a field is integer. If not, raises an error. Otherwise returns the main function.


    Parameters
    ----------
    func : function(object)
        the main function to check for.

    Returns
    ---------
    function or error
        the main function if pass validation. Error otherwise.
'''


def validateInteger(func):

    @wraps(func)
    def integerValFn(obj, val):
        if not type(val) == int:
            raise ValueError("The attribute:%s must be an integer." % getAttributeName(func))
        res = func(obj, val)
        return res
    return integerValFn


'''
    fn: validateNumber(func)
    Checks if a field is number. If not, raises an error. Otherwise returns the main function.

    Parameters
    ----------
    func : function(object)
        the main function to check for.

    Returns
    ---------
    function or error
        the main function if pass validation. Error otherwise.
'''


def validateNumber(func):

    @wraps(func)
    def numberValFn(obj, val):
        if not type(val) in (float, int):
            raise ValueError("The attribute:%s must be a number." % getAttributeName(func))
        res = func(obj, val)
        return res
    return numberValFn


'''
    fn: validateString(func)
    Checks if a field is string. If not, raises an error. Otherwise returns the main function.

    Parameters
    ----------
    func : function(object)
        the main function to check for.

    Returns
    ---------
    function or error
        the main function if pass validation. Error otherwise.
'''


def validateString(func):

    @wraps(func)
    def stringValFn(obj, val):
        if not str(val).isalpha():
            raise ValueError("The attribute:%s must be a string" % getAttributeName(func))
        res = func(obj, val)
        return res
    return stringValFn


'''
    fn: getAttributeName(func)
    Get the name from the function. It is used to determine attribute name of a class by the setter function of that
    attribute.

    Parameters
    ----------
    func : function(object)
        the main function to check for.

    Returns
    ---------
    string
        the attribute extracted from the setter method.
'''


def getAttributeName(func):
    val = str(func.__name__)
    val = val.replace("set", "")
    val = val[0].lower() + val[1:]
    return val












