'''


    Name: Orik Hoxha
    Class: ITMD 513
    Homework: 12
    Description: This program creates two methods: reverseDisplay for reversing an integer and
                                                   decimalToHex for converting a decimal to hex number.

'''



import sys


# hex decimal representation of numbers.
HEX_DEC = "0123456789ABCDEF"


'''
    fn: getUserInput(message)
    Gets the user input.

    Parameters
    ----------
    arg1 : string
        message for the console

    Returns
    ---------
    string
        returns the input of the user
'''


def getUserInput(message):
    return input(message)


'''
    fn: validateInputBlank(message)
    Validate the user input basic case. Checks for the blank input.

    Parameters
    ----------
    arg1 : string
        message for the console

    Returns
    ---------
    string | integer
        returns the input of the user after validation.

'''


def validateInputBlank(message):

    # Runs until the user inputs a non-blank value.
    while True:
        userInput = getUserInput(message)
        if userInput == '':
            print("Please do not leave the input blank")
        else:
            break
    return eval(userInput)


'''
    fn: validateInputInteger(message)
    Validate the user input basic case. Checks for integer value.

    Parameters
    ----------
    arg1 : string
        message for the console

    Returns
    ---------
    integer
        returns the input of the user after validation.

'''


def validateInputInteger(message):
    while True:
        userInput = validateInputBlank(message)
        if isinstance(userInput, int):
            break
        else:
            print("Please enter a digit")
    return userInput


'''
    fn: validateInputIntegerPositive(message)
    Validate the user input basic case. Checks for positive integer value.

    Parameters
    ----------
    arg1 : string
        message for the console

    Returns
    ---------
    integer
        returns the input of the user after validation.

'''


def validateInputIntegerPositive(message):
    while True:
        userInput = validateInputInteger(message)
        if userInput <= 0:
            print("Please enter an integer > 0")
        else:
            break
    return userInput


'''
    fn: validateInputIntegerMaxVal(message)
    Validate the user input basic case. Checks for positive integer value less than maximum integer supported in python.

    Parameters
    ----------
    arg1 : string
        message for the console

    Returns
    ---------
    integer
        returns the input of the user after validation.

'''


def validateInputIntegerMaxVal(message):
    while True:
        userInput = validateInputIntegerPositive(message)
        if userInput > sys.maxsize:
            print("Please enter a smaller number than %d " % sys.maxsize)
        else:
            break
    return userInput


'''
    fn: reverseDisplay(value)
    Reverse the integer. Prints reminder on each recursion call. Divides the number by 10 to move to the next integer
    to be printed.

    Parameters
    ----------
    arg1 : int
        the integer to be reversed.

    Returns
    ---------
    integer
        returns the reversed integer.

'''


def reverseDisplay(value):
    if value == 0:
        return
    else:
        print(str((int(value % 10))), end=" ")
        reverseDisplay(int(value / 10))


'''
    fn: decimalToHex(value)
    Convert the decimal to hex. Divides the number by 16. Gets the reminder from the value and 16. 
    Creates the string and appends the mapped value from hex.

    Parameters
    ----------
    arg1 : int
        the integer to be converted.

    Returns
    ---------
    string
        returns the converted integer to hex

'''


def decimalToHex(value):
    val = ""
    if value > 0:
        hexNumber = decimalToHex(int(value / 16))
        hexDigit = value % 16
        val += (hexNumber + mapDecToHex(hexDigit))
    return val


'''
    fn: mapDecToHex(charPos)
    Checks the position returned by the reminder of the number. Returns the hex representation of the number.
    Iex (11 -> B)  (12 -> C)

    Parameters
    ----------
    arg1 : int
        the integer to be converted.

    Returns
    ---------
    char
        returns the char at position n of the HEX_DEC string.

'''


def mapDecToHex(charPos):
    return HEX_DEC[charPos]


# test for reverse
def testReverseDisplay():
    userInput = validateInputIntegerMaxVal("Please enter an integer > 0: ")
    print("Method executing: reverseDisplay()")
    reverseDisplay(userInput)

# test for dec to hex
def testMapDecToHex():
    userInput = validateInputIntegerMaxVal("Please enter an integer > 0: ")
    print("Method executing: decimalToHex()")
    print("Decimal: %d to hex: %s" % (userInput, decimalToHex(userInput)))


def main():
    testReverseDisplay()
    #testMapDecToHex()


if __name__ == '__main__':
    main()



