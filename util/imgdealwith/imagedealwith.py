# -*- coding:UTF-8 -*-

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os


# 照片灰度处理：完了之后，
# 首先在照片的左上角，和左下角标记对应横着的颜色，竖着的颜色，
# 其次横着的字体左上角标记，竖着的字体左下角标记
def myconvert(myimg='csrgb.png'):
    img_src = Image.open(myimg)
    # 转换图片的模式为L
    img_src = img_src.convert('L')
    myimgArr = myimg.split(".")
    img_src.save("" + myimgArr[0] + "L." + myimgArr[1] + "", "png")


def imageProcesse(imgInfoDir):
    im = Image.open(imgInfoDir['sourceimgPathName'])
    draw = ImageDraw.Draw(im)
    for imgInfobj in imgInfoDir['imgInfoList']:
        if imgInfobj.direction == '0':
            ttfont = ImageFont.truetype(os.path.join(os.getcwd(), "util/imgdealwith", "simsun.ttc"), imgInfobj.valueSize)
            draw.text(imgInfobj.coordinate, imgInfobj.value, fill=(0, 0, 0), font=ttfont)
    # im.save("cache.png", "png")
    # im1 = Image.open("cache.png")
    # im1 = im1.transpose(Image.ROTATE_270)
    # draw = ImageDraw.Draw(im1)
    # for imgInfobj in imgInfoDir['imgInfoList']:
    #     if imgInfobj.direction == '1':
    #         ttfont = ImageFont.truetype(os.path.join(os.getcwd(), "util/imgdealwith", "simsun.ttc"), imgInfobj.valueSize)
    #         draw.text(imgInfobj.coordinate, imgInfobj.value, fill=(0, 0, 0), font=ttfont)
    # im1 = im1.transpose(Image.ROTATE_90)
    # im.show()
    im.save(imgInfoDir['trgimgPathName'], "png")
    # os.remove('cache.png')


def creatimgInfoList(imgnamepath='csL.png'):
    img_src = Image.open(imgnamepath)
    f = open('imgInfoList.py', 'w')
    import sys
    old = sys.stdout
    # 将当前系统输出储存到一个临时变量中
    sys.stdout = f
    # 输出重定向到文件
    print('# -*- coding:UTF-8 -*-')
    print('from imgInfoModel import ImageInfo')
    print
    print
    print('def getimgInfoList():')
    print
    print('    return [')
    src_strlist = img_src.load()
    datafirst = src_strlist[0, 0]
    for i in range(0, img_src.size[0]):
        for j in range(0, img_src.size[1]):
            data = src_strlist[i, j]
            if datafirst == data and i != 0 and j != 0:
                print("    ImageInfo('0', (" + str(i) + ", " + str(j) + "), u'(" + str(i) + "," + str(j) + ")', 35),")
                # print("        ImageInfo('0', (" + str(i) + ", " + str(j) + "), u'00'),")
    img_src = img_src.transpose(Image.ROTATE_270)
    # 获得文字图片的每个像素点
    src_strlist = img_src.load()
    datafirst = src_strlist[0, 0]
    for i in range(0, img_src.size[0]):
        for j in range(0, img_src.size[1]):
            data = src_strlist[i, j]
            if datafirst == data and i != 0 and j != 0:
                print("    ImageInfo('1', (" + str(i) + ", " + str(j) + "), u'(" + str(i) + "," + str(j) + ")', 35),")
                # print("        ImageInfo('1', (" + str(i) + ", " + str(j) + "), u'11'),")
    print("    ]")
    # 测试一个打印输出
    sys.stdout = old
    # 还原原系统输出
    f.close()


def main():
    pass
    # myconvert('scq.png')
    # creatimgInfoList('scqL.png')
    # from imgInfoList import getimgInfoList
    # imgInfoDir = {'sourceimgPathName': 'scq.png', 'trgimgPathName': 'result.jpg', 'imgInfoList': getimgInfoList()}
    # imageProcesse(imgInfoDir)


if __name__ == '__main__':
    main()
