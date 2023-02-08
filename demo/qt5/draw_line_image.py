import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import (QApplication, QLabel, QWidget)

class MouseTracker(QtCore.QObject):
    positionChanged = QtCore.pyqtSignal(QtCore.QPoint)

    def __init__(self, widget):
        super().__init__(widget)
        self._widget = widget
        self.widget.setMouseTracking(True)
        self.widget.installEventFilter(self)

    @property
    def widget(self):
        return self._widget

    def eventFilter(self, o, e):
        if e.type() == QtCore.QEvent.MouseMove:
            self.positionChanged.emit(e.pos())
        return super().eventFilter(o, e)


class DraggableLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.LabelIsMoving = False
        self.setStyleSheet("border-color: rgb(238, 0, 0); border-width : 2.0px; border-style:inset; background: transparent;")
        self.origin = None
        # self.setDragEnabled(True)

    def mousePressEvent(self, event):
        if not self.origin:
            # update the origin point, we'll need that later
            self.origin = self.pos()
        if event.button() == Qt.LeftButton:
            self.LabelIsMoving = True
            self.mousePos = event.pos()
            # print(event.pos())

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            # move the box
            self.move(self.pos() + event.pos() - self.mousePos)

            # print(event.pos())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            print(event.pos())

    def paintEvent(self, event):
        painter = QPainter()
        painter.setBrush(Qt.red)
        # painter.setPen(qRgb(200,0,0))
        painter.drawLine(10, 10, 200, 200)

class DynamicTab(QWidget):
    def __init__(self):
        super(DynamicTab, self).__init__()
        # self.count = 0
        self.setMouseTracking(True)
        self.setAcceptDrops(True)
        self.bool = True
        self.layout = QVBoxLayout(self)
        self.label = QLabel()
        self.layout.addChildWidget(self.label)

        self.icon1 = DraggableLabel(parent=self)
        #pixmap for icon 1
        pixmap = QPixmap('E:\\haitong\\VehicleTracking\\code\\demo\\day\\20230206115934.png')
        # currentTab.setLayout(QVBoxLayout())
        # currentTab.layout.setWidget(QRadioButton())
        self.icon1.setPixmap(pixmap)
        self.icon1.setScaledContents(True)
        self.icon1.setFixedSize(20, 20)

        self.icon2 = DraggableLabel(parent=self)
        pixmap = QPixmap('icon1.png')
        # currentTab.setLayout(QVBoxLayout())
        # currentTab.layout.setWidget(QRadioButton())
        self.icon2.setPixmap(pixmap)
        self.icon2.setScaledContents(True)
        self.icon2.setFixedSize(20, 20)
            #self.label.move(event.x() - self.label_pos.x(), event.y() - self.label_pos.y())


class UI_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(UI_MainWindow, self).__init__()
        self.setWindowTitle("QHBoxLayout")
        self.PictureTab = QtWidgets.QTabWidget

    def __setupUI__(self):
        # super(UI_MainWindow, self).__init__()
        self.setWindowTitle("QHBoxLayout")
        # loadUi("IIML_test2.ui", self)
        self.tabChanged(self.PictureTab)
        # self.tabChanged(self.tabWidget)
        self.changeTabText(self.PictureTab, index=0, TabText="Patient1")
        self.Button_ImportNew.clicked.connect(lambda: self.insertTab(self.PictureTab))
        # self.PictureTab.currentChanged.connect(lambda: self.tabChanged(QtabWidget=self.PictureTab))
        # self.tabWidget.currentChanged.connect(lambda: self.tabChanged(QtabWidget=self.tabWidget))

    def tabChanged(self, QtabWidget):
        QtabWidget.currentChanged.connect(lambda : print("Tab was changed to ", QtabWidget.currentIndex()))

    def changeTabText(self, QTabWidget, index, TabText):
        QTabWidget.setTabText(index, TabText)

    def insertTab(self, QtabWidget):
        # QFileDialog.getOpenFileNames(self, 'Open File', '.')
        QtabWidget.addTab(DynamicTab(), "New Tab")
        # get number of active tab
        count = QtabWidget.count()
        # change the view to the last added tab
        currentTab = QtabWidget.widget(count-1)
        QtabWidget.setCurrentWidget(currentTab)

        pixmap = QPixmap('cat.jpg')
        #currentTab.setLayout(QVBoxLayout())
        #currentTab.layout.setWidget(QRadioButton())

        # currentTab.setImage("cat.jpg")
        currentTab.label.setPixmap(pixmap)
        currentTab.label.setScaledContents(True)
        currentTab.label.setFixedSize(self.label.width(), self.label.height())
        tracker = MouseTracker(currentTab.label)
        tracker.positionChanged.connect(self.on_positionChanged)
        self.label_position = QtWidgets.QLabel(currentTab.label, alignment=QtCore.Qt.AlignCenter)
        self.label_position.setStyleSheet('background-color: white; border: 1px solid black')
        currentTab.label.show()
        # print(currentTab.label)

    @QtCore.pyqtSlot(QtCore.QPoint)
    def on_positionChanged(self, pos):
        delta = QtCore.QPoint(30, -15)
        self.label_position.show()
        self.label_position.move(pos + delta)
        self.label_position.setText("(%d, %d)" % (pos.x(), pos.y()))
        self.label_position.adjustSize()

    # def SetupUI(self, MainWindow):
    #
    #     self.setLayout(self.MainLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    UI_MainWindow = UI_MainWindow()
    UI_MainWindow.__setupUI__()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(UI_MainWindow)
    widget.setFixedHeight(900)
    widget.setFixedWidth(1173)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")