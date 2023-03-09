# NaverApi 쿨래스 - OpenApi 인터넷 통해서 데이터를 전달 받음
from urllib.request import Request, urlopen
from urllib.parse import quote
import datetime
import json     # 결과는 json으로

class NaverApi:
    # 생성자
    def __init__(self) -> None:
        print('Naver API 생성')


    def get_request_url(self, url):
        req = Request(url)

        req.add_header('X-Naver-Client-Id','Rqd2BaDD9ojdExFpCvta')
        req.add_header('X-Naver-Client-Secret','Q84vvvjtBr')

        try:
            res = urlopen(req)
            if res.getcode() == 200:
                print(f'[{datetime.datetime.now()}] NaverAPI 요청 성공')
                return res.read().decode('utf-8')
            else:
                print(f'[{datetime.datetime.now()}] NaverAPI 요청 실패')
                return None
        except Exception as e:
            print(f'[{datetime.datetime.now()}] 예외발생 : {e}')
            return None


    def get_naver_search(self, node, search, start, display):
        base_url = 'https://openapi.naver.com/v1/search'
        node_url = f'/{node}.json'
        params = f'?query={quote(search)}&start={start}&display={display}'

        url = base_url + node_url + params
        retData = self.get_request_url(url)

        if retData == None:
            return None
        else:
            return json.loads(retData)

    # json 데이터 -> list 변환
    def get_post_data(self,post,outputs):
        title = post['title']
        description = post['description']
        originallink = [originallink]
        link = post['link']

        # Tue, 07 Mar 2023 17:04:00 +0900 문자열이 날아들어걸 날짜형으로 변경
        pData = datetime.datetime.strptime(post['pubData'], '%a, %d, %b, %Y, %H:%H:%S 0900')
        pubData = pData.strftime('%Y-%m-%d %H:%M:%S')