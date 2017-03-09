from AccessDatabase import *
from AccessYahoo import *

listFromDB = getStockList()
print listFromDB
decodedJSON = map(lambda x:json.loads(x),queryFromList(listFromDB))
print decodedJSON[0]['query']['results']['Articles']['Article'][0]['Summary'].encode('utf-8')
print ""
print decodedJSON[1]['query']['results']['Articles']['Article'][0]['Summary'].encode('utf-8')