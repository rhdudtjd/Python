import pymysql

conn = pymysql.connect(host = "localhost", user = "root", password = "password", db = "db", charset='utf8')

try:
    with conn.cursor() as cur:
        # sql = "create database myDB"
        # sql = "create table mytable(ID char(20), password char(20), email char(30))"
        cur.execute(sql)
        rs = cur.fetchall()

        for row in rs:
            for data in row:
                print(data, end=' ')
            print()
finally:
    conn.close()