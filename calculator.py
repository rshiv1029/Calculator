from dis import dis
from string import digits
from tkinter import *
# from tkinter.ttk import *

BG_GRAY = "#c7e6fd"
OP_BLUE = "#c7e6fd"
BUT_BLUE = "#edf7fe"
CAMBRIA_DIGIT = ("Cambria", 24, "bold")
CAMBRIA_OP = ("Cambria", 16, "bold")
CAMBRIA_ANS = ("Cambria", 40, "bold")

def on_enter(e):
    e.widget['background'] = BUT_BLUE

    # e.config(background='OrangeRed3', foreground= "white")

def on_leave(e):
    e.widget['background'] = BG_GRAY
    # e.config(background= 'SystemButtonFace', foreground= 'black')

class Calculator:
    def __init__(self) -> None:
        # Variables needed
        self.needClear = False
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
        buttonFrame = Frame(self.mainWindow, bg=BG_GRAY)
        buttonFrame.pack(expand="True", fill="both")
        return buttonFrame

    #####################################################
    ##          Initialize Widgets for Frames          ##
    #####################################################
    def displayLabels(self):
        # UPDATE FONT/FORMATTING(FG,BG)LATER
        eq = Label(self.display, anchor=E, text=self.equation, font= CAMBRIA_OP, bg= "#85a8fc")
        eq.pack(expand="True", fill="both")
        total = Label(self.display, anchor=E, text=self.answer, font= CAMBRIA_ANS, bg= "#85a8fc")
        total.pack(expand="True", fill="both")
        return total,eq

    def initButtons(self) -> None:
        # UPDATE FONT/FORMATTING(FG,BG)LATER
        for digit,gridVal in self.digits.items():
            button = Button(self.buttons, text=str(digit), borderwidth=0, command=lambda l=digit: self.modifyEquation(l), bg=OP_BLUE, font=CAMBRIA_DIGIT)
            button.grid(row=gridVal[0], column=gridVal[1], sticky=NSEW)
            button.bind('<Enter>', on_enter)
            button.bind('<Leave>', on_leave)
        for digit,info in self.operators.items():
            button = Button(self.buttons, text=str(info[0]), borderwidth=0, command=lambda l=digit: self.modifyEquation(l), bg=OP_BLUE, font=CAMBRIA_OP)
            button.grid(row=info[1][0], column=info[1][1],sticky=NSEW)
            button.bind('<Enter>', on_enter)
            button.bind('<Leave>', on_leave)
        self.initSpecialButtons()

    def initSpecialButtons(self) -> None:    
        equalButton = Button(self.buttons, text='=', borderwidth=0, command=lambda: self.modifyAnswer(), bg=OP_BLUE, font=CAMBRIA_OP)
        equalButton.grid(row=4, column=3, columnspan=2, sticky=NSEW) 
        equalButton.bind('<Enter>', on_enter)
        equalButton.bind('<Leave>', on_leave)
        clearButton = Button(self.buttons, text='C', borderwidth=0, command=lambda: self.clear(), bg=OP_BLUE, font=CAMBRIA_OP)
        clearButton.grid(row=0, column=0, columnspan=4, sticky=NSEW)
        clearButton.bind('<Enter>', on_enter)
        clearButton.bind('<Leave>', on_leave) 

    ############################################
    ##          Auxilliary Functions          ##
    ############################################
    def updateEquationLabel(self):
        self.equationLabel.config(text=self.equation)

    def updateAnswerLabel(self):
        self.answerLabel.config(text=self.answer)

    def modifyEquation(self, digit):
        if self.needClear:
            self.needClear = False
            self.clear()
        self.equation += str(digit)
        self.updateEquationLabel()
    
    def modifyAnswer(self):
        self.answer = eval(self.equation)
        self.updateAnswerLabel()
        self.needClear = True
    
    def clear(self):
        self.equation = ""
        self.answer = ""
        self.updateAnswerLabel()
        self.updateEquationLabel()
    
    
    
    def run(self):
        self.mainWindow.mainloop()

if __name__ == "__main__":
    c = Calculator()
    c.run()
