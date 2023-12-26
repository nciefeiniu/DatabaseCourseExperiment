import traceback
from .mysql import ExecSql
from util.log_util import WriteConsoleLog

class StudentInsertUpdateFunc(object):
    def AddStudent(student):
        try:
            sql = "insert into student(Sno, Sname, Ssex, Sage, Sdept,Scholarship) values(\'%s\',\'%s\',\'%s\',%s,\'%s\',\'%s\')" % (student.Sno, student.Sname, student.Ssex, student.Sage, student.Sdept,student.Scholarship)
            WriteConsoleLog(sql)
            return ExecSql().run_command(sql=sql)
        except Exception as e:
            WriteConsoleLog("新增学生失败")
            return None

    def UpdateStudent(student):
        try:
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
            WriteConsoleLog(sql)
            return ExecSql().run_command(sql=sql)
        except Exception as e:
            WriteConsoleLog("更新学生信息失败")
            return None

class CourseInsertUpdateFunc(object):
    def AddCourse(course):
        try:
            sql = "insert into course(Cno, Cname, Cpno, Ccredit) values(\'%s\',\'%s\',\'%s\',%s)" % (course.Cno, course.Cname, course.Cpno, course.Ccredit)
            WriteConsoleLog(sql)
            return ExecSql().run_command(sql=sql)
        except Exception as e:
            WriteConsoleLog("增加课程信息失败")
            return None

    def UpdateCourse(course):
        try:
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
            WriteConsoleLog(sql)
            return ExecSql().run_command(sql=sql)
        except Exception as e:
            WriteConsoleLog("更新课程信息失败")
            return None

class SCInfoFunc(object):
    def AddSC(sc):
        try:
            sql = "insert into sc(Sno, Cno, Grade) values(\'%s\',\'%s\',%s)" % (sc.Sno, sc.Cno, sc.Grade)
            WriteConsoleLog(sql)
            return ExecSql().run_command(sql=sql)
        except Exception as e:
            WriteConsoleLog("增加成绩失败")
            return None

    def UpdateSC(sc):
        try:
            #如果有一些属性是空的，就不写入sql语句中
            sql = "update sc set "
            if sc.Grade != "":
                sql += "Grade = %s, " % sc.Grade
            sql = sql[:-2]
            sql += " where Sno = \'%s\' and Cno = \'%s\'" % (sc.Sno, sc.Cno)
            WriteConsoleLog(sql)
            return ExecSql().run_command(sql=sql)
        except Exception as e:
            WriteConsoleLog("更新成绩失败")
            return None

class ScStasticfunc(object):
    #按系统计学生的平均成绩、最好成绩、最差成绩、优秀率、不及格人数。
    def GetAverMaxMinBySdept(Sdept):
        try:
            sql = "select avg(Grade),max(Grade),min(Grade) from sc,student where sc.Sno = student.Sno and Sdept = \'%s\'" % Sdept
            WriteConsoleLog(sql)
            print(ExecSql().get_one(sql=sql))
            return ExecSql().get_one(sql=sql)
        except Exception as e:
            WriteConsoleLog("统计成绩时失败")
            return None

    def GetScExcellentRateBySdept(Sdept):
        try:
            #先获取优秀人数，再除以总人数
            sql = "select count(*) from sc,student where sc.Sno = student.Sno and Sdept = \'%s\' and Grade >= 90" % Sdept
            WriteConsoleLog(sql)
            cntExccel = ExecSql().get_all(sql=sql)
            sql = "select count(*) from sc,student where sc.Sno = student.Sno and Sdept = \'%s\'" % Sdept
            WriteConsoleLog(sql)
            cntTotal = ExecSql().get_all(sql=sql)
            return cntExccel[0]['count(*)']/cntTotal[0]['count(*)']
        except Exception as e:
            WriteConsoleLog("统计优秀率时失败")
            return None

    def GetScFailNumBySdept(Sdept):
        try:
            #先获取不及格人数，再除以总人数
            sql = "select count(*) from sc,student where sc.Sno = student.Sno and Sdept = \'%s\' and Grade < 60" % Sdept
            WriteConsoleLog(sql)
            cntFail = ExecSql().get_all(sql=sql)
            sql = "select count(*) from sc,student where sc.Sno = student.Sno and Sdept = \'%s\'" % Sdept
            WriteConsoleLog(sql)
            cntTotal = ExecSql().get_all(sql=sql)
            return cntFail[0]['count(*)']/cntTotal[0]['count(*)']
        except Exception as e:
            WriteConsoleLog("统计不及格人数时失败")
            return None

class SortFunction(object):
    #按系对学生成绩进行排名
    def SortStudentInSameSdept(Sdept):
        try:
            sql = "select Sname,Cname,Grade from sc,student,course where sc.Sno = student.Sno and sc.Cno = course.Cno and Sdept = \'%s\' order by Grade desc" % Sdept
            WriteConsoleLog(sql)
            return ExecSql().get_all(sql=sql)
        except Exception as e:
            WriteConsoleLog("统计排名时失败")
            return None

class StudentInfoQueryFunc(object):
    #输入学号，显示该学生的基本信息和选课信息。
    def GetStudentInfoBySno(Sno):
        try:
            sql = "select * from student where Sno = \'%s\'" % Sno
            WriteConsoleLog(sql)
            return ExecSql().get_one(sql=sql)
        except Exception as e:
            WriteConsoleLog("统计学生信息时失败")
            return None

    def GetStudentCourseInfoBySno(Sno):
        try:
            sql = "select * from sc,course where sc.Cno = course.Cno and Sno = \'%s\'" % Sno
            WriteConsoleLog(sql)
            return ExecSql().get_all(sql=sql)
        except Exception as e:
            WriteConsoleLog("统计学生课程信息时失败")
            return None
