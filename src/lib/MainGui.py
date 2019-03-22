from tkinter import Tk, Label, Button
from .Translation import Translation
# how i can do 1 import for 2 files ?
class MainGui():

    def __init__(self, master):
        CurrentLangue = "Pl"
        self.master = master
        master.title("Golf Time Pro")

        self.label = Label(master, text=Translation.translator("Welcome on our application",CurrentLangue))
        self.label.pack()

        self.greet_button = Button(master, text=Translation.translator("Greet",CurrentLangue), command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text=Translation.translator("Close",CurrentLangue), command=master.quit)
        self.close_button.pack()

    def greet(self):
        print(Translation.translator("Welcome on our application",CurrentLangue))
