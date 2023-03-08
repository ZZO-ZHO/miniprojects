# Gt Designer 디자인 사용
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from NaverAPI import *

class qtApp(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('./studyPyQt/naverApiSearch.ui', self)

        # 검색 버튼 클릭 시그널 / 슬롯함수
        self.btnSearch.clicked.connect(self.btnSearchClicked) 
        # 텍스트박스 입력후 엔터치면 처리
        self.txtSearch.returnPressed.connect(self.txtSearchReturned)

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
            while result != None and result ['display'] != 0:
                for post in result['items']:
                    api.get_post_data(post, outputs)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())