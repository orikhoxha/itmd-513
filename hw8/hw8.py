'''


    Name: Orik Hoxha
    Class: ITMD 513
    Description: This program lists, adds, changes, searches, and deletes persons from the list.

'''

import re
import os


LIST_OPTION = ["add", "lookup", "change", "delete", "list", "exit"]


emailPatternRegex = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"

FILE_NAME_PERSONS_LIST = "persons-1.txt"


'''
    fn: isStringEmpty(message)
    Checks if the string is empty.

    Parameters
    ----------
    string : string
        the string to check the length for.

    Returns
    ---------
    boolean
        returns true if the length >= 1, otherwise false.
'''


def isStringEmpty(string):
    return len(string.strip()) == 0


'''
    fn: isStringAlpha(message)
    Checks if the string contains alphabet characters only.

    Parameters
    ----------
    string : string
        the string to check the characters for.

    Returns
    ---------
    boolean
        returns true if string contains alphabet characters only.
'''


def isStringAlpha(string):
    return string.replace(" ", "").isalpha()


'''
    fn: isValidEmail(message)
    Checks if email is valid. Uses the regular expression to validate.

    Parameters
    ----------
    string : string
        the string to check the characters for.

    Returns
    ---------
    boolean
        returns true if string is email.
'''


def isValidEmail(string):
    return re.match(emailPatternRegex, string)


'''
    fn: validatePersonInputBlank(message)
    Checks if input is blank.

    Parameters
    ----------
    message : string
        the string to check the characters for.

    Returns
    ---------
    boolean
        returns true if string is email.
'''


def validatePersonInputBlank(message):
    while True:
        personInput = input(message)
        if isStringEmpty(personInput):
            print('Please do not leave the input blank')
        else:
            break
    return personInput


'''
    fn: validatePersonInputBlank(message)
    Outputs the error message if the string is empty.

    Parameters
    ----------
    message : string
        The message to output.

    Returns
    ---------
    string
        returns person input.
'''


def validatePersonName(message):

    while True:
        personInput = validatePersonInputBlank(message)

        if not isStringAlpha(personInput):
            print("The name can contain only alphabetic characters(a-z) (A-Z)")
        else:
            break

    return personInput


'''
    fn: validatePersonEmail(message)
    Outputs the error message if the string is not email.

    Parameters
    ----------
    message : string
        The message to output.

    Returns
    ---------
    string
        returns person input.
'''


def validatePersonEmail(message):

    while True:
        personInput = validatePersonInputBlank(message)
        if not isValidEmail(personInput):
            print("The email address is not vaild. Please enter correct.")
        else:
            break

    return personInput


'''
    fn: validateListOption(message)
    Checks if the the person option is one of the list options.

    Parameters
    ----------
    message : string
        The message to output.

    Returns
    ---------
    string
        returns input
'''


def validateListOption(message):
    while True:
        personInput = validatePersonInputBlank(message)
        if personInput not in LIST_OPTION:
            print("Please choose from the options " + str(LIST_OPTION))
            return None
        else:
            break

    return personInput


'''
    fn: addNewPerson(name, email)
    Adds new person to the list of dictionaries.

    Parameters
    ----------
    name : string
        The name.
        
    email : string
        The email.

    Returns
    ---------
    void
'''


def addNewPerson(name, email):
    personList.append({"name": name, "email": email})


'''
    fn: lookupEmailAddress(name)
    Checks for the email address of the name.

    Parameters
    ----------
    name : string
        The name.

    Returns
    ---------
    string
        returns email address.
'''


def lookupEmailAddress(name):
    assert personExists(name)
    for person in personList:
        if person["name"] == name:
            return person["email"]
    return None


'''
    fn: updateEmail(personName, newPersonEmail)
    Updates the email address of the person.

    Parameters
    ----------
    personName : string
        The name.
        
    newPersonEmail : string
        The new email of the person.

    Returns
    ---------
    void
'''


def updateEmail(personName, newPersonEmail):

    assert personExists(personName)

    for person in personList:
        if person["name"] == personName:
            person["email"] = newPersonEmail
            break


'''
    fn: deleteByName(name)
    Deletes the person.

    Parameters
    ----------
    name : string
        The name.

    Returns
    ---------
    void
'''


def deleteByName(name):
    assert personExists(name)
    global personList
    personList = list(filter(lambda person: person["name"] != name, personList))


'''
    fn: personExists(name)
    Checks if the person exists.

    Parameters
    ----------
    name : string
        The name.

    Returns
    ---------
    Boolean
        True if the person exists. False otherwise.
'''


def personExists(name):
    for person in personList:
        if person["name"] == name:
            return True
    return False


'''
    fn: personNotExistsMessage(name)
    Prints the message for person doesn't exist.

    Parameters
    ----------
    name : string
        The name.

    Returns
    ---------
    void
'''


def personExistsMessage(name):
    print("Person %s exist" % name)


'''
    fn: personNotExistsMessage(name)
    Prints the message for person doesn't exist.

    Parameters
    ----------
    name : string
        The name.

    Returns
    ---------
    void
'''


def personNotExistsMessage(name):
    print("Person %s doesn't exist" % name)


'''
    fn: personActionMessage(name, action)
    Prints the message action(add,delete,change) for a person.

    Parameters
    ----------
    name : string
        The name.
        
    action : string
        The action (add, delete,change)

    Returns
    ---------
    void
'''


def personActionMessage(name, action):
    print("Person %s  %s" % (name, action))


'''
    fn: listEmptyMessage()
    Prints the list empty message.

    Returns
    ---------
    void
'''


def listEmptyMessage():
    print("The list is empty")


'''
    fn: fileExists(fileName)
    Checks if file exists.
    
    Parameters
    ----------
    fileName : string
        The file name.

    Returns
    ---------
    Boolean
        True if file exists. False otherwise.
'''


def fileExists(fileName):
    return os.path.isfile(fileName)


'''
    fn: saveToFile(personList, fileName)
    Opens a file. Saves the list of persons to the file, and closes the file.

    Parameters
    ----------
    personListr : list
        The list of persons to save to the file.

    fileName : string
        The file name to save the list of persons.

    Returns
    ---------
    void
'''


def saveToFile(personList, fileName):
    file = open(fileName, "w")
    for person in personList:
        file.write(toString(person) + "\n")
    file.close()


'''
    fn: loadPersonListFromFile(fileName)
    Opens a file. Converts rows to name, email values and saves to the list of persons.

    Parameters
    ----------
    fileName : string
        The file name to save the list of persons.

    Returns
    ---------
    list
        List of persons.
'''


def loadPersonListFromFile(fileName):

    if fileExists(FILE_NAME_PERSONS_LIST):
        file = open(fileName, "r")
        personList = []

        for person in file:
            personRow = {}
            for personAttributes in person.split(","):
                keyValue = personAttributes.rstrip("\n").split(":")
                personRow[keyValue[0].strip()] = keyValue[1].strip()
            personList.append(personRow)

        file.close()
        return personList
    else:
        print("File doesn't exist")


'''
    fn: printOptions(fileName)
    Prints the options for the first time program starts.

    Returns
    ---------
    void
'''


def printOptions():
    print("To add a person type add \n"
          "To lookup a person's email please type lookup \n"
          "To change the email address for existing person please type change \n"
          "To delete a person please type delete \n"
          "Choose exit to terminate the program")


'''
    fn: personAddAction(fileName)
    Gets the name and email. Prints the message for adding a person.
    
    Returns
    ---------
    void
'''


def personAddAction():

    personInputName = validatePersonName("Enter name: ")

    if personExists(personInputName):
        personExistsMessage(personInputName)
    else:
        personInputEmailAddress = validatePersonEmail("Email address: ")
        addNewPerson(personInputName, personInputEmailAddress)
        personActionMessage(personInputName, "added")


'''
    fn: personLookupAction()
    Gets the name for person. Prints the message for searching a person.
    
    Returns
    ---------
    void
'''


def personLookupAction():
    personLookupName = validatePersonInputBlank("Enter the name to search the email:")
    if not personExists(personLookupName):
        personNotExistsMessage(personLookupName)
    else:
        print("The email address is " + lookupEmailAddress(personLookupName))


'''
    fn: personDeleteAction()
    Gets the name for person. Prints the message for deleting a person.

    Returns
    ---------
    void
'''


def personDeleteAction():
    personInputName = validatePersonInputBlank("Enter name to delete: ")
    if not personExists(personInputName):
        personNotExistsMessage(personInputName)
    else:
        deleteByName(personInputName)
        personActionMessage(personInputName, "deleted")


'''
    fn: personChangeAction()
    Gets the name for person. Prints the message for changing a person's email.

    Returns
    ---------
    void
'''


def personChangeAction():
    personInputName = validatePersonInputBlank("Enter name to update the email: ")
    if not personExists(personInputName):
        personNotExistsMessage(personInputName)
    else:
        personInputNewEmail = validatePersonEmail("Enter new email address: ")
        updateEmail(personInputName, personInputNewEmail)
        personActionMessage(personInputName, "email changed")


'''
    fn: personListAction()
    Checks the list size. Prints the message for the list size accordingly.

    Returns
    ---------
    void
'''


def personListAction():
    if len(personList) == 0:
        listEmptyMessage()
    else:
        printpersonList(personList)


'''
    fn: personListAction(person)
    Formats the person dictionary to a name, email format.

    Parameters
    ----------
    person : dictionary
        The dictionary of the person.

    Returns
    ---------
    string
        string of the person dictionary to name, email.
'''


def toString(person):
    return "name: %s, email: %s" % (person["name"], person["email"])


'''
    fn: printpersonList(personList)
    Prints the persons list.

    Parameters
    ----------
    personList : list of dictionaries
        The list of the person dictionaries.

    Returns
    ---------
    void
'''


def printpersonList(personList):
    for person in personList:
        print(toString(person))


'''
    fn: printSavedFileMessage(personList)
    Prints the message when the program is terminated.

    Returns
    ---------
    void
'''


def printSavedFileMessage():
    print("You have terminated the program. Changes made in the file %s " % FILE_NAME_PERSONS_LIST)


'''
    fn: makepersonAction(personInputList)
    Makes actions depending on the list options that the person chooses.

    Parameters
    ----------
    personInputList : list of dictionaries
        The list of the person dictionaries.

    Returns
    ---------
    void
'''


def makepersonAction(personInputList):

    if personInputList == "add":
        personAddAction()
    elif personInputList == "lookup":
        personLookupAction()
    elif personInputList == "delete":
        personDeleteAction()
    elif personInputList == "change":
        personChangeAction()
    elif personInputList == "list":
        personListAction()


# loads the persons from the file to a list of dictionaries
personList = loadPersonListFromFile(FILE_NAME_PERSONS_LIST)


'''
    fn: main()
    Checks for person input while the person doesn't type exit. When exit, the program terminates.

    Returns
    ---------
    void
'''


def main():

    print("List loaded from file: " + FILE_NAME_PERSONS_LIST)

    printOptions()
    personInputList = validateListOption("Please choose from the list %s options: " % str(LIST_OPTION))

    while personInputList != "exit":
        makepersonAction(personInputList)
        personInputList = validateListOption("Please choose from the list %s options: " % str(LIST_OPTION))

    printSavedFileMessage()

    print("person list after change is ")
    printpersonList(personList)

    saveToFile(personList, FILE_NAME_PERSONS_LIST)


if __name__ == '__main__':
    main()