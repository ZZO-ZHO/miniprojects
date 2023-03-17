import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pymysql


class qtApp(QMainWindow):
    conn = None
    def __init__(self):
        super().__init__()
        uic.loadUi('C:/Source/zzo/busstop_modify.ui', self)
        # self.setWindowIcon(QIcon('bustopimage.png'))
        self.setWindowTitle('BusStop v0.1')
        self.date = QDate.currentDate()
        self.datetime = QDateTime.currentDateTime()
        self.initDB()
        # 해당 버스 클릭 확인위함
        self.flag1,self.flag2,self.flag3=0,0,0
        
        #클릭 시 배경 버튼 색 변경하기 위함
        self.buttonclick='background-color:rgb(100,100,255);font: 9pt "나눔고딕";' #클릭
        self.buttonrelease='background-color:rgb(255,255,255);font: 9pt "나눔고딕";' #해제

        self.timer = QTimer(self)
        self.timer.start(1)
        self.timer.timeout.connect(self.initDB)
        
        # 버튼시그널
        self.busPlus.clicked.connect(self.busPlusClicked)
        self.busMinus.clicked.connect(self.busMinusClicked)
        self.btnBus1.clicked.connect(self.btnBus1Clicked)
        self.btnBus2.clicked.connect(self.btnBus2Clicked)
        self.btnBus3.clicked.connect(self.btnBus3Clicked)
        
        #초기화면 버스선택 x --> released로 클릭 불가능하게 설정
        self.btnreleased()


    # 탈 버스가 선택된 경우 탑승 대기/취소 버튼 클릭 가능하게
    def btnclicked(self):
        self.busPlus.setEnabled(True)
        self.busMinus.setEnabled(True)

    # 탈 버스가 선택된 경우 탑승 대기/취소 버튼 클릭 불가능하게
    def btnreleased(self):
        self.busPlus.setEnabled(False)
        self.busMinus.setEnabled(False)


    def btnBus1Clicked(self):
        if self.flag1==0:
            self.btnBus1.setStyleSheet(f'{self.buttonclick}') # 배경색 변경
            self.btnBus2.setStyleSheet(f'{self.buttonrelease}')
            self.btnBus3.setStyleSheet(f'{self.buttonrelease}')
            
            #탑승 대기 / 취소 버튼 활성화
            self.btnclicked()

            self.flag1=1
            self.flag2=0
            self.flag3=0

            #대기 클릭 시 busPlusClicked 함수를 , 취소 클릭 시 busMinusCliced 함수를 실행
            if self.busPlus.isChecked():
                self.busPlusClicked()
            elif self.busMinus.isChecked():
                self.busMinusClicked()
        
        elif self.flag1==1:
            self.btnBus1.setStyleSheet(f'{self.buttonrelease}')
            self.btnreleased() 
            self.flag1=0
            

    def btnBus2Clicked(self):
        if self.flag2==0:
            self.btnBus1.setStyleSheet(f'{self.buttonrelease}')
            self.btnBus2.setStyleSheet(f'{self.buttonclick}')
            self.btnBus3.setStyleSheet(f'{self.buttonrelease}')
            #탑승 대기 / 취소 버튼 활성화
            self.btnclicked()
            
            self.flag1=0
            self.flag2=1
            self.flag3=0

            if self.busPlus.isChecked():
                self.busPlusClicked()
            elif self.busMinus.isChecked():
                self.busMinusClicked()

        elif self.flag2==1:
            self.btnBus2.setStyleSheet(f'{self.buttonrelease}')
            # 버튼 비활성화
            self.btnreleased()
            self.flag2=0


    def btnBus3Clicked(self):
        if self.flag3==0:
            self.btnBus1.setStyleSheet(f'{self.buttonrelease}')
            self.btnBus2.setStyleSheet(f'{self.buttonrelease}')
            self.btnBus3.setStyleSheet(f'{self.buttonclick}')
            self.btnclicked()

            self.flag1=0
            self.flag2=0
            self.flag3=1

            if self.busPlus.isChecked():
                self.busPlusClicked()
            elif self.busMinus.isChecked():
                self.busMinusClicked()

        elif self.flag3==1:
            self.btnBus3.setStyleSheet(f'{self.buttonrelease}')
            self.btnreleased()
            self.flag3=0

    
    def busPlusClicked(self):
        if self.flag1==1:
            self.count1 += 1 
            self.setting1()

        elif self.flag2==1:
            self.count2 += 1 
            self.setting2()

        elif self.flag3==1:
            self.count3 += 1 
            self.setting3()

    def busMinusClicked(self):
        if self.flag1==1:
            if self.count1 == 0:
                pass
            else:
                self.count1 -= 1 
                self.setting1()

        elif self.flag2==1:
            if self.count2 == 0:
                pass
            else:
                self.count2 -= 1 
                self.setting2()

        elif self.flag3==1:
            if self.count3 == 0:
                pass
            else:
                self.count3 -= 1 
                self.setting3()
            
    def initDB(self):
        self.conn = pymysql.connect(host='210.119.12.69', user='root', password='12345', db='bus', charset='utf8')
        cur = self.conn.cursor()
        query='''
        SELECT bus_cnt
          FROM bus_table
         WHERE bus_num = %s
              '''



        self.statusBar().showMessage(self.datetime.toString(Qt.DefaultLocaleLongDate))
        cur.execute(query,('10'))
        data=cur.fetchone()
        self.count1 = int(data[0])
        self.bus1Cnt.setText(str(data[0]))
      

        cur.execute(query,('100-1'))
        data=cur.fetchone()
        self.count2 = int(data[0])
        self.bus2Cnt.setText(str(data[0]))

        cur.execute(query,('155'))
        data=cur.fetchone()
        self.count3 = int(data[0])
        self.bus3Cnt.setText(str(data[0]))


    def setting1(self):
        self.conn = pymysql.connect(host='210.119.12.69', user='root', password='12345', db='bus', charset='utf8')
        cur = self.conn.cursor()
        query = '''UPDATE bus_table
                      SET bus_cnt = %s
                    WHERE bus_num = %s '''
        
        self.bus1Cnt.setText(str(self.count1))
        cur.execute(query, (self.count1, '10'))
        self.conn.commit()
        self.conn.close()
        
        #1번 버스 탑승 대기 / 취소 버튼 클릭 이후 flag,stylesheet 복구 및 버튼 비활성화
        self.flag1=0
        self.btnBus1.setStyleSheet(f'{self.buttonrelease}')
        self.btnreleased()


    def setting2(self):
        self.conn = pymysql.connect(host='210.119.12.69', user='root', password='12345', db='bus', charset='utf8')
        cur = self.conn.cursor()
        query = '''UPDATE bus_table
                      SET bus_cnt = %s
                    WHERE bus_num = %s '''
        

        self.bus2Cnt.setText(str(self.count2))
        cur.execute(query, (self.count2, '100-1'))
        self.conn.commit()
        self.conn.close()
    
        #2번 버스 탑승 대기 / 취소 버튼 클릭 이후 flag,stylesheet 복구 및 버튼 비활성화
        self.flag2=0
        self.btnBus2.setStyleSheet(f'{self.buttonrelease}')
        self.btnreleased()

    def setting3(self):
        self.conn = pymysql.connect(host='210.119.12.69', user='root', password='12345', db='bus', charset='utf8')
        cur = self.conn.cursor()
        query = '''UPDATE bus_table
                      SET bus_cnt = %s
                    WHERE bus_num = %s '''

        self.bus3Cnt.setText(str(self.count3))
        cur.execute(query, (self.count3, '155'))
        self.conn.commit()
        self.conn.close()

        #3번 버스 탑승 대기 / 취소 버튼 클릭 이후 flag,stylesheet 복구 및 버튼 비활성화
        self.flag3=0
        self.btnBus3.setStyleSheet(f'{self.buttonrelease}')
        self.btnreleased()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())