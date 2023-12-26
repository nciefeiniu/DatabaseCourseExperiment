from model.data_models import Student, Course, SC
from model.model_funcs import StudentInsertUpdateFunc, CourseInsertUpdateFunc, SCInfoFunc,ScStasticfunc,SortFunction,StudentInfoQueryFunc
from model.mysql import InitMysql

from util.log_util import WriteOutputLog

def ConnectDb(host, port, user, password, database):
    # 连接数据库
    InitMysql(host, port, user, password, database)

def InsertStudentInfo(Sno, Sname, Ssex, Sage, Sdept,Scholarship):
    # 新增学生信息
    student = Student(Sno, Sname, Ssex, Sage, Sdept,Scholarship)
    StudentInsertUpdateFunc.AddStudent(student)

def UpdateStudentInfo(Sno, Sname, Ssex, Sage, Sdept,Scholarship):
    # 更新学生信息
    student = Student(Sno, Sname, Ssex, Sage, Sdept,Scholarship)
    StudentInsertUpdateFunc.UpdateStudent(student)

def InsertCourseInfo(Cno, Cname, Cpno, Ccredit):
    # 新增课程信息
    course = Course(Cno, Cname, Cpno, Ccredit)
    CourseInsertUpdateFunc.AddCourse(course)

def UpdateCourseInfo(Cno, Cname, Cpno, Ccredit):
    # 更新课程信息
    course = Course(Cno, Cname, Cpno, Ccredit)
    CourseInsertUpdateFunc.UpdateCourse(course)

def InsertSCInfo(Sno, Cno, Grade):
    # 新增成绩
    sc = SC(Sno, Cno, Grade)
    SCInfoFunc.AddSC(sc)

def UpdateSCInfo(Sno, Cno, Grade):
    # 更新成绩
    sc = SC(Sno, Cno, Grade)
    SCInfoFunc.UpdateSC(sc)

def GetScStastic(Sdept):
    # 获取与成绩有关的统计数据
    resAverMaxMin = ScStasticfunc.GetAverMaxMinBySdept(Sdept)
    resExcel = ScStasticfunc.GetScExcellentRateBySdept(Sdept)
    resFail = ScStasticfunc.GetScFailNumBySdept(Sdept)
    if resAverMaxMin == None:
        WriteOutputLog("该学院没有相关的成绩记录")
        return
    output = "学院：%s\n" % Sdept + "平均分：%s\n" % resAverMaxMin['avg(Grade)'] + "最高分：%s\n" % resAverMaxMin['max(Grade)'] + "最低分：%s\n" % resAverMaxMin['min(Grade)'] + "优秀率：%s\n" % resExcel + "不及格人数：%s\n" % resFail
    WriteOutputLog(output)

def GetSortedStudentListByDept(Sdept):
    res = SortFunction.SortStudentInSameSdept(Sdept)
    if res == None:
        WriteOutputLog("该学院没有相关的成绩记录")
        return
    output = "学院：%s\n" % Sdept + "姓名\t课程\t成绩\n"
    for i in res:
        print(i)
        output += "%s\t%s\t%s\t\n" % (i['Sname'], i['Cname'], i['Grade'])
    WriteOutputLog(output)

def GetStudentBasicInfo(Sno):
    resBasicInfo = StudentInfoQueryFunc.GetStudentInfoBySno(Sno)
    resCourseInfo = StudentInfoQueryFunc.GetStudentCourseInfoBySno(Sno)
    if resBasicInfo == None:
        WriteOutputLog("该学生不存在")
        return
    output = "学号：%s\n" % resBasicInfo['Sno'] + "姓名：%s\n" % resBasicInfo['Sname'] + "性别：%s\n" % resBasicInfo['Ssex'] + "年龄：%s\n" % resBasicInfo['Sage'] + "学院：%s\n" % resBasicInfo['Sdept'] + "奖学金：%s\n" % resBasicInfo['Scholarship'] + "课程信息：\n"
    output += "课程号\t课程名\t先修课程号\t学分\n"
    for i in resCourseInfo:
        output += "%s\t%s\t%s\t%s\n" % (i['Cno'], i['Cname'], i['Cpno'], i['Ccredit'])
    WriteOutputLog(output)