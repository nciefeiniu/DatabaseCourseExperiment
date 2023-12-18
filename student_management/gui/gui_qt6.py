from PyQt6.QtWidgets import QWidget,QPushButton,QVBoxLayout,QTabWidget,QLabel
from controller import button_events



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)  # 设置窗口的位置和大小
        self.setWindowTitle('学生管理系统')  # 设置窗口的标题

        # 选项卡初始化
        self.tabWidget = QTabWidget(self)  # 创建一个选项卡控件

        self.tabStudentInfo = QWidget()  # 新生入学信息增加，学生信息修改。
        self.tabStudentInfo.layout = QVBoxLayout(self.tabStudentInfo)
        self.tabStudentInfo.layout.addWidget(QLabel("This is Tab 1"))
        self.tabWidget.addTab(self.tabStudentInfo, "Tab 1")  # 添加第一个选项卡

        self.tab2 = QWidget()  # 创建第二个选项卡的内容
        self.tab2.layout = QVBoxLayout(self.tab2)
        self.tab2.layout.addWidget(QLabel("This is Tab 2"))
        self.tabWidget.addTab(self.tab2, "Tab 2")  # 添加第二个选项卡

        layout = QVBoxLayout(self)  # 创建一个垂直布局
        layout.addWidget(self.tabWidget)  # 将按钮添加到布局中
