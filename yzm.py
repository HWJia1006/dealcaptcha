from PIL import Image
import pytesseract
import cv2
import os
import random

pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'
img_folder = './img'
result_file = 'results' + str(random.randint(1, 10000)) + ".txt"
print(result_file)

# 设置 Tesseract 的参数
custom_config = r'--oem 3 --psm 6'


def ocr_captcha(image_path):
    # 打开并从图片中提取文本
    image = cv2.imread(image_path)
    # 对图像进行二值化
    _, image = cv2.threshold(image, 138, 255, cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(image, config=custom_config)
    return text


res = []
files = os.listdir(img_folder)
for i in files:
    f_path = os.path.join(img_folder, i)
    print(f_path)
    captcha_text = ocr_captcha(f_path)
    print('Num：', captcha_text)
    res.append('{}:{}'.format(i, captcha_text))
print(res)
with open(result_file, 'w') as f:
    for i in res:
        f.write(i)
