import pymysql

cursor = None
conn = None

from util.log_util import WriteConsoleLog

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

        


def InitMysql(host, port, user, password, database):
    try:
        global conn, cursor
        conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database,charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        initTables()
        initRules()
    except Exception as e:
        print(e)
        WriteConsoleLog("数据库初始化未成功完成")


def initTables():
    sqlStudent = """
        CREATE TABLE IF NOT EXISTS student(
            Sno CHAR(20) NOT NULL,
            Sname CHAR(20),
            Ssex CHAR(10),
            Sage INT,
            Sdept CHAR(20),
            Scholarship CHAR(20),
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
            FOREIGN KEY (Sno) REFERENCES student(Sno),
            FOREIGN KEY (Cno) REFERENCES course(Cno)
        )
        """
    
    cursor.execute(sqlStudent)
    cursor.execute(sqlCourse)
    cursor.execute(sqlSC)
    conn.commit()
    WriteConsoleLog("数据库表初始化完毕")

def initRules():
    try:
        sqlConstraint = """
            ALTER TABLE SC ADD CONSTRAINT CHECK_GRADE CHECK (Grade BETWEEN 0 AND 100)
            """
        sqlTrigger = """
            CREATE TRIGGER update_bonus
            BEFORE UPDATE ON SC
            FOR EACH ROW
            BEGIN
                IF New.Grade > 95 THEN
                    UPDATE Student SET Scholarship='是' WHERE Sno=New.Sno;
                ELSE 
                    IF (NOT EXISTS (SELECT * FROM SC WHERE Sno=New.Sno AND Cno != New.Cno AND Grade>95))  AND Old.Grade>95 THEN
                        UPDATE Student SET Scholarship='否' WHERE Sno=New.Sno;
                    END IF;
                END IF;
            END; 
            """
        if not constraint_exists('SC', 'CHECK_GRADE'):
            cursor.execute(sqlConstraint)
        if not trigger_exists('update_bonus'):
            cursor.execute(sqlTrigger)
        conn.commit()
        WriteConsoleLog("数据库规则初始化完毕")
    except Exception as e:
        print(e)
        WriteConsoleLog("初始化规则失败，请参考README.md；数据库表初始化成功的情况下，您仍可对数据库进行操作")

def constraint_exists(table_name, constraint_name):
    cursor.execute("""
        SELECT COUNT(*)
        FROM information_schema.TABLE_CONSTRAINTS 
        WHERE CONSTRAINT_SCHEMA = DATABASE() 
        AND TABLE_NAME = %s 
        AND CONSTRAINT_NAME = %s
    """, (table_name, constraint_name))
    res = cursor.fetchone()
    return res['COUNT(*)'] == 1

def trigger_exists(trigger_name):
    cursor.execute("""
        SELECT COUNT(*)
        FROM information_schema.TRIGGERS 
        WHERE TRIGGER_SCHEMA = DATABASE() 
        AND TRIGGER_NAME = %s
    """, (trigger_name,))
    res = cursor.fetchone()
    return res['COUNT(*)'] == 1