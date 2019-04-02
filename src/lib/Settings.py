
class Settings(object):
    """class supports settings from Settings.txt
    file is responsible for their correct operation"""

    path = '/home/stach/Desktop/Python3/GolfApp/Settings.txt'

    def lines (argument):
        # Function read  value of settings.txt file
        with open(Settings.path) as f:
            list = []
            #  change functions so that you do not have to change the range
            for x in range(2) :
                x = f.readline().split(":")
                x =x[1]
                lenC = len(x) -1
                x = x[0:lenC]
                list.append(x)
        return list[argument]

    def CurrentLangue() :
        return Settings.lines(0)

    def saveOption(currentOption,option):

        # Function for refactoring
        # if the other options will have the same values ​, replace all
        # is responsible for saving the new CurrentLangue value
        with open(Settings.path,'r+') as f :
            file = f.read()
            new_text = file.replace(currentOption, option)
            f.seek(0)
            f.write(new_text)
            f.truncate()

    def CurrentResolution() :
        return Settings.lines(1)

    def saveResolution(CurrentResolution,variable):
        if variable.get() != Settings.CurrentResolution() :
            Settings.saveOption(Settings.CurrentResolution(),variable.get())
            CurrentResolution = variable.get()
