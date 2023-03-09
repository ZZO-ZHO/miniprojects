# Gt Designer 디자인 사용
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from NaverAPI import *
from urllib.request import urlopen
import webbrowser   # 웹브라우저 모듈

class qtApp(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('./studyPyQt/naverApiMovie.ui', self)
        self.setWindowIcon(QIcon('./studyPyQt/movie.png'))
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
        url = self.tblResult.item(selected, 5).text()
        webbrowser.open(url)

    def txtSearchReturned(self):
        self.btnSearchClicked()

    def btnSearchClicked(self):
        search = self.txtSearch.text()

        if search == '':
            QMessageBox.warning(self, '경고', '영화이름을 입력하세요!')  # warning 안하고 about하면 아이콘 안뜸
            return
        else:
            api = NaverApi()  # NaverApi 클래스 객체
            node = 'movie'  # movie로 변경하면 영화검색
            display = 100  # 검색결과 몇개 출력할건지

            result = api.get_naver_search(node, search, 1, display)
            #print(result)
            # 리스트뷰에 출력가능
            items = result['items']
            # print(len(items))
            self.makeTable(items)
    
    # 테이블 위젯에 데이터 표시
    def makeTable(self, items) -> None:
        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection)  # 단일선택만 하도록
        self.tblResult.setColumnCount(7)
        self.tblResult.setRowCount(len(items))  # 현재100개 행 생성
        self.tblResult.setHorizontalHeaderLabels(['영화제목', '개봉년도', '감독', '출연진', '평점', '링크', '포스터'])
        self.tblResult.setColumnWidth(0, 150)
        self.tblResult.setColumnWidth(1, 70)
        self.tblResult.setColumnWidth(4, 50)
        # 컬럼 데이터 수정금지
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers)    # 컬럼수정금지
        
        for i, post in enumerate(items):    # 0, 영화
            title =  self.replaceHtmlTag(post['title'])
            subtitle = post['subtitle']
            title = f'{title} ({subtitle})'
            pubDate = post['pubDate']
            director = post['director'].replace('|',',')[:-1]
            actor = post['actor'].replace('|',',')[:-1]
            userRating = post['userRating']
            link = post['link']
            img_url = post['image']

            # 포스터 이미지 추가
            if img_url != '':
                data = urlopen(img_url).read()  # 2진 데이터 - 네이버 영화에있는 이미지 다운, 덱스트형태의 데이터
                image = QImage()
                image.loadFromData(data)
                # QTableWidget 이미지를 그냥 넣을수없음 QLabel() 집어넣은뒤 QLabel -> QlabelWideget
                imgLable = QLabel()
                imgLable.setPixmap(QPixmap(image))

                # data를 이미지로 저장가능!
                # f = open(f'./studyPyQt/temp/image_{i+1}.png', mode='wb')
                # f.write(data)
                # f.close()

            # image = QImage(Request.get(post['image'], stream = True))
            # imgData = urlopen(post['image']).read()
            # image = QPixmap()
            # if imgData != None:
            #     image.loadFromData(imgData)
            #     imgLabel = QLabel()
            #     imgLabel.setPixmap(QPixmap.fromImage(image))
            #     imgLabel.setGeometry(0,0,60,100)
            #     imgLabel.resize(60, 100)
            # setItem(행, 열, 넣을 데이터)
            self.tblResult.setItem(i, 0, QTableWidgetItem(title))
            self.tblResult.setItem(i, 1, QTableWidgetItem(pubDate))
            self.tblResult.setItem(i, 2, QTableWidgetItem(director))
            self.tblResult.setItem(i, 3, QTableWidgetItem(actor))
            self.tblResult.setItem(i, 4, QTableWidgetItem(userRating))
            self.tblResult.setItem(i, 5, QTableWidgetItem(link))
            self.tblResult.setItem(i, 6, QTableWidgetItem(img_url))

            if img_url != '':
                self.tblResult.setCellWidget(i,6,imgLable)
                self.tblResult.setRowHeight(i,110)
            else:
                self.tblResult.setItem(i, 6, QTableWidgetItem('--- NO Paster ! ---'))
            # self.tblResult.setCellWidget(1,6,imgLabel)

    def replaceHtmlTag(self, sentence) -> str:
        result = sentence.replace('&lt;','<')   # lesser than
        result = result.replace('&gt;','>')     # greater than
        result = result.replace('<b>','')       # bold
        result = result.replace('</b>','') 
        result = result.replace('&apos;',"'")   # apostopy 홑따옴표
        result = result.replace('&quot;','"')    # quotation mark 쌍따옴표
        # 변환안된 특수문자가 나타나면 추가

        # result = sentence.replace('&lt;','<').replace('&gt;','>').replace('<b>','').replace('</b>','').replace('&apos;',"'").replace('&quot;','"')

        return result


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())