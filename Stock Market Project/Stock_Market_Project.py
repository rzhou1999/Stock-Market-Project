from AccessDatabase import *
from AccessYahoo import *
from ArticleAnalyzer import *
from Probabilities import *

def createArticleList(dictObject, symbolList):
    dictObject = filter(lambda x:len(x)!=0 and x['query']['results']['Articles'].get('Article', 0) != 0,dictObject)
    listOfArticles = []
    for i in range(len(dictObject)):
        dictObject[i]['query']['results']['Articles']['Symbol'] = symbolList[i]
    for singleDictObject in dictObject:
        for art in singleDictObject['query']['results']['Articles']['Article']:
            listOfArticles.append(article(singleDictObject['query']['results']['Articles']['Symbol'],art['Summary'], art['Content'], singleDictObject['query']['created'], art['GUID'], art['PubDate']))
    return listOfArticles
#generateProbabilities()
listFromDB = getStockList()

def loadJsonSafe(jsonString):
    try:
        json_object = json.loads(jsonString)
    except ValueError, e:
        return {}
    return json_object

decodedJSON = map(lambda x:loadJsonSafe(x),queryFromList(listFromDB))
temp = createArticleList(decodedJSON, listFromDB)
insertList(temp)
#print decodedJSON[0]['query']['results']['Articles']['Article'][0]['Summary'].encode('utf-8')
#print ""
#print decodedJSON[1]['query']['results']['Articles']['Article'][0]['Summary'].encode('utf-8')