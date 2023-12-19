from model.student_model import Student
from model.student_management_func import StudentInfoModel

def InsertStudentInfo(Sno, Sname, Ssex, Sage, Sdept,Scholarship):
    # 将数据插入数据库
    student = Student(Sno, Sname, Ssex, Sage, Sdept,Scholarship)
    StudentInfoModel.AddStudent(student)

def UpdateStudentInfo(Sno, Sname, Ssex, Sage, Sdept,Scholarship):
    # 将数据插入数据库
    student = Student(Sno, Sname, Ssex, Sage, Sdept,Scholarship)
    StudentInfoModel.UpdateStudent(student)