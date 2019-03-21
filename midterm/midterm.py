from re import match as re_match
'''
    Midterm: This program calculates the loan amortization based on the loan amount,
             nr of years, and annual interest rate

    Name: Orik Hoxha
    Class: ITMD 513

'''


# Display output utils
# Columns to output. Cols can be switched or removed.
PROJECTION_TABLE_COLS = ["Payment#", "Interest", "Principal", "Balance"]
# Space between the columns output
SPACE_BETWEEN_COLS_HEADER = 12


MIN_AMT = 50

MIN_YEARS_LOAN = 1
MAX_YEARS_LOAN = 50


MIN_INTEREST_RATE_PERCENTAGE = 1
MAX_INTEREST_RATE_PERCENTAGE = 50


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
    Validate blank input.

    Parameters
    ----------
    arg1 : string
        message for the console

    Returns
    ---------
    string
        returns the input of the user after validation.

'''


def validateInputBlank(message):

    # Runs until the user inputs a non-blank value.
    while True:
        user_input = getUserInput(message)
        if user_input == '':
            print("Please do not leave the input blank")
        else:
            break
    return user_input


'''
    fn: validateInputNumber(message)
    Validate input is number.

    Parameters
    ----------
    arg1 : string
        message for the console

    Returns
    ---------
    int or float
        returns the input of the user after validation.

'''


def validateInputNumber(message):
    while True:
        user_input = validateInputBlank(message)
        if not user_input.lstrip("-").replace(".", "").isdigit():
            print("Please enter a digit")
        elif float(user_input) <= 0:
            print("Please enter a positive number")

        else:
            break

    return eval(user_input)


'''
    fn: validateInputInt(message)
    Validate input is integer.

    Parameters
    ----------
    arg1 : string
        message for the console

    Returns
    ---------
    int
        returns the input of the user after validation.

'''


def validateInputInt(message):
    while True:
        user_input = validateInputNumber(message)
        if not isinstance(user_input, int):
            print("The number must be integer")
        else:
            break
    return user_input


'''
    fn: validateInputPercentage(message)
    Validate the annual interest rate. Check for the minumum and maximum allowed values

    Parameters
    ----------
    arg1 : string
        message for the console

    Returns
    ---------
    int or float
        returns the input of the user after validation.

'''


def validateInputPercentage(message):
    while True:
        user_input = validateInputNumber(message)
        if user_input > MAX_INTEREST_RATE_PERCENTAGE or user_input < MIN_INTEREST_RATE_PERCENTAGE:
            print("Please enter percentage between %s and %s" % (MIN_INTEREST_RATE_PERCENTAGE, MAX_INTEREST_RATE_PERCENTAGE))
        else:
            break
    return user_input


'''
    fn: validateInputYears(message)
    Validate the number of years. Check for the minumum and maximum allowed values.

    Parameters
    ----------
    arg1 : string
        message for the console

    Returns
    ---------
    int
        returns the input of the user after validation.

'''


def validateInputYears(message):
    while True:
        user_input = validateInputInt(message)
        if user_input > MAX_YEARS_LOAN or user_input < MIN_YEARS_LOAN:
            print("Please enter number of years between %s and %s" % (MIN_YEARS_LOAN, MAX_YEARS_LOAN))
        else:
            break
    return user_input


'''
    fn: calculateMonthlyInterestRate(annualInterestRate)
    Calculate the monthly interest rate. Formula used ( annual interest rate / months per year / 100).

    Parameters
    ----------
    arg1 : float
        The annual interest rate in percentage.
        
    Returns
    ---------
    float
        returns the month interest rate.

'''


def calculateMonthlyInterestRate(annualInterestRate):
    assert isinstance(annualInterestRate, (int, float))
    return round(annualInterestRate / 12 / 100, 6)


'''
    fn: calculateMonthlyInterest(annualInterestRate, balance)
    Calculate the monthly interest. Formula used ( annual interest rate * balance).

    Parameters
    ----------
    arg1 : float
        The monthly interest rate.
        
    arg2 : float
        Current balance.

    Returns
    ---------
    float
        returns the month interest.

'''


def calculateMonthlyInterest(monthyInterestRate, balance):
    return round(monthyInterestRate * balance, 2)


'''
    fn: calculatePrincipal(monthlyPayment, monthlyInterest)
    Calculate the monthly interest. Formula used ( monthly payment - monthly interest).

    Parameters
    ----------
    arg1 : float
        The monthly payment.

    arg2 : float
        The monthly interest.

    Returns
    ---------
    float
        returns the monthly principal.

'''


def calculatePrincipal(monthlyPayment, monthlyInterest):
    return round(monthlyPayment - monthlyInterest, 2)


'''
    fn: calculateRemainingBalance(balance, principal)
    Calculate the remaining balance. In order to handle values when the final balance goes under 0 like 
    -0.03, then returns 0. Formula used ( balance - principal).

    Parameters
    ----------
    arg1 : float
        The current balance.

    arg2 : float
        The principal.

    Returns
    ---------
    float
        returns the monthly principal.

'''


def calculateRemainingBalance(balance, principal):
    balance = round(balance - principal, 2)
    if balance <= 0:
        return 0
    return balance


'''
    fn: calculateMonthlyPayment(loanAmt,monthInterestRate, period)
    Calculate the monthly payment. 
    Formula used ( loan amount * monthly interest rate / (1 - (1 + month interest rate)^ -period))

    Parameters
    ----------
    arg1 : float
        The loan amount.

    arg2 : float
        The monthly interest rate.
    
    arg3 : int
        The period of loan.

    Returns
    ---------
    float
        returns the monthly principal.

'''


def calculateMonthlyPayment(loanAmt,monthInterestRate, period):
    return round(loanAmt * monthInterestRate / (1 - pow(1 + monthInterestRate, -period)), 2)


'''
    fn: calculateTotalPayment(monthlyPayment, periodMonth)
    Calculate the total payment for the loan. Formula used ( monthly payment * period of years in months)

    Parameters
    ----------
    arg1 : float
        The monthly payment.

    arg2 : int
        Period of years in months.

    Returns
    ---------
    float
        returns the total payment.

'''


def calculateTotalPayment(monthlyPayment,periodMonth):
    return round(monthlyPayment * periodMonth, 2)


'''
    fn: periodYearToMonth(years)
    Convert years to months.

    Parameters
    ----------
    arg1 : float
        The years.

    Returns
    ---------
    int
        returns the number of months.

'''


def periodYearToMonth(years):
    assert isinstance(years, int)
    return years * 12


'''
    fn: createLoanAmortization(loanAmt,periodInMonth,monthlyInterestRate, monthlyPayment)
    Generates a list of payment nr, interest, principal and balance per each month.

    Parameters
    ----------
    arg1 : float
        The loan amount.

    arg2 : int
        Period of years in months.
        
    arg3 : int
        Monthly interest rate.
        
    arg4 : int
        Monthly payment.

    Returns
    ---------
    list of (key,value)
        returns the list of each month details(payment nr, interest, principal and balance)

'''


def createLoanAmortization(loanAmt,periodInMonth,monthlyInterestRate, monthlyPayment):

    loanAmortizationList = []

    balance = loanAmt

    for i in range(1, periodInMonth + 1):
        monthlyInterest = calculateMonthlyInterest(monthlyInterestRate, balance)
        principal = calculatePrincipal(monthlyPayment, monthlyInterest)
        balance = calculateRemainingBalance(balance, principal)
        loanAmortizationList.append({"Payment#": i, "Interest": monthlyInterest, "Principal": principal, "Balance": balance})

    return loanAmortizationList


'''
    fn: prettifyAmortizationMonth(row, spaceBetweenHeader)
    Calculates the spaces between columns to be display for each row - month.

    Parameters
    ----------
    arg1 : dictionary
        The key,value dictionary with the info for the month.

    arg2 : int
        Spaces between cols.


    Returns
    ---------
    string
        returns the month values with spaces calculated.

'''


def prettifyAmortizationMonth(row, spaceBetweenHeader):

    amortizationRow = ""

    for header in PROJECTION_TABLE_COLS:
        valToPrint = str(row[header])
        amortizationRow += valToPrint + " " * (len(spaceBetweenHeader) + len(header) - len(valToPrint))

    return amortizationRow


'''
    fn: buildHeader(headerList, spaceBetween)
    Builds the header columns.

    Parameters
    ----------
    arg1 : list
        List of columns to be displayed

    arg2 : int
        Spaces between column headers.


    Returns
    ---------
    string
        returns the header with columns formatted.

'''

def buildHeader(headerList, spaceBetween):
    header = ""
    for value in headerList:
        header += value + spaceBetween
    return header


'''
    fn: displayAmortizationSchedule(monthlyPayment, totalPayment, loanAmortizationList)
    Displays the monthly payment, total payment, column headers, and monthly amortization rows.

    Parameters
    ----------
    arg1 : float
        The monthly payment.

    arg2 : float
        The total payment.
        
    arg3 : list
        The list of monthly loan amortization.


    Returns
    ---------
    void

'''


def displayAmortizationSchedule(monthlyPayment, totalPayment, loanAmortizationList):

    print("")
    print("Monthly Payment:" + str(monthlyPayment))
    print("Total Payment: " + str(totalPayment))
    print("")

    spaceBetween = " " * SPACE_BETWEEN_COLS_HEADER

    print(buildHeader(PROJECTION_TABLE_COLS, spaceBetween))

    for row in loanAmortizationList:
        print(prettifyAmortizationMonth(row, spaceBetween))


'''
    fn: main()
    Gets the input for loan amount, nryears, and annual interest rate.
    Calls the monthInterestRate, periodInMonth, monthlyPayment, totalPayment, and loanAmortizationList methods
    for calculation of the monthly loan amortization. Finally, calls the displayAmortizationSchedule method
    for displayin the amortization values.

    Parameters
    ----------
    arg1 : float
        The monthly payment.

    arg2 : float
        The total payment.

    arg3 : list
        The list of monthly loan amortization.


    Returns
    ---------
    void

'''


def main():
    loanAmt = validateInputNumber("Please enter the amount: ")
    nrYears = validateInputYears("Number of years: ")
    annualInterestRate = validateInputPercentage("Annual Interest rate in percentage(%):")

    monthInterestRate = calculateMonthlyInterestRate(annualInterestRate)
    periodInMonth = periodYearToMonth(nrYears)
    monthlyPayment = calculateMonthlyPayment(loanAmt, monthInterestRate, periodInMonth)

    totalPayment = calculateTotalPayment(monthlyPayment, periodInMonth)

    loanAmortizationList = createLoanAmortization(loanAmt, periodInMonth, monthInterestRate, monthlyPayment)

    displayAmortizationSchedule(monthlyPayment, totalPayment, loanAmortizationList)


if __name__ == '__main__':
    main()


