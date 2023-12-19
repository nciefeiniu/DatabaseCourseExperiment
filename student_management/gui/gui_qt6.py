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
        self.btnStudentInsert = QPushButton("新生入学信息增加",self)
        self.btnStudentInsert.clicked.connect(lambda:button_events.InsertStudentInfo(self.editSno.text(), self.editSname.text(), self.editSsex.text(), self.editSage.text(), self.editSdept.text(),self.editScholarship.text()) )
        self.btnStudentUpdate = QPushButton("学生信息修改",self)
        self.btnStudentUpdate.clicked.connect(lambda:button_events.UpdateStudentInfo(self.editSno.text(), self.editSname.text(), self.editSsex.text(), self.editSage.text(), self.editSdept.text(),self.editScholarship.text()) )
        #文本框
        self.editSname = QLineEdit(self)
        self.editSno = QLineEdit(self)
        self.editSsex = QLineEdit(self)
        self.editSage = QLineEdit(self)
        self.editSdept = QLineEdit(self)
        self.editScholarship = QLineEdit(self)
        #标签
        self.labelSname = QLabel("姓名",self)
        self.labelSno = QLabel("学号",self)
        self.labelSsex = QLabel("性别",self)
        self.labelSage = QLabel("年龄",self)
        self.labelSdept = QLabel("专业",self)
        self.labelScholarship = QLabel("奖学金",self)
        #设置布局
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

        self.tabWidget.addTab(self.tabStudentInfo, "Tab 1")  # 添加第一个选项卡

        self.tab2 = QWidget()  # 创建第二个选项卡的内容
        self.tab2.layout = QVBoxLayout(self.tab2)
        self.tab2.layout.addWidget(QLabel("This is Tab 2"))
        self.tabWidget.addTab(self.tab2, "Tab 2")  # 添加第二个选项卡

        layout = QVBoxLayout(self)  # 创建一个垂直布局
        layout.addWidget(self.tabWidget)  # 将按钮添加到布局中
