from AccessDatabase import *
from AccessYahoo import *
from ArticleAnalyzer import *

def createArticleList(dictObject, symbolList):
    listOfArticles = []
    for i in range(len(dictObject)):
        dictObject['query']['results']['Articles']['Symbol'] = symbolList[i]
    for art in dictObject['query']['results']['Articles']['Article']:
        listOfArticles.append(article(dictObject['query']['results']['Articles']['Symbol'],art['Summary'], art['Content'], dictObject['query']['created'], art['GUID'], art['PubDate']))
    return listOfArticles

listFromDB = getStockList()
print listFromDB
decodedJSON = map(lambda x:json.loads(x),queryFromList(listFromDB))
temp = createArticleList(decodedJSON[0], listFromDB)
print temp
insertResult(temp[0])
#print decodedJSON[0]['query']['results']['Articles']['Article'][0]['Summary'].encode('utf-8')
#print ""
#print decodedJSON[1]['query']['results']['Articles']['Article'][0]['Summary'].encode('utf-8')