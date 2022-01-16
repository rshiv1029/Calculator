from dis import dis
from string import digits
from tkinter import *
# from tkinter.ttk import *

class Calculator:
    def __init__(self) -> None:
        # Variables needed
        self.equation = ""
        self.answer = ""
        self.digits = { 
            7:(1,1), 8:(1,2), 9:(1,3), 
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            '.':(4,1), 0:(4,2)
        }
        self.operators = {
            "/": ("\u00F7", (0,4)),
            "*": ("\u00D7", (1,4)),
            "-": ("-", (2,4)),
            "+": ("+", (3,4)),
        }
        # Init the GUI for Calculator
        self.mainWindow = Tk()
        self.mainWindow.title("Calculator")
        self.mainWindow.geometry("375x667")
        
        # Call functions to init frames
        self.display, self.buttons = self.initFrames()

        self.buttons.rowconfigure(0,weight=1)
        for x in range(1,5):
            self.buttons.rowconfigure(x,weight=1)
            self.buttons.columnconfigure(x,weight=1)
        self.answerLabel, self.equationLabel = self.displayLabels()
        self.initButtons()

    #############################################
    ##          Initialize two frames          ##
    #############################################          
    def initFrames(self):
        return self.initDisplayFrame(), self.initButtonsFrame()

    def initDisplayFrame(self):
        displayFrame = Frame(self.mainWindow, height=222)
        
        displayFrame.pack(expand="True", fill="both")
        return displayFrame
    
    def initButtonsFrame(self):
        # Init the frame to add widgets
        buttonFrame = Frame(self.mainWindow)
        buttonFrame.pack(expand="True", fill="both")
        return buttonFrame

    #####################################################
    ##          Initialize Widgets for Frames          ##
    #####################################################
    def displayLabels(self):
        # UPDATE FONT/FORMATTING(FG,BG)LATER
        eq = Label(self.display, anchor=E, text=self.equation)
        eq.pack(expand="True", fill="both")
        total = Label(self.display, anchor=E, text=self.answer)
        total.pack(expand="True", fill="both")
        return total,eq

    def initButtons(self) -> None:
        # UPDATE FONT/FORMATTING(FG,BG)LATER
        for digit,gridVal in self.digits.items():
            button = Button(self.buttons, text=str(digit), borderwidth=0, command=lambda l=digit: self.modifyEquation(l))
            button.grid(row=gridVal[0], column=gridVal[1], sticky=NSEW)
        
        for info in self.operators.values():
            button = Button(self.buttons, text=str(info[0]), borderwidth=0, command=lambda l=info[0]: self.modifyEquation(l))
            button.grid(row=info[1][0], column=info[1][1],sticky=NSEW)
        self.initSpecialButtons()

    def initSpecialButtons(self) -> None:    
        equalButton = Button(self.buttons, text='=', borderwidth=0, command=lambda: self.modifyAnswer())
        equalButton.grid(row=4, column=3, columnspan=2, sticky=NSEW) 
        clearButton = Button(self.buttons, text='C', borderwidth=0)
        clearButton.grid(row=0, column=0, columnspan=4, sticky=NSEW) 

    ############################################
    ##          Auxilliary Functions          ##
    ############################################
    def updateEquationLabel(self):
        self.equationLabel.config(text=self.equation)

    def updateAnswerLabel(self):
        self.answerLabel.config(text=self.answer)

    def modifyEquation(self, digit):
        self.equation += str(digit)
        self.updateEquationLabel()
    
    def modifyAnswer(self):
        self.answer = eval(self.equation)
        self.updateAnswerLabel()

    def run(self):
        self.mainWindow.mainloop()

if __name__ == "__main__":
    c = Calculator()
    c.run()
