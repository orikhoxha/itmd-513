import math
import re


# This program validates the bank card. It also checks what type of card it is
# Name: Orik Hoxha
# Email: ohoxha@hawk.iit.edu
# Class : ITMD: 513


# Card Type Constants
VISA_CARD_PREFIX = 4
MASTER_CARD_PREFIX = 5
AMERICAN_EXPRESS_CARD_PREFIX = 37
DISCOVER_CARD_PREFIX = 6

VISA_CARD_STRING = "Visa"
MASTER_CARD_STRING = "Master"
AMERICAN_EXPRESS_CARD_STRING = "American Express"
DISCOVER_CARD_STRING = "Discover"


# Return true if the card number is valid
def isValid(number):

    numSize = getSize(number)

    if numSize < 13 or numSize > 16:
        return False

    if (prefixMatched(number, MASTER_CARD_PREFIX) or prefixMatched(number, VISA_CARD_PREFIX) or
        prefixMatched(number, AMERICAN_EXPRESS_CARD_PREFIX) or prefixMatched(number, DISCOVER_CARD_PREFIX)):

            numberReversed = str(number)[::-1]

            sumDoubleEvenPlaces = sumOfDoubleEvenPlaces(numberReversed)
            sumOddPlaces = sumOfOddPlace(numberReversed)
            sumOddEvenPlaces = sumDoubleEvenPlaces + sumOddPlaces

            if sumOddEvenPlaces % 10 == 0:
                return True
            else:
                return False

    else:
        return False


# Get the result from Step 2


''' 
    fn: sumOfDoubleEvenPlaces (message)
    Gets the card number. Calculates the sum of double even places

    Parameters
    ----------
    arg1 : string
        card number

    Returns
    ---------
    string
        returns the sum of the double even places

'''


def sumOfDoubleEvenPlaces(number):
    sumDoublePlaces = 0
    for idx in range(getSize(number)):
        if idx % 2 == 1:
            sumDoublePlaces += getDigit(int(number[idx]) * 2)
    return sumDoublePlaces



''' 
    fn: getSize (message)
    Return the number of digits in d. Supports length for string and int types

    Parameters
    ----------
    arg1 : string or int
        card number(d)

    Returns
    ---------
    int
        returns the size of the number

'''


# Return the number of digits in d
def getSize(d):

    # check if number is 0

    if d == 0 or d == '0':
        return 0

    if type(d) is str:
        return len(d)
    if type(d) is int:
        return int(math.log10(d)) + 1


# Return this number if it is a single digit, otherwise, return
# the sum of the two digits
def getDigit(number):
    if getSize(number) == 1:
        return number
    return int(number / 10) + int(number % 10)


# Return sum of odd place digits in number
def sumOfOddPlace(number):
    sumOfOddPlaces = 0
    number = str(number)
    for idx in range(getSize(number)):
        if idx % 2 == 0:
            sumOfOddPlaces += int(number[idx])
    return sumOfOddPlaces


# Return true if the digit d is a prefix for number
def prefixMatched(number, d):
    return getPrefix(number, 1) == d


# Return the first k number of digits from number. If the
# number of digits is less than k, return number
def getPrefix(number, k):
    if k == 0:
        return -1
    return int(number[0:k])


''' 
    fn: get_user_input(message)
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

def get_user_input(message):
    return input(message)


''' 
    fn: validate_input_blank(message)
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

def validate_input_blank(message):

    # Runs until the user inputs a non-blank value.
    while True:
        user_input = get_user_input(message)
        if user_input == '':
            print("Please do not leave the input blank")
        else:
            break
    return user_input


''' 
    fn: validate_is_number(message)
    Validate the user input basic case. Checks if thhe input is a number.

    Parameters
    ----------
    arg1 : string
        message for the console

    Returns
    ---------
    string
        returns the input of the user after validation.

'''

def validate_is_number(message):

    # Runs until the user inputs a non-blank numerical value.
    while True:
        user_input = validate_input_blank(message)
        num_format = re.compile(r'^\-?[1-9][0-9]*\.?[0-9]*')
        is_number = re.match(num_format, user_input)
        if not is_number:
            print("Please enter a digit")
        else:
            break
    return str(user_input)


''' 
    fn: checkCardType(message)
    Checks the card type.

    Parameters
    ----------
    arg1 : string
        number entered

    Returns
    ---------
    string
        returns true or false, whether the card is within a card type.

'''

def checkCardType(number):
    if prefixMatched(number, VISA_CARD_PREFIX):
        return VISA_CARD_STRING
    if prefixMatched(number, MASTER_CARD_PREFIX):
        return MASTER_CARD_STRING
    if prefixMatched(number, AMERICAN_EXPRESS_CARD_PREFIX):
        return AMERICAN_EXPRESS_CARD_STRING
    if prefixMatched(number, DISCOVER_CARD_PREFIX):
        return DISCOVER_CARD_PREFIX


# Main method to invoke card validation
def main():
    userInputCard = validate_is_number("Enter your card number(1-9):")

    if isValid(userInputCard):
        print("Your card is valid. Card type: " + checkCardType(userInputCard))
    else:
        print("Your card is invalid")


# Call Main method
main()