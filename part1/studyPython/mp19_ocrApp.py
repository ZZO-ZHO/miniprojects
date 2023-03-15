# 글자추출
# 이미지 처리 모듈 pillow
# OCR 모듈 pip install pillow
from PIL import Image
import pytesseract as tess

img_path = './studyPython/기사.png'
tess.pytesseract.tesseract_cmd = 'C:/DEV/Tools/Tesseract-OCR/tesseract.exe'

result = tess.image_to_string(Image.open(img_path), lang='kor')
print(result)