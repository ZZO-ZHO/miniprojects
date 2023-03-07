# PyQt 복습 - 직접 디자인 코딩

import sys
from PyQt5.QtWidgets import *

class qtApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lblMessage = QLabel('메시지 : ', self)
        self.lblMessage.setGeometry(10, 10, 300, 50)

        btnOK = QPushButton('OK', self)
        btnOK.setGeometry(280, 250, 100, 40)
        btnOK.clicked.connect(self.btnOK_clicked)

        self.setGeometry(300, 200, 400, 300)
        self.setWindowTitle('복습PyQt')
        self.show()
    
    def btnOK_clicked(self):
        self.lblMessage.clear()
        self.lblMessage.setText('메시지 : OK')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    sys.exit(app.exec_())