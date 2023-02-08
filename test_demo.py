from PySide6.QtCore import QThread


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


