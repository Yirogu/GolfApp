from .Settings import Settings
from .Translation import Translation
class Refresh :
    def refresh(variable,element):
        # Check current langue if is diffrent, expect change after reset
        if variable != Settings.CurrentLangue() :
            Settings.saveLangue(Settings.CurrentLangue(),variable)
            CurrentLangue = variable
            return element.config(text = Translation.translator("Langue",CurrentLangue)),CurrentLangue
