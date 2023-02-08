import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import *
 
from ui.untitled import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent = None) :
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.click)

    def click(self):
        self.ui.pushButton.setText("测试")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.setWindowTitle("第一个程序")
    win.show()
    app.exit(app.exec_())