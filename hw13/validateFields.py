'''
    Name: Orik Hoxha
    Class: ITMD 513
    Homework: 13
'''


'''
    fn: isInteger(val)
    Checks if a number is integer.

    Parameters
    ----------
    val : eval
       The velue to check.

    Returns
    ---------
    boolean
        True if val is integer. False otherwise.
'''


def isInteger(val):
    if isinstance(val, int):
        return True
    return False


'''
    fn: isNegative(val)
    Checks if a number is negative.

    Parameters
    ----------
    val : integer
       The velue to check.

    Returns
    ---------
    boolean
        True if val is negative. False otherwise.
'''


def isNegative(val):
    if val < 0:
        return True
    return False


'''
    fn: validatePositiveInteger(*args)
    Checks if a number is negative.

    Parameters
    ----------
    args : array of args.
       The arguments to validate.

    Returns
    ---------
    boolean
        True if positive integer. False otherwise.
'''


def validatePositiveInteger(*args):
    print(*args)
    for val in args:
        if val == "":
            continue
        if not(isInteger(val)):
            return False
        if isNegative(val):
            return False
    return True
