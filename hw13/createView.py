'''
    Name: Orik Hoxha
    Class: ITMD 513
    Homework: 13
'''


import tkinter

# Static default values for GUI
LABEL_FONT = ('Helvetica', 20, 'bold')
TEXT_FONT =  ('Helvetica', 5, 'bold')
WINDOW_BG_COLOR = '#ffffcb'
DIMENSION = "900x500"
DEFAULT_BORDER = 2

DEFAULT_TEXT_VAL = "0.00"


'''
    fn: createInput(frame)
    Creates an Entry on the particular frame.

    Parameters
    ----------
    frame : Frame
       The frame holding the entry.

    Returns
    ---------
    Entry
'''


def createInput(frame):
    return tkinter.Entry(frame, bg=WINDOW_BG_COLOR, font=LABEL_FONT, bd=3, width=7)


'''
    fn: createLabel(frame, text, default-> background)
    Creates a Label on the particular frame.

    Parameters
    ----------
    frame : Frame
       The frame holding the entry.
       
    text : string
       The value to be shown on label.
       
    background : string
       The background of the frame.

    Returns
    ---------
    Label
'''


def createLabel(frame, text, background=WINDOW_BG_COLOR):
    return tkinter.Label(frame, text=text, bg=background, pady=8, font=LABEL_FONT)


'''
    fn: createInputs(frame, numInputs)
    Creates a number of inputs.

    Parameters
    ----------
    frame : Frame
       The frame holding the inputs.

    numInputs : integer
       Number of inputs to create

    Returns
    ---------
    array
        array of the inputs
'''


def createInputs(frame, numInputs):
    row = 0
    inputsArr = []
    for i in range(0, numInputs):
        input = createInput(frame)
        input.grid(row=row, column=1, sticky='w')
        inputsArr.append(input)
        row += 1
    return inputsArr


'''
    fn: createLabels(frame, labelArray)
    Creates a number of labels.

    Parameters
    ----------
    frame : Frame
       The frame holding the inputs.

    numLabels : array of string
       The array of the string values for creating the labels.

    Returns
    ---------
    array
        array of the labels
'''


def createLabels(frame, labelArray):
    row = 0
    labelsArray = []
    for label in labelArray:
        label = createLabel(frame, label)
        label.grid(row=row, column=0, sticky='e')
        labelsArray.append(label)
        row += 1
    return labelsArray


'''
    fn: createLabelsDefaultText(frame, numLabels, defaultLabelText)
    Creates a number of labels.

    Parameters
    ----------
    frame : Frame
       The frame holding the labels.

    numLabels : integer
       Number of labels to create
       
    defaultLabelText : string
       Default value for the labels.

    Returns
    ---------
    array
        array of the labels
'''


def createLabelsDefaultText(frame, numLabels, defaultLabelText):
    row = 0
    labelsArray = []
    for label in range(0, numLabels):
        label = createLabel(frame, defaultLabelText)
        label.grid(row=row, column=1, sticky='e')
        labelsArray.append(label)
        row += 1
    return labelsArray


'''
    fn: getNumberOrZeroFromInput(input)
    Gets the value from sn Entry widget. Returns 0 if input is empty. Otherwise return the value entered.

    Parameters
    ----------
    input : Entry
       The input.

    Returns
    ---------
    int|float|string
        the number from the input.
'''


def getNumberOrZeroFromInput(input):
    val = input.get()
    if val == "":
        return 0
    try:
        return eval(val)
    except NameError:
        return val

