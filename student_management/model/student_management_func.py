from .mysql import ExecSql

class StudentInfoModel(object):
    def AddStudent(student):
        #sql = "insert into student(Sno, Sname, Ssex, Sage, Sdept,Scholarship) values(\'%s\',\'%s\',\'%s'\,%s,\'%s\',\'%s\')".format(student.Sno, student.Sname, student.Ssex, student.Sage, student.Sdept,student.Scholarship)
        sql = "insert into student(Sno, Sname, Ssex, Sage, Sdept,Scholarship) values(\'%s\',\'%s\',\'%s\',%s,\'%s\',\'%s\')" % (student.Sno, student.Sname, student.Ssex, student.Sage, student.Sdept,student.Scholarship)
        print(sql)
        args = list()
        return ExecSql().run_command(sql=sql)
