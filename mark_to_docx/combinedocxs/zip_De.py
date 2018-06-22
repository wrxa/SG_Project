# /usr/bin/python
# coding=utf-8
import os, sys, time
import zipfile


def zip_de(filedir, fname, fpath):

    filename = fname    # 要解压的文件
    filedir = filedir + fpath   # 解压后放入的目录
    r = zipfile.is_zipfile(filename)
    if r:
        starttime = time.time()
        fz = zipfile.ZipFile(filename,'r')
        for file in fz.namelist():
            print(file)
            # 打印zip归档中目录
            fz.extract(file, filedir)
        endtime = time.time()
        times = endtime - starttime
    else:
        print('This file is not zip file')
    print('times' + str(times))


if __name__ == '__main__':
    filedir = "D:\\py_buffer\\docx_Pro\\"
    os.rename("test1.docx", "test1.zip")
    os.rename("test2.docx", "test2.zip")
    os.rename("test3.docx", "test3.zip")
    zip_de(filedir, 'test1.zip', 'test1\\')
    zip_de(filedir, 'test2.zip', 'test2\\')
    zip_de(filedir, 'test3.zip', 'test3\\')