# 암호해제 앱
import itertools
import time
import zipfile
passwd_string = '0123456789'
# passwd_string = '0123456789abcdefghijkmln'

file = zipfile.ZipFile('./studyPython/암호는.zip')
isFind = False

for i in range(4,5):
    attempts = itertools.product(passwd_string,repeat=i)
    for attempts in attempts:
        try_pass = ''.join(attempts)
        print(try_pass)
        
        try:
            file.extractall(pwd=try_pass.encode(encoding='utf-8'))
            print(f'암호는 {try_pass}입니다.')
            isFind=True; break
        except:
            pass
    
    if isFind == True: break