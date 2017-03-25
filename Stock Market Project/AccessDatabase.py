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
#takes articles higher than a certain threshold and writes their symbols to a text file.
def getSplits():
    db = MySQLdb.connect(host=HOST,
    user=USER,
    passwd=PASSWORD,
    db=NAME)
    cursor = db.cursor()
    cursor.execute("SELECT symbol FROM results WHERE score>26.0") #Change number to use new strictness
    splits = cursor.fetchall()
    splits=open("splits.txt","w")
    splits.write('\n'.join(lambda x:x[0], splits))
    splits.close()
#used in recreating probabilities. Takes all articles above/below a certain threshold and returns a list of their contents.
def getLikelyArticles():
    db = MySQLdb.connect(host=HOST,
    user=USER,
    passwd=PASSWORD,
    db=NAME)
    cursor = db.cursor()
    cursor.execute("SELECT contents FROM results WHERE score>26.0") #Change number to use new strictness
    splits = cursor.fetchall()
    cursor.execute("SELECT contents FROM results WHERE score<26.0") #Change number to use new strictness
    notSplits = cursor.fetchall()
    db.close()
    return [map(lambda x:x[0], splits)[:40],map(lambda x:x[0], notSplits)[:40]]
#used to match stock_pk to stock_fk from stocks table to results table.
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
#inserts a list of articles.
def insertList(articles):
    for i in articles:
        insertResult(i)
#inserts all articles into the database, unless article.source already exists in the database.
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