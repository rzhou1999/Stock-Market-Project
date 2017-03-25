from AccessDatabase import *
from AccessYahoo import *
from ArticleAnalyzer import *
from Probabilities import *
import time
#creates list of articles from converted json object dictObject. Takes in a symbol list, which is then assigned to corresponding entries.
def createArticleList(dictObject, symbolList):
    dictObject = filter(lambda x:len(x)!=0 and x['query']['results']['Articles'].get('Article', 0) != 0,dictObject)
    listOfArticles = []
    for i in range(len(dictObject)):
        dictObject[i]['query']['results']['Articles']['Symbol'] = symbolList[i]
    for singleDictObject in dictObject:
        for art in singleDictObject['query']['results']['Articles']['Article']:
            listOfArticles.append(article(singleDictObject['query']['results']['Articles']['Symbol'],art['Summary'], art['Content'], singleDictObject['query']['created'], art['GUID'], art['PubDate']))
    return listOfArticles
#json safe handling of returned YQL queries. YQL will sometimes throw errors in html, which are then filtered out here.
def loadJsonSafe(jsonString):
    try:
        json_object = json.loads(jsonString)
    except ValueError, e:
        return {}
    return json_object
#main program
def mainQuery():
    start = time.time()
    listFromDB = getStockList()
    print str(time.time() - start) + " seconds to complete stock list retrieval."
    decodedJSON = map(lambda x:loadJsonSafe(x),queryFromList(listFromDB))
    print str(time.time() - start) + " seconds to complete YQL queries."
    temp = createArticleList(decodedJSON, listFromDB)
    insertList(temp)
    print str(time.time() - start) + " seconds to complete."
    

commandLookup = {'loadDB':generateProbabilitiesDB,
                 'load':generateProbabilities,
                 'main':mainQuery,
                 'write':getSplits(),
                 'quit': lambda : None}
command = ""
while command != "quit":
    command = raw_input("Command:")
    commandLookup[command]()