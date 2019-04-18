import mysql.connector
from mysql.connector import errorcode
conn = None
cursor = None
try:
    conn = mysql.connector.connect(database='db01',user='root',password='choumysql')
    cursor = conn.cursor();
    sql = "select ename, hiredate, salary from employee where ename like %s"
    ename = input('輸入名稱 : ')
    ename1 =str('%'+ename+'%')
    cursor.execute(sql,(ename1,))

    for ename, hiredate, salary in cursor:
        print('name={},hiredate={},salary={}'.format(ename,hiredate,salary))
    print("total",cursor.rowcount,"employees")


except mysql.connector.Error as err:
    print('err')
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()




