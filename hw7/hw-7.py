'''
    This program reads the phone nr entered by user, validates it, and if the user has entered a mix of letters and numbers
    ,the system returns the converted number.

    Name: Orik Hoxha
    Class: ITMD 513

'''


#phone length validation
PHONE_NR_LENGTH = 10

#character to look for in the number
SPECIAL_CHAR = "-"

#length of each part of the phone number iex. DDD-DDD-DDDD
FIRST_PART, SECOND_PART, THIRD_PART = 3, 3, 4


'''
    fn: mapAlphaNumericValues(char)
    Map a character to a corresponding number.

    Parameters
    ----------
    char : string
        character to be mapped.



    Returns
    ---------
    Number
        returns number mapped with the character.
'''

def mapAlphaNumericValues(char):
    alphaNumericMapValues = {
        "A": 2, "B": 2, "C": 2,
        "D": 3, "E": 3, "F": 3,
        "G": 4, "H": 4, "I": 4,
        "J": 5, "K": 5, "L": 5,
        "M": 6, "N": 6, "O": 6,
        "P": 7, "Q": 7, "R": 7, "S": 7,
        "T": 8, "U": 8, "V": 8,
        "W": 9, "X": 9, "Y": 9, "Z": 9,
    }
    return str(alphaNumericMapValues.get(char,0))


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
    fn: validateUserInput(message)
    Validate the user input basic case. Checks for the blank input.

    Parameters
    ----------
    arg1 : string
        message for the console

    Returns
    ---------
    string
        returns the input of the user after validation.

'''

def validateUserInputBlank(message):

    # Runs until the user inputs a non-blank value.
    while True:
        user_input = getUserInput(message)
        if user_input == '':
            print("Please do not leave the input blank")
        else:
            break
    return user_input



'''
    fn: validatePhoneNrLength(message)
    Gets the user input. Calls another method to check for number validation.

    Parameters
    ----------
    arg1 : string
        message for the console.

    Returns
    ---------
    string
        returns the input of the user - phone number.
'''

def validatePhoneNrLength(message):

    # Runs until the user inputs a non-blank value.
    while True:
        phoneNr = validateUserInputBlank(message)
        if not hasSpecialLengthFormat(phoneNr):
            print("The number must contain 9 digits in the format XXX-XXX-XXXX. If letters then follow (D-digit) (L-letter) DDD-LLL-LLLL ")
        else:
            break
    return phoneNr


'''
    fn: replaceSpecialChar(phoneNr)
    Removes all special characters from the phone number.

    Parameters
    ----------
    arg1 : string
        phone number.

    Returns
    ---------
    string
        returns phone number without the special characters.
'''


def replaceSpecialChar(phoneNr):
    return phoneNr.replace(SPECIAL_CHAR, "")


'''
    fn: checkPhoneNrLength(phoneNr)
    Calls the replaceSpecialChar() for removing special characters from a number. Checks the length
    of the phone number.

    Parameters
    ----------
    arg1 : string
        phone number.

    Returns
    ---------
    number
        length of the phone number.
'''


def checkPhoneNrLength(phoneNr):
    return len(replaceSpecialChar(phoneNr)) == PHONE_NR_LENGTH


'''
    fn: splitPhoneNr(phoneNr)
    Splits the phone number based on a special character. Used to get the parts of the phone number.

    Parameters
    ----------
    arg1 : string
        phone number.

    Returns
    ---------
    list
        list of parts of the phone number.
'''


def splitPhoneNr(phoneNr):
    return phoneNr.split(SPECIAL_CHAR)


'''
    fn: hasSpecialLengthFormat(phoneNr)
    Checks the special format length of a phone nr. Also, checks if the first part is a digit, second part is a digit or
    an alpha, and third part is digit or an alpha.

    Parameters
    ----------
    arg1 : string
        phone number.

    Returns
    ---------
    Boolean
        returns true if the phone nr has special length and format. False otherwise.
'''


def hasSpecialLengthFormat(phoneNr):

    if phoneNr.find(SPECIAL_CHAR) == -1:
        return False

    if not checkPhoneNrLength(phoneNr):
        return False
    else:
        phoneNrSplit = splitPhoneNr(phoneNr)

        phoneNrFirstPart = phoneNrSplit[0]
        phoneNrSecondPart = phoneNrSplit[1]
        phoneNrThirdPart = phoneNrSplit[2]

        if ((len(phoneNrFirstPart), len(phoneNrSecondPart), len(phoneNrThirdPart)) == (FIRST_PART, SECOND_PART, THIRD_PART) and
             phoneNrFirstPart.isdigit() and ((phoneNrSecondPart.isalpha() and phoneNrThirdPart.isalpha()) or
                (phoneNrSecondPart.isdigit() and phoneNrThirdPart.isdigit()))):
            return True

        return False


'''
    fn: hasAlpaExtension(phoneNr)
    Checks if the second and third part of the number is a string of characters.

    Parameters
    ----------
    arg1 : string
        phone number.

    Returns
    ---------
    Boolean
        returns true if second and third part are characters. False otherwise.
'''


def hasAlpaExtension(phoneNr):
    phoneNr = replaceSpecialChar(phoneNr)
    return phoneNr[FIRST_PART:].isalpha()


'''
    fn: formatPhoneNrWithSpecialChar(phoneNr)
    Formats the phone nr first, second and third part in format (DDD-DDD-DDDD).

    Parameters
    ----------
    arg1 : string
        phone number.

    Returns
    ---------
    Boolean
        returns phone number in format (DDD-DDD-DDDD) .
'''


def formatPhoneNrWithSpecialChar(phoneNr):
    return "%s-%s-%s" % (phoneNr[:FIRST_PART], phoneNr[SECOND_PART:SECOND_PART + SECOND_PART], phoneNr[SECOND_PART + SECOND_PART:])


'''
    fn: extractNrFromAlpha(phoneNr)
    Calls the method hasSpecialLengthFormat() to check if the number contains special format.
    Calls the method hasAlpaExtension() to check if the number has characters.
    Extracts the number from the character, and returns the phone nr formatted. 
    If the phone nr is entered in format ex. 555-333-1111, then it will return the same number.

    Parameters
    ----------
    arg1 : string
        phone number.

    Returns
    ---------
    string
        returns the phone nr from the user input entered mix of digits and characters.Otherwise,
        returns the same phone nr as entered.
'''


def extractNrFromAlpha(phoneNr):
    if hasSpecialLengthFormat(phoneNr):
        if hasAlpaExtension(phoneNr):
            convertedPhoneNr = ""
            firstPart = phoneNr[:FIRST_PART]
            phoneNr = replaceSpecialChar(phoneNr)[FIRST_PART:]
            phoneNr = phoneNr.upper()
            for char in phoneNr:
                convertedPhoneNr += mapAlphaNumericValues(char)

            return formatPhoneNrWithSpecialChar(firstPart + convertedPhoneNr)
        else:
            return phoneNr

    return False

'''
    fn: main()
    Prints the phone nr entered by the user.

    Returns
    ---------
    void
'''


def main():
    userPhoneNr = validatePhoneNrLength("Please enter phone nr in format XXX-XXX-XXXX: ")
    print(extractNrFromAlpha(userPhoneNr))


if __name__ == '__main__':
    main()




