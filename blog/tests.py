from django.test import TestCase

# Create your tests here.

import datetime


import base64


#base编码
def convert(image):
    with open(image, 'rb') as f:  # 以二进制读取图片
        data = f.read()
        encodestr = base64.b64encode(data)  # 得到 byte 编码的数据
        print(str(encodestr, 'utf-8'))  # 重新编码数据
        return encodestr




def jiema(encodestr):#解码,保存为图片
    with open('1.jpg','wb') as f:
        baseimg = base64.b64decode(encodestr)
        f.write(baseimg)



if __name__ == "__main__":
    img = convert("20180904090809.png")
    jiema(img)