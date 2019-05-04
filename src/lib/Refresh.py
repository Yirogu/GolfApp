from .Settings import Settings
from .Translation import Translation

class Refresh :
    def refresh(variable,*elements):
        # Check current langue if is diffrent, expect change in live application
        if variable != Settings.CurrentLangue() :
            Settings.saveOption(Settings.CurrentLangue(),variable)
            CurrentLangue = variable
            for element in elements :
                element[0].config(text = Translation.translator(element[1],CurrentLangue)),CurrentLangue

    def refeshing(variable,StartPage,About_Page,Settings_Page,Play_Page,Help_Page,Tournament_Page,Player_Page) :
        # values ​​for refresh()
        Refresh.refresh(variable.get(),
                    # StartPage
        [StartPage.button0,"Play"],
        [StartPage.button1,"About us"],
        [StartPage.button2,"Settings"],
        [StartPage.button3,"Help"],
        [StartPage.close_button,"Close"],
                    # About_Page
        [About_Page.label,"About us"],
        [About_Page.button1,"Back to Home"],
                    # Settings_Page
        [Settings_Page.label,"Settings"],
        [Settings_Page.label1,"Langue"],
        [Settings_Page.label2,"Resolution"],
        [Settings_Page.button1,"Save"],
        [Settings_Page.button2,"Back to Home"],

                    # Play_Page
        [Play_Page.button0,"Tournament"],
        [Play_Page.button1,"Back to Home"],

                    #Tournament_Page
        [Tournament_Page.button0,"Start"],
        [Tournament_Page.button1,"Add Players"],
        [Tournament_Page.button2,"Format,Rules,itc"],
        [Tournament_Page.button3,"Back to Home"],
                    #Help_Page
        [Help_Page.button0,"Wiki"],
        [Help_Page.button1,"Send Ticket/Error"],
        [Help_Page.button2,"Call to service"],
        [Help_Page.button3,"Back to Home"])
