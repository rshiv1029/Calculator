from dis import dis
from tkinter import *
from tkinter.ttk import *

class Calculator:
    def __init__(self) -> None:
        # Variables needed
        self.equation = "Equation..."
        self.answer = 0
        self.digits = { 
            7:(1,1), 8:(1,2), 9:(1,3), 
            4:(2,1), 5:(2,2), 6:(3,3),
            1:(3,1), 2:(3,2), 3:(2,3),
            '.':(4,1), 0:(4,2), '=':(4,3)
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
        self.display = self.initDisplayFrame()
        self.buttons = self.initButtonsFrame()

        self.answerLabel, self.equationLabel = self.displayLabels()
        self.initButtons()

    def initDisplayFrame(self):
        displayFrame = Frame(self.mainWindow, height=222)
        
        displayFrame.pack(expand="True", fill="both")
        return displayFrame

    def displayLabels(self):
        # UPDATE FONT/FORMATTING(FG,BG)LATER
        eq = Label(self.display, anchor=E, text=self.equation)
        eq.pack(expand="True", fill="both")
        total = Label(self.display, anchor=E, text=str(self.answer))
        total.pack(expand="True", fill="both")
        return total,eq

    def initButtonsFrame(self) -> None:
        # Init the frame to add widgets
        buttonFrame = Frame(self.mainWindow)
        buttonFrame.pack(expand="True", fill="both")
        return buttonFrame
    
    def initButtons(self) -> None:
        # UPDATE FONT/FORMATTING(FG,BG)LATER
        for digit,gridVal in self.digits.items():
            button = Button(self.buttons, text=str(digit))
            button.grid(row=gridVal[0], column=gridVal[1], sticky=NSEW)
        for info in self.operators.values():
            button = Button(self.buttons, text=str(info[0]))
            button.grid(row=info[1][0], column=info[1][1],sticky=NSEW)
        
        
    def run(self):
        self.mainWindow.mainloop()

if __name__ == "__main__":
    c = Calculator()
    c.run()
