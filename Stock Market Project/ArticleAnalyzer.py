from keys import *
from AccessDatabase import *

class article:
    def __init__(self, symbol, summary, contents, retrieveDate, source, date):
        self.fk = getKey(symbol)
        self.summary = summary
        self.contents = contents
        self.retrieveDate = ' '.join(retrieveDate.split('T'))[:-1]
        self.source = source
        self.date = date[:-13].replace(' ','')
        self.score = -1

    def evaluate(self):
        splitScore = 0
        for key in splitKeywords:
            if key in self.contents:
                splitScore = splitScore + splitKeywords[key]
