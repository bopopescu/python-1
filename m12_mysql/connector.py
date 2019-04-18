import mysql.connector
conn = mysql.connector.connect(database='db01',user='root',password='choumysql')
from mysql.connector import connection
conn = connection.MySQLConnection(database='db01',user='root',password='choumysql')

import mysql.connector
config = {
    'database' : 'db01',
    'user' : 'root',
    'password' : 'choumysql'
}
conn = mysql.connector.connect(**config)
