import MySQLdb
from mysecret import DATABASE_USER, DATABASE_PASS, DATABASE_HOST

db = MySQLdb.connect(host=DATABASE_HOST, user=DATABASE_USER,
                     passwd=DATABASE_PASS, db="opascree_lan-seats")
c = db.cursor()
c.execute("""SELECT * from tickets""")
