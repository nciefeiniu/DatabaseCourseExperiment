from model.student_model import Student
from model.student_info_model import StudentInfoModel

class StudentInfoButtonEvents(object):
    @staticmethod
    def AddStudentInfo(Sno, Sname, Ssex, Sage, Sdept,Scholarship):
        # 将数据插入数据库
        student = Student(Sno, Sname, Ssex, Sage, Sdept,Scholarship)
        StudentInfoModel.AddStudent(student)