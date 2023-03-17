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
        uic.loadUi('./test/busstop2.ui', self)
        self.setWindowIcon(QIcon('./test/busstop.png'))
        self.setWindowTitle('BusStop v0.1')
        self.date = QDate.currentDate()
        self.datetime = QDateTime.currentDateTime()
        self.initDB()

        # 버튼시그널
        self.busPlus.clicked.connect(self.busPlusClicked)
        self.busMinus.clicked.connect(self.busMinusClicked)
        self.btnBus1.clicked.connect(self.btnBus1Clicked)
        self.btnBus2.clicked.connect(self.btnBus2Clicked)
        self.btnBus3.clicked.connect(self.btnBus3Clicked)

    def btnBus1Clicked(self):
        if self.btnBus1.isChecked():
            if self.busPlus.isChecked():
                self.busPlusClicked()

            elif self.busMinus.isChecked():
                self.busMinusClicked()

    def btnBus2Clicked(self):
        if self.btnBus2.isChecked():
            if self.busPlus.isChecked():
                self.busPlusClicked()

            elif self.busMinus.isChecked():
                self.busMinusClicked()

    def btnBus3Clicked(self):
        if self.btnBus3.isChecked():
            if self.busPlus.isChecked():
                self.busPlusClicked()

            elif self.busMinus.isChecked():
                self.busMinusClicked()
    
    def busPlusClicked(self):
        if self.btnBus1.isChecked():
            self.count1 += 1 
            self.setting1()

        elif self.btnBus2.isChecked():
            self.count2 += 1 
            self.setting2()

        elif self.btnBus3.isChecked():
            self.count3 += 1 
            self.setting3()

    def busMinusClicked(self):
        if self.btnBus1.isChecked():
            if self.count1 == 0:
                pass
            else:
                self.count1 -= 1 
                self.setting1()

        elif self.btnBus2.isChecked():
            if self.count2 == 0:
                pass
            else:
                self.count2 -= 1 
                self.setting2()

        elif self.btnBus3.isChecked():
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())