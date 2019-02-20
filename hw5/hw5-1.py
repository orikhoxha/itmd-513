'''
    This program multiplies 2 matrixes. It expects n number of digits input from the user
    separated by space iex. 3 4 5 6.

    Name: Orik Hoxha
    Class: ITMD 513

'''


'''
    fn: isStringEmpty(message)
    Checks if the string is empty.

    Parameters
    ----------
    lst : string
        the string to check the length for.

    Returns
    ---------
    boolean
        returns true if the length >= 1, otherwise false.
'''

def isStringEmpty(lst):
    return len(lst.strip()) == 0


'''
    fn: convertStringToList(string)
    Converts a string to a list.

    Parameters
    ----------
    string : string
        the string to be converted to a list.

    Returns
    ---------
    list
        returns a list of string split based on the space.
'''


def convertStringToList(string):
    list_converted = string.split()
    return list_converted


'''
    fn: convertStrListToNrList(list)
    Converts a string list to a number list. If it encounters an error on conversion, throws an exception.

    Parameters
    ----------
    list : list(strings)
        the string list to be converted to a number list.

    Returns
    ---------
    list or false
        returns the list if the conversion successful, otherwise returns false.
'''


def convertStrListToNrList(lst):

    lst = convertStringToList(lst)

    try:
        lst = [float(numeric_string) for numeric_string in lst]
        return lst
    except ValueError:
        return False


'''
    fn: validate_user_input(message)
    Validates the user input list. Checks if the input is empty, or the input is not a number. Keeps repeating
    until the validation is successful.

    Parameters
    ----------
    message : string
        Console message to show to the user.

    Returns
    ---------
    list(float)
        returns a converted list of numbers
'''

def validate_user_input(message):
    while True:
        userInput = input(message)
        if isStringEmpty(userInput):
            print('Please do not leave the input blank')
        elif not convertStrListToNrList(userInput):
            print('List can only contain digits')
        else:
            break
    return convertStrListToNrList(userInput)



'''
    fn: isSorted(lst)
    Checks if the list is sorted.

    Parameters
    ----------
    list : list(float)
        The list to check for the sort.

    Returns
    ---------
    boolean
        returns true if list is sorted, false otherwise.
'''

def isSorted(lst):

    list_len = len(lst)

    for i in range(list_len - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True


'''
    fn: main(lst)
    Runs the program. Gets the user input, passes to the isSorted method, and passes the list to the isSorted fn.

    Returns
    ---------
    void
'''


def main():

    userList = validate_user_input("Enter list: ")
    if isSorted(userList):
        print("The list is already sorted")
    else:
        print("The list is not sorted")


if __name__ == '__main__':
    main()
