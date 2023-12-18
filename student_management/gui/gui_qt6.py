from PyQt6.QtWidgets import QWidget,QPushButton,QVBoxLayout
from controller import button_events



class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)  # 设置窗口的位置和大小
        self.setWindowTitle('学生管理系统')  # 设置窗口的标题
        self.button = QPushButton('Click me!', self)  # 创建一个按钮
        self.button.clicked.connect(button_events.on_button_clicked)  # 连接按钮的点击信号到槽函数
        layout = QVBoxLayout(self)  # 创建一个垂直布局
        layout.addWidget(self.button)  # 将按钮添加到布局中
