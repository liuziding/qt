import sys
from PySide6 import QtWidgets, QtGui

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QGraphicsView,
    QGraphicsScene,
    QGraphicsEllipseItem,
)

from PySide6.QtGui import QPainterPath, QTransform, QPen, QBrush, QColor, QPainter

from PySide6.QtCore import QThread, QUrl, Qt
from PySide6.QtGui import QPainter
from PySide6.QtMultimedia import (QAudio, QAudioOutput, QMediaFormat,
                                  QMediaPlayer)
 
from ui.untitled import Ui_MainWindow


PORT_PEN_COLOR = "#000000"
PORT_BRUSH_COLOR = "#ebebeb"
EDGE_PEN_COLOR = "#474747"

class VideoThread(QThread):
    # change_pixmap_signal = pyqtSignal(np.ndarray)
    def __init__(self, video_path, graphicsView):
        self.player = QMediaPlayer()
        self.item = QGraphicsVideoItem()
        self.player.setVideoOutput(item)
        self.graphicsView = graphicsView
        self.graphicsView.scene().addItem(self.item)
        self.graphicsView.show()
        self.player.setSource(video_path)
        self.player.play()

    def run(self):
        self.player.play()
        # # capture from web cam
        # cap = cv2.VideoCapture(0)
        # while True:
        #     ret, cv_img = cap.read()
        #     if ret:
        #         self.change_pixmap_signal.emit(cv_img)

class GraphicsView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)

        scene = QtWidgets.QGraphicsScene()
        self.setScene(scene)
        
        self.setRenderHint(QPainter.RenderHint.Antialiasing)

        self._pixmap_item = QtWidgets.QGraphicsPixmapItem()
        scene.addItem(self.pixmap_item)

        self._polygon_item = QtWidgets.QGraphicsPolygonItem(self.pixmap_item)

    @property
    def pixmap_item(self):
        return self._pixmap_item

    @property
    def polygon_item(self):
        return self._polygon_item

    def setPixmap(self, pixmap):
        self.pixmap_item.setPixmap(pixmap)



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


class MainWindow(QMainWindow):
    def __init__(self, parent = None) :
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.lineEdit.setText("E:\\haitong\\VehicleTracking\\code\\demo\\day\\day-409-3-0000_0030.mp4")
        self.ui.lineEdit_4.setText("E:\\haitong\\VehicleTracking\\code\\demo\\day\\day-409-3-0000_0030.mp4")
        self.ui.lineEdit_9.setText("E:\\haitong\\VehicleTracking\\code\\demo\\day\\day-409-3-0000_0030.mp4")
        self.ui.lineEdit_11.setText("E:\\haitong\\VehicleTracking\\code\\demo\\day\\day-409-3-0000_0030.mp4")

        self.ui.lineEdit_2.setText("[[361, 194], [1044, 198], [1044,657], [374, 657]]")
        self.ui.lineEdit_5.setText("[[361, 194], [1044, 198], [1044,657], [374, 657]]")
        self.ui.lineEdit_8.setText("[[361, 194], [1044, 198], [1044,657], [374, 657]]")
        self.ui.lineEdit_12.setText("[[361, 194], [1044, 198], [1044,657], [374, 657]]")

        self.ui.lineEdit_3.setText("[(424, 461), (865, 461)]")
        self.ui.lineEdit_6.setText("[(424, 461), (865, 461)]")
        self.ui.lineEdit_7.setText("[(424, 461), (865, 461)]")
        self.ui.lineEdit_10.setText("[(424, 461), (865, 461)]")

        # self.ui.textBrowser.setText("检测框选区域：[[361, 194], [1044, 198], [1044,657], [374, 657]]\n\
        #     过线区域检测：[(424, 461), (865, 461)]")
        # self.ui.lineEdit2.setText('''检测框选区域：[[361, 194], [1044, 198], [1044,657], [374, 657]]
        #     过线区域检测：[(424, 461), (865, 461)]''')
        self.ui.pushButton.clicked.connect(self.loadVideo1)
        self.ui.pushButton_2.clicked.connect(self.setLine)
        self.ui.pushButton_3.clicked.connect(self.setArea)

        self.ui.pushButton_6.clicked.connect(self.loadVideo2)

        self.ui.pushButton_7.clicked.connect(self.loadVideo3)
        self.ui.pushButton_10.clicked.connect(self.loadVideo4)

    def loadVideo1(self):
        video_path = self.ui.lineEdit.text()
        self.ui.pushButton.setEnabled(False)
        self.ui.lineEdit.setEnabled(False)

        self.player = QMediaPlayer()
        qurl_path = QUrl("file:" + video_path)
        # self.player.errorOccurred.connect(self._player_error)
        # self.player.playbackStateChanged.connect(self.update_buttons)
        self.player.setSource(qurl_path)
        self.player.setVideoOutput(self.ui.widget)     
        self.player.play()

    def loadVideo2(self):
        video_path = self.ui.lineEdit_4.text()
        self.ui.pushButton_6.setEnabled(False)
        self.ui.lineEdit_4.setEnabled(False)

        self.player = QMediaPlayer()
        qurl_path = QUrl("file:" + video_path)
        # self.player.errorOccurred.connect(self._player_error)
        # self.player.playbackStateChanged.connect(self.update_buttons)
        self.player.setSource(qurl_path)
        self.player.setVideoOutput(self.ui.widget_2)     
        self.player.play()

    def loadVideo3(self):
        video_path = self.ui.lineEdit_9.text()
        self.ui.pushButton_7.setEnabled(False)
        self.ui.lineEdit_9.setEnabled(False)

        self.player = QMediaPlayer()
        qurl_path = QUrl("file:" + video_path)
        # self.player.errorOccurred.connect(self._player_error)
        # self.player.playbackStateChanged.connect(self.update_buttons)
        self.player.setSource(qurl_path)
        self.player.setVideoOutput(self.ui.widget_3)     
        self.player.play()
    
    def loadVideo4(self):
        video_path = self.ui.lineEdit_11.text()
        self.ui.pushButton_10.setEnabled(False)
        self.ui.lineEdit_11.setEnabled(False)

        self.player = QMediaPlayer()
        qurl_path = QUrl("file:" + video_path)
        # self.player.errorOccurred.connect(self._player_error)
        # self.player.playbackStateChanged.connect(self.update_buttons)
        self.player.setSource(qurl_path)
        self.player.setVideoOutput(self.ui.widget_4)     
        self.player.play()

    def setLine(self):
        self.ui.pushButton_2.setText("测试")
        self.ui.pushButton_2.setEnabled(False)
        self.ui.lineEdit_2.setEnabled(False)

        self.graphicsview = GraphicsView()        
        # pixmap = QtGui.QPixmap(QUrl.fromLocalFile("E:\\haitong\\VehicleTracking\\code\\demo\\day\\20230206115934.png"))
        pixmap = QtGui.QPixmap("E:\\haitong\\VehicleTracking\\code\\demo\\day\\20230206115934.png")
        self.graphicsview.setPixmap(pixmap)
        self.setCentralWidget(GraphicsView())
        self.show()

    def setArea(self):
        self.ui.pushButton_3.setText("测试111")
        self.ui.pushButton_3.setEnabled(False)
        self.ui.lineEdit_3.setEnabled(False)

        self.setCentralWidget(GraphicsView())
        self.show()
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.setWindowTitle("第一个程序11111")
    win.show()
    app.exit(app.exec())
