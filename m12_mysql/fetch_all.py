import mysql.connector
from mysql.connector import errorcode
conn = None
cursor = None
try:
    conn = mysql.connector.connect(database='db01',user='root',password='choumysql')
    cursor = conn.cursor();
    sql = "select ename, hiredate, salary from employee"
    cursor.execute(sql)
    emps = cursor.fetchall()

    for ename, hiredate, salary in emps:
        print('name={},hiredate={},salary={}'.format(ename,hiredate,salary))
    print("=============================================")
    for emp in emps:
        print('name={} ,hiredate={} ,salary={}'.format(emp[0],emp[1],emp[2]))
    print("total",cursor.rowcount,"employees")


except mysql.connector.Error as err:
    print('err')
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()




