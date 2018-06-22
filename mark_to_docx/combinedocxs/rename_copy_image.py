# coding:utf-8
import os
import os.path


# 拷贝sourceDir目录下的文件,到targetDir下
def copyFiles(sourceDir, targetDir):
    if(os.path.exists(sourceDir) and os.path.exists(targetDir)):
        if sourceDir.find(u".svn") > 0:
            return
        for file in os.listdir(sourceDir):
            sourceFile = os.path.join(sourceDir, file)
            targetFile = os.path.join(targetDir, file)
            if os.path.isfile(sourceFile):
                if not os.path.exists(targetDir):
                    os.makedirs(targetDir)
                if not os.path.exists(targetFile) or (
                        os.path.exists(targetFile) and
                        (os.path.getsize(targetFile) !=
                         os.path.getsize(sourceFile))):
                    open(targetFile, "wb").write(open(sourceFile, "rb").read())
            if os.path.isdir(sourceFile):
                copyFiles(sourceFile, targetFile)


# 复制某一个文件夹下所有文件到另一目录
def coverFiles(sourceDir, targetDir):
    if(os.path.exists(sourceDir) and os.path.exists(targetDir)):
        for file in os.listdir(sourceDir):
            sourceFile = os.path.join(sourceDir, file)
            targetFile = os.path.join(targetDir, file)
            # cover the files
            if os.path.isfile(sourceFile):
                open(targetFile, "wb").write(open(sourceFile, "rb").read())
