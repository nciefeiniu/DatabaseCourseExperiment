from .mysql import ExecSql

class StudentInfoModel(object):
    def AddStudent(student):
        #sql = "insert into student(Sno, Sname, Ssex, Sage, Sdept,Scholarship) values(\'%s\',\'%s\',\'%s'\,%s,\'%s\',\'%s\')".format(student.Sno, student.Sname, student.Ssex, student.Sage, student.Sdept,student.Scholarship)
        sql = "insert into student(Sno, Sname, Ssex, Sage, Sdept,Scholarship) values(\'%s\',\'%s\',\'%s\',%s,\'%s\',\'%s\')" % (student.Sno, student.Sname, student.Ssex, student.Sage, student.Sdept,student.Scholarship)
        print(sql)
        return ExecSql().run_command(sql=sql)
    def UpdateStudent(student):
        #如果有一些属性是空的，就不写入sql语句中
        sql = "update student set "
        if student.Sname != "":
            sql += "Sname = \'%s\', " % student.Sname
        if student.Ssex != "":
            sql += "Ssex = \'%s\', " % student.Ssex
        if student.Sage != "":
            sql += "Sage = %s, " % student.Sage
        if student.Sdept != "":
            sql += "Sdept = \'%s\', " % student.Sdept
        if student.Scholarship != "":
            sql += "Scholarship = \'%s\', " % student.Scholarship
        sql = sql[:-2]
        sql += " where Sno = \'%s\'" % student.Sno
        print(sql)
        return ExecSql().run_command(sql=sql)
