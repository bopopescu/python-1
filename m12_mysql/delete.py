import mysql.connector
from mysql.connector import errorcode
conn = None
cursor = None
try:
    conn = mysql.connector.connect(database='db01',user='root',password='choumysql')
    cursor = conn.cursor();

    ins = "delete from employee where empno = %s"
    ins_data = 1011
    cursor.execute(ins,(ins_data,))
    conn.commit()
    print("insert",cursor.rowcount,'employee')

    query = "select ename, hiredate, salary from employee"
    cursor.execute(query)
    for ename, hiredate, salary in cursor:
        print('ename={}, hiredate={},salary={}'.format(ename,hiredate,salary))
    print('total',cursor.rowcount,'employee')


except mysql.connector.Error as err:
    print(err)
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()




