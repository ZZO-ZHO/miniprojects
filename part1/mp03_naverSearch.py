# Gt Designer 디자인 사용
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from NaverAPI import *
import webbrowser   # 웹브라우저 모듈

class qtApp(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('./studyPyQt/naverApiSearch.ui', self)
        self.setWindowIcon(QIcon('./studyPyQt/newspaper.png'))
        # 검색 버튼 클릭 시그널 / 슬롯함수
        self.btnSearch.clicked.connect(self.btnSearchClicked) 
        # 텍스트박스 입력후 엔터치면 처리
        self.txtSearch.returnPressed.connect(self.txtSearchReturned)
        self.tblResult.doubleClicked.connect(self.tblResultDoubleClicked)

    def tblResultDoubleClicked(self):
        # row = self.tblResult.currentIndex().row()
        # column = self.tblResult.currentIndex().column()
        # print(row, column)
        selected = self.tblResult.currentRow()
        url = self.tblResult.item(selected, 1).text()
        webbrowser.open(url)

    def txtSearchReturned(self):
        self.btnSearchClicked()

    def btnSearchClicked(self):
        search = self.txtSearch.text()

        if search == '':
            QMessageBox.warning(self, '경고', '검색어를 입력하세요!')  # warning 안하고 about하면 아이콘 안뜸
            return
        else:
            api = NaverApi()  # NaverApi 클래스 객체
            node = 'news'  # movie로 변경하면 영화검색
            outputs = []    # 결과로 담을 변수
            display = 100  # 검색결과 몇개 출력할건지

            result = api.get_naver_search(node, search, 1, display)
            # print(result)
            # 리스트뷰에 출력가능
            items = result['items']
            self.makeTable(items)
    
    # 테이블 위젯에 데이터 표시
    def makeTable(self, items) -> None:
        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection)  # 단일선택만 하도록
        self.tblResult.setColumnCount(2)
        self.tblResult.setRowCount(len(items))  # 현재100개 행 생성
        print(len(items))
        self.tblResult.setHorizontalHeaderLabels(['기사제목', '뉴스링크'])
        self.tblResult.setColumnWidth(0, 310)
        self.tblResult.setColumnWidth(1, 260)
        # 컬럼 데이터 수정금지
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers)

        for i, post in enumerate(items):    # 0, 뉴스
            title =  self.replaceHtmlTag(post['title'])
            originallink = post['originallink']
            # setItem(행, 열, 넣을 데이터)
            self.tblResult.setItem(i, 0, QTableWidgetItem(title))
            self.tblResult.setItem(i, 1, QTableWidgetItem(originallink))

    def replaceHtmlTag(self, sentence) -> str:
        result = sentence.replace('&lt;','<')   # lesser than
        result = result.replace('&gt;','>')     # greater than
        result = result.replace('<b>','')       # bold
        result = result.replace('</b>','') 
        result = result.replace('&apos;',"'")   # apostopy 홑따옴표
        result = result.replace('&quot;','"')    # quotation mark 쌍따옴표
        # 변환안된 특수문자가 나타나면 추가

        result = sentence.replace('&lt;','<').replace('&gt;','>').replace('<b>','').replace('</b>','').replace('&apos;',"'").replace('&quot;','"')

        return result


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())