import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QGraphicsView,
    QGraphicsScene,
    QGraphicsRectItem,
)
from PySide6.QtGui import QAction, QPainterPath
from PySide6.QtCore import Qt

from PySide6.QtGui import QColor, QPen, QBrush, QTransform


class GraphicsScene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSceneRect(-100, -100, 200, 200)
        self.selected = None
        self.selected_offset_x = 0
        self.selected_offset_y = 0

    def mousePressEvent(self, event) -> None:
        if event.button() == Qt.LeftButton:
            x = event.scenePos().x()
            y = event.scenePos().y()

            # rectangle
            rectitem = QGraphicsRectItem(0, 0, 10, 10)
            rectitem.setPos(x - 5, y - 5)
            rectitem.setPen(QPen(QColor(0, 0, 0), 1.0, Qt.SolidLine))
            rectitem.setBrush(QBrush(QColor(255, 255, 255, 255)))
            # rectitem.setFlag(QGraphicsItem.ItemIsMovable, True)

            # Line
            self.path_item = self.addPath(QPainterPath())
            self.start_point = event.scenePos()
            self.end_point = self.start_point
            self.update_path()
            self.addItem(rectitem)

        elif event.button() == Qt.RightButton:
            x = event.scenePos().x()
            y = event.scenePos().y()

            if not self.selected:
                item = self.itemAt(event.scenePos(), QTransform())
                # print(item)

                if item:
                    print("selected:", item)
                    self.selected = item
                    self.selected.setBrush(QBrush(QColor(255, 0, 0, 255)))
                    self.selected_offset_x = x - item.pos().x()
                    self.selected_offset_y = y - item.pos().y()
                    # self.selected_offset_x = 5  # rect_width/2   # to keep center of rect
                    # self.selected_offset_y = 5  # rect_height/2  # to keep center of rect
        # super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        # print('move:', event.button())
        # print('move:', event.buttons())
        if event.buttons() == Qt.RightButton:  # `buttons()` instead of `button()`
            if self.selected:
                print("moved")
                x = event.scenePos().x()
                y = event.scenePos().y()
                self.selected.setPos(
                    x - self.selected_offset_x, y - self.selected_offset_y
                )
        elif event.buttons() == Qt.LeftButton:
            self.end_point = event.scenePos()
            self.update_path()
        # super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        # print('release:', event.button())
        # print('release:', event.buttons())
        if event.button() == Qt.RightButton:
            if self.selected:
                print("released")
                self.selected.setBrush(QBrush(QColor(255, 255, 255, 255)))
                self.selected = None
        elif event.button() == Qt.LeftButton:
            self.end_point = event.scenePos()

            x = event.scenePos().x()
            y = event.scenePos().y()
            rectitem = QGraphicsRectItem(0, 0, 10, 10)
            rectitem.setPos(x - 5, y - 5)
            rectitem.setPen(QPen(QColor(0, 0, 0), 1.0, Qt.SolidLine))
            rectitem.setBrush(QBrush(QColor(255, 255, 255, 255)))
            self.addItem(rectitem)
            self.update_path()

        # super().mouseReleaseEvent(event)

    def update_path(self):
        if not self.start_point.isNull() and not self.end_point.isNull():
            path = QPainterPath()
            path.moveTo(self.start_point)
            path.lineTo(self.end_point)
            self.path_item.setPath(path)


class GraphicsView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.scene = self.setScene(GraphicsScene())


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(450, 350)
        self.setWindowTitle("Main Window")
        self.setup_main_window()
        self.create_actions()
        self.create_menu()
        self.show()

    def setup_main_window(self):
        """Create and arrange widgets in the main window."""
        self.setCentralWidget(GraphicsView())

    def create_actions(self):
        """Create the application's menu actions."""
        # Create actions for File menu
        self.quit_act = QAction("&Quit")
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.triggered.connect(self.close)

    def create_menu(self):
        """Create the application's menu bar."""
        self.menuBar().setNativeMenuBar(False)
        # Create file menu and add actions
        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(self.quit_act)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())