from AccessDatabase import *
from AccessYahoo import *
from ArticleAnalyzer import *
from Probabilities import *

def createArticleList(dictObject, symbolList):
    listOfArticles = []
    for i in range(len(dictObject)):
        dictObject[i]['query']['results']['Articles']['Symbol'] = symbolList[i]
    for singleDictObject in dictObject:
        for art in singleDictObject['query']['results']['Articles']['Article']:
            listOfArticles.append(article(singleDictObject['query']['results']['Articles']['Symbol'],art['Summary'], art['Content'], singleDictObject['query']['created'], art['GUID'], art['PubDate']))
    return listOfArticles
generateProbabilities()
#listFromDB = getStockList()
#print listFromDB
#decodedJSON = map(lambda x:json.loads(x),queryFromList(listFromDB[0:50]))
#temp = createArticleList(decodedJSON[0:50], listFromDB)
#insertList(temp)
#print decodedJSON[0]['query']['results']['Articles']['Article'][0]['Summary'].encode('utf-8')
#print ""
#print decodedJSON[1]['query']['results']['Articles']['Article'][0]['Summary'].encode('utf-8')