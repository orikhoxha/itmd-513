'''
    Name: Orik Hoxha
    Class: ITMD 513
    Description: This script defines the functions for validating specific business logic attributes from ProductionWorker class.
                 They are used as decorators/extensions of the setter functions in the up-mentioned classes.
'''


# Dictionary of shift values.
DICT_SHIFT_NUMS = {"DAY_SHIFT": 1, "NIGHT_SHIFT": 2}


'''
    fn: validateShift(func)
    Checks if the shiftNr is within values(1,2). If not, raises an error. Otherwise returns the main function.

    Parameters
    ----------
    func : function(object)
        the main function to check for.

    Returns
    ---------
    function or error
        the main function if pass validation. Error otherwise.
'''


def validateShift(func):
    def shiftValFn(obj, val):
        if val not in DICT_SHIFT_NUMS.values():
            raise ValueError("The attribute: shiftNr must be %s or %s" % (DICT_SHIFT_NUMS["DAY_SHIFT"],
                                                                          DICT_SHIFT_NUMS["NIGHT_SHIFT"]))
        res = func(obj, val)
        return res
    return shiftValFn

