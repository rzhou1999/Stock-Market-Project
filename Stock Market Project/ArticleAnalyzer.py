from keys import *
from AccessDatabase import *

class article:
    def __init__(self, symbol, summary, contents, retrieveDate, source, date):
        self.fk = getKey(symbol)
        self.symbol = symbol
        self.summary = summary
        self.contents = contents
        self.retrieveDate = ' '.join(retrieveDate.split('T'))[:-1]
        self.source = source
        temp = date[:-13].split(' ')
        self.date = '-'.join([temp[2],temp[0].zfill(2),temp[1].zfill(2)])
        self.score = self.evaluate()

    def evaluate(self):
        formatted = self.contents.translate(None, string.punctuation).lower()
        splitScore = 0
        for key in keywords:
            if key in formatted:
                splitScore = splitScore + keywords[key]
        return splitScore