import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from polygon_ui import Ui_MainWindow


class GraphicsView(QtWidgets.QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        scene = QtWidgets.QGraphicsScene(self)
        self.setScene(scene)

        self._pixmap_item = QtWidgets.QGraphicsPixmapItem()
        scene.addItem(self.pixmap_item)

        self._polygon_item = QtWidgets.QGraphicsPolygonItem(self.pixmap_item)
        self.polygon_item.setPen(QtGui.QPen(QtCore.Qt.black, 5, QtCore.Qt.SolidLine))
        self.polygon_item.setBrush(QtGui.QBrush(QtCore.Qt.red, QtCore.Qt.VerPattern))

    @property
    def pixmap_item(self):
        return self._pixmap_item

    @property
    def polygon_item(self):
        return self._polygon_item

    def setPixmap(self, pixmap):
        self.pixmap_item.setPixmap(pixmap)

    def resizeEvent(self, event):
        self.fitInView(self.pixmap_item, QtCore.Qt.KeepAspectRatio)
        super().resizeEvent(event)

    def mousePressEvent(self, event):
        sp = self.mapToScene(event.pos())
        lp = self.pixmap_item.mapFromScene(sp)

        poly = self.polygon_item.polygon()
        poly.append(lp)
        self.polygon_item.setPolygon(poly)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.graphicsview = GraphicsView()
        lay = QtWidgets.QVBoxLayout(self.label)
        lay.addWidget(self.graphicsview)

        pixmap = QtGui.QPixmap("E:\\haitong\\VehicleTracking\\code\\demo\\day\\20230206115934.png")
        self.graphicsview.setPixmap(pixmap)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())