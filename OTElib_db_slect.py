
import sqlite3
import sys
TEclass = sys.argv[1]
dbfile = sys.argv[2]


sqll = 'SELECT * FROM OTElib WHERE class=\'' + TEclass + '\''

db = sqlite3.connect(dbfile)
cur =db.cursor()

cur.execute(sqll)
x = cur.fetchall()
print(x)






