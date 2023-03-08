# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Source\miniprojects\part1\studyPyQt\naverApiMovie.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(640, 400))
        Form.setMaximumSize(QtCore.QSize(640, 400))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        Form.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 621, 61))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.searchLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.searchLayout.setContentsMargins(0, 0, 0, 0)
        self.searchLayout.setObjectName("searchLayout")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.splitter = QtWidgets.QSplitter(self.groupBox)
        self.splitter.setGeometry(QtCore.QRect(10, 20, 601, 23))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.txtSearch = QtWidgets.QLineEdit(self.splitter)
        self.txtSearch.setObjectName("txtSearch")
        self.btnSearch = QtWidgets.QPushButton(self.splitter)
        self.btnSearch.setMaximumSize(QtCore.QSize(90, 16777215))
        self.btnSearch.setObjectName("btnSearch")
        self.searchLayout.addWidget(self.groupBox)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 80, 621, 311))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.resultLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.resultLayout.setContentsMargins(0, 0, 0, 0)
        self.resultLayout.setObjectName("resultLayout")
        self.tblResult = QtWidgets.QTableWidget(self.verticalLayoutWidget_2)
        self.tblResult.setObjectName("tblResult")
        self.tblResult.setColumnCount(0)
        self.tblResult.setRowCount(0)
        self.resultLayout.addWidget(self.tblResult)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "네이버 API 뉴스검색 앱"))
        self.groupBox.setTitle(_translate("Form", "뉴스 검색"))
        self.label.setText(_translate("Form", "검색어"))
        self.btnSearch.setText(_translate("Form", "검색"))
