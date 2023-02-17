# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1242, 966)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 1181, 911))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox_7 = QGroupBox(self.layoutWidget)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.lineEdit_10 = QLineEdit(self.groupBox_7)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(30, 420, 420, 20)) # 第四列 第四个输入框
        self.pushButton_10 = QPushButton(self.groupBox_7)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(470, 356, 80, 28)) #第四列 第一个按钮
        self.textBrowser_5 = QTextBrowser(self.groupBox_7)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        self.textBrowser_5.setGeometry(QRect(30, 30, 518, 36)) # 第四列 第一个输入框
        self.lineEdit_11 = QLineEdit(self.groupBox_7)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setGeometry(QRect(30, 360, 420, 20)) # 第四列 第二个输入框
        self.pushButton_11 = QPushButton(self.groupBox_7)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(470, 386, 80, 28)) # 第四列 第二个按钮
        self.pushButton_12 = QPushButton(self.groupBox_7)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(470, 416, 80, 28)) # 第四列 第三个按钮
        self.lineEdit_12 = QLineEdit(self.groupBox_7)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setGeometry(QRect(30, 390, 420, 20)) # 第四列 第三个输入框
        self.widget_4 = QVideoWidget(self.groupBox_7)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(30, 80, 518, 271)) # 第四列 视频区域

        self.gridLayout_2.addWidget(self.groupBox_7, 1, 1, 1, 1)

        self.groupBox_4 = QGroupBox(self.layoutWidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.textBrowser_2 = QTextBrowser(self.groupBox_4)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(30, 30, 518, 36)) # 第一列 第一个输入框
        self.pushButton = QPushButton(self.groupBox_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(470, 356, 80, 28)) # 第一列 第一个按钮
        self.lineEdit = QLineEdit(self.groupBox_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 360, 420, 20)) # 第一列 第二个输入框
        self.pushButton_2 = QPushButton(self.groupBox_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(470, 386, 80, 28)) # 第一列 第二个按钮
        self.widget = QVideoWidget(self.groupBox_4)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 80, 518, 271)) # 第一列 视频区域
        self.pushButton_3 = QPushButton(self.groupBox_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(470, 416, 80, 28)) # 第一列 第三个按钮
        self.lineEdit_2 = QLineEdit(self.groupBox_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(30, 390, 420, 20)) # 第一列 第三个输入框
        self.lineEdit_3 = QLineEdit(self.groupBox_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(30, 420, 420, 20)) # 第一列 第四个输入框

        self.gridLayout_2.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.layoutWidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.widget_3 = QVideoWidget(self.groupBox_6)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(30, 80, 518, 271)) # 第三列 视频区域
        self.lineEdit_7 = QLineEdit(self.groupBox_6)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(30, 420, 420, 20)) # 第三列 第四个输入框
        self.lineEdit_8 = QLineEdit(self.groupBox_6)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(30, 390, 420, 20)) # 第三列 第三个输入框
        self.lineEdit_9 = QLineEdit(self.groupBox_6)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(30, 360, 420, 20)) # 第三列 第二个输入框
        self.textBrowser_4 = QTextBrowser(self.groupBox_6)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(30, 30, 518, 36)) # 第三列 第一个输入框
        self.pushButton_7 = QPushButton(self.groupBox_6)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(470, 356, 80, 28)) # 第三列 第一个按钮
        self.pushButton_8 = QPushButton(self.groupBox_6)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(470, 386, 80, 28)) # 第三列 第二个按钮
        self.pushButton_9 = QPushButton(self.groupBox_6)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(470, 416, 80, 28)) # 第三列 第三个按钮

        self.gridLayout_2.addWidget(self.groupBox_6, 1, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.layoutWidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.textBrowser_3 = QTextBrowser(self.groupBox_5)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(30, 30, 518, 36)) # 第二列 第一个输入框
        self.widget_2 = QVideoWidget(self.groupBox_5)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(30, 80, 518, 271)) # 第二列 视频区域
        self.pushButton_4 = QPushButton(self.groupBox_5)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(470, 416, 80, 28)) # 第二列 第三个按钮
        self.lineEdit_4 = QLineEdit(self.groupBox_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(30, 360, 420, 20)) # 第二列 第二个输入框
        self.lineEdit_5 = QLineEdit(self.groupBox_5)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(30, 390, 420, 20)) # 第二列 第三个输入框
        self.lineEdit_6 = QLineEdit(self.groupBox_5)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(30, 420, 420, 20)) # 第二列 第四个输入框
        self.pushButton_5 = QPushButton(self.groupBox_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(470, 386, 80, 28)) # 第二列 第二个按钮
        self.pushButton_6 = QPushButton(self.groupBox_5)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(470, 356, 80, 28)) # 第二列 第一个按钮

        self.gridLayout_2.addWidget(self.groupBox_5, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1242, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Load Video", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Set Lines", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Set Area", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Load Video", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Set Lines", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Set Area", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Load Video", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Set Lines", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Set Area", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Set Area", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Set Lines", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Load Video", None))
    # retranslateUi

