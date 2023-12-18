class StudentInfoModel(object):
    def AddStudent(student):
        sql = "insert into student(Sno, Sname, Ssex, Sage, Sdept,Scholarship) values(%s,%s,%s,%s,%s,%s)"
        args = (student.Sno, student.Sname, student.Ssex, student.Sage, student.Sdept,student.Scholarship)
        return ExecSql.run_command(sql, args)
