import mysql.connector
from mysql.connector import errorcode
conn = None
cursor = None
try:
    conn = mysql.connector.connect(database='db01',user='root',password='choumysql')
    cursor = conn.cursor();
    upd = "update employee set salary = %s where empno = %s"
    upd_data=(50000,1001)
    cursor.execute(upd,upd_data)
    conn.commit()

    sql = "select ename, hiredate, salary from employee where empno = %s"
    empno = eval(input("employee no : "))
    cursor.execute(sql,(empno,))
    emps = cursor.fetchone()
    if emps is not None:
        print(emps)
        print("name={}, hiredate= {},salary= {}".format(emps[0],emps[1],emps[2]))
    else:
        print('No data')


except mysql.connector.Error as err:
    print('err')
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()




