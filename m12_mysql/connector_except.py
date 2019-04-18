import mysql.connector
from mysql.connector import errorcode
conn = None
try:
    conn = mysql.connector.connect(database='db01',user='root',password='choumysql')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('user or passwd error')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('database not existed')
    else:
        print('err')
finally:
    if conn:
        print('close')
        conn.close()




