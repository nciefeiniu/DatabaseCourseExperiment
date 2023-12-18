import pymysql

# 定义一个静态类，用来存放SQL语句
class SQL:
    # 查询语句
    QUERY = "SELECT * FROM {table} WHERE {field}=%s;"
    QUERY_ALL = "SELECT * FROM {table};"
    # 插入语句
    INSERT = "INSERT INTO {table} ({field}) VALUES ({value});"
    # 更新语句
    UPDATE = "UPDATE {table} SET {field}=%s WHERE {where};"
    # 删除语句
    DELETE = "DELETE FROM {table} WHERE {field}=%s;"


class SqlExecutor(object):
    def __init__(self, host, port, user, password, database, charset="utf8"):
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database,
                                    charset=charset)
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def close(self):
        self.cursor.close()
        self.conn.close()

    def get_one(self, sql, args=None):
        self.cursor.execute(sql, args)
        return self.cursor.fetchone()

    def get_all(self, sql, args=None):
        self.cursor.execute(sql, args)
        return self.cursor.fetchall()

    def run_command(self, sql, args=None):
        self.cursor.execute(sql, args)
        self.conn.commit()
        return self.cursor.lastrowid