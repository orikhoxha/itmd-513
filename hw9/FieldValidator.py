'''
    Name: Orik Hoxha
    Class: ITMD 513
    Description: This script defines the functions for validating fields from CoffeeVendingMachine class.
                 They are used as decorators/extensions of the setter functions in the up-mentioned class.
'''


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
    def negativeValFn(obj, val):
        if val < 0:
            raise ValueError("The value cannot be negative")
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
    def integerValFn(obj, val):
        if not type(val) == int:
            raise ValueError("The value must be an integer")
        res = func(obj, val)
        return res
    return integerValFn


'''
    fn: validatePriceSet(func)
    Checks if a field is divisible by 5. If not, raises an error. Otherwise returns the main function.

    Parameters
    ----------
    func : function(object)
        the main function to check for.

    Returns
    ---------
    function or error
        the main function if pass validation. Error otherwise.
'''


def validatePriceSet(func):
    def divisibleByFive(obj, val):
        if (val * 100) % 5 != 0:
            raise ValueError("The price must be divisible by 5")
        res = func(obj, val)
        return res
    return divisibleByFive




