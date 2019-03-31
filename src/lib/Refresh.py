from .Settings import Settings
from .Translation import Translation
class Refresh :
    def refresh(variable,element):
        # Check current langue if is diffrent, expect change after reset
        if variable != MainGui.CurrentLangue :
            Settings.saveLangue(MainGui.CurrentLangue,variable)
            MainGui.CurrentLangue = variable
            return element.config(text = Translation.translator("Langue",MainGui.CurrentLangue))
