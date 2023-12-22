import pymysql

cursor = None
conn = None


class ExecSql(object):
    global cursor
    def run_command(self, sql, args=None):
        cursor.execute(sql, args)
        conn.commit()
        return cursor.lastrowid
    
    def close(self):
        cursor.close()
        conn.close()

    def get_one(self, sql, args=None):
        cursor.execute(sql, args)
        return cursor.fetchone()

    def get_all(self, sql, args=None):
        cursor.execute(sql, args)
        return cursor.fetchall()

        


def InitMysql():
    global conn, cursor
    conn = pymysql.connect(host='localhost', port=3306, user='test', password='test', database='test',charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    initTables()
    print("数据库连接成功")
    #初始化完毕
    print("初始化完毕")


def initTables():
    sqlStudent = """
        CREATE TABLE IF NOT EXISTS student(
            Sno CHAR(20) NOT NULL,
            Sname CHAR(20),
            Ssex CHAR(10),
            Sage INT,
            Sdept CHAR(20),
            Scholarship INT,
            PRIMARY KEY (Sno)
        )
        """
    sqlCourse = """
        CREATE TABLE IF NOT EXISTS course(
            Cno CHAR(20) NOT NULL,
            Cname CHAR(20),
            Cpno CHAR(20),
            Ccredit INT,
            PRIMARY KEY (Cno)
        )
        """
    sqlSC = """
        CREATE TABLE IF NOT EXISTS sc(
            Sno CHAR(20) NOT NULL,
            Cno CHAR(20) NOT NULL,
            Grade INT,
            PRIMARY KEY (Sno,Cno),
            FOREIGN KEY (Sno) REFERENCES student(Sno),
            FOREIGN KEY (Cno) REFERENCES course(Cno)
        )
        """
    cursor.execute(sqlStudent)
    cursor.execute(sqlCourse)
    cursor.execute(sqlSC)
    conn.commit()