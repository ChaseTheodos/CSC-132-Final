##################################################
# Name: Chase Theodos
# Date: 11/01/21
# Description: CSC 132 - Final Project
##################################################

from tkinter import *
from playsound import playsound
from time import sleep
import headshots
import os

def launch():
    # the main GUI
    class MainGUI(Canvas):
        # list that holds user entered numbers
        combination = []
        # the constructor
        def __init__(self, parent):
            bg = PhotoImage(file="/home/pi/CSC132-Final/GUI/techBG.png")
            Canvas.__init__(self, parent)
            self.setupGUI()

        # sets up the GUI
        def setupGUI(self):

            # the button layout
            # 1 2 3
            # 4 5 6
            # 7 8 9
            #   0
            # UNLOCK

            # there are 5 rows (0 through 4)
            for row in range(5):
                Grid.rowconfigure(self, row, weight=1)
            # there are 3 columns (0 through 2)
            for col in range(3):
                Grid.columnconfigure(self, col, weight=1)

            # first row
            # 1
            img = PhotoImage(file="/home/pi/CSC132-Final/GUI/numPad/1.png")
            button = Button(self, image=img, \
                            borderwidth=0, highlightthickness=0, command=lambda: \
                    self.process("1"))
            button.image = img
            button.grid(row=2, column=0, sticky=N + S + E + W)
            # 2
            img = PhotoImage(file="/home/pi/CSC132-Final/GUI/numPad/2.png")
            button = Button(self, image=img, \
                            borderwidth=0, highlightthickness=0, \
                             command=lambda: \
                    self.process("2"))
            button.image = img
            button.grid(row=2, column=1, sticky=N + S + E + W)
            # 3
            img = PhotoImage(file="/home/pi/CSC132-Final/GUI/numPad/3.png")
            button = Button(self, image=img, \
                            borderwidth=0, highlightthickness=0, \
                             command=lambda: \
                    self.process("3"))
            button.image = img
            button.grid(row=2, column=2, sticky=N + S + E + W)
            # end first

            # second row
            # 4
            img = PhotoImage(file="/home/pi/CSC132-Final/GUI/numPad/4.png")
            button = Button(self,  image=img, \
                            borderwidth=0, highlightthickness=0, \
                             command=lambda: \
                    self.process("4"))
            button.image = img
            button.grid(row=3, column=0, sticky=N + S + E + W)
            # 5
            img = PhotoImage(file="/home/pi/CSC132-Final/GUI/numPad/5.png")
            button = Button(self,  image=img, \
                            borderwidth=0, highlightthickness=0, \
                             command=lambda: \
                    self.process("5"))
            button.image = img
            button.grid(row=3, column=1, sticky=N + S + E + W)
            # 6
            img = PhotoImage(file="/home/pi/CSC132-Final/GUI/numPad/6.png")
            button = Button(self,  image=img, \
                            borderwidth=0, highlightthickness=0, \
                             command=lambda: \
                    self.process("6"))
            button.image = img
            button.grid(row=3, column=2, sticky=N + S + E + W)
            # end second

            # third row
            # 7
            img = PhotoImage(file="/home/pi/CSC132-Final/GUI/numPad/7.png")
            button = Button(self,  image=img, \
                            borderwidth=0, highlightthickness=0, \
                             command=lambda: \
                    self.process("7"))
            button.image = img
            button.grid(row=4, column=0, sticky=N + S + E + W)
            # 8
            img = PhotoImage(file="/home/pi/CSC132-Final/GUI/numPad/8.png")
            button = Button(self,  image=img, \
                            borderwidth=0, highlightthickness=0, \
                             command=lambda: \
                    self.process("8"))
            button.image = img
            button.grid(row=4, column=1, sticky=N + S + E + W)
            # 9

            img = PhotoImage(file="/home/pi/CSC132-Final/GUI/numPad/9.png")
            button = Button(self,  image=img, \
                            borderwidth=0, highlightthickness=0, \
                             command=lambda: \
                    self.process("9"))
            button.image = img
            button.grid(row=4, column=2, sticky=N + S + E + W)
            # end third

            # fourth row
            # 0
            img = PhotoImage(file="/home/pi/CSC132-Final/GUI/numPad/0.png")
            button = Button(self,  image=img, \
                            borderwidth=0, highlightthickness=0, \
                             command=lambda: \
                    self.process("0"))
            button.image = img
            button.grid(row=5, column=1, sticky=N + S + E + W)

            # unlock
            img = PhotoImage(file="/home/pi/CSC132-Final/GUI/numPad/unlock.png")
            button = Button(self,  image=img, \
                            borderwidth=0, highlightthickness=0, \
                             command=lambda: \
                    self.process("tryUnlock"))
            button.image = img
            button.grid(row=6, column=0, columnspan=3, sticky=N + S + E + W)
            # end fourth

            # pack the GUI
            self.pack(fill=BOTH, expand=1)

            # pack the GUI
            self.pack(fill=BOTH, expand=1)

        def process(self, button):
            os.system('mpg123 /home/pi/CSC132-Final/audio/beep.mp3 &')
            combo = [1,8,9,4]
            admin = [1,3,3,7]
            # detects unlock button press
            if button == "tryUnlock":
                # correct combination
                if MainGUI.combination == combo:
                    sleep(0.5)
                    os.system('mpg123 /home/pi/CSC132-Final/audio/accessGranted.mp3 &')
                    window.destroy()
                elif MainGUI.combination == admin:
                    sleep(0.5)
                    os.system('mpg123 /home/pi/CSC132-Final/audio/adminAccess.mp3')
                    headshots.headshots()
                # wrong combination
                else:
                    sleep(0.5)
                    os.system('mpg123 /home/pi/CSC132-Final/audio/accessDenied.mp3')
                MainGUI.combination.clear()
            # reset combination list
            else:
                MainGUI.combination.append(int(button))

    # create the window
    window = Tk()
    # set the window title
    window.title("CSC 132 Final")
    # fullscreen
    window.attributes('-fullscreen', True)
    # generate the GUI
    p = MainGUI(window)
    # display the GUI and wait for user interaction
    window.mainloop()

