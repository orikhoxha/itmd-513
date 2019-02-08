import math
# must have between 13 and 16 digits

'''
    4 - visa
    5 - Mastercard credit cards
    37 - American Express cards
    6 - for Discovery cards
'''

'''
# Return true if the card number is valid
def isValid(number):

'''

# Get the result from Step 2
def sumOfDoubleEvenPlaces(number):
    number_string = str(number)
    for num in number_string[::-2]:
        print(num)


'''
# Return this number if it is a single digit, otherwise, return
# the sum of the two digits
def getDigit(number):
    size  =  getSize(number)
    if size == 1:
        return number

    return firstDigit(number) + lastDigit(number)




# Return sum of odd place digits in number
def sumOfOddPlace(number):
'''


'''
# Return true if the digit d is a prefix for number
def prefixMatched(number, d):



# Return the number of digits in d
def getSize(d):
    return int(math.log10(d)) + 1



# Return the first k number of digits from number. If the
# number of digits is less than k, return number
def getPrefix(number, k):
    if number < k:
        return number



def firstDigit(number):
    return int(number / 10)

def lastDigit(number):
    return int(number % 10)

'''

sumOfDoubleEvenPlaces(123456)