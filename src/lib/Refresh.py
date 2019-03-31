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
