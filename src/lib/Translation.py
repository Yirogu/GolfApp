class Translation():

    """set polish or english langue"""

    words = {
            'Close' : {'Eng' : 'Close','Pl' : 'Zamknij'},
            'Greet' : {'Eng' : 'Greet','Pl' : 'Powitanie'},
            'Help' : {'Eng' : 'Help','Pl' : 'Pomoc'},
            'Langue' : {'Eng' : 'Langue','Pl' : 'Jezyk'},
            'Play' : {'Eng' : 'Play','Pl' : 'Graj'},
            'Save' : {'Eng':'Save','Pl' : 'Zapisz'},
            'Settings' : {'Eng' : 'Settings','Pl' : 'Ustawienia'},
            'Start' : {'Eng' : 'Start','Pl' : 'Rozpocznij'},
            'Tournament' : {'Eng' : 'Tournament','Pl' : 'Turniej'},
            'Resolution' :{'Eng':"Resolution","Pl":"Rozdzielczosc"},
            'Wiki' :{'Eng':"Wiki","Pl":"Encyklopedia"}
            }

    sentences = {
            'About us' :
                {'Eng' : 'About us','Pl' : 'O Nas'},
            'Add Players' :
                {'Eng' : 'Add Players','Pl' : 'Dodaj Graczy'},
            'Back to Home' :
                {'Eng' : 'Back to Home','Pl' : 'Wroc do menu'},
            'Call to service' :
                {'Eng' : 'Call to service','Pl' : 'Zadzwon do serwisu'},
            'Format,Rules,itc' :
                {'Eng' : 'Format,Rules,itc','Pl' : 'Format,Zasady,itp'},
            'Send Ticket/Error' :
                {'Eng' : 'Send Ticket/Error','Pl' : 'Wyslij zapytanie/zglos blad'},
            'Welcome on our application' :
                {'Eng' : 'Welcome on our application','Pl' : 'Witamy w naszej aplikacji'}}

    def translator(text,langue = 'Eng') :
        # function is trying to translate a sentence or word
        # if it can not do it, return text

        if len(text.split(" ")) > 1 or len(text.split(",")) > 1  :
            return Translation.sentenceTranslate(text,langue)
        else :
            return Translation.wordsTranslate(text,langue)

    def sentenceTranslate(text,langue):
        # This function is part of the translator (),
        # and it supports sentences

        sentences = Translation.sentences
        if text in sentences :
            sentence = sentences[text][langue]
            return sentence
        else :
            return text

    def wordsTranslate(text,langue):
        # This function is part of the translator (),
        # and it supports words

        words = Translation.words
        if text in words :
            word = words[text][langue]
            return word
        else :
            return text
