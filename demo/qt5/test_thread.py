# PyQt5 Video Recorder
from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread
import imutils
import cv2, time
import sys
import time
import os
from datetime import datetime
import multiprocessing

class VideoStreamWidget(object):
    def __init__(self, cam_link,index):
        self.folder = f"CAM_{index}"
        self.cam_link = cam_link
        self.path = os.path.expanduser(f'~\\Documents\\{self.folder}')
        print(self.path)
        self.date_now = datetime.now().strftime('%Y%m%d')
        self.output_dir = os.path.join(self.path, 'rtsp_saved', self.date_now)
        os.makedirs(self.output_dir, exist_ok=True)
        self.date_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.output_fpath = os.path.join(self.output_dir, 'saved_{}.avi'.format(self.date_time))
        print(self.output_fpath)
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID') 
        self.out = cv2.VideoWriter(self.output_fpath, self.fourcc, 30, (640,480))
        self.capture = cv2.VideoCapture(self.cam_link)
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()
        
    def update(self):
        # Read the next frame from the stream in a different thread
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()
                self.out.write(self.frame)

    def stop(self):
        try:
        	self.thread.stop()
        	self.out.release()
	        self.capture.release()
	        cv2.destroyAllWindows()
	        print("Stopped")
	        exit(1)
        except:
	            pass

def run(cam_url,cam_index):
    video_stream_widget = VideoStreamWidget(int(cam_url),cam_index)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(600, 100)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_start1 = QtWidgets.QPushButton(Form)
        self.btn_start1.setObjectName("btn_start1")
        self.gridLayout.addWidget(self.btn_start1, 0, 0, 1, 1)
        self.btn_stop1 = QtWidgets.QPushButton(Form)
        self.btn_stop1.setObjectName("btn_stop1")
        self.gridLayout.addWidget(self.btn_stop1, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel("Developed By Sihab Sahariar")
        self.gridLayout.addWidget(self.label, 1, 0)
        self.btn_start1.clicked.connect(self.play1)
        self.btn_stop1.clicked.connect(self.stop1)       
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle("PyQt5 RTSP Recorder Using Multiprocessing")
        self.btn_start1.setText(_translate("Form", "Start Recording"))
        self.btn_stop1.setText(_translate("Form", "Stop Recording"))

    def play1(self):
    	self.proc = multiprocessing.Process(target=run, args=('0','TEST')) #rtsp link(rtsp://user:password@ip:port/ or webcam index)
    	self.proc.start()

    def stop1(self):
    	self.proc.terminate()
    	self.proc.join()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())