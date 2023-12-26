from PyQt6.QtWidgets import QApplication
from gui import gui_qt6
import model.mysql
def main():
    app = QApplication([])  # 创建应用程序对象
    window = gui_qt6.MainWindow()  # 创建窗口
    window.show()  # 显示窗口
    app.exec()  # 进入应用程序的主循环

if __name__ == '__main__':
    main()