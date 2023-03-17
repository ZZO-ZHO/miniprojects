import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pymysql

btn_true = 'background-color:rgb(100,100,255);font: 9pt "나눔고딕";'
btn_false = 'background-color:rgb(255,255,255);font: 9pt "나눔고딕";'

class qtApp(QMainWindow):
    conn = None

    def __init__(self):
        super().__init__()
        uic.loadUi('C:/Source/zzo/busstop_modify.ui', self)
        self.setWindowIcon(QIcon('busstopimage.png'))
        self.setWindowTitle('BusStop v0.1')
        self.date = QDate.currentDate()
        self.datetime = QDateTime.currentDateTime()
        self.initDB()
        # 해당 버스 클릭 확인위함
        self.flag1,self.flag2,self.flag3=0,0,0
        #self.font=QFont('나눔고딕',9)
        
        # 버튼시그널
        self.busPlus.clicked.connect(self.busPlusClicked)
        self.busMinus.clicked.connect(self.busMinusClicked)
        self.btnBus1.clicked.connect(self.btnBus1Clicked)
        self.btnBus2.clicked.connect(self.btnBus2Clicked)
        self.btnBus3.clicked.connect(self.btnBus3Clicked)
        
        # 버튼 활성화 / 비활성화 
        # self.btnBus1.released.connect(self.btnBusRelease)
        # self.btnBus2.released.connect(self.btnBusRelease)
        # self.btnBus3.released.connect(self.btnBusRelease)

        #버스 미선택 시 탑승 대기 / 취소 버튼 비활성화
        self.busPlus.setEnabled(False)
        self.busMinus.setEnabled(False)
        

    # 버튼 활성화 / 비활성화
    # def btnBusRelease(self):
    #     self.btnBus1.setEnabled(True)
    #     self.btnBus2.setEnabled(True)
    #     self.btnBus3.setEnabled(True)

    def countbtn(self, state):
        if state == True:
            self.busPlus.setEnabled(True)
            self.busMinus.setEnabled(True)
        elif state == False:    
            self.busPlus.setEnabled(False)
            self.busMinus.setEnabled(False)

    # 버튼 1 클릭시에
    def btnBus1Clicked(self):
        if self.flag1==0:
            self.btnBus1.setStyleSheet(f'{btn_true}') # 배경색 변경
            self.btnBus2.setStyleSheet(f'{btn_false}')
            self.btnBus3.setStyleSheet(f'{btn_false}')
            self.countbtn(True)
            #self.btnBus1.setFont(self.font)
            self.flag1=1
            self.flag2=0
            self.flag3=0

            # self.btnBus2.setEnabled(False)
            # self.btnBus3.setEnabled(False)

            if self.busPlus.isChecked():
                self.busPlusClicked()
            elif self.busMinus.isChecked():
                self.busMinusClicked()
        
        elif self.flag1==1:
            self.btnBus1.setStyleSheet(f'{btn_false}')
            self.countbtn(False)
            self.flag1=0
            

    def btnBus2Clicked(self):
        if self.flag2==0:
            self.btnBus1.setStyleSheet(f'{btn_false}')
            self.btnBus2.setStyleSheet(f'{btn_true}')
            self.btnBus3.setStyleSheet(f'{btn_false}')
            self.countbtn(True)
            
            #self.btnBus2.setFont(self.font)
            self.flag1=0
            self.flag2=1
            self.flag3=0

            # self.btnBus1.setEnabled(False)
            # self.btnBus3.setEnabled(False)

            if self.busPlus.isChecked():
                self.busPlusClicked()
            elif self.busMinus.isChecked():
                self.busMinusClicked()

        elif self.flag2==1:
            self.btnBus2.setStyleSheet(f'{btn_false}')
            self.countbtn(False)
            self.flag2=0


    def btnBus3Clicked(self):
        if self.flag3==0:
            self.btnBus1.setStyleSheet(f'{btn_false}')
            self.btnBus2.setStyleSheet(f'{btn_false}')
            self.btnBus3.setStyleSheet(f'{btn_true}')
            self.countbtn(True)
            #self.btnBus3.setFont(self.font)
            self.flag1=0
            self.flag2=0
            self.flag3=1

            # self.btnBus2.setEnabled(False)
            # self.btnBus1.setEnabled(False)

            if self.busPlus.isChecked():
                self.busPlusClicked()
            elif self.busMinus.isChecked():
                self.busMinusClicked()

        elif self.flag3==1:
            self.btnBus3.setStyleSheet(f'{btn_false}')
            self.countbtn(False)
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
        self.conn = pymysql.connect(host='210.119.12.69', user='root', password='12345', db='bus', charset='utf8')  # 210.119.12.69
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
        
        
        self.flag1=0
        self.btnBus1.setStyleSheet(f'{btn_false}')
        self.busPlus.setEnabled(False)
        self.busMinus.setEnabled(False)
        #self.btnBusRelease()

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
    
        self.flag2=0
        self.btnBus2.setStyleSheet(f'{btn_false}')
        self.busPlus.setEnabled(False)
        self.busMinus.setEnabled(False)
        

        #self.btnBusRelease()

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

        self.flag3=0
        self.btnBus3.setStyleSheet(f'{btn_false}')
        self.busPlus.setEnabled(False)
        self.busMinus.setEnabled(False)

        #self.btnBusRelease()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())