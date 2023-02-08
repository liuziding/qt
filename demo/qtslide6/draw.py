import sys


PORT_PEN_COLOR = "#000000"
PORT_BRUSH_COLOR = "#ebebeb"
EDGE_PEN_COLOR = "#474747"

from PyQt5 import QtCore,QtGui
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QWidget
from polygon_ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__(*args, **kwargs)
        # super().__init__()
        self.setupUi(self)

        self.setGeometry(0, 0, 800, 600)
        self.setCentralWidget(GraphicsView())
        self.show()

        pixmap = QPixmap('E:\\haitong\\VehicleTracking\\code\\demo\\day\\20230206115934.png')
        pixmap = QtGui.QPixmap("E:\\haitong\\VehicleTracking\\code\\demo\\day\\20230206115934.png")
        self.graphicsview.setPixmap(pixmap)


class GraphicsView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.setScene(GraphicsScene())
        self.setRenderHint(QPainter.RenderHint.Antialiasing)

class GraphicsScene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSceneRect(-10000, -10000, 20000, 20000)
        self._port_pen = QPen(QColor(PORT_PEN_COLOR))
        self._port_brush = QBrush(QColor(PORT_BRUSH_COLOR))
        self._edge_pen = QPen(QColor(EDGE_PEN_COLOR))
        self._edge_pen.setWidth(4)

    def mousePressEvent(self, event):
        clicked_item = self.itemAt(event.scenePos(), QTransform())
        if event.buttons() == Qt.MouseButton.LeftButton:
            if clicked_item is not None:
                # edge item
                pos = clicked_item.scenePos()
                pos.setX(pos.x() + 6)
                pos.setY(pos.y() + 6)
                self.edge = self.addPath(QPainterPath())
                self.edge.setPen(self._edge_pen)
                self.start_pos = pos
                self.end_pos = self.start_pos
                self.update_path()
            else:
                x = event.scenePos().x()
                y = event.scenePos().y()
                # port item
                start_port = Ellipse()
                start_port.setPos(x - 6, y - 6)
                start_port.setPen(self._port_pen)
                start_port.setBrush(self._port_brush)
                start_port.setZValue(10000.0)
                self.addItem(start_port)
                # edge item
                self.edge = self.addPath(QPainterPath())
                self.edge.setPen(self._edge_pen)
                self.start_pos = event.scenePos()
                self.end_pos = self.start_pos
                self.update_path()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            print(f"moving, x : {event.scenePos().x()}, y : {event.scenePos().y()}")
            self.end_pos = event.scenePos()
            try:
                self.update_path()
            except AttributeError:
                pass

    def mouseReleaseEvent(self, event) -> None:
        released_item = self.itemAt(event.scenePos(), QTransform())
        if event.button() == Qt.MouseButton.LeftButton:
            if released_item is not None and released_item.type() != 2:
                self.end_pos = released_item.scenePos()
                self.end_pos.setX(self.end_pos.x() + 6)
                self.end_pos.setY(self.end_pos.y() + 6)
                if not self.start_pos.isNull() and not self.end_pos.isNull():
                    path = QPainterPath()
                    path.moveTo(self.start_pos.x() - 1, self.start_pos.y() - 1)
                    path.lineTo(self.end_pos)
                    self.edge.setPath(path)
            else:
                x = event.scenePos().x() + 1
                y = event.scenePos().y() + 1
                end_port = QGraphicsEllipseItem(0, 0, 10, 10)
                end_port.setPos(x - 6, y - 6)
                end_port.setPen(self._port_pen)
                end_port.setBrush(self._port_brush)
                end_port.setZValue(10000.0)
                self.addItem(end_port)

    def update_path(self):
        if not self.start_pos.isNull() and not self.end_pos.isNull():
            path = QPainterPath()
            path.moveTo(self.start_pos.x() - 1, self.start_pos.y() - 1)
            path.lineTo(self.end_pos)
            self.edge.setPath(path)


class Ellipse(QGraphicsEllipseItem):
    def __init__(self):
        super().__init__()
        self.setRect(0, 0, 10, 10)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec())