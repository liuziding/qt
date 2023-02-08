import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget)
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt

class MouseTracker(QWidget):
    distance_from_center = 0
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)

    def initUI(self):
        self.setGeometry(200, 200, 1000, 500)
        self.setWindowTitle('Mouse Tracker')
        self.label = QLabel(self)
        self.label.resize(500, 40)
        self.show()
        self.pos = None

    def mouseMoveEvent(self, event):
        distance_from_center = round(((event.y() - 250)**2 + (event.x() - 500)**2)**0.5)
        self.label.setText('Coordinates: ( %d : %d )' % (event.x(), event.y()) + "Distance from center: " + str(distance_from_center))       
        self.pos = event.pos()
        self.update()

    def paintEvent(self, event):
        if self.pos:
            q = QPainter(self)
            q.drawLine(self.pos.x(), self.pos.y(), 500, 250)


app = QApplication(sys.argv)
ex = MouseTracker()
sys.exit(app.exec_())