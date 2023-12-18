import pymysql

cursor = None
conn = None


class ExecSql(object):
    global cursor
    def run_command(self, sql, args=None):
        cursor.execute(sql, args)
        conn.commit()
        return self.cursor.lastrowid
    
    def close(self):
        cursor.close()
        self.conn.close()

    def get_one(self, sql, args=None):
        cursor.execute(sql, args)
        return self.cursor.fetchone()

    def get_all(self, sql, args=None):
        cursor.execute(sql, args)
        return self.cursor.fetchall()

        


def InitMysql():
    global conn, cursor
    conn = pymysql.connect(host='localhost', port=3306, user='test', password='test', database='test',charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    print("数据库连接成功")