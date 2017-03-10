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

def insert(article):
    db = MySQLdb.connect(host=HOST,
                     user=USER,
                     passwd=PASSWORD,
                     db=NAME)
    cursor = db.cursor()

    matches = cursor.execute("SELECT source FROM results WHERE name=%s", (article.source))
    if len(matches)!= 0:
        return

    try:
        query = """
            INSERT INTO results
            ('stock_fk', 'date_retrieved','retrieved_from','event_date','score')
            VALUES
            ('%(fk)', '%(retrieve)','%(source)','%(date)','%(score)')
            """ % {'fk': article.fk, 'retrieve': article.retrieveDate, 'source': article.source, 'date': article.date, 'score':article.score}
        cursor.execute(query)
        self.connection.commit()
    except:
        self.connection.rollback()
