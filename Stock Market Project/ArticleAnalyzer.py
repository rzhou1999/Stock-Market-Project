from keys import *

class article:
    def __init__(summary, contents, retrieveDate, source, date):
        self.summary = summary
        self.contents = contents
        self.retrieveDate = retrieveDate
        self.source = source
        self.date = date #might need to be formatted to dateTime mysql format
        self.score = -1
        self.type = "NONE"

    def evaluate(self):
        splitScore = 0
        for key in splitKeywords:
            if key in self.contents:
                splitScore = splitScore + splitKeywords[key]
        acquisitionScore = 0
        for key in acquisitionKeywords:
            if key in self.contents:
                acquisitionScore = acquisitionScore + acquisitionKeywords[key]
        if splitKeywords > acquisitionScore:
            self.score = splitScore
            self.type = "SPLIT"
        else:
            self.score = acquisitionScore
            self.type = "ACQUISITION"