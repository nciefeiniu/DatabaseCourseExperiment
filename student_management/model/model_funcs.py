from .mysql import ExecSql

class StudentInsertUpdateFunc(object):
    def AddStudent(student):
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


class CourseInsertUpdateFunc(object):
    def AddCourse(course):
        sql = "insert into course(Cno, Cname, Cpno, Ccredit) values(\'%s\',\'%s\',\'%s\',%s)" % (course.Cno, course.Cname, course.Cpno, course.Ccredit)
        print(sql)
        return ExecSql().run_command(sql=sql)
    def UpdateCourse(course):
        #如果有一些属性是空的，就不写入sql语句中
        sql = "update course set "
        if course.Cname != "":
            sql += "Cname = \'%s\', " % course.Cname
        if course.Cpno != "":
            sql += "Cpno = \'%s\', " % course.Cpno
        if course.Ccredit != "":
            sql += "Ccredit = %s, " % course.Ccredit
        sql = sql[:-2]
        sql += " where Cno = \'%s\'" % course.Cno
        print(sql)
        return ExecSql().run_command(sql=sql)
    
class SCInfoFunc(object):
    def AddSC(sc):
        sql = "insert into sc(Sno, Cno, Grade) values(\'%s\',\'%s\',%s)" % (sc.Sno, sc.Cno, sc.Grade)
        print(sql)
        return ExecSql().run_command(sql=sql)
    def UpdateSC(sc):
        #如果有一些属性是空的，就不写入sql语句中
        sql = "update sc set "
        if sc.Grade != "":
            sql += "Grade = %s, " % sc.Grade
        sql = sql[:-2]
        sql += " where Sno = \'%s\' and Cno = \'%s\'" % (sc.Sno, sc.Cno)
        print(sql)
        return ExecSql().run_command(sql=sql)

class ScStasticfunc(object):
    #按系统计学生的平均成绩、最好成绩、最差成绩、优秀率、不及格人数。
    def GetAverMaxMinBySdept(Sdept):
        sql = "select avg(Grade),max(Grade),min(Grade) from sc,student where sc.Sno = student.Sno and Sdept = \'%s\'" % Sdept
        print(sql)
        return ExecSql().get_all(sql=sql)
    def GetScExcellentRateBySdept(Sdept):
        #先获取优秀人数，再除以总人数
        sql = "select count(*) from sc,student where sc.Sno = student.Sno and Sdept = \'%s\' and Grade >= 90" % Sdept
        print(sql)
        cntExccel = ExecSql().get_all(sql=sql)
        sql = "select count(*) from sc,student where sc.Sno = student.Sno and Sdept = \'%s\'" % Sdept
        print(sql)
        cntTotal = ExecSql().get_all(sql=sql)
        return cntExccel[0][0]/cntTotal[0][0]
    def GetScFailNumBySdept(Sdept):
        #先获取不及格人数，再除以总人数
        sql = "select count(*) from sc,student where sc.Sno = student.Sno and Sdept = \'%s\' and Grade < 60" % Sdept
        print(sql)
        cntFail = ExecSql().get_all(sql=sql)
        sql = "select count(*) from sc,student where sc.Sno = student.Sno and Sdept = \'%s\'" % Sdept
        print(sql)
        cntTotal = ExecSql().get_all(sql=sql)
        return cntFail[0][0]/cntTotal[0][0]
    
class SortFunction(object):
    #按系对学生成绩进行排名
    def SortStudentInSameSdept(Sdept):
        sql = "select Sname,Cname,Grade from sc,student,course where sc.Sno = student.Sno and sc.Cno = course.Cno and Sdept = \'%s\' order by Grade desc" % Sdept
        print(sql)
        return ExecSql().get_all(sql=sql)
    
class StudentInfoQueryFunc(object):
    #输入学号，显示该学生的基本信息和选课信息。
    def GetStudentInfoBySno(Sno):
        sql = "select * from student where Sno = \'%s\'" % Sno
        print(sql)
        return ExecSql().get_all(sql=sql)
    def GetStudentCourseInfoBySno(Sno):
        sql = "select * from sc,course where sc.Cno = course.Cno and Sno = \'%s\'" % Sno
        print(sql)
        return ExecSql().get_all(sql=sql)