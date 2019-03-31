import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from .Translation import Translation
from .Settings import Settings
from .Refresh import Refresh

# how i can do 1 import for 2 files ?
LARGE_FONT = ("Verdana", 12)
CurrentLangue = Settings.CurrentLangue()
class MainGui(tk.Tk):

    def __init__ (self,*args,**kwargs) :

        tk.Tk.__init__(self,*args,**kwargs)
        tk.Tk.title(self,"Golf Time Pro")
        img = tk.PhotoImage(file='/home/stach/Desktop/Python3/GolfApp/src/lib/logo.gif')
        self.tk.call('wm','iconphoto',self._w,img)

        container = tk.Frame(self)
        container.pack(side='top',fill='both', expand = True )
        container.grid_rowconfigure(0,weight =1)
        container.grid_columnconfigure(0,weight = 1)

        self.frames = {}
        # Place t o add next Frames
        for F in (StartPage,About_Page,Settings_Page) :

            frame  = F(container,self)

            self.frames[F] = frame

            frame.grid(row = 0 ,column = 0, sticky = "nsew")
        self.show_frame(StartPage)

    def show_frame(self,cont):

        frame =self.frames[cont]
        frame.tkraise()

def qf (param):
    print(param)



class StartPage (tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        button1 = ttk.Button(self,text = Translation.translator("About us",CurrentLangue),
        command = lambda :controller.show_frame(About_Page))
        button1.pack()

        button2 = ttk.Button(self,text = Translation.translator("Settings",CurrentLangue),
        command = lambda :controller.show_frame(Settings_Page))
        button2.pack()

        self.close_button = ttk.Button(self, text=Translation.translator("Close",CurrentLangue), command=self.quit)
        self.close_button.pack()



    def greet(self):
        print(Translation.translator("Welcome on our application",CurrentLangue))
class About_Page(tk.Frame) :
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text=Translation.translator("About us",CurrentLangue),font =LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self,text = Translation.translator("Back to Home",CurrentLangue),
        command = lambda :controller.show_frame(StartPage))
        button1.pack()


class Settings_Page(tk.Frame) :
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text=Translation.translator("Settings",CurrentLangue),font =LARGE_FONT)
        label.pack(pady=10,padx=10)
        variable = tk.StringVar(parent)
        variable.set(Settings.CurrentLangue())
        leng = ["Eng","Pl"]
        label1 = tk.Label(self,text=Translation.translator("Langue",CurrentLangue),font =LARGE_FONT)
        label1.pack(pady=10,padx=10)
        self.popupMenu = tk.OptionMenu(self, variable,*leng)
        self.popupMenu.pack()

        def refeshing() :
            Refresh.refresh(variable.get(),
            [label,"Settings"],
            [label1,"Langue"],
            [button1,"Save"],
            [button2,"Back to Home"])

        button1 = ttk.Button(self,text = Translation.translator("Save",CurrentLangue),
        command = refeshing)
        button1.pack()


        button2 = ttk.Button(self,text = Translation.translator("Back to Home",CurrentLangue),
        command = lambda :controller.show_frame(StartPage))
        button2.pack()
