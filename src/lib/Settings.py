
class Settings(object):
    """class supports settings from Settings.txt
    file is responsible for their correct operation"""

    path = '/home/stach/Desktop/Python3/GolfApp/Settings.txt'

    def CurrentLangue() :
        with open(Settings.path) as f:
            file = f.readline()
            file = file.split(":")
            currentLangue  = file[1]
            lenC = len(currentLangue) -1
            currentLangue = currentLangue[0:lenC]
        return currentLangue

    def saveLangue(currentLangue,langue):
        # Function for refactoring
        # if the other options will have the same values ​, replace all
        # is responsible for saving the new CurrentLangue value
        with open(Settings.path,'r+') as f :
            file = f.read()
            new_text = file.replace(currentLangue, langue)
            f.seek(0)
            f.write(new_text)
            f.truncate()
    def lines (argument):
        with open(Settings.path) as f:
            list = []
            for  x in range(2)
                x = f.readline().split(":")
                list.append(x[1])


        return list[argument]





res = Settings.lines(1)
