from model.data_models import Student, Course, SC
from model.model_funcs import StudentInsertUpdateFunc, CourseInsertUpdateFunc, SCInfoFunc,ScStasticfunc,SortFunction,StudentInfoQueryFunc

def InsertStudentInfo(Sno, Sname, Ssex, Sage, Sdept,Scholarship):
    # 将数据插入数据库
    student = Student(Sno, Sname, Ssex, Sage, Sdept,Scholarship)
    StudentInsertUpdateFunc.AddStudent(student)

def UpdateStudentInfo(Sno, Sname, Ssex, Sage, Sdept,Scholarship):
    # 将数据插入数据库
    student = Student(Sno, Sname, Ssex, Sage, Sdept,Scholarship)
    StudentInsertUpdateFunc.UpdateStudent(student)

def InsertCourseInfo(Cno, Cname, Cpno, Ccredit):
    # 将数据插入数据库
    course = Course(Cno, Cname, Cpno, Ccredit)
    CourseInsertUpdateFunc.AddCourse(course)

def UpdateCourseInfo(Cno, Cname, Cpno, Ccredit):
    # 将数据插入数据库
    course = Course(Cno, Cname, Cpno, Ccredit)
    CourseInsertUpdateFunc.UpdateCourse(course)

def InsertSCInfo(Sno, Cno, Grade):
    # 将数据插入数据库
    sc = SC(Sno, Cno, Grade)
    SCInfoFunc.AddSC(sc)

def UpdateSCInfo(Sno, Cno, Grade):
    # 将数据插入数据库
    sc = SC(Sno, Cno, Grade)
    SCInfoFunc.UpdateSC(sc)

def GetScStastic(Sdept):
    # 获取与成绩有关的统计数据
    resAverMaxMin = ScStasticfunc.GetAverMaxMinBySdept(Sdept)
    resExcel = ScStasticfunc.GetScExcellentRateBySdept(Sdept)
    resFail = ScStasticfunc.GetScFailNumBySdept(Sdept)

def GetSortedStudentListByDept(Sdept):
    res = SortFunction.SortStudentInSameSdept(Sdept)

def GetStudentBasicInfo(Sno):
    resBasicInfo = StudentInfoQueryFunc.GetStudentInfoBySno(Sno)
    resCourseInfo = StudentInfoQueryFunc.GetStudentCourseInfoBySno(Sno)