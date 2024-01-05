from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QTabWidget, QLabel, QLineEdit, QTextEdit, QComboBox
from controller import button_events
from util.log_util import SetConsoleLogTarget, SetOutputLogTarget


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 日志输出
        self.textLogEditWidget = QTextEdit(self)
        self.textOutputEditWidget = QTextEdit(self)
        SetConsoleLogTarget(self.textLogEditWidget)
        SetOutputLogTarget(self.textOutputEditWidget)
        self.setGeometry(300, 300, 1000, 800)  # 设置窗口的位置和大小
        self.setWindowTitle('学生管理系统')  # 设置窗口的标题

        # 选项卡初始化
        self.tabWidget = QTabWidget(self)  # 创建一个选项卡控件
        self.tabStudentInfo = QWidget()  # 新生入学信息增加，学生信息修改。
        self.tabStudentInfo.layout = QVBoxLayout(self.tabStudentInfo)
        # 按钮
        # 数据库
        self.btnSqlConnect = QPushButton("连接数据库")
        self.btnSqlConnect.clicked.connect(
            lambda: button_events.ConnectDb(self.editDbHost.text(), int(self.editDbPort.text()), self.editDbUser.text(),
                                            self.editDbPassword.text(), self.editDbName.text()))
        # 学生管理
        self.btnStudentInsert = QPushButton("新生入学信息增加", self)
        self.btnStudentInsert.clicked.connect(
            lambda: button_events.InsertStudentInfo(self.editSno.text(), self.editSname.text(), self.editSsex.text(),
                                                    self.editSage.text(), self.editSdept.text(),
                                                    self.comboScholarship.currentText()))
        self.btnStudentUpdate = QPushButton("学生信息修改", self)
        self.btnStudentUpdate.clicked.connect(
            lambda: button_events.UpdateStudentInfo(self.editSno.text(), self.editSname.text(), self.editSsex.text(),
                                                    self.editSage.text(), self.editSdept.text(),
                                                    self.comboScholarship.currentText()))
        # 课程信息维护
        self.btnAddCourse = QPushButton("新增课程", self)
        self.btnUpdateCourse = QPushButton("修改课程", self)
        self.btnAddCourse.clicked.connect(
            lambda: button_events.InsertCourseInfo(self.editCno.text(), self.editCname.text(), self.editCpno.text(),
                                                   self.editCcredit.text()))
        self.btnUpdateCourse.clicked.connect(
            lambda: button_events.UpdateCourseInfo(self.editCno.text(), self.editCname.text(), self.editCpno.text(),
                                                   self.editCcredit.text()))
        # 学生成绩管理
        self.btnScInsert = QPushButton("学生成绩增加", self)
        self.btnScUpdate = QPushButton("学生成绩修改", self)
        self.btnScInsert.clicked.connect(
            lambda: button_events.InsertSCInfo(self.scEditSno.text(), self.scEditCno.text(), self.scEditGrade.text()))
        self.btnScUpdate.clicked.connect(
            lambda: button_events.UpdateSCInfo(self.scEditSno.text(), self.scEditCno.text(), self.scEditGrade.text()))
        # 成绩信息统计
        self.btnScStastic = QPushButton("成绩信息统计", self)
        self.btnScStastic.clicked.connect(lambda: button_events.GetScStastic(self.stasticEditSdept.text()))
        self.btnScRank = QPushButton("学生成绩排名", self)
        self.btnScRank.clicked.connect(lambda: button_events.GetSortedStudentListByDept(self.stasticEditSdept.text()))
        # 学生信息查询
        self.btnQueryStudentInfo = QPushButton("学生信息查询", self)
        self.btnQueryStudentInfo.clicked.connect(lambda: button_events.GetStudentBasicInfo(self.editQuerySno.text()))

        # 文本框/下拉框
        ## 数据库
        self.editDbHost = QLineEdit(self)
        self.editDbPort = QLineEdit(self)
        self.editDbUser = QLineEdit(self)
        self.editDbPassword = QLineEdit(self, echoMode=QLineEdit.EchoMode.Password)
        self.editDbName = QLineEdit(self)
        ## 学生管理
        self.editSname = QLineEdit(self)
        self.editSno = QLineEdit(self)
        self.editSsex = QLineEdit(self)
        self.editSage = QLineEdit(self)
        self.editSdept = QLineEdit(self)
        # editScholarship是下拉框
        self.comboScholarship = QComboBox(self)
        self.comboScholarship.addItem("否")
        self.comboScholarship.addItem("是")
        ## 课程信息维护
        self.editCno = QLineEdit(self)
        self.editCname = QLineEdit(self)
        self.editCpno = QLineEdit(self)
        self.editCcredit = QLineEdit(self)
        # 学生成绩管理
        self.scEditSno = QLineEdit(self)
        self.scEditCno = QLineEdit(self)
        self.scEditGrade = QLineEdit(self)
        # 成绩信息统计
        self.stasticEditSdept = QLineEdit(self)
        # 学生信息查询
        self.editQuerySno = QLineEdit(self)

        # 标签
        ## 数据库
        self.labelDbHost = QLabel("主机", self)
        self.labelDbPort = QLabel("端口", self)
        self.labelDbUser = QLabel("用户名", self)
        self.labelDbPassword = QLabel("密码", self)
        self.labelDbName = QLabel("数据库名", self)
        ##学生管理
        self.labelSname = QLabel("姓名", self)
        self.labelSno = QLabel("学号", self)
        self.labelSsex = QLabel("性别", self)
        self.labelSage = QLabel("年龄", self)
        self.labelSdept = QLabel("专业", self)
        self.labelScholarship = QLabel("奖学金", self)
        ##课程信息维护
        self.labelCno = QLabel("课程号", self)
        self.labelCname = QLabel("课程名", self)
        self.labelCpno = QLabel("前置课程", self)
        self.labelCcredit = QLabel("学分", self)
        ##学生成绩管理
        self.scLabelSno = QLabel("学号", self)
        self.scLabelCno = QLabel("课程号", self)
        self.scLabelGrade = QLabel("成绩", self)
        ##成绩信息统计
        self.stasticLabelSdept = QLabel("专业", self)
        ##学生信息查询
        self.labelQuerySno = QLabel("学号", self)

        # 设置布局
        # 数据库
        self.tabDb = QWidget()
        self.tabDb.layout = QVBoxLayout(self.tabDb)
        self.tabDb.layout.addWidget(self.btnSqlConnect)
        self.tabDb.layout.addWidget(self.labelDbHost)
        self.tabDb.layout.addWidget(self.editDbHost)
        self.tabDb.layout.addWidget(self.labelDbPort)
        self.tabDb.layout.addWidget(self.editDbPort)
        self.tabDb.layout.addWidget(self.labelDbUser)
        self.tabDb.layout.addWidget(self.editDbUser)
        self.tabDb.layout.addWidget(self.labelDbPassword)
        self.tabDb.layout.addWidget(self.editDbPassword)
        self.tabDb.layout.addWidget(self.labelDbName)
        self.tabDb.layout.addWidget(self.editDbName)
        self.tabWidget.addTab(self.tabDb, "数据库")  # 添加第一个选项卡
        # 学生管理
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
        self.tabStudentInfo.layout.addWidget(self.comboScholarship)
        self.tabWidget.addTab(self.tabStudentInfo, "学生信息管理")  # 添加第一个选项卡

        # 课程信息维护
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

        # 学生成绩管理
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

        # 成绩信息统计
        self.tab4 = QWidget()
        self.tab4.layout = QVBoxLayout(self.tab4)
        self.tab4.layout.addWidget(self.btnScStastic)
        self.tab4.layout.addWidget(self.btnScRank)
        self.tab4.layout.addWidget(self.stasticLabelSdept)
        self.tab4.layout.addWidget(self.stasticEditSdept)
        self.tabWidget.addTab(self.tab4, "成绩信息统计")

        # 学生信息查询
        self.tab5 = QWidget()
        self.tab5.layout = QVBoxLayout(self.tab5)
        self.tab5.layout.addWidget(self.btnQueryStudentInfo)
        self.tab5.layout.addWidget(self.labelQuerySno)
        self.tab5.layout.addWidget(self.editQuerySno)
        self.tabWidget.addTab(self.tab5, "学生信息查询")

        layout = QVBoxLayout(self)  # 创建一个垂直布局
        layout.addWidget(self.tabWidget)  # 将tab组件添加到布局中
        layout.addWidget(self.textLogEditWidget)  # 将日志输出添加到布局中
        layout.addWidget(self.textOutputEditWidget)  # 将查询结果输出添加到布局中
