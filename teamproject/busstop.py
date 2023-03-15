import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pymysql


class qtApp(QMainWindow):
    conn = None

    # count2 = 0

    def __init__(self):
        super().__init__()
        uic.loadUi('C:/Source/zzo/busstop.ui', self)
        # self.setWindowIcon(QIcon('./studyPyQt/addressbook.png'))          아이콘
        # self.setWindowTitle('BuSTOP v0.1')
        self.initDB()

    #     # 버튼시그널
        self.bus1Plus.clicked.connect(self.bus1PlusClicked)
        self.bus1Minus.clicked.connect(self.bus1MinusClicked)
        self.bus2Plus.clicked.connect(self.bus2PlusClicked)
        self.bus2Minus.clicked.connect(self.bus2MinusClicked)
        self.bus3Plus.clicked.connect(self.bus3PlusClicked)
        self.bus3Minus.clicked.connect(self.bus3MinusClicked)
        
    def bus1PlusClicked(self):
        self.count1 += 1 
        self.setting()

    def bus2PlusClicked(self):
        self.count2 += 1 
        self.setting()

    def bus3PlusClicked(self):
        self.count3 += 1 
        self.setting()

    def bus1MinusClicked(self):
        if self.count1 == 0:
            pass
        else:
            self.count1 -= 1 
            self.setting()

    def bus2MinusClicked(self):
        if self.count2 == 0:
            pass
        else:
            self.count2 -= 1 
            self.setting()
    
    def bus3MinusClicked(self):
        if self.count3 == 0:
            pass
        else:
            self.count3 -= 1 
            self.setting()   

    def initDB(self):
        self.conn = pymysql.connect(host='210.119.12.69', user='root', password='12345', db='bus', charset='utf8')
        cur = self.conn.cursor()
        query='''
        SELECT bus_cnt
          FROM bus_table
         WHERE bus_num = %s
        '''
        cur.execute(query,('100-1'))
        data=cur.fetchone()
        self.count1 = int(data[0])
        self.bus1Cnt.setText(str(data[0]))

        cur.execute(query,('155'))
        data=cur.fetchone()
        self.count2 = int(data[0])
        self.bus2Cnt.setText(str(data[0]))

        cur.execute(query,('10'))
        data=cur.fetchone()
        self.count3 = int(data[0])
        self.bus3Cnt.setText(str(data[0]))



    def setting(self):
        self.conn = pymysql.connect(host='210.119.12.69', user='root', password='12345', db='bus', charset='utf8')
        cur = self.conn.cursor()
        query = '''UPDATE bus_table
                      SET bus_cnt = %s
                    WHERE bus_num = %s '''
        
        self.bus1Cnt.setText(str(self.count1))
        self.bus2Cnt.setText(str(self.count2))
        self.bus3Cnt.setText(str(self.count3))
        cur.execute(query, (self.count1, '100-1'))
        cur.execute(query, (self.count2, '155'))
        cur.execute(query, (self.count3, '10'))

        self.conn.commit()
        self.conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())