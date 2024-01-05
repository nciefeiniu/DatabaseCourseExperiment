class Student(object):
    Sno = ""
    Sname = ""
    Ssex = ""
    Sage = ""
    Sdept = ""
    Scholarship = ""

    def __init__(self, Sno, Sname, Ssex, Sage, Sdept, Scholarship):
        self.Sno = Sno
        self.Sname = Sname
        self.Ssex = Ssex
        self.Sage = Sage
        self.Sdept = Sdept
        self.Scholarship = Scholarship


class Course(object):
    Cno = ""
    Cname = ""
    Cpno = ""
    Ccredit = ""

    def __init__(self, Cno, Cname, Cpno, Ccredit):
        self.Cno = Cno
        self.Cname = Cname
        self.Cpno = Cpno
        self.Ccredit = Ccredit


class SC(object):
    Sno = ""
    Cno = ""
    Grade = ""

    def __init__(self, Sno, Cno, Grade):
        self.Sno = Sno
        self.Cno = Cno
        self.Grade = Grade
