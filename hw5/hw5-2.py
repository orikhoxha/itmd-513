'''
    This program checks if a list is sorted. It expects n number of digits input from the user
    separated by space iex. 3 4 5 6.

    Name: Orik Hoxha
    Class: ITMD 513

'''

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
    listConverted = string.split()
    return listConverted


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
        lst = [eval(numeric_string) for numeric_string in lst]
        return lst
    except ValueError:
        return False


'''
    fn: buildMatrixFromList(lst, rows, cols)
    Converts a string list to a matrix.

    Parameters
    ----------
    lst : list(strings)
        the string list to be converted to a matrix.
    
    rows : int
        number of rows for the matrix.
        
    cols : int
        number of cols for the matrix.

    Returns
    ---------
    list of lists
        returns the matrix.
'''

def buildMatrixFromList(lst, rows, cols):

    if len(lst) != (rows * cols):
        return False

    matrix = list()
    index_boundary = 0
    for i in range(rows):
        cols_arr = lst[index_boundary: index_boundary + cols]
        index_boundary += cols
        matrix.append(cols_arr)

    return matrix


'''
    fn: multiply2Matrixed(matrix1, matrix2)
    Multiplies the two matrixes and produces the third matrix. It makes sure that the rows and columns length
    is correctly entered for the multiplication.

    Parameters
    ----------
    matrix1 : list of lists
        matrix 1 to be multiplied.

    matrix2 : list of lists
        matrix 2 to be multiplied.

    Returns
    ---------
    list of lists
        returns the multiplication of matrix1 and matrix2. 
'''

def multiply2Matrixed(matrix1, matrix2):

    matrix1RowsLen = getMatrixRowSize(matrix1)
    matrix1ColsLen = getMatrixColSize(matrix1)

    matrix2RowsLen = getMatrixRowSize(matrix2)
    matrix2ColsLen = getMatrixColSize(matrix2)

    if matrix1ColsLen != matrix2RowsLen:
        return False

    matrixProduct = initEmptyMatrix(matrix1RowsLen, matrix2ColsLen)

    for i in range(matrix1RowsLen):
        for j in range(matrix2ColsLen):
            for k in range(matrix1ColsLen):
                matrixProduct[i][j] += matrix1[i][k] * matrix2[k][j]
                if type(matrixProduct[i][j]) is float:
                    matrixProduct[i][j] = round(matrixProduct[i][j], 1)

    return matrixProduct


'''
    fn: validateUserInput(message)
    Check if user input is empty.

    Parameters
    ----------
    message : string
        message to be displayed in the console.


    Returns
    ---------
    string 
        returns the user input. 
'''

def validateUserInput(message):
    while True:
        userInput = input(message)
        if isStringEmpty(userInput):
            print('Please do not leave the input blank.')
        else:
            break
    return userInput


'''
    fn: validateUserInput(message)
    Extends the basic validation. Checks if the numbers entered are all digits.

    Parameters
    ----------
    message : string
        message to be displayed in the console.


    Returns
    ---------
    list (int or float) 
        returns the user input as a converted list from the string. 
'''

def validateUserInputList(message):
    while True:
        userInput = validateUserInput(message)
        if not convertStrListToNrList(userInput):
            print("Please enter only digits.")
        else:
            break
    return convertStrListToNrList(userInput)


'''
    fn: validateMatrixLength(message, rows, cols)
    Checks if the matrix rows and cols are matching with the values entered by the user.

    Parameters
    ----------
    message : string
        message to be displayed in the console.
        
    rows : string
        rows for the matrix.
        
    cols : string
        columns for the matrix.


    Returns
    ---------
    string
        returns the user input.
'''

def validateMatrixLength(message, rows, cols):
    while True:
        userInput = validateUserInputList(message)
        if len(userInput) != (rows * cols):
            print("The number of values within a matrix must be  %s" % (rows * cols))
        else:
            break

    return userInput


'''
    fn: validateMatrixWidthHeight(message)
    Checks if the matrix rows and cols is a digit and  >= 2

    Parameters
    ----------
    message : string
        message to be displayed in the console.

    Returns
    ---------
    string
        returns the user input.
'''


def validateMatrixWidthHeight(message):
    while True:
        userInput = validateUserInput(message)
        try:
            userInput = int(userInput)
            if userInput < 2:
                print("The matrix must contain at least 2 rows/columns ")
            else:
                return userInput
        except ValueError:
            print("Please enter a valid row or column length")



'''
    fn: isStringEmpty(message)
    Checks if the string after trimming is empty.

    Parameters
    ----------
    message : string
        message to be displayed in the console.

    Returns
    ---------
    boolean
        returns true if string length > 0, else false
'''


def isStringEmpty(lst):
    return len(lst.strip()) == 0


'''
    fn: printPrettifyMatrix(matrix)
    Prints the matrix in a human readable format

    Parameters
    ----------
    matrix : list of lists
        matrix to print.

    Returns
    ---------
    void
'''


def printPrettifyMatrix(matrix):
    rows = getMatrixRowSize(matrix)
    for i in range(rows):
        print(matrix[i])


'''
    fn: initEmptyMatrix(rows, cols)
    Initializes an empty array. Used for the product of the matrix1 and matrix2.

    Parameters
    ----------
    rows : string
        rows to be created. Matches with the number of rows in the matrix1.
        
    cols : string
        cols to be created. Matches with the number of cols in the matrix2.

    Returns
    ---------
    list of lists
        returns the matrix initialized with 0 values.
'''


def initEmptyMatrix(rows, cols):
    matrix = [[0 for x in range(cols)] for y in range(rows)]
    return matrix


'''
    fn: getMatrixColSize(matrix)
    Calculates the number of columns in a matrix.

    Parameters
    ----------
    matrix : string
        matrix to calculate the colums size for.

    Returns
    ---------
    int
        returns the number of columns in matrix.
'''


def getMatrixColSize(matrix):
    return len(matrix[0])


'''
    fn: getMatrixRowSize(matrix)
    Calculates the number of rows in a matrix.

    Parameters
    ----------
    matrix : string
        matrix to calculate the rows size for.

    Returns
    ---------
    int
        returns the number of columns in matrix.
'''

def getMatrixRowSize(matrix):
    return len(matrix)


'''
    fn: main()
    Starts the program. Gets the inputs for the matrixes, and checks if they are having the same length. If not,
    the multiplication will not continue.

    Parameters
    ----------
    matrix : string
        matrix to calculate the rows size for.

    Returns
    ---------
    int
        returns the number of columns in matrix.
'''


def main():
    matrix1RowsLength = validateMatrixWidthHeight("Please type the first matrix rows length:")
    matrix1ColsLength = validateMatrixWidthHeight("Please type the first matrix cols length:")

    matrix1 = validateMatrixLength("Please enter %s input digits for matrix 1:" % (matrix1ColsLength * matrix1RowsLength), matrix1RowsLength, matrix1ColsLength)

    matrix1 = buildMatrixFromList(matrix1, matrix1RowsLength, matrix1ColsLength)

    matrix2RowsLength = validateMatrixWidthHeight("Please type the matrix 2 rows length:")
    matrix2ColsLength = validateMatrixWidthHeight("Please type the matrix 2 cols length:")

    matrix2 = validateUserInputList(
        "Please enter %s input digits for matrix 2:" % (matrix2RowsLength * matrix2ColsLength))

    matrix2 = buildMatrixFromList(matrix2, matrix2RowsLength, matrix2ColsLength)

    if matrix1ColsLength != matrix2RowsLength:
        print("Cannot multiply. Validation matrix1(numcols) = matrix2(numrows).")
    else:
        matrixProduct = multiply2Matrixed(matrix1, matrix2)
        printPrettifyMatrix(matrixProduct)


if __name__ == '__main__':
    main()

