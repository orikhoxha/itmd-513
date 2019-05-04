'''
    Name: Orik Hoxha
    Class: ITMD 513
    Homework: 13
    Description: This class creates the GUI for the Change Counter app. It creates the labels, inputs and button for
                 calculating the total change value.
'''


import tkinter
from tkinter import messagebox
import createView
from ChangeCounter import ChangeCounter
import validateFields


class ChangeCounterGUI(object):

    # Labels array for the inputs. Will be used to dynamically create the lable widgets.
    labelInputArr = ['Quarters:', 'Dimes:', 'Nickles:', 'Pennies:', 'Half-dollar:', 'Dollar coin:']

    # lable values on the right side. Will be used to dynamically create the lable widgets.
    labelValueArr = ['Quarter value: $', 'Dime value: $', 'Nickle Value: $', 'Penny value: $', 'Half-dollar value: $',
                     'Dollar coin value: $']

    '''
        fn: __init__()
        Constructor for creating the ChangeCounterGUI object. Creates 4 frames: header, main(left main,right main).
        Initializes a ChangeCounter which will be used to organize the inputs into an object.

        Returns
        ---------
        Object
            returns self from constructor.
    '''

    def __init__(self):
        self.mainWindow = tkinter.Tk()
        self.headerFrame = tkinter.Frame()

        self.changeCounter = ChangeCounter()

        createView.createLabel(self.headerFrame, "Change counter").grid(row=0, column=0)
        self.horizontalLine = tkinter.Frame(height=1, width=900, bg="black")

        self.mainContentFrame = tkinter.Frame(bg=createView.WINDOW_BG_COLOR)
        self.mainContentLeft  = tkinter.Frame(self.mainContentFrame, bg=createView.WINDOW_BG_COLOR)
        self.mainContentRight = tkinter.Frame(self.mainContentFrame, bg=createView.WINDOW_BG_COLOR)

        self.createMainContent(self.mainContentLeft, self.mainContentRight)
        self.mainContentLeft.grid(row=0, column=1, padx=70, pady=30)
        self.mainContentRight.grid(row=0, column=3, padx=20)

        self.setWindowConfigurations()
        self.headerFrame.pack()
        self.horizontalLine.pack()
        self.mainContentFrame.pack()
        self.mainWindow.mainloop()

    '''
        fn: setWindowConfigurations()
        Sets the window main configurations for the GUI.

        Returns
        ---------
        void
    '''

    def setWindowConfigurations(self):
        self.mainWindow.geometry(createView.DIMENSION)
        self.mainWindow.configure(background=createView.WINDOW_BG_COLOR)

    '''
        fn: createMainContent()
        Sets the window main configurations for the GUI.
        
        Parameters
        ----------
        leftFrame : Frame
           Left frame with lable and input.

        rightFrame : Frame
           Right frame with lable and output.

        Returns
        ---------
        void
    '''

    def createMainContent(self, leftFrame, rightFrame):
        self.createLeftContent(leftFrame)
        self.createRightContent(rightFrame)

    '''
        fn: createLeftContent(frame)
        Create the left content of the main content. It calls the helper method createLabels for dynamically 
        creating the labels, and inputs.

        Parameters
        ----------
        frame : Frame
           Left frame with lable and input.

        Returns
        ---------
        void
    '''

    def createLeftContent(self, frame):

        self.computeBtn = tkinter.Button(frame, text="Compute",
                                         bg=createView.WINDOW_BG_COLOR,
                                         borderwidth=2, relief="solid",
                                         width=14,
                                         command=self.computeChangeCounter,
                                         font=('Helvetica', 15, 'bold')).grid(row=6, column=0, sticky='w')

        (self.quarterLabel, self.dimesLabel,
         self.nicklesLabel, self.penniesLabel,
         self.halfDollarLabel, self.coinDollarLabel) = createView.createLabels(frame, self.labelInputArr)

        (self.quarterInput, self.dimesInput,
         self.nicklesInput, self.penniesInput,
         self.halfDollarInput, self.coinDollarInput) = createView.createInputs(frame, len(self.labelInputArr))

    '''
        fn: createRightContent(frame)
        Create the right content of the main content. It calls the helper method createLabels for dynamically 
        creating the labels, and outputs.

        Parameters
        ----------
        frame : Frame
           Right frame with lable and input.

        Returns
        ---------
        void
    '''

    def createRightContent(self, frame):

        (self.quarterValueLabel,
         self.dimensValueLabel,
         self.nicklesValueLabel,
         self.penniesValueLabel,
         self.halfDollarValueLabel,
         self.coinDollarValueLabel) = createView.createLabels(frame, self.labelValueArr)

        (self.quartersValue,
         self.dimesValue,
         self.nicklesValue,
         self.penniesValue,
         self.halfDollarValue,
         self.coinDollarValue) = createView.createLabelsDefaultText(frame, len(self.labelInputArr), "0.00")

        self.totalValueLabel = createView.createLabel(frame, "Total Change value: $").grid(row=6, column=0, sticky='e')
        self.totalValue = createView.createLabel(frame, '0.00')
        self.totalValue.grid(row=6, column=1, sticky='w')

    '''
        fn: computeChangeCounter(frame)
        Gets the values from the inputs. Validates the values and creates the object ChangeCounter.

        Parameters
        ----------
        frame : Frame
           Right frame with lable and input.

        Returns
        ---------
        void
    '''

    def computeChangeCounter(self):

        quarterVal     = createView.getNumberOrZeroFromInput(self.quarterInput)
        dimesVal       = createView.getNumberOrZeroFromInput(self.dimesInput)
        nicklesVal     = createView.getNumberOrZeroFromInput(self.nicklesInput)
        penniesVal     = createView.getNumberOrZeroFromInput(self.penniesInput)
        halfDollarVal  = createView.getNumberOrZeroFromInput(self.halfDollarInput)
        coinDollar     = createView.getNumberOrZeroFromInput(self.coinDollarInput)

        if validateFields.validatePositiveInteger(quarterVal, dimesVal, nicklesVal, penniesVal, halfDollarVal, coinDollar):
            print("Here")
            self.changeCounter.setQuarters(quarterVal)
            self.changeCounter.setDimes(dimesVal)
            self.changeCounter.setNickles(nicklesVal)
            self.changeCounter.setPennies(penniesVal)
            self.changeCounter.setHalfDollar(halfDollarVal)
            self.changeCounter.setDollar(coinDollar)
            self.setCounterValues(self.changeCounter)
        else:
            tkinter.messagebox.showinfo("Error", "Values must be a positive integer.")

    '''
        fn: setCounterValues(changeCounter)
        Updates the output values for each input for the change counter.

        Parameters
        ----------
        changeCounter : ChangeCounter
           The changeCounter object.

        Returns
        ---------
        void
    '''

    def setCounterValues(self, changeCounter):
        self.quartersValue['text'] = changeCounter.calculateQuarters()
        self.dimesValue['text']    = changeCounter.calculateDimes()
        self.nicklesValue['text']  = changeCounter.calculateNickles()
        self.penniesValue['text']  = changeCounter.calculatePennies()
        self.halfDollarValue['text'] = changeCounter.calculateHalfDollars()
        self.coinDollarValue['text'] = changeCounter.getDollar()
        self.totalValue['text']      = changeCounter.calculateChangeCounter()


def main():
    ChangeCounterGUI()

if __name__ == '__main__':
    main()

