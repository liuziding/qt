import sys
from PySide6.QtWidgets import (QApplication,QPushButton,QVBoxLayout, QLabel,
                      QHBoxLayout,QFileDialog,QWidget,QSlider, QScrollArea,
                      QListWidget, QListWidgetItem, QMainWindow, QMenuBar)
from PySide6.QtCore import QUrl, Qt, QSize
from PySide6.QtGui import QAction
from PySide6.QtMultimedia import QMediaPlayer,QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget

class MyVideoWidget(QVideoWidget): #建立QVideoWidget的子类，重新keyPressEvent()事件
    def __init__(self,parent=None):
        super().__init__(parent)
    def keyPressEvent(self,event):  #全屏后按Esc键回到原状态
        if event.key() == Qt.Key_Escape and self.isFullScreen():
            self.setFullScreen(False)
    def mouseDoubleClickEvent(self,event): #双击全屏显示
        if not self.isFullScreen():
            self.setFullScreen(True)
        else:
            self.setFullScreen(False)

class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1200, 760)
        self.setupUi()

    def setupUi(self): # 界面
        """建立主程序界面"""
        menubar = self.menuBar()

        self.language_type = "en" # 语言类型

        self.file_menu = menubar.addMenu("文件") # 一级菜单

        self.dir_setting_action = QAction("目录设置", self) # 子菜单
        self.dir_setting_action.triggered.connect(self.dir_setting_clicked) # 信号与槽
        self.file_menu.addAction(self.dir_setting_action) # 将子菜单添加进一级菜单

        self.data_setting_action = QAction("数据库配置", self) # 子菜单
        self.data_setting_action.triggered.connect(self.data_setting_clicked)
        self.file_menu.addAction(self.data_setting_action)

        self.video_setting_action = QAction("视频配置", self) #子菜单
        self.video_setting_action.triggered.connect(self.video_setting_clicked)
        self.file_menu.addAction(self.video_setting_action)

        self.detect_model_setting_action = QAction("检测模型配置", self) # 子菜单
        self.detect_model_setting_action.triggered.connect(self.detect_model_setting_clicked)
        self.file_menu.addAction(self.detect_model_setting_action)

        self.tracking_model_setting_action = QAction("跟踪模型配置", self) # 子菜单
        self.tracking_model_setting_action.triggered.connect(self.tracking_model_setting_clicked)
        self.file_menu.addAction(self.tracking_model_setting_action)

        self.about_menu = menubar.addMenu("关于我们") # 一级菜单

        self.cn_change_action = QAction("中文", self) # 子菜单
        self.cn_change_action.triggered.connect(self.switch_language_clicked)
        self.about_menu.addAction(self.cn_change_action)

        self.en_change_action = QAction("英文", self) # 子菜单
        self.en_change_action.triggered.connect(self.switch_language_clicked)
        self.about_menu.addAction(self.en_change_action)

        self.list_widget = QListWidget()
        self.list_widget.resize(200, 710)

        for i in range(100):
            item = QListWidgetItem(f"video{i+1}")
            item.setToolTip(f"{i}. Item woshizhongguoren woshizhongguoen")
            item.setSizeHint(QSize(0, 40))

            self.list_widget.addItem(item)

        # 将列表控件添加到滚动区域
        scroll_area = QScrollArea()
        scroll_area.setFixedSize(200, 730)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) # 关闭垂直滚动条
        scroll_area.setWidget(self.list_widget)

        self.videoWidget = MyVideoWidget() # 显示视频的控件
        self.audioOutput = QAudioOutput() # 播放音频设备
        self.audioOutput.setVolume(0.5) # 控制音量
        self.btn_open = QPushButton("打开媒体文件") # 打开音频或视频按钮
        self.btn_play_stop = QPushButton("播放/暂停") # 播放/停止按钮
        self.btn_play_stop.setEnabled(False)
        self.btn_pause_continue = QPushButton("暂停/继续") # 暂停/继续按钮
        self.btn_pause_continue.setEnabled(False)
        self.btn_mute = QPushButton("静音") # 静音按钮
        self.btn_fullScreen = QPushButton("全屏")
        self.progress_slider = QSlider(Qt.Horizontal) # 播放进度滑块
        self.progress_slider.setSingleStep(1)

        self.volume_slider = QSlider(Qt.Horizontal) # 音量控制滑块
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(50)
        self.volume_slider.setTickInterval(5)
        self.volume_slider.setTickPosition(QSlider.TicksAbove)
        self.playback_rate_slider = QSlider(Qt.Horizontal) # 播放速率控制滑块
        self.playback_rate_slider.setRange(-100, 100)
        self.playback_rate_slider.setValue(20)
        self.playback_rate_slider.setTickInterval(5)
        self.playback_rate_slider.setTickPosition(QSlider.TicksAbove)

        action_layout = QHBoxLayout() # 按钮水平布局
        action_layout.addWidget(self.btn_open)
        action_layout.addWidget(self.btn_play_stop)
        action_layout.addWidget(self.btn_pause_continue)
        action_layout.addWidget(self.btn_mute)
        action_layout.addWidget(self.btn_fullScreen)
        action_layout.addWidget(self.volume_slider)
        action_layout.addWidget(self.playback_rate_slider)

        right_layout = QVBoxLayout(self) # 垂直布局
        right_layout.setContentsMargins(12, 4, 10, 0)
        right_layout.addWidget(self.videoWidget)
        right_layout.addWidget(self.progress_slider)
        right_layout.addLayout(action_layout)

        
        self.player = QMediaPlayer(self) # 音频和视频播放器
        self.player.setVideoOutput(self.videoWidget) # 设置播放器的视频输出控件
        self.player.setAudioOutput(self.audioOutput) # 设置播放器的音频输出设备
        self.player.hasAudioChanged.connect(self.has_audio_video_changed) # 信号连接
        self.player.hasVideoChanged.connect(self.has_audio_video_changed) # 信号连接
        self.btn_open.clicked.connect(self.btn_open_clicked) # 信号与槽函数
        self.btn_play_stop.clicked.connect(self.btn_play_stop_clicked) # 信号与槽连接
        self.btn_pause_continue.clicked.connect(self.btn_pause_continue_clicked)
        self.btn_mute.clicked.connect(self.btn_mute_clicked) # 信号与槽函数
        self.btn_fullScreen.clicked.connect(self.btn_fullScreen_clicked) # 信号与槽函数
        self.progress_slider.actionTriggered.connect(self.player_setPosition) # 信号与槽函数
        self.player.durationChanged.connect(self.player_duration_changed) # 信号与槽函数
        self.volume_slider.valueChanged.connect(self.player_setVolume) # 信号与槽函数
        self.playback_rate_slider.valueChanged.connect(self.play_setPlayRate) # 信号连接
        self.player.positionChanged.connect(self.progress_slider.setValue) # 信号与槽函数

        # 将左右控件添加到主窗口中
        main_widget = QWidget()
        main_layout = QHBoxLayout(main_widget)
        main_layout.addWidget(scroll_area)
        main_layout.addLayout(right_layout)

        # 将主窗口设置为应用程序的主窗口
        self.setCentralWidget(main_widget)

        self.list_widget.itemClicked.connect(self.on_item_clicked)

    def dir_setting_clicked(self): # 点击目录配置菜单按钮
        print("点击了目录配置菜单按钮")

    def data_setting_clicked(self): # 点击数据库配置菜单按钮
        print("点击数据库配置菜单按钮")

    def video_setting_clicked(self): # 点击视频配置菜单按钮
        print("点击视频配置菜单按钮")

    def detect_model_setting_clicked(self): # 点击检测模型配置菜单按钮
        print("点击检测模型配置菜单按钮")

    def tracking_model_setting_clicked(self): # 点击跟踪模型配置菜单按钮
        print("点击检测模型配置菜单按钮")

    def switch_language_clicked(self): # 切换中英文菜单栏
        sender = self.sender()

        if sender == self.cn_change_action:
            # 切换为中文
            self.file_menu.setTitle("文件")
            self.dir_setting_action.setText("目录设置")
            self.data_setting_action.setText("数据库配置")
            self.video_setting_action.setText("视频配置")
            self.detect_model_setting_action.setText("检测模型配置")
            self.tracking_model_setting_action.setText("跟踪模型配置")
            self.about_menu.setTitle("关于我们")
            self.cn_change_action.setText("中文")
            self.en_change_action.setText("英文")
        else:
            # 切换为英文
            self.file_menu.setTitle("Files")
            self.dir_setting_action.setText("dirSetting")
            self.data_setting_action.setText("dataSetting")
            self.video_setting_action.setText("videoSetting")
            self.detect_model_setting_action.setText("detectModelSetting")
            self.tracking_model_setting_action.setText("trackingModelSetting")
            self.about_menu.setTitle("About us")
            self.cn_change_action.setText("chinese")
            self.en_change_action.setText("english")
    
    def has_audio_video_changed(self, has): # 有音频和视频时的槽函数
        if has:
            self.btn_play_stop.setEnabled(True)
            self.btn_play_stop.setText("播放")
        else:
            self.btn_play_stop.setEnabled(False)
            self.btn_play_stop.setText("播放/暂停")

    def btn_open_clicked(self):
        fileName, fil = QFileDialog.getOpenFileName(self, caption="选择影音文件", dir="d:\\",
        filter="影音文件(*.wav *.mp4 *.wma *.avi *.wmv *.rm *.asf);;所有文件(*.*)")
        if fileName:
            url = QUrl.fromLocalFile(fileName)
            self.player.setSource(url) # 设置播放器的播放内容
            self.progress_slider.setValue(0)
            self.playback_rate_slider.setValue(20)
            self.player.play()

    def btn_play_stop_clicked(self):
        print(self.btn_play_stop.text())

        if self.btn_play_stop.text() == "播放":
            self.player.play()
            self.btn_play_stop.setText("暂停")
            self.btn_pause_continue.setEnabled(True)
            self.btn_pause_continue.setText("暂停")
        elif self.btn_play_stop.text() == "暂停":
            self.player.stop()
            self.btn_play_stop.setText("播放")
            self.btn_pause_continue.setEnabled(False)
            self.btn_pause_continue.setText("暂停/继续")
        self.progress_slider.setValue(0)
        self.playback_rate_slider.setValue(20)
    
    def btn_pause_continue_clicked(self): # 暂停/继续按钮的槽函数
        if self.btn_pause_continue.text() == "暂停":
            self.player.pause()
            self.btn_pause_continue.setText("继续")
        elif self.btn_pause_continue.text() == "继续":
            self.player.play()
            self.btn_pause_continue.setText("暂停")

    def btn_mute_clicked(self): # 静音按钮的槽函数
        muted = self.audioOutput.isMuted()
        self.audioOutput.setMuted(not muted)
        if self.audioOutput.isMuted():
            self.btn_mute.setText("放音")
        else:
            self.btn_mute.setText("静音")

    def btn_fullScreen_clicked(self): # 全屏展示
        self.videoWidget.setFullScreen(True)

    def player_setPosition(self, action):
        self.player.setPosition(self.progress_slider.value())

    def player_duration_changed(self, duration): # 播放器放时长的槽函数
        self.progress_slider.setRange(0, duration)

    def player_setVolume(self, value): # 音量滑块的槽函数
        self.audioOutput.setVolume(value / 100)

    def play_setPlayRate(self): # 播放速率滑块的槽函数
        if self.player.hasVideo():
            self.player.setPlaybackRate(self.playback_rate_slider.value() / 20)

    def on_item_clicked(self, item: QListWidgetItem):
        # 获取项目所在的列
        column = self.list_widget.row(item)
        fileName = "{}{}{}".format("/Users/fengye/Downloads/video", column, ".mp4")
        url = QUrl.fromLocalFile(fileName)
        self.player.setSource(url) # 设置播放器的播放内容
        self.progress_slider.setValue(0)
        self.playback_rate_slider.setValue(20)
        self.player.play()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = VideoPlayer()
    window.setWindowTitle("视频播放")
    window.show()

    sys.exit(app.exec())