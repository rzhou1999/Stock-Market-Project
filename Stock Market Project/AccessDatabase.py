import MySQLdb

HOST = "localhost"
USER = "devel"
PASSWORD = "devel"
NAME = "stockmarketupdates"

def getStockList():
    db = MySQLdb.connect(host=HOST,
                     user=USER,
                     passwd=PASSWORD,
                     db=NAME)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM stocks")
    temp = cursor.fetchall()
    db.close()
    return map(lambda x:x[1], temp)