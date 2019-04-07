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
        [StartPage.button1,"About us"],
        [StartPage.button2,"Settings"],
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
        [Play_Page.button1,"Back to Home"])
