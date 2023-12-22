from PyQt6.QtWidgets import QWidget,QPushButton,QVBoxLayout,QTabWidget,QLabel,QLineEdit
from controller import button_events




class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 1000,800)  # 设置窗口的位置和大小
        self.setWindowTitle('学生管理系统')  # 设置窗口的标题

        # 选项卡初始化
        self.tabWidget = QTabWidget(self)  # 创建一个选项卡控件

        self.tabStudentInfo = QWidget()  # 新生入学信息增加，学生信息修改。
        self.tabStudentInfo.layout = QVBoxLayout(self.tabStudentInfo)
        #按钮
        #学生管理
        self.btnStudentInsert = QPushButton("新生入学信息增加",self)
        self.btnStudentInsert.clicked.connect(lambda:button_events.InsertStudentInfo(self.editSno.text(), self.editSname.text(), self.editSsex.text(), self.editSage.text(), self.editSdept.text(),self.editScholarship.text()) )
        self.btnStudentUpdate = QPushButton("学生信息修改",self)
        self.btnStudentUpdate.clicked.connect(lambda:button_events.UpdateStudentInfo(self.editSno.text(), self.editSname.text(), self.editSsex.text(), self.editSage.text(), self.editSdept.text(),self.editScholarship.text()) )
        #课程信息维护
        self.btnAddCourse = QPushButton("新增课程",self)
        self.btnUpdateCourse = QPushButton("修改课程",self)
        self.btnAddCourse.clicked.connect(lambda:button_events.InsertCourseInfo(self.editCno.text(), self.editCname.text(), self.editCpno.text(), self.editCcredit.text()) )
        self.btnUpdateCourse.clicked.connect(lambda:button_events.UpdateCourseInfo(self.editCno.text(), self.editCname.text(), self.editCpno.text(), self.editCcredit.text()) )
        #学生成绩管理
        self.btnScInsert = QPushButton("学生成绩增加",self)
        self.btnScUpdate = QPushButton("学生成绩修改",self)
        self.btnScInsert.clicked.connect(lambda:button_events.InsertSCInfo(self.scEditSno.text(), self.scEditCno.text(), self.scEditGrade.text()) )
        self.btnScUpdate.clicked.connect(lambda:button_events.UpdateSCInfo(self.scEditSno.text(), self.scEditCno.text(), self.scEditGrade.text()) )
        #成绩信息统计
        self.btnScStastic = QPushButton("成绩信息统计",self)
        self.btnScStastic.clicked.connect(lambda:button_events.GetScStastic(self.stasticEditSdept.text()) )
        self.btnScRank = QPushButton("学生成绩排名",self)
        self.btnScRank.clicked.connect(lambda:button_events.GetSortedStudentListByDept(self.stasticEditSdept.text()) )
        #学生信息查询
        self.btnQueryStudentInfo = QPushButton("学生信息查询",self)
        self.btnQueryStudentInfo.clicked.connect(lambda:button_events.GetStudentBasicInfo(self.editQuerySno.text()) )

        #文本框
        ## 学生管理
        self.editSname = QLineEdit(self)
        self.editSno = QLineEdit(self)
        self.editSsex = QLineEdit(self)
        self.editSage = QLineEdit(self)
        self.editSdept = QLineEdit(self)
        self.editScholarship = QLineEdit(self)
        ## 课程信息维护
        self.editCno = QLineEdit(self)
        self.editCname = QLineEdit(self)
        self.editCpno = QLineEdit(self)
        self.editCcredit = QLineEdit(self)
        #学生成绩管理
        self.scEditSno = QLineEdit(self)
        self.scEditCno = QLineEdit(self)
        self.scEditGrade = QLineEdit(self)
        #成绩信息统计
        self.stasticEditSdept = QLineEdit(self)
        #学生信息查询
        self.editQuerySno = QLineEdit(self)

        #标签
        ##学生管理
        self.labelSname = QLabel("姓名",self)
        self.labelSno = QLabel("学号",self)
        self.labelSsex = QLabel("性别",self)
        self.labelSage = QLabel("年龄",self)
        self.labelSdept = QLabel("专业",self)
        self.labelScholarship = QLabel("奖学金",self)
        ##课程信息维护
        self.labelCno = QLabel("课程号",self)
        self.labelCname = QLabel("课程名",self)
        self.labelCpno = QLabel("前置课程",self)
        self.labelCcredit = QLabel("学分",self)
        ##学生成绩管理
        self.scLabelSno = QLabel("学号",self)
        self.scLabelCno = QLabel("课程号",self)
        self.scLabelGrade = QLabel("成绩",self)
        ##成绩信息统计
        self.stasticLabelSdept = QLabel("专业",self)
        ##学生信息查询
        self.labelQuerySno = QLabel("学号",self)

        
        #设置布局
        #学生管理
        self.tabStudentInfo.layout.addWidget(self.btnStudentInsert)
        self.tabStudentInfo.layout.addWidget(self.btnStudentUpdate)
        self.tabStudentInfo.layout.addWidget(self.labelSname)
        self.tabStudentInfo.layout.addWidget(self.editSname)
        self.tabStudentInfo.layout.addWidget(self.labelSno)
        self.tabStudentInfo.layout.addWidget(self.editSno)
        self.tabStudentInfo.layout.addWidget(self.labelSsex)
        self.tabStudentInfo.layout.addWidget(self.editSsex)
        self.tabStudentInfo.layout.addWidget(self.labelSage)
        self.tabStudentInfo.layout.addWidget(self.editSage)
        self.tabStudentInfo.layout.addWidget(self.labelSdept)
        self.tabStudentInfo.layout.addWidget(self.editSdept)
        self.tabStudentInfo.layout.addWidget(self.labelScholarship)
        self.tabStudentInfo.layout.addWidget(self.editScholarship)
        self.tabWidget.addTab(self.tabStudentInfo, "学生信息管理")  # 添加第一个选项卡

        #课程信息维护
        self.tab2 = QWidget()  # 创建第二个选项卡的内容
        self.tab2.layout = QVBoxLayout(self.tab2)
        self.tab2.layout.addWidget(self.btnAddCourse)
        self.tab2.layout.addWidget(self.btnUpdateCourse)
        self.tab2.layout.addWidget(self.labelCno)
        self.tab2.layout.addWidget(self.editCno)
        self.tab2.layout.addWidget(self.labelCname)
        self.tab2.layout.addWidget(self.editCname)
        self.tab2.layout.addWidget(self.labelCpno)
        self.tab2.layout.addWidget(self.editCpno)
        self.tab2.layout.addWidget(self.labelCcredit)
        self.tab2.layout.addWidget(self.editCcredit)
        self.tabWidget.addTab(self.tab2, "课程信息管理")  # 添加第二个选项卡

        #学生成绩管理
        self.tab3 = QWidget()
        self.tab3.layout = QVBoxLayout(self.tab3)
        self.tab3.layout.addWidget(self.btnScInsert)
        self.tab3.layout.addWidget(self.btnScUpdate)
        self.tab3.layout.addWidget(self.scLabelSno)
        self.tab3.layout.addWidget(self.scEditSno)
        self.tab3.layout.addWidget(self.scLabelCno)
        self.tab3.layout.addWidget(self.scEditCno)
        self.tab3.layout.addWidget(self.scLabelGrade)
        self.tab3.layout.addWidget(self.scEditGrade)
        self.tabWidget.addTab(self.tab3, "学生成绩管理")

        #成绩信息统计
        self.tab4 = QWidget()
        self.tab4.layout = QVBoxLayout(self.tab4)
        self.tab4.layout.addWidget(self.btnScStastic)
        self.tab4.layout.addWidget(self.btnScRank)
        self.tab4.layout.addWidget(self.stasticLabelSdept)
        self.tab4.layout.addWidget(self.stasticEditSdept)
        self.tabWidget.addTab(self.tab4, "成绩信息统计")

        #学生信息查询
        self.tab5 = QWidget()
        self.tab5.layout = QVBoxLayout(self.tab5)
        self.tab5.layout.addWidget(self.btnQueryStudentInfo)
        self.tab5.layout.addWidget(self.labelQuerySno)
        self.tab5.layout.addWidget(self.editQuerySno)
        self.tabWidget.addTab(self.tab5, "学生信息查询")

        layout = QVBoxLayout(self)  # 创建一个垂直布局
        layout.addWidget(self.tabWidget)  # 将tab组件添加到布局中
