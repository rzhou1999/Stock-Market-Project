from keys import *
from AccessDatabase import *
import string

class article:
    def __init__(self, symbol, summary, contents, retrieveDate, source, date):
        self.fk = getKey(symbol)
        self.symbol = symbol
        self.summary = summary
        self.contents = ''.join((e.encode('ascii','ignore') if (not e is None) else "") for e in contents['Paragraph'][1:-1]).translate(None, string.punctuation).lower()
        self.retrieveDate = ' '.join(retrieveDate.split('T'))[:-1]
        self.source = source
        temp = date[:-13].split(' ')
        self.date = '-'.join([temp[2],temp[0].zfill(2),temp[1].zfill(2)])
        self.score = self.evaluate()

    def evaluate(self):
        splitScore = 0
        for key in keys:
            if key in self.contents:
                splitScore = splitScore + keys[key]
        return splitScore