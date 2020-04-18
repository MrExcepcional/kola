import json

from textblob import TextBlob


class Translator(object):
    """docstring for Translate"""
        
    language_interested = []
    language_avoid =[]
    changes = False

    def detect(self, text):
        return TextBlob(text).detect_language()

    def in_interest(self, lang):
        return lang in self.language_interested

    def in_avoid(self, lang):
        return lang in self.language_avoid

    def add_to_avoid(self, lang):
        self.language_avoid.append(lang)
        self.changes = True

    def add_to_interest(self, lang):
        self.language_interested.append(lang)
        self.changes = True

    def save_state(self):
        if self.changes:
            with open('idiomas.json','w') as outfile:
                json.dump(
                    [self.language_interested,
                    self.language_avoid, 
                    self.language_unclassified], 
                    outfile
                )
            self.changes = False
        else: print('No se detectaron cambios en los lenguages.')

    def open_state(self):
        file = open('idiomas.json')
        l = json.load(file)
        self.language_interested = l[0]
        self.language_avoid = l[1]
        self.language_unclassified = l[2]
        file.close()

    def ask_classify(self, lang):
        response = input(f'Shall I classify {lang} as interest?: ')
        if response.lower()[0] == 'y':
            self.add_to_interest(lang)
        else:
            self.add_to_avoid(lang)