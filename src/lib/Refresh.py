from .Settings import Settings
from .Translation import Translation

class Refresh :
    def refresh(variable,*elements):
        # Check current langue if is diffrent, expect change after reset
        if variable != Settings.CurrentLangue() :
            Settings.saveLangue(Settings.CurrentLangue(),variable)
            CurrentLangue = variable
            for element in elements :
                element[0].config(text = Translation.translator(element[1],CurrentLangue)),CurrentLangue

    def refeshing(variable,StartPage,About_Page,Settings_Page) :

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
        [Settings_Page.button1,"Save"],
        [Settings_Page.button2,"Back to Home"])
