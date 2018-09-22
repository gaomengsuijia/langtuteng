from django.test import TestCase

# Create your tests here.
import base64



def baseencode(file):
    """
    文件Base64编码
    :param file:
    :return:
    """
    f = open(file,'rb')
    raw_data = f.read()
    f.close()

    base64data = base64.b64encode(raw_data)
    return base64data



def basedecode(base64data):
    """
    文件Base64解码
    :param base64data:
    :return:
    """
    with open('E:\\file.txt','wb') as f:
        f.write(base64.b64decode(base64data))
        print("文件保存成功")



if __name__ == '__main__':
    base64data = baseencode('E:\Baidu-baidu.csv')
    print(base64data)
    basedecode(base64data)