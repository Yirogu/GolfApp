import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from .Translation import Translation
from .Settings import Settings
from .Refresh import Refresh
from .Database import Database

# how i can do 1 import for 2 files ?
LARGE_FONT = ("Verdana", 12)
CurrentLangue = Settings.CurrentLangue()
CurrentResolution = Settings.CurrentResolution()

class MainGui(tk.Tk):

    def __init__ (self,*args,**kwargs) :
        tk.Tk.__init__(self,*args,**kwargs)
        MainGui.master = self
        tk.Tk.title(self,"Golf Time Pro")
        img = tk.PhotoImage(file='/home/stach/Desktop/Python3/GolfApp/src/lib/logo.gif')
        self.tk.call('wm','iconphoto',self._w,img)
        MainGui.master.geometry(CurrentResolution)

        container = tk.Frame(self)
        container.pack(side='top',fill='both', expand = True )
        container.grid_rowconfigure(0,weight =1)
        container.grid_columnconfigure(0,weight = 1)
        self.frames = {}
        MainGui.frames =StartPage,About_Page,Settings_Page,Play_Page,Help_Page,Tournament_Page,Player_Page
        # Place t o add next Frames
        #  Try add all pages to 1 variable and use over class
        for F in (MainGui.frames) :

            frame  = F(container,self)

            self.frames[F] = frame

            frame.grid(row = 0 ,column = 0, sticky = "nsew")
        self.show_frame(StartPage)


    def show_frame(self,cont):

        frame =self.frames[cont]
        frame.tkraise()

class StartPage (tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        StartPage.button0 = ttk.Button(self,text = Translation.translator("Play",CurrentLangue),
        command = lambda :controller.show_frame(Play_Page))
        StartPage.button0.pack()

        StartPage.button1 = ttk.Button(self,text = Translation.translator("About us",CurrentLangue),
        command = lambda :controller.show_frame(About_Page))
        StartPage.button1.pack()

        StartPage.button2 = ttk.Button(self,text = Translation.translator("Settings",CurrentLangue),
        command = lambda :controller.show_frame(Settings_Page))
        StartPage.button2.pack()

        StartPage.button3 = ttk.Button(self,text = Translation.translator("Help",CurrentLangue),
        command = lambda :controller.show_frame(Help_Page))
        StartPage.button3.pack()

        StartPage.close_button = ttk.Button(self, text=Translation.translator("Close",CurrentLangue), command=self.quit)
        StartPage.close_button.pack()

class Play_Page(tk.Frame) :
    # To Do
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        Play_Page.button0 = ttk.Button(self,text = Translation.translator("Tournament",CurrentLangue),
        command = lambda :controller.show_frame(Tournament_Page))
        Play_Page.button0.pack()


        Play_Page.button1 = ttk.Button(self,text = Translation.translator("Back to Home",CurrentLangue),
        command = lambda :controller.show_frame(StartPage))
        Play_Page.button1.pack()

class Tournament_Page(tk.Frame) :
    # To Do
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        Tournament_Page.button0 = ttk.Button(self,text = Translation.translator("Start",CurrentLangue),
        command = lambda :controller.show_frame(Tournament_Page))
        Tournament_Page.button0.pack()

        Tournament_Page.button1 = ttk.Button(self,text = Translation.translator("Add Players",CurrentLangue),
        command = lambda :controller.show_frame(Player_Page))
        Tournament_Page.button1.pack()

        Tournament_Page.button2 = ttk.Button(self,text = Translation.translator("Format,Rules,itc",CurrentLangue),
        command = lambda :controller.show_frame(StartPage))
        Tournament_Page.button2.pack()

        Tournament_Page.button3 = ttk.Button(self,text = Translation.translator("Back to Home",CurrentLangue),
        command = lambda :controller.show_frame(StartPage))
        Tournament_Page.button3.pack()


class Player_Page(tk.Frame) :
    # To Do
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        Play_Page.button0 = ttk.Button(self,text = Translation.translator("Add Player",CurrentLangue),
        command = lambda :controller.show_frame(Tournament_Page))
        Play_Page.button0.pack()
        Player_Page.T = tk.Text(self, height=2, width=30)
        Player_Page.T.pack()
        quote = Database.readAll()
        Player_Page.T.insert(tk.END, quote)

        Play_Page.button1 = ttk.Button(self,text = Translation.translator("Back to Home",CurrentLangue),
        command = lambda :controller.show_frame(StartPage))
        Play_Page.button1.pack()

class About_Page(tk.Frame) :
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        About_Page.label = tk.Label(self,text=Translation.translator("About us",CurrentLangue),font =LARGE_FONT)
        About_Page.label.pack(pady=10,padx=10)

        About_Page.button1 = ttk.Button(self,text = Translation.translator("Back to Home",CurrentLangue),
        command = lambda :controller.show_frame(StartPage))
        About_Page.button1.pack()

class Settings_Page(tk.Frame) :
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        Settings_Page.label = tk.Label(self,text=Translation.translator("Settings",CurrentLangue),font =LARGE_FONT)
        Settings_Page.label.pack(pady=10,padx=10)

        variable = tk.StringVar(parent)
        variable.set(CurrentLangue)
        leng = ["Eng","Pl"]

        variable1 = tk.StringVar(parent)
        variable1.set(CurrentResolution)

        #  If resolution is bigger than gui on ubuntu ,
        # aplication can t change resolution to another.

        resolution = ["1280x720","1366x768","1600x900","1920x1080"]

        Settings_Page.label1 = tk.Label(self,text=Translation.translator("Langue",CurrentLangue),font =LARGE_FONT)
        Settings_Page.label1.pack(pady=10,padx=10)
        Settings_Page.popupMenu = tk.OptionMenu(self, variable,*leng)
        Settings_Page.popupMenu.pack()

        Settings_Page.label2 = tk.Label(self,text=Translation.translator("Resolution",CurrentLangue),font =LARGE_FONT)
        Settings_Page.label2.pack(pady=10,padx=10)
        Settings_Page.popupMenu1 = tk.OptionMenu(self, variable1,*resolution)
        Settings_Page.popupMenu1.pack()
        var = tk.IntVar()
        Settings_Page.check = tk.Checkbutton(
            self, text="fullscreen",
            variable=var)
        Settings_Page.check.pack()

#           Add all frames to Translation on live application
#           and save Resolution.
        def saveSettings (fullscreen = var):

            Refresh.refeshing(variable,StartPage,About_Page,Settings_Page,Play_Page,Help_Page,Tournament_Page,Player_Page)
            MainGui.master.attributes("-fullscreen", fullscreen.get())
            Settings.saveResolution(CurrentResolution,variable1,MainGui.master)



        Settings_Page.button1 = ttk.Button(self,text = Translation.translator("Save",CurrentLangue),


        command =lambda:saveSettings())
        Settings_Page.button1.pack()


        Settings_Page.button2 = ttk.Button(self,text = Translation.translator("Back to Home",CurrentLangue),
        command = lambda :controller.show_frame(StartPage))
        Settings_Page.button2.pack()

class Help_Page(tk.Frame) :
    # To Do
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        Help_Page.button0 = ttk.Button(self,text = Translation.translator("Wiki",CurrentLangue),
        command = lambda :controller.show_frame(Tournament))
        Help_Page.button0.pack()

        Help_Page.button1 = ttk.Button(self,text = Translation.translator("Send Ticket/Error",CurrentLangue),
        command = lambda :controller.show_frame(Tournament))
        Help_Page.button1.pack()

        Help_Page.button2 = ttk.Button(self,text = Translation.translator("Call to service",CurrentLangue),
        command = lambda :controller.show_frame(Tournament))
        Help_Page.button2.pack()

        Help_Page.button3 = ttk.Button(self,text = Translation.translator("Back to Home",CurrentLangue),
        command = lambda :controller.show_frame(StartPage))
        Help_Page.button3.pack()
