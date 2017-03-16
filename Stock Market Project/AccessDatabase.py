import MySQLdb
import ConfigParser

#retrieves DB info from credentials.ini
Config = ConfigParser.ConfigParser()
Config.read('credentials.ini')
HOST = Config.get('DBLogIn','HOST')
USER = Config.get('DBLogIn','USER')
PASSWORD = Config.get('DBLogIn','PASSWORD')
NAME = Config.get('DBLogIn','NAME')

#queries the DB for a list of stock symbols
def getStockList():
    db = MySQLdb.connect(host=HOST,
                     user=USER,
                     passwd=PASSWORD,
                     db=NAME)
    cursor = db.cursor()
    cursor.execute("SELECT stock_name FROM stocks")
    temp = cursor.fetchall()
    db.close()
    return map(lambda x:x[0], temp)

def getLikelyArticles():
    db = MySQLdb.connect(host=HOST,
    user=USER,
    passwd=PASSWORD,
    db=NAME)
    cursor = db.cursor()
    cursor.execute("SELECT contents FROM results WHERE score>5.0") #Change number to use new strictness
    splits = cursor.fetchall()
    cursor.execute("SELECT contents FROM results WHERE score<0.5") #Change number to use new strictness
    notSplits = cursor.fetchall()
    db.close()
    return [map(lambda x:x[0], splits),map(lambda x:x[0], notSplits)]

def getKey(symbol):
    db = MySQLdb.connect(host=HOST,
    user=USER,
    passwd=PASSWORD,
    db=NAME)
    cursor = db.cursor()
    cursor.execute("SELECT stocks_pk FROM stocks WHERE stock_name=%s", symbol)
    temp = cursor.fetchall()
    db.close()
    return temp[0][0]

def insertList(articles):
    for i in articles:
        insertResult(i)

def insertResult(article):
    db = MySQLdb.connect(host=HOST,
                     user=USER,
                     passwd=PASSWORD,
                     db=NAME)
    cursor = db.cursor()
    matches = cursor.execute("SELECT retrieved_from FROM results WHERE retrieved_from=%s", (article.source))
    if matches != 0L:
        return

    query = ("INSERT INTO results (symbol,stock_fk, date_retrieved,retrieved_from,event_date,score,contents) VALUES ('%s',%s, '%s','%s','%s',%s,'%s')" % (article.symbol, article.fk, article.retrieveDate, article.source, article.date, article.score, article.contents[:8192]))
    cursor.execute(query)
    db.commit()
    db.close()