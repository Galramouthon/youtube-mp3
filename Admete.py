from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from pytube import YouTube
import sys
import os
import ctypes
import glob

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        label1 = QLabel('유튜브 다운로더', self)
        label1.setAlignment(Qt.AlignVCenter)
        label1.move(100, 40)
 
        self.lbl = QLabel(self)
        self.lbl.move(60, 40)

        self.youtube_url = QLineEdit(self) # 텍스트 
        self.youtube_url.move(20, 100) # 텍스트 위치

        btnRun = QPushButton("OK", self)	# 버튼 텍스트
        btnRun.move(200, 100)	# 버튼 위치
        btnRun.clicked.connect(self.btnRun_clicked)

        self.setWindowTitle('Admete')
        self.setGeometry(800, 400, 300, 200)
        self.show()

    # 버튼 이벤트
    def btnRun_clicked(self):

        # 폴더 생성
        dirs = os.getcwd
        path = './Admete-Downloads'
        # os.mkdir(path)
        os.makedirs(path, exist_ok=True)

        # mp4 다운
        # YouTube(self.youtube_url.text()).streams.first().download('./Admete-Downloads')

        # mp3 다운
        YouTube(self.youtube_url.text()).streams.filter(only_audio=True).first().download('./Admete-Downloads')
        # webbrowser.open(self.youtube_url.text())

        # mp4에서 mp3변환 
        files = glob.glob('./Admete-Downloads/*.mp4')
        for x in files:
            if not os.path.isdir(x):
                filename = os.path.splitext(x)
                try:
                    os.rename(x,filename[0] + '.mp3')
                except:
                    pass

        guidance = QMessageBox.question(self, 'Admete', '다운로드 완료! \nAdmete-Downloads로 저장했습니다', QMessageBox.Cancel)
  
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '종료', '창을 닫으시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
