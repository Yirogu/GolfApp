from tkinter import *
from tkinter import messagebox
from .Translation import Translation
# how i can do 1 import for 2 files ?
class MainGui():
    CurrentLangue = 'Pl'
    def __init__(self, master):

        self.master = master
        master.title("Golf Time Pro")
        variable = StringVar(master)
        # variable.set('Eng')

        self.popupMenu = OptionMenu(master, variable,'Eng','Pl' )
        self.popupMenu.pack()


        self.label = Label(master, text=Translation.translator("Welcome on our application",self.CurrentLangue))
        self.label.pack()

        self.greet_button = Button(master, text=Translation.translator("Greet",self.CurrentLangue), command=self.greet)
        self.greet_button.pack()
        
        self.reset_button = Button(master, text=Translation.translator("reset",self.CurrentLangue), command=lambda:MainGui.reset(variable.get(),master).quit)
        self.reset_button.pack()

        self.close_button = Button(master, text=Translation.translator("Close",self.CurrentLangue), command=master.quit)
        self.close_button.pack()

    def reset(variable,master):
        if variable != MainGui.CurrentLangue :
            MainGui.CurrentLangue = variable
            print(MainGui.CurrentLangue)
            return master
    def greet(self):
        print(Translation.translator("Welcome on our application",self.CurrentLangue))
