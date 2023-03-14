# 스레드학습
# 기본 프로세스 1개 서브 프로세스 5개 동시진행
import threading
import time

# Thread를 상속받은 백그라운드잡업 클래스
class BackgroundWorker(threading.Thread):
    # 생성자
    def __init__(self, names: str) -> None:
        super().__init__()
        self.name = f'{threading.current_thread().name} : {names}'

    def run(self) -> None:
        print(f'BackGround Start : {self._name}')
        time.sleep(2)
        print(f'BackGround End : {self._name}')

if __name__ == '__main__':
    print('기본 프로세스 시작')

    for i in range(5):
        name = f'서브 스레드 {i}'
        th = BackgroundWorker(name)
        th.start()

    print('기본 프로세스 종료')
