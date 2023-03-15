# 스레드 사용앱
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *  # Qt.white
import time

MAX = 1000

class BackgroundWorker(QThread):    # PyQt5 스레드르르 위한 클래스 존재
    procChange = pyqtSignal(int)    # 커스텀 시그널(마우그 클릭같이 사용자가 만든것)

    def __init__(self, count = 0, parent = None) -> None:
        super().__init__()
        self.parent = parent
        self.working = True
        self.count = count

    def run(self):  # 스레드를 시작하면 run 실행
        # self.parent.pgbTask.setRange(0,100)
        # for i in range(0, 101):
        #    print(f'스레드 출력 > {i}')
        #    self.parent.pgbTask.setValue(i)
        #    self.parent.txbLog.append(f'스레드 출력 > {i}')
        while self.working:
            if self.count <= MAX:
             self.procChange.emit(self.count)
             self.count += 1
             time.sleep(0.001) # 너무 세밀할경우 GUI 처리를 제대로 하지 못함
            else:
                self.working = False


class qtApp(QWidget):
    def __init__(self):
            super().__init__()
            uic.loadUi('./studyThread/threadApp.ui', self)
            self.setWindowTitle('스레드 앱 v0.4')
            self.pgbTask.setValue(0)

            self.btnStart.clicked.connect(self.btnStartClicked)
            # 스레드 초기화
            self.worker = BackgroundWorker(parent=self,count=0)
            # 백그라운드 워커에 있는 시그널을 접근 슬롯 함수
            self.worker.procChange.connect(self.procUpdated)
            self.pgbTask.setRange(0,100)
    
    # @pyqtSlot(int)
    def procUpdated(self, count):
         self.txbLog.append(f'스레드 출력 > {count}')
         self.pgbTask.setValue(count)
         print(f'스레드 출력 > {count}')

    # @pyqtSlot()    
    def btnStartClicked(self):
        self.worker.start()
        self.worker.working = True
        self.worker.count = 0
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())